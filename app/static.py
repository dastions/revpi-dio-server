import os
import falcon


class StaticFileResource:
    def __init__(self, directory):
        self.directory = directory

    def on_get(self, req, resp, filename):
        """Handles GET requests for static files"""
        filepath = os.path.join(self.directory, filename)
        try:
            with open(filepath, 'rb') as f:
                content = f.read()
                resp.content_type = self._get_content_type(filename)
                resp.body = content
        except FileNotFoundError:
            raise falcon.HTTPNotFound(description='File not found')

    def _get_content_type(self, filename):
        """Determine the content type based on file extension"""
        if filename.endswith('.css'):
            return 'text/css'
        elif filename.endswith('.js'):
            return 'application/javascript'
        elif filename.endswith('.html'):
            return 'text/html'
        elif filename.endswith('.png'):
            return 'image/png'
        elif filename.endswith('.jpg') or filename.endswith('.jpeg'):
            return 'image/jpeg'
        # Add more content types as needed
        return 'application/octet-stream'