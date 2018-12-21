# pyway2sms
Pythonic API for accessing Way2SMS, a programmable SMS sending service in India, features.


## Points to be noted ::

  - There're main 4 features which are accessible from this API. Note that, these are currently provided services by Way2SMS.
  - You can send sms, check your way2sms wallet balance, create sender id ( for which of course you need to be a paid user ) and get report of your usage till date.
  - I've written four python script, which perform necessary tasks for you. Example usage is provided for each of them below.
  - Services are exclusively available in India.
  - Sender should be from India.
  - Recepient should also be from India.
  - You're free to send upto 10 SMSes daily at no charge.
  - SMS can be sent in 9 local languages. Find supported language list at [way2sms](http://www.way2sms.com/).
  - As Way2SMS is providing paid SMS sending service, the best way to use [pyway2sms](https://www.github.com/itzmeanjan/pyway2sms/)
  is to integrate it with your existing software. 
  - Provides a very easy to understand and use API.
  - Remember, you need to get API_KEY and SECRET, after you login at [way2sms](http://www.way2sms.com/).
  - If you want to check whether everything is working as expected, use test keys and check.
  - After successful testing you can easily generate keys for production purpose use.
  - More info [here](http://www.way2sms.com/business), for business purpose usage.
  - Pricing details are provided [here](http://www.way2sms.com/pricing).
 
 
 
 ### Example Usage of [pyway2sms](https://www.github.com/itzmeanjan/pyway2sms/) :
 
 
 #### send_sms :
 
  ```
    from pyway2sms.send_sms import send
    
    '''
      first four arguments are compulsory. 
      sender_id has a default value WAYSMS, don't change it unless you're using paid version and generated one sender_id using create_sender_id.create() 
      
      use_type is stage by default, which is to be provided for testing purposes.
      If you're using this API for final production purposes, make sure you're put use_type='prod', in parameter list of send() 
      function.
      don't change base_url, this is where request is sent.
    '''
    
    print(send('api-key', 'secret', 'target-phone-number', 'message-to-be-sent-to-target'))
    
  ```
  
  
  #### create_sender_id :
  
    ```
      from pyway2sms.create_sender_id import create
      
      '''
        3 arguments are mandatory.
        use_type is set to 'stage', which to be used for testing purposes only.
        For production purpose, make sure you set use_type='prod'.
        No need to change base_url.
      '''
      
      
      print(create('api-key', 'secret', 'sender-id-to-be-created'))
    ```
    
   
   #### get_report :
   
   
    ```
      from pyway2sms.get_report import get
      
      '''
        to_date argument has a default value of current date.
        sender_id is set to default value 'WAYSMS'.
        set use_type to 'prod', for production purpose use.
        Don't change base_url.
      '''
      
      print(get('api-key', 'secret', 'starting-date-of-report'))
    ```
    
  #### wallet :
  
  
    ```
      from pyway2sms.wallet import get_info
      
      '''
        set use_type to 'prod', for production purpose use.
        only two arguments are compulsory.
      '''
      
      print(get_info('api-key', 'secret'))
    ```
    
  
 **25 SMSes can be sent during testing period using test key and test secret, which can be obtained [here](http://www.way2sms.com/).**
 
 
 All responses returned from function calls are python dicts. 
 
 
 There're some other submodules within main module, such as **perform_post_query** and **validate**, which are finally powering up main functionalities provided by [pyway2sms](https://www.github.com/itzmeanjan/pyway2sms/). 
 
 
 **validate** submodule validates user inputs such as, API_KEY, SECRET, USE_TYPE, TARGET_MOBILE_NUMBER( +91 is not required to be added in front of number ), SENDER_ID & DATE (in case of requesting for report of usage of API, from_date and to_date and validated).
 
 API_KEY has length of 32 and is of alphanumeric, whereas SECRET is 16 character lengthy and alphanumeric. SENDER_ID is by default 'WAYSMS', can be set to some alphabetic sequence of length 6.
 
 
 ## New Feature Added ::
 
 
  Now, you can use **pyway2sms.mobile** module **to get information about certain Indian Mobile Numbers**. Feature is provided [here](http://www.way2sms.com/Location), using a Web based interface.
  
  All I've done is just fetched html page, performing post query and then parsed it using BeautifulSoup, and extracted required information from that page. 
  
  This mobile module also exposes an easy to use API, if you need to store fetched records in a local database. It stores records in a local levelDB database, using its python API, **plyvel**. You can also fetch all records or search for a certain record using mobile number stored in local database using **pyway2sms.mobile.fetch_record()** function.


 Remember, while passing mobile number you just need to pass a valid Indian Mobile Numbe( without +91 ).

 #### Example Usage of pyway2sms.mobile :
 
 
```
#!/usr/bin/python3

try:
    from sys import argv
    from subprocess import run
    from way2sms.mobile import get_info, store_record, fetch_record
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def app(db_name='mobile_number_info'):
    run('clear')
    if(len(argv) != 2):
        print('[+]Usage : {0} \'XXXXXXXXXX\' | f\n\nE.g.\t{0} 8945904746\n\t{0} f,\twhere f = fetch i.e. fetches all stored records\n'.format(argv[0]))
        return
    arg = argv[1]
    if(arg.isalpha()):
        if(arg.lower() != 'f'):
            print('[!]Bad argument :/')
            return
        print('[+]Available records ...\n')
        for i in fetch_record(db_name):
            print(i)
        print('\n')
        return
    mobile_num = arg  # mobile number should be 10 digit Indian mobile number
    print('[+]Finding ...')
    resp = get_info(mobile_num)  # fetched response
    if(resp.get('error')):
        print(resp)
        print(fetch_record(db_name, mobile=mobile_num))
        return
    print(resp)
    print(store_record(mobile_num, resp, db_name))
    return


if __name__ == '__main__':
    try:
        app()
    except KeyboardInterrupt:
        print('\n[!]Terminated')
    finally:
        exit(0)

```

You can just copy aforementioned code and put it in a file outside **pyway2sms** directory.
Make it executable using 

```
  >> chmod +x file_name.py
```
Then run it using 

```
  >> ./file_name.py f # which fetches all records
  >> ./file_name.py XXXXXXXXXX # fetches available information from Way2SMS and stores them in local database
```

Before you copy the code and put it in a file, make sure you have cloned this repo using,
```
  >> git clone https://www.github.com/itzmeanjan/pyway2sms/
```

And use python3. I've tested it on Ubuntu, Fedora, Arch and Mint, where it works fine. You need to install plyvel, python API for accessing levelDB using,
```
  >> pip3 install plyvel --user
```

Alright, now I need to tell you something really important before you start using this module and have fun. 

Don't ever use this program for automating your queries, which might lead to unexpected load at Way2SMS servers and you might get banned.

**This program is purely written with no intension of using someone else's private information. I've just created a programmatic way of fetching query result from Way2SMS. This is just for educational purpose. Any data returned is not anyhow guaranteed to be correct. !!!Use at your own risk!!!**


 Finally thanks to **WAY2SMS**, for providing such a great service. 
 

 More info can be found [here](http://www.way2sms.com/).


 Hope it was helpful :)
