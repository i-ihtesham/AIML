from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup"):
        return "Hey! How's it going?"
    
    if user_message in ("who are you", "who are you?"):
        return "I am Cryto Bot, I am here to help you with trading"
    
    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    if user_message in ("price of eth", "eth price"):
        return "price is 1141.64$"
    
    if user_message in ("price of btc", "btc price"):
        return "price is 20297.40$"
    
    if user_message in ("price of sol", "sol price"):
        return "price is 41.21$"
    
    if user_message in ("account balance"):
        return "Balance: 13.2364ETH"
    
    if user_message in ("market status"):
        li = ["Bitcoin and Ethereum dropped a percent each, whereas Avalanche and Solana plunged 3-4 percent each. The total cryptocurrency trading volume zoomed more than 15% to $57.19 billion"]
        return li[0];
    


    return "I don't understand you."