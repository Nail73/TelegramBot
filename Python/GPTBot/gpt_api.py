import openai
import telebot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


token = "6185263204:AAGTCJmXUeen-ueqiRABbLeYuk-8VxnvgGE"
bot = telebot.TeleBot(token)

class GPT:
    def __init__(self):
        openai.api_key = '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'
        self.__messages = []

    def request(self, task):
        self.__messages.append({'role': 'user', 'content': task})
        print('Запрос отправлен...')
        answer = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = self.__messages
            )
        self.__messages.append({'role': 'assistant', 'content': answer.choices[0].message.content})
        return answer.choices[0].message.content

def handle_message(update, context):
    assist = GPT()
    data = update.message.text
    if '*' in data:
        response = assist.request(data)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
    dispatcher.add_handler(message_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
