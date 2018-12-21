#!/usr/bin/python3

try:
    from plyvel import DB, Error as plError
    import re
    from bs4 import BeautifulSoup
    from requests import post
    from validate import validate_phone_number
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def __format_db_query_result__(data):
    resp = {}
    if(data):
        for i in data.split(';'):
            tmp = i.split(':')
            resp.update({tmp[0]: tmp[1]})
    return resp


def __format_db_entry__(data):
    regex1 = re.compile(r'mobile', flags=re.I)
    regex2 = re.compile(r'empty', flags=re.I)
    tmp = []
    for i, j in data.items():
        if(regex1.match(i)):
            continue
        if(regex2.match(j)):
            continue
        tmp.append('{}:{}'.format(i.strip(), j.strip()))
    return ';'.join(tmp)


def __parse_response__(content):
    parsed_content = {}
    try:
        handle = BeautifulSoup(content, features='lxml')
        target = handle.find('div', attrs={'class': 'alert-msg alert-success d-flex'})
        for i in target.findAll('li'):
            parsed_content.update({i.find('label').getText().rstrip(':'): i.find('b').getText()})
    except Exception as e:
        parsed_content = {'error': str(e)}
    return parsed_content


def __get_response__(base_url, data):
    try:
        resp = post(base_url, data=data)
        return __parse_response__(resp.content)
    except Exception as e:
        return {'error': str(e)}


def fetch_record(db_name, mobile=''):
    '''
        If no argument passed for `mobile`, all available database records are fetched.
    '''
    resp = []
    try:
        db_handle = DB(db_name, create_if_missing=True)
        if(mobile):
            if(not validate_phone_number(mobile)):
                db_handle.close()
                return [{'error': '10 digit Indian mobile number required'}]
            resp.append({mobile: __format_db_query_result__(db_handle.get(('+91'+mobile).encode('utf-8'), b'').decode('utf-8'))})
        else:
            itr = db_handle.iterator()
            for i, j in itr:
                resp.append({i.decode('utf-8'): __format_db_query_result__(j.decode('utf-8'))})
            itr.close()
        db_handle.close()
    except plError as e:
        resp = [{'error': str(e)}]
    except Exception as e:
        resp = [{'error': str(e)}]
    return resp


def store_record(mobile, data, db_name):
    '''
        I'm using levelDB, for storing records.
    '''
    resp = {'status': 'success'}
    try:
        db_handle = DB(db_name, create_if_missing=True)
        text = __format_db_entry__(data)
        if(text):
            db_handle.put(('+91'+mobile).encode('utf-8'), text.encode('utf-8'))
        db_handle.close()
    except plError as e:
        resp = {'status': str(e)}
    except Exception as e:
        resp = {'status': str(e)}
    return resp


def get_info(mobile_num, base_url='http://www.way2sms.com/Location'):
    '''
        Parsed response in form of python dict, holding found info, is returned.
    '''
    if(not validate_phone_number(mobile_num)):
        return {'error': '10 digit Indian mobile number required'}
    return __get_response__(base_url, [('mobile', mobile_num)])


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
    exit(0)
