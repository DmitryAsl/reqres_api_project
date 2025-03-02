from jsonschema import validate
from helpers.load_schema import load_schema
from helpers.api_client import api_request
from tests.config import BASE_URL
from helpers.data_provider import DataProvider

def test_get_single_user():
    param = DataProvider.get('', 'user_management', 'get_user')
    schema_for_validate = load_schema('get_single_user')
    url = f'{BASE_URL}/api/users/{param["user_id"]}'

    response = api_request(method='GET', url=url)
    response_json = response.json()

    assert response.status_code == param["status_code"]
    validate(instance=response_json, schema=schema_for_validate)
    assert response_json['data']['id'] == param["user_id"]


def test_post_create_user():
    param = DataProvider.get('', 'user_management', 'post_create_user')
    schema_for_validate = load_schema('post_create_user')
    url = f'{BASE_URL}/api/users'

    response = api_request(method='POST', url=url, json=param['body'])
    response_json = response.json()

    assert response.status_code == param['status_code']
    validate(instance=response_json, schema=schema_for_validate)
    assert response_json['name'] == param['body']['name']
    assert response_json['job'] == param['body']['job']


def test_put_update_user():
    param = DataProvider.get('', 'user_management', 'put_update_user')

    schema_for_validate = load_schema('put_update_user')
    url = f'{BASE_URL}/api/users/{param["user_id"]}'

    response = api_request(method='PUT', url=url, json=param['body'])
    response_json = response.json()

    assert response.status_code == param['status_code']
    validate(instance=response_json, schema=schema_for_validate)
    assert response_json['name'] == param['body']['name']
    assert response_json['job'] == param['body']['job']


def test_delete_user():
    param = DataProvider.get('', 'user_management', 'delete_user')
    url = f'{BASE_URL}/api/users/{param["user_id"]}'

    response = api_request(method='DELETE', url=url)

    assert response.status_code == param['status_code']
    assert not response.text


def test_negative_get_not_found_user():
    param = DataProvider.get('', 'user_management', 'get_not_found_user')
    url = f'{BASE_URL}/api/users/{param["user_id"]}'

    response = api_request(method='GET', url=url)
    response_json = response.json()

    assert response.status_code == param['status_code']
    assert response_json == {}
