#!/usr/bin/python3

try:
    from perform_post_request import post_request
    from validate import validate_api_key, validate_secret, validate_use_type, validate_sender_id
except ImportError as e:
    print('[!]Module Unavialable : {}'.format(str(e)))
    exit(0)


def create(api_key, secret, sender_id, use_type='stage', base_url='http://www.way2sms.com/api/v1/createSenderId'):
    if(validate_api_key(api_key) and validate_secret(secret) and validate_sender_id(sender_id) and validate_use_type(use_type)):
        return post_request(base_url, [('apikey', api_key), ('secret', secret), ('usetype', use_type), ('senderid', sender_id)])
    return {'error': 'bad arguments'}


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
    exit(0)