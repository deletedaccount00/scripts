from platform import system
import requests
import getpass # to input pass ( in stealth mode )
import time # 
import smtplib, ssl
import os

class email_pass:
    def __init__(self):
        port = 465
        sender_email = " " # Enter your Email here 
        pass_e = " "  # Enter your password here 
        receiver_email  = " " # Enter receiver email ( website hosting company support email )
        self.port = port
        self.pass_e = pass_e 
        self.sender_email = sender_email
        self.receiver_email = receiver_email
    



obj_email = email_pass()

message = """\
     Website is down

     """
 
def capture_os():   #Function to capture operating system name
    re = system()
    if re == 'Linux':
        os.system('clear')
    else:
        print("+ Something went wrong ")
    

def mail(): #function to send mail
    #passphrase = getpass.getpass(prompt:'Enter your Gmail password: ')
    # pas = "Null"
    # port = 465
    #sender_email = "samfortysevn@gmail.com"
    #receiver_mail = input("Send email To: ") #incase if you don' want to enter email every time , uncomment the next line and comment out this line with #
    receiver_mail = # Enter receiver email here
    print(" Sending mail from " + obj_email.sender_email + " to " + receiver_mail)
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    try: 
        with smtplib.SMTP_SSL(smtp_server, obj_email.port, context=context) as server:
            server.login(obj_email.sender_email, obj_email.pass_e)
            server.sendmail(obj_email.sender_email, obj_email.receiver_email, message)
            print("[+] Mail sent successfully ")
    except Exception as e:
        print(e)
        print("[-] Please check your internet connection ")

def requests_website():
    website_address = "http://google.com" # replace google.com with your website domain name 
    r = requests.get(website_address)
    er = r.status_code
    if (er == 200):
        print(" website is fine ")
        mail()
    else:
        print(" website is down , sending mail to hosting company in 10 sec")
        

def main_lo():
    try:
        while True:
            capture_os()
            time.sleep(20)
            requests_website()
    except KeyboardInterrupt:
        print("[+] you have pressed Keyboard key ")


if "__name__" == "__main__":
    main_lo()




