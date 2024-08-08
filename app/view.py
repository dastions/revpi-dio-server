import falcon

class MainView:
    def on_get(self, req, resp):
        try:
            with open('public/index.html', 'r', encoding='utf-8') as f:
                resp.content_type = 'text/html'
                resp.body = f.read()
        except FileNotFoundError:
            raise falcon.HTTPNotFound(description='File not found')