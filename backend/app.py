from flask import Flask, jsonify, current_app
from api.auth import bp_auth
from flask_cors import CORS

app = Flask(__name__)
   
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/help', methods = ['GET'])
def help():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)


app.register_blueprint(bp_auth, url_prefix='/api/auth')


if __name__ == '__main__':
    app.run(host="0.0.0.0")