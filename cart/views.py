"""Cart app views that will be imported to cart urls to be displayed"""
from django.shortcuts import render, redirect


def cart_view(request):
    """A view that will render cart contents"""

    return render(request, "cart.html")

def add_to_cart(request, article_id):
    """ Add a quantity of the specified product to the shopping cart
    with the size taken into account. This function was shared by Chris Zielinsky
    during Code Institute's course Ado-Boutiqe module. It was amended by myself to suit
    my project needs. """

    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    price = 0

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if article_id in list(cart.keys()):

        else:
            cart[article_id] = {'items_by_size': {size: qty}}


    request.session['cart'] = cart
    return redirect(redirect_url)
