from api.listing_api import UpdateListingAPI
from data.data import ResponseStatus as RS, ResponseMessage as RM, ListingData


class TestUpdateListing:

    def test_update_price_field_listing_valid_token_updated_successfully(self, token, image_file, listing_id):
        response = UpdateListingAPI.update_listing(token, ListingData.UPDATED_LISTING_DATA, image_file, listing_id)
        assert response.status_code == RS.OK
        assert response.json()['id'] == listing_id
        assert response.json()['price'] == ListingData.UPDATED_LISTING_DATA['price']

    def test_update_price_field_listing_invalid_token_not_updated(self, token_of_another_user, image_file, listing_id):
        response = UpdateListingAPI.update_listing(token_of_another_user, ListingData.UPDATED_LISTING_DATA, image_file,
                                                   listing_id)

        assert response.status_code == RS.UNAUTHORIZED
        assert response.json()['error'] == RM.UPDATE_LISTING_WITH_INVALID_TOKEN_ERROR
        assert response.json()['message'] == RM.UPDATE_LISTING_WITH_INVALID_TOKEN_MESSAGE
