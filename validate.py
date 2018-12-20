#!/usr/bin/python3

try:
    import re
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def validate_msg(msg):
    regex = re.compile(r'^[\w\W]{1,500}', flags=re.I)
    match = regex.match(msg)
    if(match):
        return match.group()
    return ''


def validate_date(date):
    regex = re.compile(r'^(\d{4}-((0[1-9])|1[0-2])-((0[1-9])|((1|2)\d)|(3[0-1])))$')
    if(regex.match(date)):
        return True
    return False


def validate_use_type(use_type):
    regex = re.compile(r'^(stage|prod)$', flags=re.I)
    if(regex.match(use_type)):
        return True
    return False


def validate_sender_id(sender_id):
    regex = re.compile(r'^([a-z]{6})$', flags=re.I)
    if(regex.match(sender_id)):
        return True
    return False


def validate_phone_number(phone_num):
    regex = re.compile(r'^(\d{10})$')
    if(regex.match(phone_num)):
        return True
    return False


def validate_secret(secret):
    regex = re.compile(r'^([a-z0-9]{16})$', flags=re.I)
    if(regex.match(secret)):
        return True
    return False


def validate_api_key(api_key):
    regex = re.compile(r'^([a-z0-9]{32})$', flags=re.I)
    if(regex.match(api_key)):
        return True
    return False


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
    exit(0)