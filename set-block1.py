from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlock(pos.x,pos.y,pos.z,STONE)
