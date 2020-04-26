from gym_minigrid.minigrid import *
from gym_minigrid.register import register

class TestEnv01(MiniGridEnv):
    def __init__(
        self,
        size=12,
        numObjs=4,
        cum_reward=0,
        agent_start_pos=(1,1),
        agent_start_dir=0,
    ):
        self.objs = []
        self.numObjs = numObjs
        self.cum_reward = cum_reward
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir

        super().__init__(
            grid_size=size,
            max_steps=4*size*size,
            # Set this to True for maximum speed
            see_through_walls=True
        )
    
    def _gen_grid(self, width, height):
        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        objs = []

        # Place doors
        objColor = self._rand_elem(COLOR_NAMES)
        while len(objs) < self.numObjs:
            obj = Door(objColor)
            self.place_obj(obj)
            objs.append(obj)

        self.objs = objs

        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

        self.mission = "open all doors"
        
    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)

        if action == self.actions.toggle:
            self.cum_reward = sum(obj.is_open for obj in self.objs)
            reward = self._reward()
            if self.cum_reward == self.numObjs:
                done = True

        return obs, reward, done, info

register(
    id = 'MiniGrid-Empty-Test-v1',
    entry_point = 'gym_minigrid.my_envs:TestEnv01',
    # reward_threshold = 0.95
)