from gym_minigrid.minigrid import *
from gym_minigrid.register import register

class ObstaclesRandomStartGoalEnv8x8(MiniGridEnv):
    def __init__(
        self,
        size=8,
        obstacles = 5,
        # agent_start_pos=(1,1),
        agent_start_pos=None,
        agent_start_dir=0,
    ):
        self.obstacles = obstacles
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir

        super().__init__(
            grid_size=size,
            max_steps=4*size*size,
            # Set this to True for maximum speed
            # see_through_walls=True
        )
    
    def _gen_grid(self, width, height):
        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

        # Place obstacles
        for i in range(self.obstacles):
            self.place_obj(Wall())

        # Place a goal object somewhere
        self.place_obj(Goal())

        self.mission = "reach the green goal square"
        
    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info


register(
    id='MiniGrid-Obstacles-RandomStartGoal-8x8-v001',
    entry_point='gym_minigrid.my_envs:ObstaclesRandomStartGoalEnv8x8'
)