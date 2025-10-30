import hashlib
class Block: 
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index       
        self.timestamp = timestamp   
        self.data = data  
        self.previous_hash = previous_hash 
        self.nonce = 0 
        self.hash = self.create_hash()
    def create_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()
    def mine_block(self, difficulty):
        self.nonce = 0
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.create_hash() 
        print(f"Block mined: {self.hash} with nonce: {self.nonce}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 6
    def create_genesis_block(self):
        return Block(0, "2025-10-12 00:00", "Bloc de genèse", "0")
    def get_latest_block(self):
        return self.chain[-1]
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current= self.chain[i]
            prev = self.chain[i - 1]
            if current.hash != current.create_hash():
                return False
            if current.previous_hash != prev.hash:
                return False
        return True
if __name__ == "__main__":
    import json
    # Exemple d'utilisation simple : créer une blockchain, ajouter des blocs et sauvegarder
    bc = Blockchain()
    bc.difficulty = 6  # réduire la difficulté pour l'exemple local
    bc.add_block(Block(1, "2025-10-12 00:05", "Ronaldo envoie 5 BTC"))
    bc.add_block(Block(2, "2025-10-12 00:10", "Vini envoie 5 BTC"))
    bc.add_block(Block(3, "2025-10-13 01:00", "Fetah envoie 10 BTC"))

    print("Chaîne valide ?", bc.is_chain_valid())
    chain_dicts = [b.__dict__ for b in bc.chain]
    print(json.dumps(chain_dicts, ensure_ascii=False, indent=4))

    with open("blocks.json", "w", encoding="utf-8") as f:
        json.dump(chain_dicts, f, ensure_ascii=False, indent=4)