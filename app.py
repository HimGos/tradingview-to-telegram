from flask import *
from config import telegram_bot_sendtext

app = Flask(__name__)


# This webhook takes input from Tradingview Webhook in form of JSON
@app.route('/webhook', methods=['GET', 'POST'])
def home():
    message = request.data.decode('utf-8')
    print(message)
    print(type(message))
    # json_data = request.json
    # symbol = str(json_data['symbol'])                    # Extracting Symbol from JSON
    # price = str(json_data['price']).replace(".", "\\.")  # Extracting Price from JSON
    # message = f"""New Signal \U0001F514 \n{symbol} : {price} \n TP1: 50 Pips\n TP2: 100 Pips"""
    telegram_bot_sendtext(message)  # Displaying message on Telegram
    # print(type(json_data))
    return message

if __name__ == "__main__":
    app.run(port=80)
