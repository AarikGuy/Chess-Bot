﻿# Chess-Bot
## Setting Up Dev Environment
1. To setup the dev environment, you will first need to sign up for lichess.org. You can't use an already existing account if games have been played on the account. Once the bot plays games on lichess.org, the account will permanently be set to the bot account status.

2. Once You've made an account, generate a OAUTH2 token here to have your bot play games through the lichess API: https://lichess.org/account/oauth/token/create?scopes%5B%5D=bot:play&description=lichess-bot 

3. Add your API token to the secrets.json file.
4. Create a python virtual environment:
    python -m venv chess_bot
5. Activate the dev environment:
chess_bot/Scripts/Activate.ps1
6. Install the project dependencies:
pip install -r requirements.txt

