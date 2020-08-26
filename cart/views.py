"""Cart app views that will be imported to cart urls to be displayed"""
from django.shortcuts import render, redirect, reverse


def cart_view(request):
    """A view that will render cart contents"""
    context = {
        "title": 'Basket Contents',
    }
    return render(request, "cart.html", context)

def add_to_cart(request, article_id):
    """ Add a quantity of the specified product to the shopping cart
    with the size taken into account. Logic used in this function was shared by Chris Zielinsky
    during Code Institute's course Ado-Boutiqe module. Function was re-written/amended
    by myself to suit my project needs.  """

    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if article_id in list(cart.keys()):
            if size in cart[article_id]['items_by_size'].keys():
                cart[article_id]['items_by_size'][size] += qty
            else:
                cart[article_id]['items_by_size'][size] = qty

        else:
            cart[article_id] = {'items_by_size': {size: qty}}


    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, article_id):
    """ Update quantity of the specified product in the shopping cart
    with the size taken into account. Logic used in this function was shared by Chris Zielinsky
    during Code Institute's course Ado-Boutiqe module. Function was re-written/amended
    by myself to suit my project needs.  """

    qty = int(request.POST.get('qty'))
    size = None


    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if qty > 0:
            cart[article_id]['items_by_size'][size] = qty

        else:
            del cart[article_id]['items_by_size'][size]
            if not cart[article_id]['items_by_size']:
                cart.pop(article_id)

    request.session['cart'] = cart
    return redirect(reverse('cart_view'))
