import falcon, json
from app.logger import log
from app.model import ModuleDIO

class InputsController:
    # get
    def on_get(self, req, resp, **kwargs):
        log("GET - /api/inputs")
        
        inputs = ModuleDIO.get_inputs()
        resp.status = falcon.HTTP_200
        resp.media = {
            'status': 200,
            'inputs': inputs
        }