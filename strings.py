# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})
# TODO: maybe add a preformat to all strings in this file

# Currency symbol
currency_symbol = "€"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} disponibili"

# Answer: the start command was sent and the bot should welcome the user
conversation_after_start = "Ciao!\n" \
                           "Benvenuto su greed!"

# Answer: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Allora, {username}, cosa vorresti fare?"

# Notification: the conversation has expired
conversation_expired = "🕐 Il bot non ha ricevuto messaggi per un po' di tempo, quindi ha chiuso la conversazione.\n" \
                       "Per riavviarne una nuova, invia il comando /start."

# User menu: order
menu_order = "🛍 Ordina"


# User menu: order status
menu_order_status = "❓ Stato ordini"

# User menu: add credit
menu_add_credit = "💵 Ricarica"

# User menu: bot info
menu_info = "ℹ️ Informazioni sul bot"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Questo bot funziona solo in chat private."

# Error: a message was sent in a chat, but no worker exists for that chat. Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ La conversazione con il bot è interrotta.\n" \
                           "Per riavviarla, manda il comando /start al bot."
