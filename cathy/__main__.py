from os import environ
import os
from sys import argv
from dotenv import load_dotenv, find_dotenv
from cathy import Cathy
from pathlib import Path
import dotenv
from os.path import join, dirname



def print_usage():
    print("Usage:")
    print("  cathy")
    print("DISCORD_TOKEN, DATABASE, DISCORD_CHANNEL should be environment variables.")
    print("They can be placed in a `.env` file.")
    print("The database will be created if it does not exist.")
    print("For more info, visit: http://cathy-docs.rtfd.io/")


def main():  # If called by entrypoint
    if '--help' in argv or '-h' in argv:
        print_usage()
        exit()
    # dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(verbose=True)
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    # load_dotenv(find_dotenv())
    DISCORD_TOKEN="NzgxMDUyOTM2Mjk3NTEyOTgw.X74COw.dACKthDv17mIgUEnkD36SMuyWUs"
    DISCORD_CHANNEL="chat-with-bot"
    DATABASE="/opt/cathy/db.sqlite3"

    errors = []
    environ['DISCORD_TOKEN'] = 'NzgxMDUyOTM2Mjk3NTEyOTgw.X74COw.dACKthDv17mIgUEnkD36SMuyWUs'
    environ['DISCORD_CHANNEL'] = 'chat-with-bot'
    environ['DATABASE'] ='NONE'

    if not os.getenv('DISCORD_TOKEN'):
        errors.append('No DISCORD_TOKEN found in environment variables.')
    if not os.getenv('DISCORD_CHANNEL'):
        errors.append('No DISCORD_CHANNEL found in environment variables.')
    if not os.getenv('DATABASE'):
        errors.append('No DATABASE found in environment variables.')
    if errors:
        for error in errors:
            print(f"Error: {error}")
        exit(1)

    bot = Cathy(environ['DISCORD_CHANNEL'], environ['DISCORD_TOKEN'], environ['DATABASE'])
    bot.run()


if __name__ == '__main__':  # for `python -m` invocation
    main()
