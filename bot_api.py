from flask import Flask, request
import requests, os


app = Flask(__name__)

CHAT_ID = os.getenv('CHAT_ID')
TOKEN = os.getenv('TOKEN')
API_URL = f"https://api.telegram.org/bot{TOKEN}/"


@app.route('/send', methods=['POST'])
def send():
    msg_data = request.get_json()
    params = {
        'chat_id': CHAT_ID, 
        'text': msg_data['msg']  
    }
    res = requests.post(f"{API_URL}sendMessage", data=params).json()
    
    if res["ok"]:
        return {
            "statusCode": 200,
            "body": 'sent'
        }
    else:
        return {
            "statusCode": 200,
            "body": res
        }



@app.route('/')
def index():
    return f"Soy el index!", 200


if __name__ == '__main__':
    app.run()
    