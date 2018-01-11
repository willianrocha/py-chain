from unittest import TestCase
from unittest.mock import Mock, patch
import json
from core.transaction import Transaction, json, time, sha256

class TestTransactions(TestCase):
    def setUp(self):
        self.valid = {'from':{'user1':-10},'to':{'user2':10}}
        self.valid_hash = '766cfeec822a02c28205dc97a10ad25246e3727dda3113e4d2cc9c712676eb1c'
        self.valid_time = 1515681558.5318768
        self.trans = Transaction()

    def test_IsValidTx(self):
        tests = [
        [{'from':{'user1':-10},'to':{'user2':10}},True], # 1:1
        [{'from':{'user1':-10},'to':{'user2':8}},False],
        [{'from':{'user1':-10},'to':{'user2':12}},False],
        [{'from':{'user1':-10},'to':{'user2':5,'user3':5}},True], # 1:n
        [{'from':{'user1':-10},'to':{'user2':5,'user3':4}},False],
        [{'from':{'user1':-10},'to':{'user2':5,'user3':4}},False],
        [{'from':{'user1':-10,'user2':-5},'to':{'user3':15}},True], # n:1
        [{'from':{'user1':-10,'user2':-5},'to':{'user3':14}},False],
        [{'from':{'user1':-10,'user2':-5},'to':{'user3':16}},False],
        [{'from':{'user1':-10,'user2':-5},'to':{'user3':7,'user4':8}},True],#n:n
        [{'from':{'user1':-10,'user2':-5},'to':{'user3':7,'user4':7}},False],
        [{'from':{'user1':-10,'user2':-5},'to':{'user3':7,'user4':9}},False],
        ]
        for t in tests:
            assert self.trans.isValidTx(t[0]) == t[1]

    @patch('core.transaction.time')
    def test_pushToMiner(self, time_mocked):
        time_mocked.return_value = self.valid_time
        resp = {'ts': self.valid_time, 'hash': self.valid_hash, 'data': self.valid}
        assert self.trans.pushToMiner(self.valid) == resp
