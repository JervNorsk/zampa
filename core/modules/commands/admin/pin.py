import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Pin


@core.decorators.admin.init
@core.decorators.bot_admin.bot_admin
@core.decorators.delete.init
def init(update, context):
    bot = context.bot
    chatid = str(update.message.chat_id) 
    message = update.message.text[7:]
    message_text="<b>Annuncio</b>\n\n{}" . format(message)
    connector = Connection()
    query = Sql_Pin.SQL
    connector.cur.execute(query,[chatid])
    row=connector.cur.fetchone()
    if row is not None:
        message_text = message_text + "\n\n{}".format(row[0])
        bot.send_message(update.message.chat_id, text=message_text, parse_mode='HTML')
        bot.pin_chat_message(update.message.chat_id, update.message.message_id+1)
        connector.cur.close()
        connector.db.close()