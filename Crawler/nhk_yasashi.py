##簡明日語mp3,pdf下載

import requests,os
path = "./簡明日語"

#沒有資料夾就創造一個
if not os.path.exists(path):
    os.makedirs(path)
    
#1~48課
for i in range(1,49):
    url_1= 'https://www.nhk.or.jp/lesson/update/pdf/le'+str(i)+'_zh_t.pdf'
    url_2= 'https://www.nhk.or.jp/lesson/chinese/learn/mp3/0'+str(i)+'-zh-le_01.mp3'
    r=requests.get(url_1)
    with open('./簡明日語/lesson_'+str(i)+'.pdf', 'wb') as f:
        f.write(r.content)
    r=requests.get(url_2)
    with open('./簡明日語/lesson_'+str(i)+'.mp3', 'wb') as f:
        f.write(r.content)
    print("第{lesson}課已下載".format(lesson=str(i)))