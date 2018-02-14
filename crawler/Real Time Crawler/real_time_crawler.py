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
	##TODO 0:睡覺測試
	##TODO 1:觸價寄信
'''

def main():

	#init
	count,url,export_csv=init_parm()
	init_header(export_csv)
	#Every 5 secs check
	while 1:
		if int(time.strftime('%S'))%5==0:
			count,url,export_csv=check_regular_or_after_hour(count,url,export_csv)
			count=write_data(count,url,export_csv)
			time.sleep(3.9)


def init_parm():
	'''
		Initialize url,except_csv,count
	'''

	url="http://info512ah.taifex.com.tw/Future/FusaQuote_Norl.aspx"
	export_csv='夜盤_'+str(time.strftime('%Y%m%d'))+'_tx.csv'
	count=1

	return count,url,export_csv


def check_regular_or_after_hour(count,url,export_csv):
	'''
		Check contract is day or night
	'''
	if ((time.localtime().tm_hour==5 and time.localtime().tm_min==0 and time.localtime().tm_sec==5) or 
		(time.localtime().tm_hour==13 and time.localtime().tm_min==45 and time.localtime().tm_sec==0)):
		print("睡覺覺時間")
		while(1):
			if ((time.localtime().tm_hour==8 and time.localtime().tm_min==44 and time.localtime().tm_sec==55) or 
				(time.localtime().tm_hour==14 and time.localtime().tm_min==59 and time.localtime().tm_sec==55)):
				print("開盤啦")
				break
			
	if time.localtime().tm_hour==8 and time.localtime().tm_min==44 and time.localtime().tm_sec==55:
		count=1
		url=url1
		export_csv='日盤_'+str(time.strftime('%Y%m%d'))+'_tx.csv'
		init_header(export_csv)
	
	if time.localtime().tm_hour==14 and time.localtime().tm_min==59 and time.localtime().tm_sec==55:	
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
    

def write_data(count,url,export_csv):
	'''
		Process data
	'''

	try :
		res=requests.post(url)
		res.encoding='utf-8'
		df=pandas.read_html(res.text, attrs={'class':'custDataGrid'})[0].iloc[[2], :]
		df[14]=str(time.strftime('%Y/%m/%d %H:%M:%S'))
		if(url==url2):	# '狀態' = 夜盤
			df[1]='夜盤'
		df.to_csv(export_csv,  mode='a+', header=False, index=False)
		print('{}已寫入資料第{}次, 在時間:{}'.format(export_csv, count, time.ctime()))
		print('即時報價'+df.iloc[0,2])	# Still a dataframe after using iloc
		return count+1
	except IndexError:
		print('IndexError')
		return count+1
	except ValueError:
		print('ValueError')
		return count+1
	except requests.exceptions.ConnectionError:
		print('ConnectionError')
		return count+1
	except:
		print('UnknownError')




if __name__ == '__main__':
	main()


