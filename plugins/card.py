import core.decorators
from core.sql.db_connect import Connection

keywordCard = ["miki", "bluewolf", "degron", "ryanking", "leo"]

@core.decorators.admin.user_admin
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    chatid = str(update.message.chat_id)
    userid = str(update.message.from_user.id)
    connector = Connection()
    query = 'SELECT card_img, card_bio FROM card_table WHERE user_id = %s AND id_group = %s'
    connector.cur.execute(query,[userid,chatid])
    row = connector.cur.fetchone()
    if row is not None:
        message = "<b>BIO:</b> {}".format(row[1])
        bot.send_photo(update.message.chat_id, row[0],caption=message, parse_mode='HTML')

@core.decorators.admin.user_admin
@core.decorators.delete.init
def card_update(update, context):
    bot = context.bot
    message=str(update.message.text[7:]).strip()
    if message != "":
        chatid = str(update.message.chat_id)
        userid = str(update.message.from_user.id)
        connector = Connection()
        query = 'UPDATE card_table SET card_bio = %s WHERE user_id = %s AND id_group = %s '
        connector.cur.execute(query,[message,userid,chatid])
        message = "Hai modificato con successo la BIO della tua Card!"
        bot.send_message(update.message.chat_id,message)
    else:
        bot.send_message(update.message.chat_id, text="Non puoi inserire una BIO Vuota!")