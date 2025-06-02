from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from decouple import config
from browser import download_instagram

token = config("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        text=f"Hello",
        reply_to_message_id=update.effective_message.id,
    )

async def handle_instagram_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    
    if "instagram.com" not in url:
        await update.message.reply_text("Please send a valid Instagram link.")
        return
    
    status_msg = await update.message.reply_text("⏳ Preparing to download...")

    try:
        await status_msg.edit_text("✅ Browser started...")
        link, caption_text, likes, timestamp, comments = download_instagram(url)
        caption = (
            f"✒️ Caption: {caption_text}\n"
            f"📥 Downloaded from: {url}\n"
            f"❤️ Likes: {likes}\n"
            f"💬 Comments: {comments}\n"
            f"🕒 Posted: {timestamp}"
        )

        await status_msg.edit_text("📥 Downloading video...")

        try:
            await update.message.reply_video(
                video=link,
                caption=caption
            )
        except Exception:
            await update.message.reply_text(f"Here is the Video: {link}")

        await status_msg.edit_text("✅ Video downloaded and sent!")

    except Exception as e:
        await update.message.reply_text("Something went wrong... ❌")
        print(f"Error: {e}")

app = Application.builder().token(token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_instagram_link))

print("Bot Started...")
app.run_polling()


