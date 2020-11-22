from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.player.setTilePos(pos.x-2000,pos.y,pos.z) #プレイヤーの座標を変更
