from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

#5x5x5 の四角を作成
mc.setBlocks(pos.x,pos.y,pos.z,pos.x+4,pos.y+4,pos.z+4,STONE)
#3x3x3 の四角をAIRブロックで上書き
mc.setblocks(pos.X+1,pos.y+1,pos.z+1,pos.x+3,pos.y+3,pos.z+3,AIR)
