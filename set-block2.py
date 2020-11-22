from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

#5つの石ブロックをx座標を標準にして並べる
mc.setBlock(pos.x,pos.y,pos.z,STONE)
mc.setBlock(pos.x+1,pos.y,pos.z,STONE)
mc.setBlock(pos.x+2,pos.y,pos.z,STONE)
mc.setBlock(pos.x+3,pos.y,pos.z,STONE)
mc.setBlock(pos.x+4,pos.y,pos.z,STONE)


