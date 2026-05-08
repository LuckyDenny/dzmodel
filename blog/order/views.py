from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import OrderForm
from .models import OrderItem
from cart.cart import Cart

# Create your views here.
@login_required
def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order= order, product= item['product'], quantity= item['quantity'], price= item['price'])
            cart.clear()
            return render(request, 'order/success.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, "order/create_order.html", {"form": form, "cart": cart})