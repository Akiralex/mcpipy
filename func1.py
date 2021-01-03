from mcpi.minecraft import Minecraft
from mcpi.block import *
def pyramid(height):
    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    A = ((height*2)-1)
    for i in range(height):
        mc.setBlocks(pos.x+i,pos.y+i,pos.z+i,pos.x+(A-(i+1)),pos.y+i,pos.z+(A-(i+1)),STONE)
pyramid(50) #好きな数字を入れてみよう 
