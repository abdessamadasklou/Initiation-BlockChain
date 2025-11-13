import hashlib
class Block:
    def __init__(self,timestamp,transactions,previous_hash=''):
        self.timestamp= timestamp
        self.transactions=transactions
        self.previous_hash=previous_hash
        self.nonce=0
        self.hash=self.create_hash()
    def create_hash(self):
        block_string=(str(self.previous_hash)+str(self.timestamp)+str([t.__dict__ for t in self.transactions ])+str(self.nonce)).encode()
        return hashlib.sha256(block_string).hexdigest()
    def mine_block(self,difficulty):
        target='0'*difficulty
        while self.hash[:difficulty]!= target:
            self.nonce +=1
            self.hash = self.create_hash()
        print (f"Bloc miné ! Nonce={self.nonce},Hash={self.hash}")