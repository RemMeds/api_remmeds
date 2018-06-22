import unittest
from api_remmeds.api.controllers.user_connexion_controller import UserController
from unittest.mock import patch


class TestUserConnexionControllerSuccess(unittest.TestCase):
    @patch('api_remmeds.api.controllers.user_connexion_controller.check_user_connexion')
    def test_that_it_calls_right_functions(self, mock_user_function):
        UserController.get()
        mock_user_function.assert_called_once()
