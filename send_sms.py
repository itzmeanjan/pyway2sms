#!/usr/bin/python3

try:
    from perform_post_request import post_request
    from validate import validate_api_key, validate_secret, validate_phone_number, validate_msg, validate_sender_id, validate_use_type
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def send(api_key, secret, phone, message, sender_id='WAYSMS', use_type='stage', base_url='http://www.way2sms.com/api/v1/sendCampaign'):
    if(validate_api_key(api_key) and validate_secret(secret) and validate_phone_number(phone) and validate_sender_id(sender_id) and validate_use_type(use_type)):
        message = validate_msg(message)
        return post_request(base_url, [('apikey', api_key), ('secret', secret), ('usetype', use_type), ('phone', phone), ('message', message), ('senderid', sender_id)])
    return {'error': 'bad arguments'}


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
    exit(0)
