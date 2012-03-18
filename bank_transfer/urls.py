from django.conf.urls.defaults import *
from livesettings import config_value, config_get_group

config = config_get_group('PAYMENT_BANK_TRANSFER')

urlpatterns = patterns('',
     (r'^$', 'payment_modules.bank_transfer.views.pay_ship_info', 
             {'SSL':config.SSL.value}, 'BANK_TRANSFER_satchmo_checkout-step2'),
     (r'^confirm/$', 'payment_modules.bank_transfer.views.confirm_info', 
             {'SSL':config.SSL.value}, 'BANK_TRANSFER_satchmo_checkout-step3'),
     (r'^success/$', 'payment_modules.bank_transfer.views.success', 
             {'SSL':config.SSL.value}, 'BANK_TRANSFER_satchmo_checkout-success'),
)
