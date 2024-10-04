from django.http import HttpResponse


def orders(request):
    # List of sample orders
    orders_list = [
        {'id': 1, 'item': 'Laptop', 'quantity': 1, 'total_price': '$999'},
        {'id': 2, 'item': 'Smartphone', 'quantity': 2, 'total_price': '$1398'},
        {'id': 3, 'item': 'Headphones', 'quantity': 1, 'total_price': '$199'},
        {'id': 4, 'item': 'Smartwatch', 'quantity': 1, 'total_price': '$299'}
    ]

    # Create HTML content dynamically with orders
    html_content = """
    
    <html>
        <head>
            <title>Orders</title>
            <style>
            ul {
                list-style-type: none;
                background-color: #f2f2f2;
                }
            </style>
        </head>
        <body>
        <div style="display: flex; flex-direction: column; align-items: center;">
            <h1>Welcome to the Orders Page</h1>
            <p>Here are your current orders:</p>
            <ul>
    """

    for order in orders_list:
        html_content += f"<li>Order #{order['id']}: {order['item']} - Quantity: {order['quantity']} - Total: {order['total_price']}</li>"

    html_content += """
            </ul>
            <p>Routes</p>
            <a href="/store/" style="margin: 10px;">Store</a>
            <a href="../" style="margin: 10px;">Index</a>
        </div>
        </body>
    </html>
    """

    return HttpResponse(html_content, content_type="text/html")
