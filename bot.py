#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.


import logging
from os import link
from typing import Text
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, message
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages

FIRST, SECOND = range(2)
# Callback data
VOLVER = range(1)
CUENTA, AUTORIZACIONES, INTERNACIONES, PLANES, CONTACTO = range(5)
ACCESO, RECUPERACION, MODIFICACION,CERRAR = range(4)
AUTYCONS,CONSDIR,CONSAUT,DISP,ERRADV,ANUL,COMENT,IMG = range(8)

def start(update: Update, context: CallbackContext) -> int:
    """Mensaje de inicio al ejecutar el comando `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("Usuario %s ha iniciado una conversación.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
            [InlineKeyboardButton("Cuenta de Usuario", callback_data=str(CUENTA))],
            [InlineKeyboardButton("Autorizaciones en linea", callback_data=str(AUTORIZACIONES))],
            [InlineKeyboardButton("Internaciones en linea", callback_data=str(INTERNACIONES))],
            [InlineKeyboardButton("Ingresos a planes", callback_data=str(PLANES))],
            [InlineKeyboardButton("Contacto", callback_data=str(CONTACTO))],
        ]
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Bienvenidos al bot para prestadores del IPSST, seleccione el motivo de su consulta.", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST


def VOLVER (update: Update, context: CallbackContext) -> int:
    """Menu de cuenta de Usuario"""
    query = update.callback_query
    query.answer()
    keyboard = [
           [InlineKeyboardButton("Cuenta de Usuario", callback_data=str(CUENTA))],
            [InlineKeyboardButton("Autorizaciones en linea", callback_data=str(AUTORIZACIONES))],
            [InlineKeyboardButton("Internaciones en linea", callback_data=str(INTERNACIONES))],
            [InlineKeyboardButton("Ingresos a planes", callback_data=str(PLANES))],
            [InlineKeyboardButton("Contacto", callback_data=str(CONTACTO))],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Bienvenidos al bot para prestadores del IPSST, seleccione el motivo de su consulta.", reply_markup=reply_markup
    )
    return FIRST

"""MENU PRINCIPAL"""

def CUENTA(update: Update, context: CallbackContext) -> int:
    """Menu de cuenta de Usuario"""
    query = update.callback_query
    query.answer()
    keyboard = [
            [InlineKeyboardButton("Acceso al sistema", callback_data=str(ACCESO))],
            [InlineKeyboardButton("Recuperación de contraseña", callback_data=str(RECUPERACION))],
            [InlineKeyboardButton("Modificación de contraseña", callback_data=str(MODIFICACION))],
            [InlineKeyboardButton("Cerrar sesión", callback_data=str(CERRAR))],
            [InlineKeyboardButton("Volver", callback_data=str(VOLVER))],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Cuenta de Usuario", reply_markup=reply_markup
    )
    return FIRST


def AUTORIZACIONES(update: Update, context: CallbackContext) -> int:
    """Menu de cuenta de Usuario"""
    query = update.callback_query
    query.answer()
    keyboard = [
            [InlineKeyboardButton("Autorizaciones y Consumo Simultaneo", callback_data=str(AUTYCONS))],
            [InlineKeyboardButton("Consumo directo de Autorización Previa", callback_data=str(CONSDIR))],
            [InlineKeyboardButton("Consumo de Autorización Previa", callback_data=str(CONSAUT))],
            [InlineKeyboardButton("Carga de disposiciones en Autorización", callback_data=str(DISP))],
            [InlineKeyboardButton("Errores y advertencias", callback_data=str(ERRADV))],
            [InlineKeyboardButton("Anulación de autorizaciones", callback_data=str(ANUL))],
            [InlineKeyboardButton("Ver o Adjuntar Comentarios", callback_data=str(COMENT))],
            [InlineKeyboardButton("Adjuntar imágenes", callback_data=str(IMG))],
            [InlineKeyboardButton("Volver", callback_data=str(VOLVER))],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Autorizaciones en linea", reply_markup=reply_markup
    )
    return FIRST


def INTERNACIONES(update: Update, context: CallbackContext) -> int:
    """Menu de cuenta de Usuario"""
    query = update.callback_query
    query.answer()
    keyboard = [
            [InlineKeyboardButton("Orden de internación", callback_data=str(ACCESO))],
            [InlineKeyboardButton("Autorizaciones en estado de internación", callback_data=str(RECUPERACION))],
            [InlineKeyboardButton("Modificación de Órdenes de Internación", callback_data=str(MODIFICACION))],
            [InlineKeyboardButton("Emisión de una Orden de Internación", callback_data=str(CERRAR))],
            [InlineKeyboardButton("Volver", callback_data=str(VOLVER))],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="INTERNACIONES", reply_markup=reply_markup
    )
    return FIRST

def PLANES(update: Update, context: CallbackContext) -> int:
    """Menu de cuenta de Usuario"""
    query = update.callback_query
    query.answer()
    keyboard = [
            [InlineKeyboardButton(text="Requisitos",
               url="http://ipsst.gov.ar/departamento-de-programas-de-gestion-racional-de-medicamentos/planes-especiales/requisitos-para-planes-y-programas-especiales/" ,
                callback_data=str(ACCESO))],
            [InlineKeyboardButton("Volver", callback_data=str(VOLVER))],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="PLANES", reply_markup=reply_markup
    )
    return FIRST

def CONTACTO(update: Update, context: CallbackContext) -> int:
    """Menu de cuenta de Usuario"""
    query = update.callback_query
    query.answer()
    keyboard = [
            [InlineKeyboardButton("Volver", callback_data=str(VOLVER))],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Mesa de Ayuda: 4507899", reply_markup=reply_markup
    )
    return FIRST

    """CUENTA"""

    """"OTRACOSA"""

