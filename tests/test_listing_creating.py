from api.listing_api import CreateListingAPI
from data.data import ResponseStatus as RS, ListingData


class TestCreateListing:

    def test_create_listing_created_successfully(self, token, image_file):
        response = CreateListingAPI.create_listing(token, ListingData.LISTING_DATA, image_file)
        assert response.status_code == RS.CREATED and response.json()['id'] > 0
