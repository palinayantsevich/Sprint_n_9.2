import requests
from urls import Urls


class UserAPI:
    @staticmethod
    def signup_user(email: str, password: str):
        response = requests.post(Urls.SIGNUP_USER,
                                 json={"email": email, "password": password, "submitPassword": password})
        return response

    @staticmethod
    def signin_user(email: str, password: str):
        response = requests.post(Urls.SIGNIN_USER,
                                 json={"email": email, "password": password})
        return response
