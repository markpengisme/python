# crawler
### nhk_yasashi.py
- 爬簡明日語的上課資料 
- Crawl NHK course materials
- The modules needed are `requests,os`

### TSEC_tick.py
- 爬證交所的大盤資料 
- Crawl TWSE market index
- 有分tick資料和分資料並輸出至csv 
- Have ticks data or minutes data can be output to one or more csv
- The modules needed are `requests,pandas,time,os`

### TSEC_weighted_index.py
- TSEC_tick.py的測試前身
- TSEC_tick.py older version
- The modules needed are `requests,json,csv,os`

### TX.py && TX_example_2000to2018
- 爬期交所的台指近一月的歷史資料預設3年，並輸入至csv
- Crawl Taifex's spot month index history data , and output to one csv
- TX_example_2000to2018 為輸出範例
- TX_example_2000to2018 is an output example
- The modules needed are `requests,pandas,datetime,os,csv`
- Debug modules are `traceback,sys`

### Real Time Crawler
- Crawl 5 seconds data in real time 
- Whether 'Regular' or 'After Hours'
- real_time_crawler.py