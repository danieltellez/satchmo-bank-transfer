from django.utils.translation import ugettext as _
from payment.modules.base import BasePaymentProcessor, ProcessorResult

class PaymentProcessor(BasePaymentProcessor):
    """
    Bank transfer payment processing module
    """
    def __init__(self, settings):
        self.settings = settings
        super(PaymentProcessor, self).__init__('bank_transfer', settings)

    def prepareData(self, order):
        self.order = order

    def capture_payment(self, testing=False, order=None, amount=None):
        """
        Process the transaction and return a ProcessorResult
        """
        if order:
            self.prepareData(order)
        else:
            order = self.order

        orderpayment = self.record_payment(amount=self.order.balance, reason_code="0")
        return ProcessorResult(self.key, True, _("Success"), orderpayment)
