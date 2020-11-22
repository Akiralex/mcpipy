from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

mc.postToChat(str(pos))
#石ブロックを5個並べて配置
mc.setBlock(pos.x,pos.y,pos.z,pos.x+4,pos.y,pos.z, STONE)

