from api.listing_api import ListingAPI
from data.data import ResponseStatus as RS, ResponseMessage as RM


class TestDeleteListing:

    def test_delete_listing_successfully_deleted(self, token, listing_id):
        response = ListingAPI.delete_listing(token, listing_id)

        assert response.status_code == RS.OK and response.json()['message'] == RM.LISTING_DELETED_SUCCESSFULLY
