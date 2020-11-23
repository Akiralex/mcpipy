from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

#5弾の階段を作るための繰り返し
for i in range(5):
    for j in range(3):
         mc.setBlock(pos.x+i,pos.y+i,pos.z+j,109)

