from django.conf.urls.defaults import patterns
from satchmo_store.shop.satchmo_settings import get_satchmo_setting

ssl = get_satchmo_setting('SSL', default_value=False)

urlpatterns = patterns('',
     (r'^$', 'bank_transfer.views.pay_ship_info', {'SSL':ssl}, 'BANK_TRANSFER_satchmo_checkout-step2'),
     (r'^confirm/$', 'bank_transfer.views.confirm_info', {'SSL':ssl}, 'BANK_TRANSFER_satchmo_checkout-step3'),
     (r'^success/$', 'bank_transfer.views.success', {'SSL':ssl}, 'BANK_TRANSFER_satchmo_checkout-success'),
)
