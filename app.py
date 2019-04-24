import subprocess as sp
from flask import Flask, render_template,redirect,request,session,url_for,jsonify
from datetime import datetime
import firebase
from firebase_admin import auth, firestore
from serial_grab import getSensors

secret_key='kyabaath'

app = Flask(__name__)
db = firestore.client()




@app.route('/')
def index():
    sensor_ref = db.collection('sensors').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(12).get()
    mq135values=[]
    mq135labels=[]
    mq7values=[]
    mq2values=[]
    pm2_5values=[]
    for item in sensor_ref:
        dict_item = item.to_dict()
        time=datetime.fromtimestamp(dict_item['timestamp']).strftime("%a %I:%M %p ")
        mq135labels.append(time)
        mq135values.append(dict_item['mq135'])
        mq7values.append(dict_item['mq7'])
        mq2values.append(dict_item['mq2']) 
        # pm2_5values.append(dict_item['pm25'])
    mq135labels.reverse()
    mq135values.reverse()
    mq7values.reverse()
    mq2values.reverse()
    # pm2_5values.reverse()
    if request.method=="POST":
        return redirect(url_for('/'))
    return render_template('index.html',dashactive="active",mqlabels = mq135labels ,mq135values = mq135values,mq7values = mq7values,mq2values=mq2values,pm2_5values=pm2_5values)
@app.route('/bar')
def bar():
    sensor_ref = db.collection('sensors').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(12).get()
    mq135values=[]
    mq135labels=[]
    mq7values=[]
    mq2values=[]
    pm2_5values=[]
    for item in sensor_ref:
        dict_item = item.to_dict()
        time=datetime.fromtimestamp(dict_item['timestamp']).strftime("%a %I:%M %p ")
        mq135labels.append(time)
        mq135values.append(dict_item['mq135'])
        mq7values.append(dict_item['mq7'])
        mq2values.append(dict_item['mq2']) 
        # pm2_5values.append(dict_item['pm25']) 
    mq135labels.reverse()
    mq135values.reverse()
    mq7values.reverse()
    mq2values.reverse()
    # pm2_5values.reverse()  
    if request.method=="POST":
        return redirect(url_for('/bar'))
    return render_template('bar.html',dashactive="active",mqlabels = mq135labels ,mq135values = mq135values,mq7values = mq7values,mq2values=mq2values,pm2_5values=pm2_5values)


@app.route('/pie')
def pie():
    sensor_ref = db.collection('sensors').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1).get()
    mq135values=[]
    mq135labels=[]
    mq7values=[]
    mq2values=[]
    pm2_5values=[]
    for item in sensor_ref:
        dict_item = item.to_dict()
        time=datetime.fromtimestamp(dict_item['timestamp']).strftime("%a %I:%M %p ")
        mq135labels.append(time)
        mq135values.append(dict_item['mq135'])
        mq7values.append(dict_item['mq7'])
        mq2values.append(dict_item['mq2']) 
        # pm2_5values.append(dict_item['pm25']) 
    mq135labels.reverse()
    mq135values.reverse()
    mq7values.reverse()
    mq2values.reverse()
    # pm2_5values.reverse()   
    if request.method=="POST":
        return redirect(url_for('/pie'))
    return render_template('pie.html',dashactive="active",mqlabels = mq135labels ,mq135values = mq135values,mq7values = mq7values,mq2values=mq2values,pm2_5values=pm2_5values)

@app.route('/admin',methods=['POST','GET'])
def admin():
    if request.method=="POST":
        return redirect(url_for('admin'))
    subscribers = db.collection('subscribers').get()
    subs ={}
    for person in subscribers:
        print(u'{} => {}'.format(person.id, person.to_dict()))
        subs[person.id]=person.to_dict()
    return render_template('admin_dashboard.html',adminactive="active",subs=subs)


@app.route('/subscribe',methods=['POST','GET'])
def subscribe():
    msg=""
    if request.method=="POST":
        name = request.form.get('name')
        email = request.form.get('email')
        created =datetime.now()
        if len(name)>0 and len(email)>0 and '@' in email:
            ref = db.collection('subscribers').document()
            ref.set({
                'email':email,
                'name':name,
                'created':int(datetime.timestamp(created))
                   })
            return redirect(url_for('subscribe'))
        else:
            msg="invalid details!"
    subscribers = db.collection('subscribers').get()
    subs ={}
    for person in subscribers:
        print(u'{} => {}'.format(person.id, person.to_dict()))
        subs[person.id]=person.to_dict()
    return render_template('subscribe.html',subscribeactive="active",subs=subs,msg=msg)



@app.route('/notifications')
def noti():
	return render_template('notifications.html',notifactive="active")




if __name__ == '__main__':

	app.run(host='127.0.0.1',port=8000, debug=True,threaded=True)
