import logging
import discord

def run():
	logging.basicConfig(filename="logs/bot.log", filemode='w', format="%(asctime)s:%(levelname)s:%(name)s: %(message)s", level=logging.DEBUG)
	logging.info("Start logging")
	logging.info("Finish logging")
	
if __name__ == '__main__':
	run()
