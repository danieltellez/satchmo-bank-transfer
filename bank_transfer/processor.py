"""
This is a stub and used as the default processor.
It doesn't do anything but it can be used to build out another
interface.

See the authorizenet module for the reference implementation
"""
from django.utils.translation import ugettext as _
from payment.modules.base import BasePaymentProcessor, ProcessorResult

class PaymentProcessor(BasePaymentProcessor):

    def __init__(self, settings):
        self.settings = settings

    def prepareData(self, order):
        self.order = order

    def process(self, testing=False, amount=None):
        """
        Process the transaction and return a tuple:
            (success/failure, reason code, response text)
        """
        
        orderpayment = self.record_payment(self.order, self.settings, amount=self.order.balance)

        reason_code = "0"
        response_text = _("Success")

        return (True, reason_code, response_text)

