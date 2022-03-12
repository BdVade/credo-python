from credo.transactions import Transactions
from . import SECRET_KEY, PUBLIC_KEY


class TestTransactions:
    transactions = Transactions(public_key=PUBLIC_KEY, secret_key=SECRET_KEY)

    def test_all(self):
        status, all_transactions = self.transactions.all()
        print(all_transactions)
        assert status == 200

    def test_get_one(self):#
        # TODO: Change tx_id being checked for
        status, transaction = self.transactions.get_one(10)

        assert status == 200

    def test_refund(self):

        status, transaction = self.transactions.refund(10, 2000)

        assert status == 200
