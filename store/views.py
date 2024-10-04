from django.http import HttpResponse


def store(request):
    # List of store items
    items = [
        {'name': 'Laptop', 'price': '$999'},
        {'name': 'Smartphone', 'price': '$699'},
        {'name': 'Headphones', 'price': '$199'},
        {'name': 'Smartwatch', 'price': '$299'},
        {'name': 'Tablet', 'price': '$399'}
    ]

    # Create HTML content dynamically with items
    html_content = """

    <html>
        <head>
            <title>Store</title>
            <style>
            ul {
                list-style-type: none;
                background-color: #f2f2f2;
                padding: 10px;
                }
            </style>
        </head>
        <body>
        <div style="display: flex; flex-direction: column; align-items: center;">
            <h1>Welcome to the Store Page</h1>
            <p>Here are some of our products:</p>
            <ul>
    """

    for item in items:
        html_content += f"<li>{item['name']} - {item['price']}</li>"

    html_content += """
            </ul>
            <p>Routes</p>
            <a href="/order/" style="margin: 10px;">Order</a>
            <a href="../" style="margin: 10px;">Index</a>
        </div>
        </body>
    </html>
    """

    return HttpResponse(html_content, content_type="text/html")
