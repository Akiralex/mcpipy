#ブロックを各方向に３つ配置するクラス
class ThreePutBlock():

    #初期化（コンストラクタ）
    def __init__(self, mc, blockName, pos):
        self.blockName = blockName
        self.pos = pos
        self.mc = mc

    #x座標方向にブロックを配置
    def verticalXPlacement(self):
        print(self.pos)
        print(self.blockName)
        self.mc.setBlocks(self.pos.x,self.pos.y,self.pos.z,self.pos.x+2,self.pos.y,self.pos.z,self.blockName)

    #z座標方向にブロックを配置
    def verticalZPlacement(self):
        print(self.pos)
        print(self.blockName)
        self.mc.setBlocks(self.pos.x,self.pos.y,self.pos.z,self.pos.x,self.pos.y,self.pos.z+2,self.blockName)

    #y座標方向にブロックを配置
    def horizontalPlacement(self):
        print(self.pos)
        print(self.blockName)
        self.mc.setBlocks(self.pos.x,self.pos.y,self.pos.z,self.pos.x,self.pos.y+2,self.pos.z,self.blockName)

