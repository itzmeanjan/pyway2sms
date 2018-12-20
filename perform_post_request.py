#!/usr/bin/python3

try:
    from requests import post
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def post_request(base_url, data):
    try:
        resp = post(base_url, data=data)
        return resp.json()
    except Exception as e:
        return {'error': str(e)}


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
    exit(0)