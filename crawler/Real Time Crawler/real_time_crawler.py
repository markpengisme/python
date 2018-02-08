import requests, pandas, csv, time, datetime
#url1="http://info512.taifex.com.tw/Future/FusaQuote_Norl.aspx"
url2="http://info512ah.taifex.com.tw/Future/FusaQuote_Norl.aspx"
export_csv=str(time.strftime('%Y%m%d')+'_tx.csv')


def main():
	count=1

	init_header()
	while 1:
		if int(time.strftime('%S'))%5==0:
		    count=write_data(count)
		    time.sleep(4)


def init_header():
	df_header=['商品', '狀態', '買價', '買量', '賣價', '賣量', '成交價', '漲跌', '振幅％', '成交量', '開盤', '最高', '最低', '參考價', '時間']
	with open(export_csv, 'w') as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow(df_header)
    

def write_data(count):
    #res1=requests.post(url1)
    res2=requests.post(url2)
    #res1.encoding='utf-8'
    res2.encoding='utf-8'
    df2=pandas.read_html(res2.text, attrs={'class':'custDataGrid'})[0].iloc[[2], :]
    df2[14]=str(time.strftime('%Y/%m/%d %H:%M:%S'))
    df2.to_csv(export_csv,  mode='a+', header=False, index=False)
    print('{}已寫入資料第{}次, 在時間:{}'.format(export_csv, count, time.ctime()))
    print('即時報價'+df2.iloc[0,2]) #Still a dataframe after using iloc
    return count+1

if __name__ == '__main__':
	main()
	##TODO 1:觸價寄信
	##TODO 2:日夜完整
