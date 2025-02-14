import requests
from jsonschema import validate
from helpers.load_schema import load_schema

BASE_URL = "https://reqres.in"


def test_get_single_user():
    user_id = 2
    schema_for_validate = load_schema('get_single_user')
    url = f'{BASE_URL}/api/users/{user_id}'

    response = requests.get(url=url)
    response_json = response.json()

    assert response.status_code == 200
    validate(instance=response_json, schema=schema_for_validate)
    assert response_json['data']['id'] == user_id


def test_post_create_user():
    name = "Jhon"
    job = "manager"
    body = {
        "name": name,
        "job": job
    }
    schema_for_validate = load_schema('post_create_user')
    url = f'{BASE_URL}/api/users'

    response = requests.post(url=url, json=body)
    response_json = response.json()

    assert response.status_code == 201
    validate(instance=response_json, schema=schema_for_validate)
    assert response_json['name'] == name
    assert response_json['job'] == job


def test_put_update_user():
    user_id = 10
    name = "morpheus"
    job = "zion resident"
    body = {
        "name": name,
        "job": job
    }
    schema_for_validate = load_schema('put_update_user')
    url = f'{BASE_URL}/api/users/{user_id}'

    response = requests.put(url=url, json=body)
    response_json = response.json()

    assert response.status_code == 200
    validate(instance=response_json, schema=schema_for_validate)
    assert response_json['name'] == name
    assert response_json['job'] == job


def test_delete_user():
    user_id = 1
    url = f'{BASE_URL}/api/users/{user_id}'

    response = requests.delete(url=url)

    assert response.status_code == 204
    assert not response.text


def test_register_new_user():
    user_email = "eve.holt@reqres.in"
    password = "12345"
    user_id = None
    body = {
        "email": user_email,
        "password": password
    }
    url = f'{BASE_URL}/api/register'
    schema_for_validate = load_schema('post_register_user')

    try:
        response = requests.post(url=url, json=body)
        response_json = response.json()

        assert response.status_code == 200
        user_id = response_json['id']
        validate(instance=response_json, schema=schema_for_validate)

    finally:
        # если пользователь создан, нужно удолить ТД для следующего прогона (представляем, что api работает логично)
        if user_id:
            requests.delete(url=f'{BASE_URL}/api/users/{user_id}')


def test_negative_create_empty_user():
    url = f'{BASE_URL}/api/users'

    response = requests.post(url=url)

    # тест ожидаемо будет падать в ошибку, т.к. текущее api позволяет создать пользователя без данных
    assert response.status_code == 400, (f'Пользователь с пустыми данными не должен создаваться. '
                                         f'Актуальный status_code: {response.status_code}')


def test_negative_get_not_found_user():
    user_id = 'twenty'
    url = f'{BASE_URL}/api/users/{user_id}'

    response = requests.get(url=url)
    response_json = response.json()

    assert response.status_code == 404
    assert response_json == {}
