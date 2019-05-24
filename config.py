import secret

from cogs import friendly, util, fun, macros

APP_TOKEN = secret.TOKEN
GOOGLE_CUSTOM_SEARCH_ID = secret.GOOGLE_CUSTOM_SEARCH_ID
GOOGLE_CUSTOM_SEARCH_KEY = secret.GOOGLE_CUSTOM_SEARCH_KEY

COMMAND_COGS = [
    {
        'class': friendly.Friendly_commands
    }, {
        'class': util.Util_commands
    }, {
        'class': fun.Fun
    }, {
        'class': macros.Macros
    }
    ]

BOT_ACTIVITIES = [
    "IM A BOT",
    "Nothing",
    "Ruining your life",
    "analyzing your life",
    "yeet, yeet yeet"
    ]

HOW_ARE_YOU_RESPONSES = [
    "I am a happy bot.",
    "I'm good, how are you",
    "Do I need to answer you?",
    "Not feeling so good",
    "Why do you care?"
    ":frowning:",
    ":grinning:",
    "Not the greatest, how are you?",
    ]

DEFAULT_MEME_TYPE = 'google'
#GOOGLE_MEME_SEARCH_QUERIES = ['programmer+humor', 'programming+memes', 'programming+meme', 'coding+meme']

BOT_ADMIN_ROLES = ['Admin', 'admin', 'bot-admin', 'Bot-admin',] 

ALLOWED_SPAM_CHANNELS = ['bot-spam']

COMMAND_PREFIX = '--'
MACRO_PREFIX = '++'
