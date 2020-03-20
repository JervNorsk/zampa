import core.decorators
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utility import utils
from core.sql.db_connect import Connection

#@core.decorators.owner.init
def init(update, context):
    keyboard = [InlineKeyboardButton("BOTTONE", callback_data='testingclick')]
    reply_markup = InlineKeyboardMarkup(build_menu(keyboard, n_cols=2))
    update.message.reply_text('CIAO CIAO',reply_markup=reply_markup)

def testingclick(update, context):
    bot = context.bot
    #query = update.callback_query
    bot.edit_message_text(
    message_id = update.callback_query.message.message_id,
    chat_id = update.callback_query.message.chat.id,
    text = "porcodio")

def build_menu(buttons, n_cols, header_buttons=False, footer_buttons=False):
  menu=[buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu