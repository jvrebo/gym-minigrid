from gym_minigrid.minigrid import *
from gym_minigrid.envs.empty import *
from gym_minigrid.register import register

class EmptyRandomEnv8x8(EmptyEnv):
    def __init__(self):
        super().__init__(size=8, agent_start_pos=None)

class EmptyRandomEnv16x16(EmptyEnv):
    def __init__(self):
        super().__init__(size=16, agent_start_pos=None)

class EmptyRandomStartGoalEnv(MiniGridEnv):
    def __init__(
        self,
        size=8,
        # agent_start_pos=(1,1),
        agent_start_pos=None,
        agent_start_dir=0,
    ):
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

        # Place a goal object somewhere
        self.place_obj(Goal())

        self.mission = "reach the green goal square"
        
    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info

class EmptyRandomStartGoalEnv16x16(EmptyRandomStartGoalEnv):
    def __init__(self):
        super().__init__(size=16, agent_start_pos=None)

class EmptyRandomStartGoalEnv32x32(EmptyRandomStartGoalEnv):
    def __init__(self):
        super().__init__(size=32, agent_start_pos=None)

register(
    id='MiniGrid-Empty-Random-8x8-v001',
    entry_point='gym_minigrid.my_envs:EmptyRandomEnv8x8'
)

register(
    id='MiniGrid-Empty-Random-16x16-v001',
    entry_point='gym_minigrid.my_envs:EmptyRandomEnv16x16'
)

register(
    id='MiniGrid-Empty-RandomStartGoal-8x8-v001',
    entry_point='gym_minigrid.my_envs:EmptyRandomStartGoalEnv'
)

register(
    id='MiniGrid-Empty-RandomStartGoal-16x16-v001',
    entry_point='gym_minigrid.my_envs:EmptyRandomStartGoalEnv16x16'
)

register(
    id='MiniGrid-Empty-RandomStartGoal-32x32-v001',
    entry_point='gym_minigrid.my_envs:EmptyRandomStartGoalEnv32x32'
)