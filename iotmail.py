import smtplib 
import firebase
from firebase_admin import firestore
def sendMail(sensorname,sensorvalue):
    db = firestore.client()
    subscribers = db.collection('subscribers').get()
    mailing_list =[]
    for person in subscribers:
        print(u'{} => {}'.format(person.id, person.to_dict()))
        mailing_list.append(person.to_dict().get('email'))
    
    
    for mail in mailing_list:
        symbol_pos=mail.find("@")
        dotcom_pos=mail.find(".com")
        sp=mail[symbol_pos+1:dotcom_pos]
        
        try:
            if sp=='outlook':
                server=smtplib.SMTP('smtp-mail.outlook.com',587)
                server.ehlo()
                server.starttls()
                server.login('jasdeeps396@outlook.com','jasdeep@123')
                msg='Subject: {}\n\n Value is dangerous:  {}, run for your life'.format(sensorname,sensorvalue)
                server.sendmail('jasdeeps396@outlook.com',mail,msg)
                server.quit()
                print("mail is successfully sent to the receiver")
            
            else:
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.login('jasdeeps396@gmail.com','jasdeep@123')
                msg='Subject: {}\n\n Value is dangerous:  {}, run for your life'.format(sensorname,sensorvalue)
                server.sendmail('jasdeeps396@gmail.com',mail,msg)
                server.quit()
                print("mail is successfully sent to the receiver")
           
            
        except Exception as e: 
                print(e)
