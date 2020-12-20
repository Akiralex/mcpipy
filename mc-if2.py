from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

for posX in range (20):
    for posZ in range(20):
        # プレイヤーの真下にあるブロックを取得
        blockType = mc.getBlock(pos.x+posX,pos.y - 1,pos.z+posZ)
        # 水ブロック（ブロックIDは8、止まっている水ブロックは9）
        if blockType == 8 or blockType == 9:
        # 真下に氷ブロックを（ブロック名はICE、ブロックIDは41）
            mc.setBlock(pos.x+posX,pos.y - 1,pos.z+posZ,ICE)
