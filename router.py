import falcon
from app.controllers.outputs import OutputsController
from app.controllers.inputs import InputsController

class RedirectionController:
    # get
    def on_get(self, req, resp, **kwargs):
        raise falcon.HTTPMovedPermanently('https://www.dastions.com')

# TODO: def config method for wsgi
print('=================Server API!=================')

api = falcon.API()
api.add_route('/api/inputs', InputsController())
api.add_route('/api/outputs', OutputsController())
api.add_route('/', RedirectionController())