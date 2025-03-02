import allure
from allure import step
import pytest
from jsonschema import validate
from helpers.load_schema import load_schema
from helpers.api_client import api_request
from tests.config import BASE_URL
from helpers.data_provider import DataProvider

@pytest.mark.positive
@pytest.mark.api
@allure.title('Тест на проверку регистрации нового пользователя')
def test_register_new_user():
    param = DataProvider.get('', 'registration', 'new_user')
    user_id = None
    url = f'{BASE_URL}/api/register'
    schema_for_validate = load_schema('post_register_user')

    try:
        with step('Запрос на регистрацию нового пользователя'):
            response = api_request(method='POST', url=url, json=param['body'])
            response_json = response.json()

        with step('Проверка результата'):
            assert response.status_code == param['status_code']
            user_id = response_json['id']
            validate(instance=response_json, schema=schema_for_validate)

    finally:
        if user_id:
            with step('Удаление пользователя для следующего прогона'):
                api_request(method='DELETE', url=f'{BASE_URL}/api/users/{user_id}')

@pytest.mark.negative
@pytest.mark.api
@allure.title('Тест на проверку регистрацию пользователя без данных')
def test_negative_register_new_empty_user():
    param = DataProvider.get('', 'registration', 'new_empty_user')
    url = f'{BASE_URL}/api/users'

    with step('Запрос на регистрацию пользователя без body'):
        response = api_request(method='POST', url=url)

    with step('Проверка результата'):
        # тест ожидаемо будет падать в ошибку, т.к. текущее api позволяет создать пользователя без данных
        assert response.status_code == param['status_code'], f'Пользователь с пустыми данными не должен создаваться.'
