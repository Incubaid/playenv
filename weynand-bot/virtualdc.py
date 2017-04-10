

def process_name_step2(message):
    try:
 	   bot.reply_to(message, "Howdy, how are you doing? This is written from a library file function:%s")%message
    except Exception as e:
        bot.reply_to(message, 'oooops')