#!/usr/bin/python3

try:
    from perform_post_request import post_request
    from time import time, localtime
    tm = localtime(time())
    to_date = '{}-{}-{}'.format(tm.tm_year, tm.tm_mon, tm.tm_mday)
    from validate import validate_api_key, validate_secret, validate_use_type, validate_sender_id, validate_date
except ImportError as e:
    print('[!]Module Unavialable : {}'.format(str(e)))
    exit(0)


def is_date_future(date):
    try:
        cur_date = to_date.split('-')
        target_date = date.split('-')
        if(int(target_date[0]) > int(cur_date[0])):
            return True
        elif(int(target_date[0]) == int(cur_date[0])):
            if(int(target_date[1]) > int(cur_date[1])):
                return True
            elif(int(target_date[1]) == int(cur_date[1])):
                if(int(target_date[2]) > int(cur_date[2])):
                    return True
                elif(int(target_date[2]) == int(cur_date[2])):
                    return False
                else:
                    return False
            else:
                return False
        else:
            return False
    except ValueError:
        return True
    except Exception:
        return True


def get(api_key, secret, from_date, to_date=to_date, sender_id='WAYSMS', use_type='stage', base_url='http://www.way2sms.com/api/v1/apireports'):
    if(validate_api_key(api_key) and validate_secret(secret) and validate_sender_id(sender_id) and validate_use_type(use_type) and validate_date(from_date) and validate_date(to_date)):
        if(is_date_future(from_date) or is_date_future(to_date)):
            return {'error': 'bad arguments'}
        return post_request(base_url, [('apikey', api_key), ('secret', secret), ('usetype', use_type), ('fromdate', from_date), ('todate', to_date), ('senderid', sender_id)])
    return {'error': 'bad arguments'}


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
    exit(0)