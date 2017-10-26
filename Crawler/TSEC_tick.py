import requests
import pandas as pd
import time
import os
print("##  write_tick_data_to_each_file(start,end)\tdateformat:'yyyymmdd'")
print("##  write_tick_data_to_one_file(start,end)\tdateformat:'yyyymmdd'")
print("##  write_min_data_to_one_file(start,end)\tdateformat:'yyyymmdd'")

def write_tick_data_to_each_file(inputTime1,inputTime2):
    nowTime=int(time.strftime("%Y%m%d"))
    path = "./write_tick_data_to_each_file"
    if not os.path.exists(path):
        os.makedirs(path)
    if type(inputTime1)!=int and type(inputTime2)!=int and inputTime2>inputTime1:
        print("別耍智障")
    else:
        if 20041015<inputTime1<=nowTime and 20041015<inputTime2<=nowTime :
            data=[]
            fields=[]
            inputYear1=int(str(inputTime1)[0:4])
            inputMonth1=int(str(inputTime1)[4:6])
            inputDay1=int(str(inputTime1)[6:8])
            inputYear2=int(str(inputTime2)[0:4])
            inputMonth2=int(str(inputTime2)[4:6])
            inputDay2=int(str(inputTime2)[6:8])
            t1 = (inputYear1,inputMonth1,inputDay1, 0, 0, 0, 0, 0, 0)
            t2 = (inputYear2,inputMonth2,inputDay2, 0, 0, 0, 0, 0, 0)
            days=int((time.mktime(t2)-time.mktime(t1))/86400)+1
            start=time.mktime(t1)
            print(days,"天")
            for i in range(days):
                res=requests.get("http://www.twse.com.tw/exchangeReport/MI_5MINS_INDEX?date="+time.strftime("%Y%m%d",time.localtime(start)))
                print(res.url)
                if(res.json()['stat']=='OK'):
                    fields=list(res.json()['fields'])
                    data = res.json()['data']
                    date = res.json()['date']
                    df = pd.DataFrame(data,columns=fields)
                    df.to_csv(path+"/"+date+"每5秒指數統計.csv",sep=',')
                else:
                    time.sleep(0.1)
                start+=+86400
                
            print("檔案以寫入write_tick_data_to_each_file資料夾")
        else:
            print("時間格式有錯")
            print("或著不在'20141015'和今天'"+str(nowTime)+"'中")

def write_tick_data_to_one_file(inputTime1,inputTime2):
    nowTime=int(time.strftime("%Y%m%d"))
    path = "./write_tick_data_to_one_file"
    if not os.path.exists(path):
        os.makedirs(path)
    if type(inputTime1)!=int and type(inputTime2)!=int :
        print("別耍智障")
    else:
        if 20041015<inputTime1<=nowTime and 20041015<inputTime2<=nowTime :
            data=[]
            alldata=[]
            fields=[]
            df=pd.DataFrame()
            inputYear1=int(str(inputTime1)[0:4])
            inputMonth1=int(str(inputTime1)[4:6])
            inputDay1=int(str(inputTime1)[6:8])
            inputYear2=int(str(inputTime2)[0:4])
            inputMonth2=int(str(inputTime2)[4:6])
            inputDay2=int(str(inputTime2)[6:8])
            t1 = (inputYear1,inputMonth1,inputDay1, 0, 0, 0, 0, 0, 0)
            t2 = (inputYear2,inputMonth2,inputDay2, 0, 0, 0, 0, 0, 0)
            days=int((time.mktime(t2)-time.mktime(t1))/86400)+1
            start=time.mktime(t1)
            print(days,"天")
            for i in range(days):
                res=requests.get("http://www.twse.com.tw/exchangeReport/MI_5MINS_INDEX?date="+time.strftime("%Y%m%d",time.localtime(start)))
                print(res.url)
                if(res.json()['stat']=='OK'):
                    fields=list(res.json()['fields'])
                    fields.insert(0,"日期")
                    data = res.json()['data']
                    date = res.json()['date']
                    for j in range(len(data)):
                        data[j].insert(0,date)
                    alldata+=data
                start+=+86400
                time.sleep(0.1)
            df = pd.DataFrame(alldata,columns=fields)
            df.to_csv(path+"/每5秒指數統計.csv",sep=',')
            print("檔案以寫入write_tick_data_to_one_file資料夾")
        else:
            print("時間格式有錯")
            print("或著不在'20141015'和今天'"+str(nowTime)+"'中")
            
def write_min_data_to_one_file(inputTime1,inputTime2):
    nowTime=int(time.strftime("%Y%m%d"))
    path = "./write_min_data_to_one_file"
    if not os.path.exists(path):
        os.makedirs(path)
    if type(inputTime1)!=int and type(inputTime2)!=int :
        print("別耍智障")
    else:
        if 20041015<inputTime1<=nowTime and 20041015<inputTime2<=nowTime :
            data=[]
            alldata=[]
            fields=[]
            df=pd.DataFrame()
            inputYear1=int(str(inputTime1)[0:4])
            inputMonth1=int(str(inputTime1)[4:6])
            inputDay1=int(str(inputTime1)[6:8])
            inputYear2=int(str(inputTime2)[0:4])
            inputMonth2=int(str(inputTime2)[4:6])
            inputDay2=int(str(inputTime2)[6:8])
            t1 = (inputYear1,inputMonth1,inputDay1, 0, 0, 0, 0, 0, 0)
            t2 = (inputYear2,inputMonth2,inputDay2, 0, 0, 0, 0, 0, 0)
            days=int((time.mktime(t2)-time.mktime(t1))/86400)+1
            start=time.mktime(t1)
            print(days,"天")
            for i in range(days):
                res=requests.get("http://www.twse.com.tw/exchangeReport/MI_5MINS_INDEX?date="+time.strftime("%Y%m%d",time.localtime(start)))
                print(res.url)
                if(res.json()['stat']=='OK'):
                    fields=list(res.json()['fields'])
                    fields.insert(0,"日期")
                    data = res.json()['data']
                    date = res.json()['date']
                    for j in data:
                        if j[0][-2::1] == "00":
                            data.remove(j)
                            j.insert(0,date)
                            alldata.append(j)
                start+=+86400
                time.sleep(0.1)
            df = pd.DataFrame(alldata,columns=fields)
            df.to_csv(path+"/每分指數統計.csv",sep=',')
            print("檔案以寫入write_min_data_to_one_file資料夾")
        else:
            print("時間格式有錯")
            print("或著不在'20141015'和今天'"+str(nowTime)+"'中")
            