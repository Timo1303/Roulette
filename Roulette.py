from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

bot_token = "7041456970:AAHQCff9BeB27jX4NZ3mZcKopr8hCMObeSk"
game = False
bet = False
Konto= 0
Einsatz = 0

def start(update: Update, context: CallbackContext) -> None:
    global Konto
    Konto = 1000
    update.message.reply_text('Konto: {Konto} €\nGeben Sie /bet [Betrag] [Farbe] ein, um zu wetten. Mögliche Farben: red, black\n\nOder starten Sie ein Spiel mit /play ein Spiel'.format(Konto))

def bet(update: Update, context: CallbackContext) -> None:
    global Konto
    context.user_data['bet'] = int(context.args[0])
    context.user_data['color'] = context.args[1]
    update.message.reply_text(f'{context.user_data["bet"]} € auf {context.user_data["color"]} gesetzt!')
    roulette_number = random.randint(0, 36)
    if (roulette_number != 0 and
        ((roulette_number <= 10 or (roulette_number > 18 and roulette_number <= 28)) and roulette_number % 2 == 1 and context.user_data["color"] == "red") or
        ((roulette_number > 10 and roulette_number <= 18) or (roulette_number > 28) and roulette_number % 2 == 0 and context.user_data["color"] == "red") or
        ((roulette_number <= 10 or (roulette_number > 18 and roulette_number <= 28)) and roulette_number % 2 == 0 and context.user_data["color"] == "black") or
        ((roulette_number > 10 and roulette_number <= 18) or (roulette_number > 28) and roulette_number % 2 == 1 and context.user_data["color"] == "black")):
        Konto += context.user_data['bet']
        update.message.reply_text(f"Roulette-Zahl: {roulette_number}\nFarbe: {context.user_data['color']} -> Gewonnen!\nKonto: {Konto} €")
    else:
        Konto -= context.user_data['bet']
        update.message.reply_text(f"Roulette-Zahl: {roulette_number}\nFarbe: {context.user_data['color']} -> Verloren!\nKonto: {Konto} €")

def roll_color():
    roulette_number = random.randint(0, 36)
    if roulette_number == 0:
        return "green"
    elif roulette_number % 2 == 0:
        return "red"
    else:
        return "black"

def play(update: Update, context: CallbackContext) -> None:
    global game
    global Konto
    game = True
    update.message.reply_text('Konto: Konto: {} €\n\nWie viel möchten Sie einsetzen?\n/100\n/200\n/500\n/1000\n/5000\n/10000'.format(Konto))

def hundred(update: Update, context: CallbackContext) -> None:
    global game
    global bet
    global Einsatz
    global Konto
    if game == True:
        if Konto < 100:
            update.message.reply_text('Sie haben nicht genügend Geld!')    
        else:
            Einsatz = 100
            bet = True
            update.message.reply_text('Auf was möchten Sie wetten?\n/rot\n/schwarz')
    else:
        update.message.reply_text('Bitte starten Sie ein Spiel mit /play')

def two_hundred(update: Update, context: CallbackContext) -> None:
    global game
    global bet
    global Einsatz
    global Konto
    if game == True:
        if Konto < 200:
            update.message.reply_text('Sie haben nicht genügend Geld!\n\nWie viel möchten Sie einsetzen?\n/100\n/200\n/500\n/1000\n/5000\n/10000'.format(Konto))    
        else:
            Einsatz = 200
            bet = True
            update.message.reply_text('Auf was möchten Sie wetten?\n/rot\n/schwarz')
    else:
        update.message.reply_text('Bitte starten Sie ein Spiel mit /play')

def five_hundred(update: Update, context: CallbackContext) -> None:
    global game
    global bet
    global Einsatz
    global Konto
    if game == True:
        if Konto < 500:
            update.message.reply_text('Sie haben nicht genügend Geld!\n\nWie viel möchten Sie einsetzen?\n/100\n/200\n/500\n/1000\n/5000\n/10000'.format(Konto))    
        else:
            Einsatz = 500
            bet = True
            update.message.reply_text('Auf was möchten Sie wetten?\n/rot\n/schwarz')
    else:
        update.message.reply_text('Bitte starten Sie ein Spiel mit /play')

