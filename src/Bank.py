from src import User, PaymentData


class Bank:

    def __init__(self):
        pass

    def do_payment(self, user: User, payment_data: PaymentData):
        return True

    def PagamentVisa(self, user: User, payment_data: PaymentData):
        return self.do_payment(user, payment_data)