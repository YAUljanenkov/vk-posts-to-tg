import sys
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import VK_TOKEN, VK_GROUP_ID, TELEGRAM_BOT_TOKEN, TELEGRAM_GROUP_ID
import telegram
from telegram.ext import Updater
import logging

logging.basicConfig(format=u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO)


def main():
    try:  # TODO: rewrite the code
        updater = Updater(TELEGRAM_BOT_TOKEN)
        bot = updater.bot
        vk_session = vk_api.VkApi(token=VK_TOKEN)

        long_poll = VkBotLongPoll(vk_session, VK_GROUP_ID)

        for event in long_poll.listen():

            if event.type == VkBotEventType.WALL_POST_NEW:
                logging.info('New post received')
                if event.obj.text != '':
                    bot.send_message(TELEGRAM_GROUP_ID, text=event.obj.text)
                if 'attachments' in event.obj.keys():
                    for attachment in event.obj['attachments']:
                        if attachment['type'] == 'photo':
                            for photo_size in ['photo_2560', 'photo_1280', 'photo_807', 'photo_604', 'photo_130']:
                                try:
                                    bot.send_photo(TELEGRAM_GROUP_ID, attachment['photo'][photo_size])
                                    break
                                except KeyError:
                                    continue
                        if attachment['type'] == 'doc':
                            bot.send_document(TELEGRAM_GROUP_ID, attachment['doc']['url'])
    except telegram.error.TimedOut:
        logging.error('Timeout Error in tg lib')

    except:
        logging.error("Unexpected error: {}".format(sys.exc_info()[0]))
        pass


if __name__ == '__main__':
    while True:
        main()
