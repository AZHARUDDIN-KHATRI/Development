import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, votes, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.votes = votes  # List of verified vote dicts
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Generates SHA-256 hash of the block's content."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "votes": self.votes,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        """Implements Proof-of-Work (PoW) mining algorithm."""
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"⛏️ Block {self.index} successfully mined! Hash: {self.hash}")
import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, votes, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.votes = votes  # List of verified vote dicts
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Generates SHA-256 hash of the block's content."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "votes": self.votes,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        """Implements Proof-of-Work (PoW) mining algorithm."""
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"⛏️ Block {self.index} successfully mined! Hash: {self.hash}")
