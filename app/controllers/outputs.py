import falcon, json
from app.logger import log
from app.model import ModuleDIO

class OutputsController:


    def validate_api_key(req, resp, resource, params):      
        licenses = open('.env/licenses.json')
        data = json.load(licenses)

        try:
            for license in data["licenses"]:
                log(license)
                if req.headers['X-API-KEY'] in license.get('key'):
                    return True
            
            raise falcon.HTTPForbidden('Forbidden', 'License not found')
        except KeyError:
            raise falcon.HTTPForbidden('Forbidden', 'License not found')

    # get
    def on_get(self, req, resp, **kwargs):
        log("GET - /api/outputs")
        
        outputs = ModuleDIO.get_outputs()
        resp.status = falcon.HTTP_200
        resp.media = {
            'status': 200,
            'outputs': outputs
        }
        
    # content type: application/json
    @falcon.before(validate_api_key)
    def on_post(self, req, resp, **kwargs):
        log("POST - /api/outputs")

        try:
            id = req.media['outputs']['id']
            value = req.media['outputs']['value']
        
            response = ModuleDIO.set_output(id, value)
        except Exception as err:
            log("ERROR - on_post - ", str(err))

            response = { 
                'status': 403,
                'error': "Internal Error, check logs! expected: json { image: { content: 'base 64 image encoded'}}",
                'details': str(err)
            }
            
        resp.media = response

