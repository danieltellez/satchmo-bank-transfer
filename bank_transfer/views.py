from django.views.decorators.cache import never_cache
from livesettings import config_get_group
from payment.views import confirm, payship, checkout
from satchmo_store.shop.models import Order
from satchmo_store.shop.notification import send_order_confirmation
from satchmo_utils.views import bad_or_missing

bank_transfer = config_get_group('PAYMENT_BANK_TRANSFER')

def pay_ship_info(request):
    return payship.base_pay_ship_info(request, bank_transfer, payship.simple_pay_ship_process_form, 'shop/checkout/bank_transfer/pay_ship.html')
pay_ship_info = never_cache(pay_ship_info)

def confirm_info(request):
    return confirm.credit_confirm_info(request, bank_transfer, 'shop/checkout/bank_transfer/confirm.html')
confirm_info = never_cache(confirm_info)

def success(request):
    try:
        order = Order.objects.get(id=request.session['orderID'])
    except Order.DoesNotExist:
        return bad_or_missing(request, _('Your order has already been processed.'))

    del request.session['orderID']
    return render_to_response('shop/checkout/bank_transfer/success.html',
                              {'order': order},
                              context_instance=RequestContext(request))


success = never_cache(success)
