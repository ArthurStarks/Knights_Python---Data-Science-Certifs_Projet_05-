import http.server
import socketserver
import webbrowser
import os

# Set the port number
PORT = 8000

# Create a custom handler to serve the current directory
Handler = http.server.SimpleHTTPRequestHandler

# Create the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Opening presentation in your default browser...")
    webbrowser.open(f'http://localhost:{PORT}/presentation.html')
    httpd.serve_forever() 