import sys

import poseidon

import hashlib

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.tree = self._build_tree()

    def _hash_transaction(self, transaction):
        # Hash function (using SHA-256 for demonstration)
        # return hashlib.sha256(transaction.encode()).hexdigest()
        return poseidon.hash

    def _build_tree(self):
        if len(self.transactions) == 0:
            return []

        # Create leaf nodes
        leaf_nodes = [self._hash_transaction(transaction) for transaction in self.transactions]

        # Build the tree level by level
        tree = [leaf_nodes]
        while len(tree[-1]) > 1:
            level = []
            for i in range(0, len(tree[-1]), 2):
                # Concatenate and hash pairs of nodes
                combined_hash = self._hash_transaction(tree[-1][i] + tree[-1][i + 1])
                level.append(combined_hash)
            tree.append(level)
        return tree

    def get_root(self):
        return self.tree[-1][0]

    def get_proof(self, transaction):
        index = self.transactions.index(transaction)
        proof = []
        current_level = self.tree[0]
        for i in range(len(self.tree) - 1):
            if index % 2 == 0:
                sibling_index = index + 1
            else:
                sibling_index = index - 1
            proof.append(current_level[sibling_index])
            index //= 2
            current_level = self.tree[i + 1]
        return proof

# Example usage:



def main():
    print('Hola')
    transactions = ["Transaction1", "Transaction2", "Transaction3", "Transaction4"]
    merkle_tree = MerkleTree(transactions)

    print("Merkle Tree:")
    for level in merkle_tree.tree:
        print(level)

    print("\nRoot Hash:", merkle_tree.get_root())

    transaction_to_prove = "Transaction2"
    proof = merkle_tree.get_proof(transaction_to_prove)
    print("\nProof for", transaction_to_prove, ":", proof)

    return 0

if __name__ == '__main__':
    main()
    sys.exit(0)
