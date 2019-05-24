MACROS = [
        {
         'type': 'command',
         'name': 'bothelp',
         'delete': True,
         'help': "Display the bot help message",
         'content': "I am a bot. I can do many things. One thing I do is listen to commands. To run a command, just prefix the command name with `--`. For example, to get a list of my commands, you can type `--help`. I can also do other things, but most of it is explained in the help menu. Ask someone if you need more help." 
        }, {
         'type': 'listener',
         'delete': False,
         'name': 'LittleBot',
         'help': False,
         'content': "Did someone mention me?"
        }, {
         'type': 'command',
         'delete': True,
         'name': 'listenershelp',
         'help': "What are Listeners?",
         'content': "I listen for special keywords to be mentioned in a conversation. When I hear one of the keywords I understand, I perform some action. I also listen for other things, such as when a new user joins, so I can welcome them. You can find a list of some of my listeners by using the `listListeners` command."
        }
        ]

LISTENER_LIST = [
        "There are no listeners so far!!"
        ]
