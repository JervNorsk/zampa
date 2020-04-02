import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_add_c

@core.decorators.admin.user_admin
@core.decorators.public_command.init
def init(update, context):
    connector = Connection()
    title_group = update.message.chat.title
    link_group = "https://t.me/{}".format(update.message.chat.username)
    query = Sql_add_c.SQL
    connector.cur.execute(query, (title_group, link_group))
    update.effective_message.reply_text("Community aggiunta al database!")