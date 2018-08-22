import requests
import json
import csv
import time
##大盤日資料
## 列出要的資料
def printData(start_year,end_year):
	if(start_year>end_year):
		print("開始大於結束")
	else:
		month=["01","02","03","04","05","06","07","08","09","10","11","12"]
		alldata=[["日期","開盤指數","最高指數","最低指數","收盤指數"]]
		for i in range(start_year,end_year+1):
			for j in range(len(month)):
				res=requests.get("http://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date="+str(i)+month[j]+"01")
				if('data' in res.json()):
					alldata += res.json()['data']
					time.sleep(0.1)
		#民國改西元(100年以前第一個字元是空白沒差)
		for elements in alldata[1:]:
			elements[0]=elements[0].replace(elements[0][0:3], str(int(elements[0][0:3])+ 1911))

		for elements in alldata:
			print(elements)

##儲存要的資料
def writeData(start_year,end_year):
	if(start_year>end_year):
		print("開始大於結束")
	else:
		month=["01","02","03","04","05","06","07","08","09","10","11","12"]
		f=open("export.csv","w")
		alldata=[["日期","開盤指數","最高指數","最低指數","收盤指數"]]
		for i in range(start_year,end_year+1):
			for j in range(len(month)):
				res=requests.get("http://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date="+str(i)+month[j]+"01")
				if('data' in res.json()):
					alldata += res.json()['data']
					time.sleep(0.1)
		#民國改西元(100年以前第一個字元是空白沒差)
		for elements in alldata[1:]:
			elements[0]=elements[0].replace(elements[0][0:3], str(int(elements[0][0:3])+ 1911))
			
		writer = csv.writer(f)
		writer.writerows(alldata)
		f.close
		print("已寫完所有資料")
		
	


