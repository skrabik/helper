class Message:
    def __init__(self, update):
        # try:
        self.message_id = update.json()['result'][0]['message']['message_id']
        self.chat_id = update.json()['result'][0]['message']['chat']['id']
        self.user = update.json()['result'][0]['message']['from']['username']
        self.text = update.json()['result'][0]['message']['text'].strip()
        # except:
        #     print('Не полчилось обработать сообщение')
        #     self.message_id = '111'
        #     self.chat_id = '111'
        #     self.user = 'skrabik0'
        #     self.text = '{error: 500}'