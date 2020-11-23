from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

for j in range(3):
    for i in range(4):
        mc.setBlock(pos.x+i,pos.y+i,pos.z+j,98)
mc.player.setTilePos(pos.x,pos.y,pos.z-1) #プレイヤーの座標を変更
'''
#5段の階段を作るための繰り返し
for i in range(5):
    for j in range(3):
        mc.setBlock(pos.x+i,pos.y+i,pos.z+j,109)
