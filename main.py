from blockchain import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.add_new_block('Primeiro bloco!')
    blockchain.add_new_block('Blockchain é top!')
    blockchain.add_new_block('Mais uma vez!')

    print(blockchain.get_all())
#