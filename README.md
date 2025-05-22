# Andaluh Discord Bot

Transliterate Spanish to Andalûh EPA on Discord Servers with this bot.

<img width="800" alt="andaluh-discord about" src="https://github.com/andalugeeks/andaluh-discord/raw/master/img/andaluh-discord.png?raw=true">


## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Install

You can setup a python virtualenvironment to run the bot. Let's create a virtualenv for python3 and install the dependencies using the `requirements.txt` file:

```
cd andaluh-discord/
python3 -m venv .env
pip3 install -r requirements
source .env/bin/activate
pip install -r requirements.txt
```
Now, please create your Discord Bot as per the following instructions: https://discordpy.readthedocs.io/en/latest/discord.html

Once you have your bot TOKEN, please set `DISCORD_TOKEN` environment variable and run `app/andaluhbot.py`

```
$ DISCORD_TOKEN=mytoken python3 app/andaluhbot.py
```

You can also store your token as an env var included in `./app/.env`:

```
$ cat app/.env 
DISCORD_TOKEN={your-bot-token}

$ python3 app/andaluhbot.py
```

A `docker-compose` file is also included. If you want to run the bot on a dockerized environment, edit your `DISCORD_TOKEN` inside the `docker-compose.yml` file and run:

```
$ docker-compose up --build -d
```

## Usage

The bot has 1 slash/application command (type '/' to view them). You need to use the sync prefix command first for application commands to show. The prefix set for this bot is its own @mention. Example: `@andaluhbot sync`.

* `/andaluh`: Get Andalûh EPA standard transliteration (using 'ç')

The command has two parameters:
* `text`: Text to transliterate
* `variant [Optional]`: Choose one of the three variants of transliteration instead of 'ç' (zezeo, seseo or heheo)

If the bot has the `MANAGE_WEBHOOKS` permission, it will show the transliteration using the avatar image and display name of the user who called the command, as if it was sent from their account. This allows for a more natural conversation.

## Support

Please [open an issue](https://github.com/andalugeeks/andaluh-discord/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and open a pull request.
