import sys
from botconversa_api import *

tel1 = sys.argv[1]
tel = 5511974412888
apikey = ''
first_name = sys.argv[2]
last_name = sys.argv[3]
name =  first_name + ' ' + last_name
msg = f'Olá {name}, estamos felizes por você criar sua conta conosco'
id = 410969119


response = get_subscriber_by_phone(tel, apikey)
if response:
    send_message_to_subscriber(response['id'], "text", msg, apikey)
else:
    sub = create_subscriber(tel, first_name, last_name, apikey)
    send_message_to_subscriber(id, "text", msg, apikey)

