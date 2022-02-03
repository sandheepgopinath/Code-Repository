import requests
import datetime as dt
import time

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

print('Enter the Pincode')
pinCode=input()
print('Enter the number of days to scan')
num=input()

print('\n')

today=dt.datetime.now()
for i in range(int(num)):
    day=today.day
    month=today.month
    year=today.year
    t_stamp=str(day)+'-'+str(month)+'-'+str(year)
    url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+str(pinCode)+'&date='+str(t_stamp)
    r=requests.get(url,headers=headers)
    data=r.json()
    flag=0
    try:
        
        if len(data['sessions'])>0:
            for j in range(len(data['sessions'])):
                if len(data['sessions'])>0:
                    if int(data['sessions'][j]['available_capacity_dose1'])>=0 | int(data['sessions'][j]['available_capacity_dose2'])>=0:
                        print(data['sessions'][j]['vaccine'],'Available at',data['sessions'][j]['block_name']+','+data['sessions'][j]['district_name'],'for age above '+str(data['sessions'][j]['min_age_limit']),' on '+data['sessions'][j]['date'])
                        print('Dose 1 Capacity available: ',data['sessions'][j]['available_capacity_dose1'])
                        print('Dose 2 Capacity available: ',data['sessions'][j]['available_capacity_dose2'])
                        print('Fee:',data['sessions'][j]['fee'],' INR')
                        print('\n')
                        flag=1
    except:
        print('Invalid Pincode')
    if flag==0:
        print('No vaccine available on '+t_stamp)
    today=today+dt.timedelta(days=1)
