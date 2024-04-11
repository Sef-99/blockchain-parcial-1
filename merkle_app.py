import sys

import poseidon

import merke_tree

def poseidon_init():
    security_level = 128
    input_rate = 5
    t = 100
    alpha = 5
    poseidon_hash = poseidon.Poseidon(poseidon.parameters.prime_255, security_level, alpha, input_rate, t)
    return poseidon_hash

def main():
    transactions = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [0, 7, 4, 3, 2], [8, 2, 1, 5, 2]]
    poseidon_hash = poseidon_init()
    merkle_tree = merke_tree.MerkleTree(transactions, poseidon_hash)

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
