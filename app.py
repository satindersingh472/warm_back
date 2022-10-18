from flask import request, Flask
import json
from dbhelpers import run_statement
from apihelpers import check_endpoint_info
import dbcreds

app = Flask(__name__)

@app.get('/api/gifs')
def get_restaurant():
    results = run_statement('CALL get_gifs()')
    if(type(results) == list):
        res_json = json.dumps(results, default=str)
        return res_json
    else:
        return "Sorry, there was an error getting the gifs"

if(dbcreds.production_mode == True):
    print('Running in production mode')
    import bjoern #type: ignore
    bjoern.run(app,'0.0.0.0',5000)
else:
    print('Running in TESTING MODE')
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
