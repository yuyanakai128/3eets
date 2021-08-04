from flask import Flask, jsonify,render_template, request
from api.auth import bp_auth
from api.goods import bp_goods
from flask_cors import CORS

app = Flask(__name__,template_folder="api/templates")
   
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/help', methods = ['GET'])
def help():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)

@app.route("/api/test", methods=["GET", "POST"])
def test():
    '''this is test url'''
    if request.method == "POST":
        data = request.form.to_dict()
        # from api import iroha_sdk as sdk
        # sdk.add_coin_to_admin()
        return render_template('results.html',data='ok')
    return render_template('test.html')


app.register_blueprint(bp_auth, url_prefix='/api/auth')
app.register_blueprint(bp_goods, url_prefix='/api/goods')


if __name__ == '__main__':
    app.run(host="0.0.0.0")