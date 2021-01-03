from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
mc.events.clearAll() #全てのイベントの削除

while True:
    blockHits = mc.events.pollBlockHits() #叩いた情報を格納する
      #叩いたことを確認
    if blockHits:
        print(blockHits)
        #blockHitsの情報をblockHitの個人に格納
        for blockHit in blockHits:
            print(blockHit.pos.x,blockHit.pos.y,blockHit.pos.z)
            mc.setBlock(blockHit.pos.x,blockHit.pos.y,blockHit.pos.z,DIAMOND_BLOCK)
