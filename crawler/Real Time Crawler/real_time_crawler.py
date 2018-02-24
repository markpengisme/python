import requests, pandas, csv, time, datetime
url1="http://info512.taifex.com.tw/Future/FusaQuote_Norl.aspx"
url2="http://info512ah.taifex.com.tw/Future/FusaQuote_Norl.aspx"


'''
	main -> init_parm -> LOOP(check_regular_or_after_hour [-> init_parm] -> write_data)
									   /|\										 |
										|										 |
										|________________________________________|
'''
'''
	##TODO 1:觸價寄信
'''

def main():

	#init
	count,url,export_csv=init_parm()
	init_header(export_csv)
	#Every 5 secs check
	while 1:
		vartime=time.localtime()
		print(vartime.tm_sec)
		if vartime.tm_sec%5==0:
			count,url,export_csv=check_regular_or_after_hour(count,url,export_csv,vartime)
			count=write_data(count,url,export_csv,vartime)
			time.sleep(4)


def init_parm():
	'''
		Initialize url,except_csv,count
	'''
	if (time.localtime().tm_hour>=8 and time.localtime().tm_min>=45) and (time.localtime().tm_hour<=13 and time.localtime().tm_min<=45):
		url=url1
	else:
		url=url2
	export_csv=str(time.strftime('%Y%m%d'))+'_tx.csv'
	count=1

	return count,url,export_csv


def check_regular_or_after_hour(count,url,export_csv,vartime):
	'''
		Check contract is day or night
	'''
	if ((vartime.tm_hour==5 and vartime.tm_min==0 and vartime.tm_sec==5) or 
		(vartime.tm_hour==13 and vartime.tm_min==45 and vartime.tm_sec==5)):
		print("睡覺覺時間")

		#sleep two day if today is Saturday
		if(datetime.date.today().isoweekday()==6)
			time.sleep(86400*2)
		while(1):
			if ((time.localtime().tm_hour==8 and time.localtime().tm_min==44 and time.localtime().tm_sec==55) or 
				(time.localtime().tm_hour==14 and time.localtime().tm_min==59 and time.localtime().tm_sec==55)):
				print("開盤啦")
				count=0
				break
			time.sleep(0.9)
			
	if vartime.tm_hour==8 and vartime.tm_min==45 and vartime.tm_sec==0:
		count=1
		url=url1
		export_csv='日盤_'+str(time.strftime('%Y%m%d'))+'_tx.csv'
		init_header(export_csv)
	
	if vartime.tm_hour==15 and vartime.tm_min==0 and vartime.tm_sec==0:	
		count=1
		url=url2
		export_csv='夜盤_'+str(time.strftime('%Y%m%d'))+'_tx.csv'
		init_header(export_csv)

	

	return count,url,export_csv


def init_header(export_csv):
	'''
		Initialize csv header
	'''
	df_header=['商品', '狀態', '買價', '買量', '賣價', '賣量', '成交價', '漲跌', '振幅％', '成交量', '開盤', '最高', '最低', '參考價', '時間']
	with open(export_csv, 'w') as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow(df_header)
    

def write_data(count,url,export_csv,vartime):
	'''
		Process data
	'''
	if count==0:
		return count
	try :
		res=requests.post(url)
		res.encoding='utf-8'
		df=pandas.read_html(res.text, attrs={'class':'custDataGrid'})[0].iloc[[2], :]
		df[14]=str(time.strftime('%Y/%m/%d %H:%M:%S',vartime))
		if url==url1:	# '狀態' 
			df[1]='日盤'
		else:
			df[1]='夜盤'
		df.to_csv(export_csv,  mode='a+', header=False, index=False)
		print('{}已寫入資料第{}次, 在時間:{}'.format(export_csv, count, time.ctime()))
		print('即時報價'+df.iloc[0,2])	# Still a dataframe after using iloc
		return count+1
	except IndexError:
		print('IndexError')
		write_error(export_csv,vartime)
		return count+1
	except ValueError:
		print('ValueError')
		write_error(export_csv,vartime)
		return count+1
	except requests.exceptions.ConnectionError:
		print('ConnectionError')
		write_error(export_csv,vartime)
		return count+1
	except:
		write_error(export_csv,vartime)
		print('UnknownError')

def write_error(export_csv,vartime):
	'''
		write When an error occurred
	'''
	df=pandas.DataFrame(columns=[i for i in range(15)],index=[0])
	df[0]='error'
	df[14]=str(time.strftime('%Y/%m/%d %H:%M:%S',vartime))
	df.to_csv(export_csv,  mode='a+', header=False, index=False)



if __name__ == '__main__':
	main()


