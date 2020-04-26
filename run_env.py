import gym
import gym_minigrid

from gym_minigrid.window import Window
from gym_minigrid.wrappers import *

def redraw(img):
    if not agent_view:
        img = env.render('rgb_array', tile_size=tile_size)
    window.show_img(img)

def reset():
    if seed != -1:
        env.seed(seed)

    obs = env.reset()

    global cum_reward
    cum_reward = 0

    if hasattr(env, 'mission'):
        print('Mission: %s' % env.mission)
        window.set_caption(env.mission)
    # Test for DirectionObsWrapper
    # window.set_caption('%.2f' % obs['goal_direction'])
    redraw(obs)

def step(action):
    obs, reward, done, info = env.step(action)
    print('step=%s, reward=%.2f' % (env.step_count, reward))

    global cum_reward
    
    if done:
        print('done!')
        reset()
    else:
        # Test for DirectionObsWrapper
        # window.set_caption('%.2f' % obs['goal_direction'])
        
        # Test for DirectionBonus Wrapper
        cum_reward += reward
        window.set_caption('%.2f' % cum_reward)

        redraw(obs)

def key_handler(event):
    print('pressed', event.key)

    if event.key == 'escape':
        window.close()
        return

    if event.key == 'backspace':
        reset()
        return

    if event.key == 'left':
        step(env.actions.left)
        return
    if event.key == 'right':
        step(env.actions.right)
        return
    if event.key == 'up':
        step(env.actions.forward)
        return

    # Spacebar
    if event.key == ' ':
        step(env.actions.toggle)
        return
    if event.key == 'pageup':
        step(env.actions.pickup)
        return
    if event.key == 'pagedown':
        step(env.actions.drop)
        return

    if event.key == 'enter':
        step(env.actions.done)
        return


env_name = 'MiniGrid-Empty-RandomStartGoal-16x16-v001'
agent_view = False
seed = -1
tile_size = 32
cum_reward = 0

env = gym.make(env_name)
# env = ImgObsWrapper(env) # Get rid of the 'mission' field
env = DirectionObsWrapper(env, 'angle') # Provides the angular direction to the goal 
env = DirectionBonus(env) # Add a bonus if the step was towards the goal.

window = Window('gym_minigrid - ' + env_name)
window.reg_key_handler(key_handler)
reset()

# Blocking event loop
window.show(block=True)
