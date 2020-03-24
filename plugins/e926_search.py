import core.decorators
 
@core.decorators.public_command.init
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    message=str(update.message.text[5:]).strip()
    if message != "":
        bot.send_photo(update.message.chat_id,
                   photo="https://i.imgur.com/CffJg8z.png",
                   caption="<b>WEB:</b> https://e926.net/posts?tags={0}"
                   .format(message.replace(' ','+')),
                   parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id, text="Devi digitare un criterio di ricerca!")