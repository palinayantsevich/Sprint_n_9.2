import pytest
from helper import Helper
from api.user_api import SignUpUserAPI
from api.listing_api import CreateListingAPI
from data.data import ListingData


@pytest.fixture(scope='function')
def generate_user_data():
    email = Helper.generate_user_email()
    password = Helper.generate_user_password()

    payload = {
        'email': email,
        'password': password
    }
    return payload


@pytest.fixture(scope='function')
def signup_user(generate_user_data):
    return SignUpUserAPI.signup_user(generate_user_data['email'], generate_user_data['password'])


@pytest.fixture(scope='function')
def token(signup_user):
    token = signup_user.json()['access_token']['access_token']
    return token


@pytest.fixture(scope='function')
def token_of_another_user():
    email = Helper.generate_user_email()
    password = Helper.generate_user_password()
    response = SignUpUserAPI.signup_user(email, password)
    return response.json()['access_token']['access_token']


@pytest.fixture(scope='function')
def listing_id(token, image_file):
    response = CreateListingAPI.create_listing(token, ListingData.LISTING_DATA, image_file)
    return response.json()['id']


@pytest.fixture
def image_file():
    with open(ListingData.IMAGE_PATH, "rb") as img_file:
        yield {
            "images": (ListingData.IMAGE_PATH.name, img_file, "image/png")
        }
