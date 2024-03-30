import http.server
import socketserver
import webbrowser

PORT = 8000

# Define the directory containing the HTML file
directory = "financial_market_data/trading/fxma"

# Change the working directory to serve files from the specified directory
# This ensures that the HTML file and other static assets can be accessed
os.chdir(directory)

# Handler to serve the HTML file
Handler = http.server.SimpleHTTPRequestHandler

# Start a web server on port 8000
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at localhost:{}".format(PORT))
    # Open the default web browser to the server URL
    webbrowser.open("http://localhost:{}".format(PORT))
    # Keep the server running until interrupted
    httpd.serve_forever()
