from mcpi.minecraft import Minecraft #クラスの呼び出し
mc = Minecraft.create() #Minecraftとの接続
pos = mc.player.getTilePos() #プレイヤーの現在地の座標を取得
mc.postToChat(str(pos))
