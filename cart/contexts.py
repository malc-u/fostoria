"""Contexts.py file that sets logic that is helpful in handling cart
it is imported to context processors in settings.py and can be accessed
from any application in this project"""

from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """Allow cart contents to maintain across app session"""
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for article_id, article_detail in cart.items():
        product = get_object_or_404(Product, pk=article_id)
        for size, qty in article_detail['items_by_size'].items():

            if size == 'A3':
                price = 60
            elif size  == 'A2':
                price = 75
            elif size == 'A1':
                price = 90
            elif size == 'A0':
                price = 115
            else:
                price = 140

            product_count += qty
            total += qty * price

        cart_items.append({
            'article_id': article_id,
            'qty': article_detail,
            'product': product,
            'size': size,
            'price': price,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context
    