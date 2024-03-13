import re
from rest_framework.validators import ValidationError
import requests
import threading
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
phone_number_regex = r'^\+998\d{9}$'



def check_email_or_phone(user_input):
    if re.match(email_regex, user_input) is not None:
        return "email" 
    elif re.match(phone_number_regex, user_input) is not None:
        return 'phone'
    
    else:
        data = {
            'status': False,
            'message':'Valid email or phone number was not provided'
        }
        
        raise ValidationError(data)
    


class SmsThread(threading.Thread):
    def __init__(self, sms):
        self.sms = sms
        super(SmsThread, self).__init__()
        
    def run(self):
        send_message(self.sms)
        
        
def send_message(message_text):
    url = f'https://api.telegram.org/bot7152481554:AAH-ZfJtvyFvXBPYLTTFdq9gvjDH9-nxMdg/sendMessage'
    params = {
        "chat_id": "5665497078",
        "text": message_text
    }
    response = requests.post(url, data=params)
    return response.json()


def send_sms(sms_text):
    sms_thread = SmsThread(sms_text)
    
    sms_thread.start()
    
    sms_thread.join()