from django.http import HttpResponse


def index(request):
    html_content = """
    <html>
        <head><title>Store Order</title></head>
        <body>
        <div style="display: flex; flex-direction: column; align-items: center;">
            <h1>Welcome to the Store Order Page</h1>
            <p>Routes</p>
            <a href="/store/" style="margin: 10px;">Store</a>
            <a href="/order/">Order</a>
        </div>
        </body>
    </html>
    """
    return HttpResponse(html_content, content_type="text/html")
