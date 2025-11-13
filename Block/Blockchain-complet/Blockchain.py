import time
from Block import Block
from Transaction import Transaction
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions=[]
        self.mining_reward=10
    def create_genesis_block(self):
        return Block("1-1-2025", [], "0")
    def get_last_block(self):
        return self.chain[-1]
    def create_transaction(self,transaction):
        self.pending_transactions.append(transaction)
    def mine_pending_transactions(self,miner_address):
        block = Block(time.time(),self.pending_transactions,self.get_last_block().hash)
        block.mine_block(self.difficulty)
        print("Bloc validé et ajouté à la chaîne")
        self.chain.append(block)
        self.pending_transactions=[Transaction(None,miner_address,self.mining_reward)]

    def get_balance_of_address(self,address):
        balance= 0
        for block in self.chain:
            for trans in block.transactions:
                if trans.from_addr==address:
                    balance-=trans.amount
                if trans.to_addr==address:
                    balance+= trans.amount
        return balance
    
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current= self.chain[i]
            prev = self.chain[i - 1]
            if current.hash != current.create_hash():
                return False
            if current.previous_hash != prev.hash:
                return False
        return True


# 1. Créer la blockchain
print("\n1. Création de la blockchain...")
my_blockchain = Blockchain()
print(f"✓ Blockchain créée avec difficulté = {my_blockchain.difficulty}")
print(f"✓ Récompense de minage = {my_blockchain.mining_reward}")

# 2. Créer des transactions
print("\n2. Création de transactions...")
print("   Alice envoie 50 à Bob")
my_blockchain.create_transaction(Transaction("Alice", "Bob", 50))

print("   Bob envoie 25 à Charlie")
my_blockchain.create_transaction(Transaction("Bob", "Charlie", 25))

print("   Charlie envoie 10 à Alice")
my_blockchain.create_transaction(Transaction("Charlie", "Alice", 10))

print(f"✓ {len(my_blockchain.pending_transactions)} transactions en attente")

# 3. Premier minage
print("\n3. Premier minage par 'Mineur1'...")
my_blockchain.mine_pending_transactions("Mineur1")
print(f"✓ Nombre de blocs dans la chaîne : {len(my_blockchain.chain)}")

# Afficher les soldes après le premier minage
print("\n   Soldes après le premier minage :")
print(f"   - Alice   : {my_blockchain.get_balance_of_address('Alice')}")
print(f"   - Bob     : {my_blockchain.get_balance_of_address('Bob')}")
print(f"   - Charlie : {my_blockchain.get_balance_of_address('Charlie')}")
print(f"   - Mineur1 : {my_blockchain.get_balance_of_address('Mineur1')}")

# 4. Deuxième minage (pour inclure la récompense du premier minage)
print("\n4. Deuxième minage par 'Mineur1'...")
my_blockchain.mine_pending_transactions("Mineur1")
print(f"✓ Nombre de blocs dans la chaîne : {len(my_blockchain.chain)}")

print("\n   Soldes après le deuxième minage :")
print(f"   - Alice   : {my_blockchain.get_balance_of_address('Alice')}")
print(f"   - Bob     : {my_blockchain.get_balance_of_address('Bob')}")
print(f"   - Charlie : {my_blockchain.get_balance_of_address('Charlie')}")
print(f"   - Mineur1 : {my_blockchain.get_balance_of_address('Mineur1')}")

# 5. Ajouter plus de transactions
print("\n5. Nouvelles transactions...")
print("   Bob envoie 10 à Alice")
my_blockchain.create_transaction(Transaction("Bob", "Alice", 10))

print("   Alice envoie 5 à Charlie")
my_blockchain.create_transaction(Transaction("Alice", "Charlie", 5))

# 6. Troisième minage par un autre mineur
print("\n6. Troisième minage par 'Mineur2'...")
my_blockchain.mine_pending_transactions("Mineur2")

print("\n   Soldes après le troisième minage :")
print(f"   - Alice   : {my_blockchain.get_balance_of_address('Alice')}")
print(f"   - Bob     : {my_blockchain.get_balance_of_address('Bob')}")
print(f"   - Charlie : {my_blockchain.get_balance_of_address('Charlie')}")
print(f"   - Mineur1 : {my_blockchain.get_balance_of_address('Mineur1')}")
print(f"   - Mineur2 : {my_blockchain.get_balance_of_address('Mineur2')}")

# 7. Vérification de la validité de la chaîne
print("\n7. Vérification de la validité de la blockchain...")
is_valid = my_blockchain.is_chain_valid()
print(f"✓ La blockchain est {'VALIDE' if is_valid else 'INVALIDE'}")

# 8. Afficher les détails de chaque bloc
print("\n8. Détails de la blockchain :")
print("=" * 60)
for i, block in enumerate(my_blockchain.chain):
    print(f"\nBloc #{i}")
    print(f"  Timestamp      : {block.timestamp}")
    print(f"  Hash précédent : {block.previous_hash[:20]}...")
    print(f"  Hash actuel    : {block.hash[:20]}...")
    print(f"  Nonce          : {block.nonce}")
    print(f"  Transactions   : {len(block.transactions)}")
    for j, trans in enumerate(block.transactions):
        print(f"    #{j+1}: {trans.from_addr} → {trans.to_addr} : {trans.amount}")
