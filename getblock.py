from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat(str(pos))
blockid = mc.getBlock(pos.x,pos.y,pos.z) #ブロックのIDを取得
mc.postToChat(str(blockid))
