#basic code from https://automatetheboringstuff.com/chapter16/

#import libraries
import smtplib

#get contact from receiver_lists.txt
def recipients(receiver_lists):
    emails = []
    with open('receiver_lists.txt', mode='r', encoding='utf-8') as user_file:
        for user_info in user_file:
            emails.append(user_info.split()[0])
    return emails

#connecion with server
smtp_object = smtplib.SMTP('smtp.gmail.com',587) #change host and port number here
smtp_object.ehlo()
smtp_object.starttls()

#for hidden passwords
import getpass

#login to your email
youremail = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
smtp_object.login(youremail,password)

#send email
from_address = youremail
to_address = recipients('receiver_lists.txt')
subject = input("Enter the subject line: ")
message = input("Type your message: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

#close connection
smtp_object.quit()
