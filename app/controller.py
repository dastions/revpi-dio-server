import falcon, json
from app.logger import log
from app.model import ModuleDIO

class ControllerDIO:
    def __init__(self) -> None:
        self.module_dio = ModuleDIO()


    def validate_api_key(req, resp, resource, params):      
        licenses = open('.env/licenses.json')
        data = json.load(licenses)

        try:
            if not (req.headers['X-API-KEY']):
                raise falcon.HTTPForbidden('Forbidden', 'License not found')
            for license in data["licenses"]:
                if req.headers['X-API-KEY'] == license.get('key'):
                    return True
            
            raise falcon.HTTPForbidden('Forbidden', 'License not found')
        except KeyError:
            raise falcon.HTTPForbidden('Forbidden', 'License not found')


    @falcon.before(validate_api_key)
    def on_get(self, req, resp, **kwargs):
        log("GET - /api/dio")

        # filter = req.get_param('name', default=None)
        
        inputs  = self.module_dio.get_inputs_list()
        outputs = self.module_dio.get_outputs_list()
        
        
        resp.status = falcon.HTTP_200
        resp.media = {
            'status': 200,
            'outputs': outputs,
            'inputs': inputs
        }


    @falcon.before(validate_api_key)
    def on_post(self, req, resp, **kwargs):
        log("POST - /api/dio")

        try:
            id = req.media['output']
            value = req.media['value']

            if not (isinstance(value, bool) and isinstance(id, str)):
                raise falcon.HTTPBadRequest(
                    title="Missing parameter",
                    description="The output (str) and value (bool) parameters are required."
                )
            
            result = self.module_dio.set_output(id, value)
            
            response = {
                'status': 202,
                'message': "UPDATED",
                'result': result
            }

        except Exception as err:
            log("ERROR - on_post - ", str(err))

            response = { "error": str(err) }
            
        resp.media = response

