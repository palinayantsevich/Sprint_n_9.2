import requests
from urls import Urls


class SignUpUserAPI:
    @staticmethod
    def signup_user(email: str, password: str):
        response = requests.post(Urls.SIGNUP_USER,
                                 json={"email": email, "password": password, "submitPassword": password})
        return response


class SignInUserAPI:
    @staticmethod
    def signin_user(email: str, password: str):
        response = requests.post(Urls.SIGNIN_USER,
                                 json={"email": email, "password": password})
        return response
