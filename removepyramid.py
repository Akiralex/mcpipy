from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

N=1000
for i in range(N):
    n=N-i
    width=2*n-1
    for j in range(width):
        for i in range(width):
            mc.setBlock(pos.x+i,pos.y,pos.z+j,0)
    mc.player.setTilePos(pos.x+1,pos.y+1,pos.z+1) #プレイヤーの座標を変更
    pos = mc.player.getTilePos()

