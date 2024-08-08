import falcon
from app.controller import ControllerDIO
from app.view import MainView
from app.static import StaticFileResource

class RedirectionController:
    # get
    def on_get(self, req, resp, **kwargs):
        raise falcon.HTTPMovedPermanently('https://www.dastions.com')


print('=================Server API!=================')

api = falcon.API()
api.add_route('/api/dio', ControllerDIO())
api.add_route('/', RedirectionController())
api.add_route('/sat', MainView())
api.add_route('/public/{filename}', StaticFileResource(directory='public'))
