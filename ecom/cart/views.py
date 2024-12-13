from django.shortcuts import render, get_object_or_404 # type: ignore
from .cart import Cart
from store.models import Product
from django.http import JsonResponse # type: ignore
from django.contrib import messages # type: ignore

def cart_summary(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	totals = cart.cart_total()
	return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals})





def cart_add(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		# lookup product in DB
		product = get_object_or_404(Product, id=product_id)
		
		# Save to session
		cart.add(product=product, quantity=product_qty)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return response
		# response = JsonResponse({'Product Name: ': product.name})
		response = JsonResponse({'qty': cart_quantity})
		messages.success(request, ("Product Added To Cart..."))
		return response

def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		# Call delete Function in Cart
		cart.delete(product=product_id)

		response = JsonResponse({'product':product_id})
		#return redirect('cart_summary')
		messages.success(request, ("Item Deleted From Shopping Cart..."))
		return response


def cart_update(request):
    cart = Cart(request)
    
    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            # Get and validate product_id and product_qty
            product_id = request.POST.get('product_id')
            product_qty = request.POST.get('product_qty')

            # Ensure both product_id and product_qty are provided
            if not product_id or not product_qty:
                return JsonResponse({'error': 'Product ID and quantity are required'}, status=400)

            # Convert to integers
            product_id = int(product_id)
            product_qty = int(product_qty)

            # Validate quantity is greater than 0
            if product_qty <= 0:
                return JsonResponse({'error': 'Quantity must be greater than zero'}, status=400)

            # Update the cart
            cart.update(product=product_id, quantity=product_qty)

            # Success response
            messages.success(request, "Your cart has been updated.")
            return JsonResponse({'qty': product_qty})

        except ValueError:
            # Handle invalid integer conversion
            return JsonResponse({'error': 'Invalid product ID or quantity format'}, status=400)

    # Invalid request method or action
    return JsonResponse({'error': 'Invalid request'}, status=400)
