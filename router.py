import falcon
from app.controller import ControllerDIO


class RedirectionController:
    # get
    def on_get(self, req, resp, **kwargs):
        raise falcon.HTTPMovedPermanently('https://www.dastions.com')

# TODO: def config method for wsgi
print('=================Server API!=================')

api = falcon.API()
api.add_route('/api/dio', ControllerDIO())
api.add_route('/', RedirectionController())