def AUTYCONS(update: Update, context: CallbackContext) -> int:
    """Menu de cuenta de Usuario"""
    query = update.callback_query
    query.answer()
    keyboard = [
            [InlineKeyboardButton(
            text="Video instructivo",
            url="https://www.youtube.com/watch?v=PYRVOZIfwyk&list=PLNcDLjB25GHvvpEyf1a7f_eLzuiirOV7v&index=4",
            callback_data=str(AUTYCONS))],
            [InlineKeyboardButton(
            text="Contacto",
            callback_data=str(CONTACTO))],
            [InlineKeyboardButton("Volver", callback_data=str(VOLVER))]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Ingrese al sistema, haga click en autorizaciones online, seleccione la opciòn autorizaciones y luego autorizaciones en prestador. "
            "En modalidad elija  “Autorización y Consumo Simultáneo” y cliquee el signo +. Deberá ingresar el CUIL del afiliado, si no lo conoce, "
            "haga click en la flecha de color celeste donde podrá buscarlo con el DNI y seleccionarlo. Elija la cobertura por la que se realizarán las prestaciones."
            " Indique la fecha de prescripción. Complete matrícula de prescriptor y código de diagnóstico en caso de corresponder."
            " Cargue el código de práctica, cantidad y cliquee el Signo + (realice esto tantas veces como prácticas necesite cargar). Confirme. "
            "Consulte el estado de la autorización, y el número correspondiente del consumo realizado en el extremo superior derecho.",
        reply_markup=reply_markup
    )
    return FIRST

def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token='2085069358:AAGoggcZqXuQDPHrU7TbzKyv3RK2ekkDv_k',use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(CUENTA, pattern='^' + str(CUENTA) + '$'),
                CallbackQueryHandler(AUTORIZACIONES, pattern='^' + str(AUTORIZACIONES) + '$'),
                CallbackQueryHandler(VOLVER, pattern='^' + str(VOLVER) + '$'),
                CallbackQueryHandler(INTERNACIONES, pattern='^' + str(INTERNACIONES) + '$'),
                CallbackQueryHandler(PLANES, pattern='^' + str(PLANES) + '$'),
                CallbackQueryHandler(CONSDIR, pattern='^' + str(CONSDIR) + '$'),
                CallbackQueryHandler(CONSAUT, pattern='^' + str(CONSAUT) + '$'),
                CallbackQueryHandler(DISP, pattern='^' + str(DISP) + '$'),
                CallbackQueryHandler(ERRADV, pattern='^' + str(ERRADV) + '$'),
                CallbackQueryHandler(ANUL, pattern='^' + str(ANUL) + '$'),
                CallbackQueryHandler(COMENT, pattern='^' + str(COMENT) + '$'),
                CallbackQueryHandler(IMG, pattern='^' + str(IMG) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(VOLVER, pattern='^' + str(CUENTA) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(AUTORIZACIONES) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()