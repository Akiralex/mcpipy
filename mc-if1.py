from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

#プレイヤーの真下にあるブロックのIDを取得
blockType = mc.getBlock(pos.x,pos.y - 1,pos.z)
#草ブロック（Block IDは2）

if blockType == 2:

    #真下にダイアモンドブッロク（Block ID は 41）
    mc.setBlock(pos.x,pos.y - 1,pos.z,41)
