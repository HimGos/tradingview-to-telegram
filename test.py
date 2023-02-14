from flask import *
from config import telegram_bot_sendtext

app = Flask(__name__)


# This webhook takes input from Tradingview Webhook in form of JSON
@app.route('/webhook', methods=['GET', 'POST'])
def home():
    json_data = request.get_json()
    # msg = json_data["msg"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    symbol = json_data["symbol"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    price = json_data["price"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    price = price.replace(".", "\\.")
    message = symbol + " Cross " + price  # Making a message for telegram
    print(message)
    telegram_bot_sendtext(message)  # Displaying message on Telegram
    print(type(message))
    return message

if __name__ == "__main__":
    app.run(port=80)





