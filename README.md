# Telegram-bot API-REST

## Start Flask APP
"""
export FLASK_APP=bot_api.by
flask run
"""

## Send post by terminal
"""
curl --request POST \
     --header "Content-Type: application/json" \
     --data '{"msg": "Telegram bot message"}' \
     http://localhost:5000/send
"""