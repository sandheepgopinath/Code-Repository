import requests
import datetime as dt
import time
from fake_useragent import UserAgent
ua = UserAgent()
import os
from twilio.rest import Client

minute=dt.datetime.now().minute


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACbfc46c01d77a17c3018a39b4953cc607"
auth_token = '53cbcf7d5d3a8124dee06351d1336410'
client = Client(account_sid, auth_token)


headers = {'User-Agent':ua.random}
pin=[682002,682023,682016,683101,683580,682041,682020,682025,682027]

#print('Enter the number of days to scan')
num=3

while 1:

    if dt.datetime.now().minute==minute:

        today=dt.datetime.now()
        today=today+dt.timedelta(days=1)
        for i in range(int(num)):
            today=today+dt.timedelta(days=1)
            for pinCode in pin:
                day=today.day
                month=today.month
                year=today.year
                t_stamp=str(day)+'-'+str(month)+'-'+str(year)
                url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+str(pinCode)+'&date='+str(t_stamp)
                r=requests.get(url,headers=headers)
                #print(url)
                data=r.json()
                flag=0
                try:

                    if len(data['sessions'])>0:
                        for j in range(len(data['sessions'])):
                            if len(data['sessions'])>0:
                                if int(data['sessions'][j]['available_capacity_dose1'])>0 | int(data['sessions'][j]['available_capacity_dose2'])>0:
                                    if data['sessions'][j]['vaccine']=='COVAXIN':
                                        textBody=str(data['sessions'][j]['vaccine'])+' Available at '+str(data['sessions'][j]['block_name'])+','+str(data['sessions'][j]['district_name'])+' for age above '+str(data['sessions'][j]['min_age_limit'])+' on '+data['sessions'][j]['date']
                                        textBody+=' Dose 1 Capacity available: '+str(data['sessions'][j]['available_capacity_dose1'])
                                        textBody+=' Dose 2 Capacity available: '+str(data['sessions'][j]['available_capacity_dose2'])
                                        textBody+=' Fee:'+str(data['sessions'][j]['fee'])+' INR'

                                        message = client.messages \
                                                        .create(
                                                             body=textBody,
                                                             from_='+14807127314',
                                                             to='+918921725127'
                                                         )

                                        message.sid
                                        print('Sent data')
                                        flag=1
                except:
                    message = client.messages \
                                        .create(
                                                body="Code Error",
                                                from_='+14807127314',
                                                to='+918921725127'
                                                )

                    message.sid
                    
                    
                if flag==0:
                    pass
                    #print('No vaccine available on '+t_stamp+' at '+str(pinCode))
        minute=minute+1
        print(dt.datetime.now())

