from credo.transactions import Transactions
from . import SECRET_KEY, PUBLIC_KEY

# TODO: Retest everything here
class TestTransactions:
    transactions = Transactions(public_key=PUBLIC_KEY, secret_key=SECRET_KEY)

    def test_all(self):
        status, all_transactions = self.transactions.all()
        print(all_transactions)
        assert status == 200

    def test_get_one(self):
        status, transaction = self.transactions.get_one(1264)

        assert status == 200

    def test_refund(self):

        status, transaction = self.transactions.refund(1264, 1970)
        print(transaction)
        assert status == 200
