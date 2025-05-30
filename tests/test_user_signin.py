from api.user_api import SignInUserAPI
from data.data import ResponseStatus as RS


class TestSignInUser:

    def test_signin_user_all_fields_registered_successfully(self, generate_user_data, signup_user):
        response = SignInUserAPI.signin_user(generate_user_data['email'], generate_user_data['password'])
        assert response.status_code == RS.CREATED and response.json()['user']['id'] > 0
