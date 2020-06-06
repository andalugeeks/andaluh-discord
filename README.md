# Andaluh Discord Bot

Transliterate spanish to Andalûh EPA on this Discord Servers with this bot.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Install

Use the `requirements.txt` file to install dependencies.

```
$ pip3 install -r requirements
``` 

We recommend to setup a python virtualenvironment to run the bot. Let's create a virtualenv for python3 and install the dependencies using the `requirements.txt`file:

```
$ cd andaluh-discord/
~/andaluh-discord$ python3 -m venv .env
~/andaluh-discord$ pip3 install -r requirements
~/andaluh-discord$ source .env/bin/activate
(env) ~/andaluh-discord$ pip install -r requirements.txt
```

## Usage

First, please create your Discord Bot as per the following instructions: https://discordpy.readthedocs.io/en/latest/discord.html

Once you have your bot TOKEN, please set `DISCORD_TOKEN` environment variable and run `andaluh-discord/bot.py`

```
$ DISCORD_TOKEN=mytoken python3 andaluh-discord/bot.py
```

You can also store your token as an env var included in `./andaluh-discord/.env`:

```
$ cat andaluh-discord/.env 
DISCORD_TOKEN={your-bot-token}

$ python3 andaluh-discord/bot.py
```

## Support

Please [open an issue](https://github.com/andalugeeks/andaluh-discord/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and open a pull request.