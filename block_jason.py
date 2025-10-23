import json
from Block_Hash import Block
blockchain=[]
blockchain.append(Block(0,"2025-10-12","Bloc ge genese","0"))
blockchain.append(Block(1,"2025-10-12","Ronaldo envoie 5 BTC",blockchain[-1].hash))
blockchain.append(Block(2,"2025-10-12","Vini envoie 5 BTC",blockchain[-1].hash))
blockchain.append(Block(3,"2025-10-13","Fetah envoie 10 BTC",blockchain[-1].hash))
#blockchain = blockchain[2].remove_block(blockchain,2)
print(json.dumps([b.__dict__ for b in blockchain], indent=4))
