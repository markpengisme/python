from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from argparse import ArgumentParser
import twstock
app = Flask(__name__)

line_bot_api = LineBotApi("Channel access token")
handler = WebhookHandler("Channel secret")
stock_list={}
for key, value in twstock.codes.items():
    stock_list[value.name]=value.code

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)


    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    #line_webhookverify
    if(event.reply_token==("00000000000000000000000000000000" or "ffffffffffffffffffffffffffffffff")):
        print("webhook verify")
        return



    if(event.message.text=='個股即時價格和最佳五檔'):
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="歡迎來到股票價格查詢\n請輸入股票代號(0~99999)"))
    elif(event.message.text=='個股健檢'):
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="歡迎來到股票健檢\n請輸入股票正確名稱"))
    elif(event.message.text=='免責聲明'):
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="免責聲明: 投資涉及風險，證券價格有時會大幅波動，價格可升亦可跌，更可變 得毫無價值。投資未必一定能夠賺取利潤，反而可能會招致損失，往績數字並非 未來表現的指標。投資前應先閱讀有關產品的發售文件、財務及相關的風險聲明， 並應就本身的財政、其他狀況及需要詳細考慮並考慮決定投資是否切合本身特定 的投資需要。若有需要更應諮詢獨立之法律、稅務、財政及其他專業意見，方可 作出有關投資決定。"))


    #功能1即時報價 
    #stock代號0~100000  
    elif(event.message.text.isnumeric()and int(event.message.text)>0 and int(event.message.text)<99999):
        #取得即時資料並檢查有無此股票
        realtime=twstock.realtime.get(event.message.text)
        if(realtime['success']!=True ):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="查無此股票"))
            return
        else:
            line_bot_api.reply_message(
                event.reply_token,
                [TextSendMessage(text=realtime['info']['name']+"的即時報價:"+realtime['realtime']['latest_trade_price']),
                TextSendMessage(text="最佳五檔\n" + "買價" + str(realtime['realtime']['best_bid_price']) + "\n賣價" + str(realtime['realtime']['best_ask_price']))])



    #功能2個股健檢
    elif(event.message.text in stock_list):
        stock_num=stock_list[event.message.text]
        #取得即時資料並檢查有無此股票
        realtime=twstock.realtime.get(stock_num)
        if(realtime['success']!=True ):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="查無此股票"))
            return

        #取得歷史資料和五日資料
        history = twstock.Stock(stock_num)
        bfp = list(twstock.BestFourPoint(history).best_four_point())
        
        if bfp[0]==True:
            bfp[0]="推薦買多，原因:"
        elif bfp[0]==False :
            bfp[0]="推薦放空，原因:"
        else:
            bfp[0]=["不要動最好"]

        fiveprice=[str(history.price[i]) for i in range(-1,-6,-1)]
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=realtime['info']['name']+
                "["+realtime['info']['channel']+"]"+
                "近五日價格為\n"+
                str(',\t'.join(fiveprice))+"\n"+
                ' '.join(bfp)
                ))
        return


    #功能展開
    elif event.message.text=="開始玩" :
        buttons_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/OwDxdjw.jpg',
                actions=[
                    MessageTemplateAction(
                        label='個股即時價格和最佳五檔',
                        text='個股即時價格和最佳五檔'
                    ),
                    MessageTemplateAction(
                        label='個股健檢',
                        text='個股健檢'
                    ),
                   MessageTemplateAction(
                        label='免責聲明',
                        text='免責聲明'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        
    #預設
    else :
        buttons_template = TemplateSendMessage(
            alt_text='目錄 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/OwDxdjw.jpg',
                actions=[
                    MessageTemplateAction(
                        label='開始玩',
                        text='開始玩'
                    ),
                    URITemplateAction(
                        label='影片介紹',
                        uri='https://www.youtube.com'
                    ),
                    URITemplateAction(
                        label='github原始碼',
                        uri='https://github.com/markpengisme/Python/tree/master/linestockbot'
                    ),
                    URITemplateAction(
                        label='聯絡作者',
                        uri='https://github.com/markpengisme'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='輸入無效'),buttons_template])    
    ##elif :大盤指數
    ##elif :
    #純粹echo
    '''
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    '''

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
