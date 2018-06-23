from flask import Flask, Blueprint
from api_remmeds.api.restplus import api
from api_remmeds.api.controllers.user_connexion_controller import ns as user_connexion

app = Flask(__name__)


def app_config(flask_app):
    # 127.0.01 pour pouvoir le mettre sur VM et call le hostname de la VM
    flask_app.config['SERVER_NAME'] = '127.0.0.1:5000'  # NOSONAR


def app_init(flask_app):
    bp = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(bp)
    api.add_namespace(user_connexion)
    flask_app.register_blueprint(bp)


def launch_app():
    app_config(app)
    app_init(app)
    app.run()


if __name__ == "__main__":
    launch_app()
