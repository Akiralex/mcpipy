import time
from mcpi import minecraft
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")
 
while True:
 
    for blockhit in mc.player.pollBlockHits():
        pos = blockhit.pos
        gold_block_id = 41
        mc.setBlock(pos.x, pos.y, pos.z, gold_block_id)
 
    time.sleep(1)
