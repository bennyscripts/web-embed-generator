import flask
import os
import importlib

app = flask.Flask(__name__, template_folder='templates', static_folder='assets')
app.secret_key = os.urandom(24)

for route_file in os.listdir("routes/"):
    if route_file.endswith(".py"):
        lib = importlib.import_module("routes." + route_file[:-3])
        app.register_blueprint(lib.blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)