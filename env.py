import requests

def get_offset(BOT_TOKEN):
    try:
        rez = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates').json()['result'][0]['update_id']
    except:
        rez = get_offset()
    return rez


BOT_TOKEN = '6461730554:AAFQK0QtfCdLRgphpP93s14NXryj4Y5mrRM'
USERNAME = 'skrabik0'

CHAT_ID = '1030879612'

OFFSET = get_offset(BOT_TOKEN)