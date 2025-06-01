from api.user_api import UserAPI
from data.data import ResponseMessage as RM, ResponseStatus as RS


class TestSignUpUser:

    def test_signup_user_all_fields_registered_successfully(self, generate_user_data):
        response = UserAPI.signup_user(generate_user_data['email'], generate_user_data['password'])
        assert response.status_code == RS.CREATED and response.json()['user']['id'] > 0

    def test_signup_user_existing_user_data_not_registered(self, generate_user_data, signup_user):
        response = UserAPI.signup_user(generate_user_data['email'], generate_user_data['password'])
        assert response.status_code == RS.BAD_REQUEST and response.json()['message'] == RM.EXISTING_USER_SIGNUP
