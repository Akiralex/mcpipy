from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos_org = mc.player.getTilePos()
pos = mc.player.getTilePos()

print(pos_org.x, pos_org.y,pos_org.z)

for i in range (22):
    blockType = mc.setBlock(pos.x+i,pos.y,pos.z,1)

for j in range (22):
    blockType = mc.setBlock(pos.x,pos.y,pos.z+j,1)

mc.player.setTilePos(pos.x+21,pos.y,pos.z+21) #プレイヤーの座標を変更
pos = mc.player.getTilePos()
     
for k in range (22):
    blockType = mc.setBlock(pos.x-k,pos.y,pos.z,1)

for l in range (22):
    blockType = mc.setBlock(pos.x,pos.y,pos.z-l,1)
print(pos_org.x, pos_org.y,pos_org.z)
# 元の位置に戻す
print('Back to original position')
mc.player.setTilePos(pos_org.x, pos_org.y, pos_org.z)
pos = mc.player.getTilePos()
for posX in range (20):
    for posZ in range(20):
        for posY in range (100):
        # プレイヤーと同じ高さ以上にあるブロックを取得
            if posY == 0:
                print(pos.x+posX,pos.y+posY,pos.z+posZ)
                print('Block ID:',blockType)
                
            blockType = mc.getBlock(pos.x+posX,pos.y+posY,pos.z+posZ)
            #原木の判定（ブロックIDは17）
            if blockType == 17:
                print('Block ID:',blockType)
                print('*********************************************')
                mc.setBlock(pos.x+posX,pos.y+posY,pos.z+posZ,WOOD_PLANKS)
            #葉の判定（ブロックIDは18）
            elif blockType == 18:
                print('Block ID:',blockType)
                print('*********************************************')
                mc.setBlock(pos.x+posX,pos.y+posY,pos.z+posZ,0)