def thousand(update: Update, context: CallbackContext) -> None:
    global game
    global bet
    global Einsatz
    global Konto
    if game == True:
        if Konto < 1000:
            update.message.reply_text('Sie haben nicht genügend Geld!\n\nWie viel möchten Sie einsetzen?\n/100\n/200\n/500\n/1000\n/5000\n/10000'.format(Konto))    
        else:
            Einsatz = 1000
            bet = True
            update.message.reply_text('Auf was möchten Sie wetten?\n/rot\n/schwarz')
    else:
        update.message.reply_text('Bitte starten Sie ein Spiel mit /play')

def five_thousand(update: Update, context: CallbackContext) -> None:
    global game
    global bet
    global Einsatz
    global Konto
    if game == True:
        if Konto < 5000:
            update.message.reply_text('Sie haben nicht genügend Geld!\n\nWie viel möchten Sie einsetzen?\n/100\n/200\n/500\n/1000\n/5000\n/10000'.format(Konto))    
        else:
            Einsatz = 5000
            bet = True
            update.message.reply_text('Auf was möchten Sie wetten?\n/rot\n/schwarz')
    else:
        update.message.reply_text('Bitte starten Sie ein Spiel mit /play')

def ten_thousand(update: Update, context: CallbackContext) -> None:
    global game
    global bet
    global Einsatz
    global Konto
    if game == True:
        if Konto < 10000:
            update.message.reply_text('Sie haben nicht genügend Geld!\n\nWie viel möchten Sie einsetzen?\n/100\n/200\n/500\n/1000\n/5000\n/10000'.format(Konto))    
        else:
            Einsatz = 10000
            bet = True
            update.message.reply_text('Auf was möchten Sie wetten?\n/rot\n/schwarz')
    else:
        update.message.reply_text('Bitte starten Sie ein Spiel mit /play')

def all(update: Update, context: CallbackContext) -> None:
    global game
    global bet
    global Einsatz
    global Konto
    if game == True:
        Einsatz = Konto
        bet = True
        update.message.reply_text('Auf was möchten Sie wetten?\n/rot\n/schwarz')
    else:
        update.message.reply_text('Bitte starten Sie ein Spiel mit /play')

def rot(update: Update, context: CallbackContext) -> None:
    global game
    global bet
    if bet == True:
        global Konto
        global Einsatz
        Ergebnis = roll_color()
        if Ergebnis == "red":
            Konto += Einsatz
            update.message.reply_text('Gewonnen!\nKonto: {} €\n\nNeues Spiel mit /play'.format(Konto))
        else:
            Konto -= Einsatz
            update.message.reply_text('Verloren!\nKonto: {} €\n\nNeues Spiel mit /play'.format(Konto))
        game = False
        bet = False

def schwarz(update: Update, context: CallbackContext) -> None:
    global game
    global bet
    if bet == True:
        global Konto
        global Einsatz
        Ergebnis = roll_color()
        if Ergebnis == "black":
            Konto += Einsatz
            update.message.reply_text('Gewonnen!\nKonto: {} €\n\nNeues Spiel mit /play'.format(Konto))
        else:
            Konto -= Einsatz
            update.message.reply_text('Verloren!\nKonto: {} €\n\nNeues Spiel mit /play'.format(Konto))
        game = False
        bet = False
    

def main() -> None:
    updater = Updater(bot_token, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("bet", bet))
    dispatcher.add_handler(CommandHandler("play", play))
    dispatcher.add_handler(CommandHandler("rot", rot))
    dispatcher.add_handler(CommandHandler("schwarz", schwarz))
    dispatcher.add_handler(CommandHandler("100", hundred))
    dispatcher.add_handler(CommandHandler("200", two_hundred))
    dispatcher.add_handler(CommandHandler("500", five_hundred))
    dispatcher.add_handler(CommandHandler("1000", thousand))
    dispatcher.add_handler(CommandHandler("5000", five_thousand))
    dispatcher.add_handler(CommandHandler("10000", ten_thousand))
    dispatcher.add_handler(CommandHandler("all", all))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()