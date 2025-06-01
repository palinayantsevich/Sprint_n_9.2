import requests
from urls import Urls


class ListingAPI:
    @staticmethod
    def create_listing(token, data, files):
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        }
        response = requests.post(Urls.CREATE_LISTING, headers=headers, data=data, files=files)
        return response

    @staticmethod
    def update_listing(token, data, files, listing_id):
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        }
        response = requests.patch(f'{Urls.UPDATE_LISTING}{listing_id}', headers=headers, data=data, files=files)

        return response

    @staticmethod
    def delete_listing(token, listing_id):
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        }
        response = requests.delete(f'{Urls.DELETE_LISTING}{listing_id}', headers=headers)

        return response
