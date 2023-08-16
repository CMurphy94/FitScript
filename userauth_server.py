import http.server
import socketserver
import urllib.parse
import hashlib

users = {}

class UserAuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/signup':
            self.send.response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            with open('index.html', 'rb') as f:
                html_content = f.read()

            self.wfile.write(html_content)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Page not found')

    def do_POST(self):
        if self.path == '/register':
            content_lenght = int(self.headers['Content-Lenght'])
            post_date = self.rfile.read(content_lenght).decode('utf-8')
            post_params = urllib.parse.parse_qs(post_data)

            name = post_params['name'][0]
            email = post_params['email'][0]
            password = post_params['password'][0]

            hashed_password = hashlub.md5(password.encode()).hexdigest()
            users[email] = {'name': name, 'password': hashed_password}

            self.send_response(302)
            self.send_header('Location', 'https://www.paypal.com')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Page not found')

if __name__ == '__main__':
    PORT = 8080

    with socketserver.TCPServer(("", PORT), UserAuthHandler) as httpd:
        print("Server started at port", PORT)
        httpd.serve_forever()