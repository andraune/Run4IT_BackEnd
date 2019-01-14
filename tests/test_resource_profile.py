import pytest
from run4it.api.profile.resource import Profile
from .helpers import get_response_json


@pytest.mark.usefixtures('db')
class TestRegisterResource:

    def test_content_type_is_json(self, api, client):
        url = api.url_for(Profile)
        response = client.get(url)
        assert(response.headers["Content-Type"] == 'application/json')
