from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()
width=4

for j in range(width):
    for i in range(1):
        mc.setBlock(pos.x+i,pos.y+i,pos.z+j,98)
mc.player.setTilePos(pos.x-1,pos.y,pos.z) #プレイヤーの座標を変更
pos = mc.player.getTilePos()

for j in range(width):
    for i in range(2):
        mc.setBlock(pos.x+i,pos.y+i,pos.z+j,98)
mc.player.setTilePos(pos.x-1,pos.y,pos.z) #プレイヤーの座標を変更
pos = mc.player.getTilePos()

for j in range(width):
    for i in range(3):
        mc.setBlock(pos.x+i,pos.y+i,pos.z+j,98)
mc.player.setTilePos(pos.x-1,pos.y,pos.z) #プレイヤーの座標を変更
pos = mc.player.getTilePos()

for j in range(width):
    for i in range(4):
        mc.setBlock(pos.x+i,pos.y+i,pos.z+j,98)
mc.player.setTilePos(pos.x-1,pos.y,pos.z) #プレイヤーの座標を変更
pos = mc.player.getTilePos()

#5段の階段を作るための繰り返し
for i in range(5):
    for j in range(4):
        mc.setBlock(pos.x+i,pos.y+i,pos.z+j,109)
