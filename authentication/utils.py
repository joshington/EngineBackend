
from django.core.mail import EmailMessage
import threading



#since sending email is aswell on the same thread we need to put it on adiff thread
class EmailThread(threading.Thread):
    def __init__(self,email):
        self.email = email 
        threading.Thread .__init__(self)#super class due to inheritance
    
    def run(self):
        self.email.send()

class Util:
    @staticmethod#helps us use the mthd without instantiating the class itself
    def send_email(data):
        email=EmailMessage(
            subject=data['email_subject'],body=data['email_body'],to=[data['to_email']]
        )
        EmailThread(email).start()