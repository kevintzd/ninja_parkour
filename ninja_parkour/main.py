'''
#-*- coding = utf-8 -*-
#@Time: 2020/11/16 12:55
#@Author: Zhida Tian
#@Software: PyCharm
'''
import os
import game_control as gc
from scenes import StartingMenu, game_play, game_over, credits, introduction

# game controls the whole game, when initialize will load all the resources
game = gc.control()
# store all the scene object
scene_dic = {
    'none': 'none',
    'starting': StartingMenu.startingmenu(),
    'runing_scene': game_play.game_playscene(),
    'game_over': game_over.game_overscene(),
    'Credits': credits.credits_menu(),
    'Introduction': introduction.introduction_menu()
}
start_scene = 'starting'
# initialize the first scene
game.init_scene(scene_dic, start_scene)
game.main()
os._exit(0)

