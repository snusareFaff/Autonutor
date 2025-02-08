from pyrogram import Client

# Replace 'your_api_id' and 'your_api_hash' for your values ​​from my.telegram.org
API_ID = 'your api id'
API_HASH = 'your api hash'

app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

with app:
    print(app.export_session_string())