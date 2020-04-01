
import speech_recognition as sr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email
import imaplib
from gtts import gTTS
import os, time
from bs4 import BeautifulSoup 

#fetch project name
tts = gTTS(text="Project: Voice based Email for blind", lang='en')
tts.save("name.mp3")
os.system("name.mp3") 
time.sleep(4)



#login from os
login = os.getlogin
print ("You are logging from : "+login())

#choices
print ("1. compose a mail.")
tts = gTTS(text="  option 1 compose a mail.", lang='en')
tts.save("hello.mp3")
os.system("hello.mp3") 
time.sleep(2)


print ("2. Check your inbox")
tts = gTTS(text="  option 2 Check your inbox", lang='en')
tts.save("hello.mp3")
os.system("hello.mp3") 
time.sleep(2)



tts = gTTS(text="Your choice ", lang='en')
tts.save("hello.mp3")
os.system("hello.mp3") 
time.sleep(2)

r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Your choice:")
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)
    print ("ok done!!")
    text=r.recognize_google(audio)
    try:
        print ("You said : "+text)
    except:
        print("Error occured")
        
if text == '1' or text == 'One' or text == 'one':
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print ("Your message :")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,)
        print ("ok done!!")
        text1=r.recognize_google(audio)
        print ("You said : "+text1)
        msg = text1
    msg = MIMEMultipart()
    message = text1

    password = "george112233"
    msg['From'] = "georgejoseph16.gj@gmail.com"
    msg['To'] = "dillibabua0800@gmail.com"
    msg['Subject'] = "mail for blind"
    
    msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    server.login(msg['From'], password)
    
    
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
    tts = gTTS(text="Mail is sent succesfully :", lang='en') 
    tts.save("succ.mp3")
    os.system("succ.mp3")
 
    
if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' :
    
      
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
    unm = "georgejoseph16.gj@gmail.com"
    psw = "george112233"
    mail.login(unm,psw)  
    stat, total = mail.select('Inbox') 
    print ("Number of mails in your inbox :"+str(total))
    tts = gTTS(text="Total mails are :"+str(total), lang='en') 
    tts.save("total.mp3")
    os.system("total.mp3") 
    time.sleep(2)

    
    #unseen mails
    unseen = mail.search(None, 'UnSeen') # unseen count
    print ("Number of UnSeen mails :"+str(unseen))
    tts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
    tts.save("unseen.mp3")
    os.system("unseen.mp3") 
    time.sleep(3)

    #search mails
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
    raw_email = email_data[0][1].decode("utf-8") #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    tts.save("mail.mp3")
    os.system("mail.mp3") 
    time.sleep(3)

    #Body part of mails
    stat, total1 = mail.select('Inbox')
    stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print ("Body :"+txt)
    tts = gTTS(text="Body: "+txt, lang='en')
    tts.save("body.mp3")
    os.system("body.mp3") 
    time.sleep(3)
    mail.close()
    mail.logout()
    try:
       
       mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
       mail.login("georgejoseph16.gj@gmail.com","george112233")
       mail.select('inbox')
       type, data = mail.search(None, 'ALL')
       mail_ids = data[0]
       id_list = mail_ids.split()   
       first_email_id = int(id_list[0])
       latest_email_id = int(id_list[-1])
       for i in range(latest_email_id,first_email_id, -1):
           typ, data = mail.fetch(i, '(RFC822)' )
           for response_part in data:
               if isinstance(response_part, tuple):
                   msg = email.message_from_string(response_part[1])
                   email_subject = msg['subject']
                   email_from = msg['from']
                   print ('From : ' + email_from + '\n')
                   print ('Subject : ' + email_subject + '\n')
    except Exception :
        print("Error")
