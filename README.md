# VK posts->Tg
*Transfer your VK posts to telegram immediately*

> **Warning!** This is an alpha version and is **not** tested well.
> It ~~might be~~ *is* not stable.

This bot uses VK long poll API to get notifications about posts on-time and resend them in telegram channel.
Right now bot can resend text, photos and docs from your post. Soon new options and better configuration will be added.
Also soon I'll make code prettier.

## How to configure this bot

1. Visit `vk.com/<your_group_id>?act=tokens` and create a token with "wall" rights. 
2. Enable Long Poll API here `https://vk.com/<your_group_id>?act=longpoll_api`
3. Go to Telegram and create a bot using `@BotFather`
4. Add your bot to administrators of your channel
5. Clone this repo
6. Create a file `config.py` and fill it using this template:
    ```python
    VK_TOKEN = '<YOUR TOKEN>'
    VK_GROUP_ID = '<YOUR VK GROUP ID'
    TELEGRAM_GROUP_ID = '<ID OF YOUR Tg CHANNEL>'
    TELEGRAM_BOT_TOKEN = '<BOT TOKEN>'
    REQUEST_KWARGS = {}
    ```
    I recommend you to use `@getidsbot` to get your telegram channel ID. 
7. Run `pip3 install -r requirements.txt`
8. Run `python3 main.py`
9. For Russian users: you need to configure Proxy. Do it by yourself or follow instructions below.
10. Profit!


## How to configure Proxy

### If you use HTTP Proxy
In file `config.py`:

```python
REQUEST_KWARGS={
    'proxy_url': 'http://PROXY_HOST:PROXY_PORT/',
    # Optional, if you need authentication:
    'username': 'PROXY_USER',
    'password': 'PROXY_PASS',
}

```

### If you use SOCKS5 Server

Run `pip install python-telegram-bot[socks]`

In file `config.py`:
```python
REQUEST_KWARGS={
    'proxy_url': 'socks5://URL_OF_THE_PROXY_SERVER',
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'username': 'PROXY_USER',
        'password': 'PROXY_PASS',
    }
}
```


