from django.shortcuts import render

# Create your views here.
def cart_view(request):
    """A view that will render cart contents"""

    return render(request, "cart.html")
