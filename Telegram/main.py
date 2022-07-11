from urllib import response
import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type something to get started')

def help_command(update, context):
    update.message.reply_text('1. Prices of crypto. Ex: price of btc ')
    update.message.reply_text('2. Market status')
    update.message.reply_text('3. Start trading')
    

def start_trading(update, context):
    update.message.reply_text('Listening on port 5000')
    for i in range(0,20):
        update.message.reply_text('Checking Price...')
        update.message.reply_text('Eth Price: 96.610416824437609373  DAI')

def start_trading_exc(update, context):
    update.message.reply_text('Listening on port 5000')
    update.message.reply_text('Checking price...')
    update.message.reply_text('Eth Price: 96  DAI')
    update.message.reply_text('Checking price...')
    update.message.reply_text('Eth Price: 96  DAI')
    update.message.reply_text('Checking price...')
    update.message.reply_text('Eth Price: 96  DAI')
    update.message.reply_text('Selling Eth...')
    update.message.reply_text('Ether Balance: 15.238815219708471905')
    update.message.reply_text('Dai Balance: 750.678604187702826397')
    update.message.reply_text('Successful Swap: https://ropsten.etherscan.io/tx/0x6aa86e534dcd904cd9c35818bdba141d5c16fe5ef3733ee07381e9c778926802')
    update.message.reply_text('Ether Balance: 14.236431769708471905')
    

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("trade", start_trading))
    #dp.add_handler(CommandHandler("trade", start_trading_exc))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    # dp.add_handler(error)

    updater.start_polling()
    updater.idle()

main()