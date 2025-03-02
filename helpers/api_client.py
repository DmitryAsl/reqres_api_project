from requests import request
import allure
from allure_commons.types import AttachmentType
import json
import logging


def api_request(method, url, **kwargs):
    response = request(method=method, url=url, **kwargs)

    attach_request(response)
    attach_response(response)

    logging_info = get_logging_info(response)
    logging.info(logging_info)

    return response


def get_logging_info(response):
    logging_info = {
        'method': response.request.method,
        'url': response.url,
        'status_code': response.status_code,
        'body': response.json() if response.text else ''
    }
    return logging_info


def attach_request(response):
    request_prepare = response.request
    request_data = {
        'method': request_prepare.method,
        'url': request_prepare.url,
        'headers': dict(request_prepare.headers),
        'body': json.loads(request_prepare.body.decode('utf-8')) if request_prepare.body else '',
    }
    allure.attach(body=json.dumps(request_data, indent=4, ensure_ascii=True), name='Request',
                  attachment_type=AttachmentType.TEXT, extension='json')


def attach_response(response):
    response_data = {
        'status_code': response.status_code,
        'headers': dict(response.headers),
        'body': response.json() if response.text else ''
    }
    allure.attach(body=json.dumps(response_data, indent=4, ensure_ascii=True), name="Response",
                  attachment_type=AttachmentType.TEXT, extension='json')
