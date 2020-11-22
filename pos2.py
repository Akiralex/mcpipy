from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat(str(pos.x)) #プレイヤーの現在のx座標を表示
mc.postToChat(str(pos.y)) #プレイヤーの現在のy座標を表示
mc.postToChat(str(pos.z)) #プレイヤーの現在のz座標を表示
