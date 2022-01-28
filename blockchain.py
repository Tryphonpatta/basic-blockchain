import hashlib

class Block:
    def __init__(self, previous_block_hash, transaction_info):

        self.previous_block_hash = previous_block_hash
        self.transaction_info = transaction_info

        self.block_data = "\n".join(transaction_info) + "\nprevious = " + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "A send 10 BTC to B"
t2 = "B send 15 BTC to C"
t3 = "C send 5.25 BTC to D"
t4 = "D send 30 BTC to E"
t5 = "F send 12 BTC to G"
t6 = "H send 3.5 BTC to K"

init_block = Block("First Block", [t1, t2])
print(init_block.block_data)
print(init_block.block_hash)

print()

second_block = Block(init_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

print()

third_block = Block(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash)