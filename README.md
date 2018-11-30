# VK posts->Tg
*Transfer your VK posts to telegram immediately*

> **Warning!** This is an alpha version and is **not** tested well.
> It ~~might be~~ *is* not stable.

This bot uses VK long poll API to get notifications about posts on-time and resend them in telegram channel.
Right now bot can resend text, photos and docs from your post. Soon new options and better configuration will be added.
Also soon I'll make code prettier.

## How to configure this bot

1. Visit `vk.com/<your_group_id>?act=tokens` and create a token with "wall" rights.
2. Go to Telegram and create a bot using `@BotFather`
3. Add your bot to administrators of your channel
4. Clone this repo
5. Create a file `config.py` and fill it using this template:
    ```python
    VK_TOKEN = '<YOUR TOKEN>'
    VK_GROUP_ID = '<YOUR VK GROUP ID'
    TELEGRAM_GROUP_ID = '<ID OF YOUR Tg CHANNEL>'
    TELEGRAM_BOT_TOKEN = '<BOT TOKEN>'
    ```
    I recommend you to use `@getidsbot` to get your telegram channel ID. 
6. Run `pip3 install -r requirements.txt`
7. Run `python3 main.py`
8. ...
9. Profit!



