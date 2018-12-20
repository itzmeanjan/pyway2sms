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
 
 
 All responses returned from functions are python dicts. 
 
 
 There're some other submodules with main module, such as **perform_post_query** and **validate**, which are finally powering up main functionalities provided by [pyway2sms](https://www.github.com/itzmeanjan/pyway2sms/). 
 
 
 **validate** submodule validates user inputs such as, API_KEY, SECRET, USE_TYPE, TARGET_MOBILE_NUMBER( +91 is not required to be added in front of number ), SENDER_ID & DATE (in case of requesting for report of usage of API, from_date and to_date and validated).
 
 API_KEY has length of 32 and is of alphanumeric, whereas SECRET is 16 character lengthy and alphanumeric. SENDER_ID is by default 'WAYSMS', can be set to some alphabetic sequence of length 6.
 
 
 Finally thanks to **WAY2SMS**, for providing a great service at such a low price. 
 
 More info can be found [here](http://www.way2sms.com/).
 
 
 Hope it was helpful :)
