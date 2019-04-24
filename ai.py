import pandas as pd
from datetime import datetime
import firebase
from firebase_admin import auth, firestore
import fbprophet

db =  firestore.client()

def predict():
    sensor_ref = db.collection('sensors').get()
    mq135values=[] gm_prophet = fbprophet.Prophet(changepoint_prior_scale=0.15)
    gm_prophet.fit(df)
    gm_forecast = gm_prophet.make_future_dataframe(periods=2, freq='D')
    gm_forecast = gm_prophet.predict(gm_forecast)
    print(gm_forecast)
    mq135labels=[]
    for item in sensor_ref:
        dict_item = item.to_dict()
        time=datetime.fromtimestamp(dict_item['timestamp']).strftime("%a %I:%M %p ")
        mq135labels.append(time)
        mq135values.append(dict_item['mq135'])
    df=pd.DataFrame({'ds':mq135labels,
                    'y':mq135values})
   
    return gm_forecast

