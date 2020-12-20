from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

for j in range(10):
    for i in range(10):
        mc.setBlock(pos.x,pos.y+j,pos.z+i,209)

