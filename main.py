from mcpi.minecraft import Minecraft
from mcpi.block import *
from class2 import ThreePutBlock

mc = Minecraft.create()
pos = mc.player.getTilePos()

#クラスのテスト
test = ThreePutBlock(mc,STONE,pos)
test.verticalXPlacement()
test.verticalZPlacement()
test.horizontalPlacement()

mc.player.setTilePos(pos.x + 10, pos.y, pos.z)
post = mc.player.getTilePos()

t = ThreePutBlock(mc,DIAMOND_BLOCK,post)
t.verticalXPlacement()
t.verticalZPlacement()
t.horizontalPlacement()
