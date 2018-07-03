from flask import Flask
from flask_restplus import Api
from api_remmeds.api.controllers.user_connexion_controller import ns as check_account
from api_remmeds.api.controllers.contact_controller import ns as check_repertory
from api_remmeds.api.controllers.historic_controller import ns as historic
from api_remmeds.api.controllers.raspberry_controller import ns as raspberry

app = Flask(__name__)
api = Api(app)
api.add_namespace(check_account)
api.add_namespace(check_repertory)
api.add_namespace(historic)
api.add_namespace(raspberry)

if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.26', port='15020')
