from pathlib import Path


class ResponseMessage:
    EXISTING_USER_SIGNUP = 'Почта уже используется'
    UPDATE_LISTING_WITH_INVALID_TOKEN_ERROR = 'Unauthorized'
    UPDATE_LISTING_WITH_INVALID_TOKEN_MESSAGE = 'Оффер не найден или у вас нет прав на его редактирование'
    LISTING_DELETED_SUCCESSFULLY = 'Объявление удалено успешно'


class ResponseStatus:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401


class ListingData:
    LISTING_DATA = {
        "name": "test_summary",
        "category": "Хобби",
        "condition": "Б/У",
        "city": "Казань",
        "description": "test_description",
        "price": 999
    }

    UPDATED_LISTING_DATA = {
        "name": "test_summary",
        "category": "Хобби",
        "condition": "Б/У",
        "city": "Казань",
        "description": "test_description",
        "price": 10000
    }

    IMAGE_PATH = Path("data/img/test_image.png")
