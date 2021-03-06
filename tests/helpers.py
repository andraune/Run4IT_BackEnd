import json
from run4it.api.user.model import User
from run4it.api.user.resource import Login, LoginRefresh
from run4it.api.profile.model import Profile


def get_response_json(response_data):
    return json.loads(response_data.decode("utf-8"))

def register_confirmed_user(username, email, password, height=None, weight=None, birth_date=None):
	user = User(username, email, password)
	user.confirmed = True
	profile = Profile(user)
	profile.height = height
	profile.set_weight(weight)
	profile.birth_date = birth_date
	user.save()
	profile.save()

def register_and_login_confirmed_user(testapi, testclient, username, email, password, height=None, weight=None, birth_date=None):
	register_confirmed_user(username, email, password, height, weight, birth_date)
	url = testapi.url_for(Login)
	response = testclient.post(url, data={"email": email, "password": password })
	response_json = get_response_json(response.data)
	return response_json["accessToken"], response_json["refreshToken"]

def register_and_login_user_with_unfresh_token(testapi, testclient, username, email, password, height=None, weight=None, birth_date=None):
	_,refreshtoken = register_and_login_confirmed_user(testapi, testclient, username, email, password, height, weight, birth_date)
	url = testapi.url_for(LoginRefresh)
	response = testclient.post(url, headers=get_authorization_header(refreshtoken))
	response_json = get_response_json(response.data)
	return response_json["accessToken"]

def get_authorization_header(token):
	return {'Authorization': 'Bearer {}'.format(token)}
