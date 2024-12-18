from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import cv2
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Fonction pour appliquer l'effet HDR
def apply_hdr(input_path, output_path):
    try:
        image = cv2.imread(input_path)
        if image is None:
            raise ValueError("Impossible de lire l'image")
        hdr = cv2.detailEnhance(image, sigma_s=12, sigma_r=0.15)
        cv2.imwrite(output_path, hdr)
    except Exception as e:
        raise Exception(f"Erreur lors du traitement HDR: {str(e)}")

# Commande /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bienvenue ! Envoie-moi une image, et je vais la convertir en HDR.")

# Gérer les images reçues
def handle_image(update: Update, context: CallbackContext):
    try:
        photo = update.message.photo[-1]  # La meilleure qualité d'image
        file = context.bot.getFile(photo.file_id)
        input_path = f"images/{photo.file_id}.jpg"
        output_path = f"images/{photo.file_id}_hdr.jpg"

        # Télécharge l'image
        file.download(input_path)

        # Applique l'effet HDR
        apply_hdr(input_path, output_path)

        # Envoie l'image transformée
        update.message.reply_photo(photo=open(output_path, "rb"))
    except Exception as e:
        update.message.reply_text(f"Désolé, une erreur est survenue: {str(e)}")
    finally:
        # Nettoyage des fichiers
        for path in [input_path, output_path]:
            if os.path.exists(path):
                os.remove(path)

# Main
def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo, handle_image))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    main()
