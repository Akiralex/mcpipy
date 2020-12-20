from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos_org = mc.player.getTilePos()
pos = mc.player.getTilePos()

mc.events.clearAll()#イベントの削除
while True:
    for i in mc.events.pollChatPosts():
        if i.message == "&exit":
            exit()
