from wappdriver import WhatsApp

with WhatsApp() as bot:
    bot.send('David Piso Valencia',
             'El asistente de voz te saluda'
            )