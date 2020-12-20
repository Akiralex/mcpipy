from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
mc.events.clearAll()#イベントの削除
while True:
    pos = mc.player.getTilePos()
    #チャットイベントの取得と処理
    for i in mc.events.pollChatPosts():
        #exitがチャットに入力されたら終了
        if i.message == "&exit":
            mc.postToChat("stop")
            exit()#ブログラム終了命令
        #$woodがチャットに入力された自身のいる左表に原木を置く    
        elif i.message == "&wood":
            mc.setBlock(pos.x,pos.y,pos.z,WOOD_PLANKS)
