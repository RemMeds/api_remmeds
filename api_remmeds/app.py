from flask import Flask
from flask_restplus import Api
from api_remmeds.api.controllers.user_connexion_controller import ns as check_account

app = Flask(__name__)
api = Api(app)
api.add_namespace(check_account)

if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.26', port='15020')
