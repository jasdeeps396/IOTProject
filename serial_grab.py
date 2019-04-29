import serial
import firebase
from time import sleep
from firebase_admin import firestore
from datetime import datetime
from iotmail import sendMail


def getSensors():
    db = firestore.client()
    ser = serial.Serial('/dev/ttyACM0')
    ser.flushInput()
    print('starting..')
    while True:
        try:
            ser_bytes = ser.readline()
            decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            decoded_bytes = decoded_bytes.split(',')
            
            print('values ',decoded_bytes)
            ref = db.collection('sensors').document(str(int(datetime.timestamp(datetime.now()))))
            try:
                mq135=decoded_bytes[0]
                mq135=int(mq135)
                if mq135>300:
                    sendMail("Air Quality",mq135)
                
                ref.set({
                'mq135':mq135,
                'mq7':decoded_bytes[1],
                'mq2':decoded_bytes[2],
                'pm25':decoded_bytes[3],
                'timestamp':int(datetime.timestamp(datetime.now()))
            })
            
            except Exception as e:
                print(e)
                print("LOL")
                break

        except Exception as e:
            print(e)
            print("Keyboard Interrupt")
            break



if __name__ == '__main__':
    getSensors()
