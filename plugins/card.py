import core.decorators
from core.sql.db_connect import Connection

keywordCard = ["miki", "bluewolf", "degron", "ryanking", "leo"]

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