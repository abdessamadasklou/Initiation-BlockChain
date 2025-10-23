import hashlib
class Block:
    def __init__(self,index,timestamp,data,previous_hash=''):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previous_hash=previous_hash
    
        self.hash=self.create_hash()
    def create_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}".encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def remove_block(self, blockchain, index):
        if 0 <= index >= len(blockchain):
            raise IndexError("Can't remove block from the blockchain.")
        del blockchain[index]
        # We will have to change the previous_hash, nonce, and chain of subsequent blocks
        for i in range(index, len(blockchain)):
            blockchain[i].previous_hash = blockchain[i-1].hash if i > 0 else '0'
            blockchain[i].nonce = 0
            blockchain[i].hash = blockchain[i].create_hash()
        
        return blockchain
    

genesis_block = Block(0, "2025-10-12 00:00", "Bloc de genèse", previous_hash="0") 
# Chaîne sous forme de liste Python 
blockchain = [genesis_block] 
# Afficher le bloc de genèse 
print("Index:", genesis_block.index) 
print("Timestamp:", genesis_block.timestamp) 
print("Données:", genesis_block.data) 
print("Previous Hash:", genesis_block.previous_hash) 
print("Hash:", genesis_block.hash)  # vide pour l'instant 


# Créer un second bloc 
bloc1 = Block(1, "2025-10-12 00:05", "Ronaldo envoie 5 BTC", 
previous_hash=genesis_block.hash) 
blockchain.append(bloc1) 
# Afficher la chaîne de blocs 
for bloc in blockchain : 
    print(f"Bloc {bloc.index} : data={bloc.data}, prev_hash={bloc.previous_hash}, hash={bloc.hash}" )