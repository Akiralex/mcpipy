from mcpi.minecraft import Minecraft
from mcpi.block import *
mc = Minecraft.create()
pos = mc.player.getTilePos()

#豆腐を作るための関数。引数は幅、高さ、奥行き。戻り値なし
def tofu(Width, Height, Depth):

    X2 = Width - 1     #x座標の終点位置
    Y2 = Height - 1     #y座標の終点位置   
    Z2 = Depth - 1     #z座標の終点位置   

    AIR_X2 = X2 - 1 #空気の描画用のx座標の終点
    AIR_Y2 = Y2 - 1 #空気の描画用のy座標の終点
    AIR_Z2 = Z2 - 1 #空気の描画用のz座標の終点

    #ブロックの配置とくり抜き
    mc.setBlocks(pos.x,pos.y,pos.z,pos.x+X2,pos.y+Y2,pos.z+Z2,STONE)
    mc.setBlocks(pos.x+1,pos.y+1,pos.z+1,pos.x+AIR_X2,pos.y+AIR_Y2,pos.z+AIR_Z2,AIR)

tofu(5,5,5)    
