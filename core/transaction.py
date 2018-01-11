from hashlib import sha256
from time import time
import json
from core.block import Block

class Transaction:
    def __init__(self):
        self.out = 0
        self.blck = Block()

    # Verify if the transaction is valid or not
    def isValidTx(self, tx):
        # {'from':{'user1':-10},'to':{'user2':10}}
        # TODO: Check if the balance is available and usernames are valid
        # Structure:
        # From
        #   user_name : withdrawals
        # To
        #   user_name : deposits
        try:
            withdrawals_out = sum(tx['from'].values())
            deposit_in      = sum(tx['to'].values())
        except KeyError:
            return False
        if withdrawals_out + deposit_in == 0:
            return True
        return False

    # Prepare to send the transaction to the mining pool
    def pushToMiner(self, tx):
        j = json.dumps(tx, sort_keys=True).encode('utf-8')
        hsh = sha256(j).hexdigest()
        t = time()
        full_transaction = {'ts': t, 'hash': hsh, 'data' : tx}
        return full_transaction
