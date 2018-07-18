from unittest.mock import patch
from api_remmeds.app import app

client = app.test_client()


@patch('api_remmeds.api.controllers.user_connexion_controller.check_user_connexion')
class TestUserConnexionController:
    def test_that_it_calls_right_functions(self, mock_user_connection):
        client.get('user/check_account/fake_username&fake_password')
        mock_user_connection.assert_called_once()

    def test_that_it_returns_correct_json(self, mock_user_connection):
        mock_user_connection.return_value = True, 19
        response = client.get('user/check_account/fake_username&fake_password')
        data = response.get_json()
        assert data == {"connection": True, "user_id": 19}


@patch('api_remmeds.api.controllers.user_connexion_controller.check_mail')
class TestMailController:
    def test_that_it_calls_right_functions(self, mock_check_mail):
        client.get('user/check_mail/fake_mail@fake.fr')
        mock_check_mail.assert_called_once()

    def test_that_it_returns_correct_json(self, mock_check_mail):
        mock_check_mail.return_value = False, "Already in database, can't create this user"
        response = client.get('user/check_mail/fake_mail@fake.fr')
        data = response.get_json()
        assert data == {"creation_posibility": False,
                        "data": "Already in database, can't create this user"}


@patch('api_remmeds.api.controllers.user_connexion_controller.check_mail')
@patch('api_remmeds.api.controllers.user_connexion_controller.create_account')
@patch('api_remmeds.api.controllers.user_connexion_controller.add_empty_compartment_new_account')
class TestAccountController:
    def test_that_it_calls_right_functions_if_mail_ok(self, mock_add_empty_comp, mock_create_account, mock_check_mail):
        client.post('user/create_account/mail&password&lastname&firstname&bf&lun&din&bed')
        mock_check_mail.return_value = True
        mock_check_mail.assert_called_once()
        mock_create_account.assert_called_once()
        mock_add_empty_comp.assert_called_once()

    # def test_that_it_calls_right_functions_if_mail_ko(self, mock_add_empty_comp, mock_create_account, mock_check_mail):
    #     client.post('user/create_account/mail&password&lastname&firstname&bf&lun&din&bed')
    #     mock_check_mail.return_value = False
    #     mock_check_mail.assert_called_once()
    #     mock_create_account.assert_not_called()
    #     mock_add_empty_comp.assert_not_called()

    def test_that_it_returns_correct_json(self, mock_add_empty_comp, mock_create_account, mock_check_mail):
        response = client.post('user/create_account/mail&password&lastname&firstname&bf&lun&din&bed')
        data = response.get_json()
        assert data == {"creation": "DONE"}

    # def test_that_it_returns_correct_json_if_ko(self, mock_add_empty_comp, mock_create_account, mock_check_mail):
    #     response = client.post('user/create_account/mail&password&lastname&firstname&bf&lun&din&bed')
    #     mock_check_mail.return_value = False
    #     data = response.get_json()
    #     assert data == {"creation": "ABORDED"}
