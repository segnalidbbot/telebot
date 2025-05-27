import asyncio
import requests
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from datetime import datetime

BOT_TOKEN = '7996855061:AAFz6yh7CDhtRIRkhA0vSXjBJkcTIOBHXrE'
CHANNEL_USERNAME = '@consulenteperilrisparmio'

TWILIO_SID = 'AC63154505cf21e886275887d14b3d105e'
TWILIO_TOKEN = 'fa8b60c5387d6072bffbcce5a668e97d'
TWILIO_FROM = 'whatsapp:+14155238886'
TWILIO_TO = 'whatsapp:+393511937470'

prodotti = [
    {
        "nome": "📱 Smartphone Xiaomi Redmi 14C 8+256GB",
        "prezzo": "99,99€ (da 169,00€)",
        "link": "https://www.bigtelemarketing.com/shop/smartphone-e-cellulari"
    },
    {
        "nome": "📺 Smart TV VOV 32'' HD Android",
        "prezzo": "109,99€ (da 149,99€)",
        "link": "https://www.bigtelemarketing.com/shop/tv-e-audio-video"
    }
]

def genera_messaggio():
    messaggio = f"🕒 *Promo del {datetime.now().strftime('%d/%m/%Y %H:%M')}*\n\n"
    for p in prodotti:
        messaggio += f"{p['nome']}\n💰 *{p['prezzo']}*\n👉 {p['link']}\n\n"
    messaggio += "📲 WhatsApp: https://wa.me/393511937470\n🌐 www.bigtelemarketing.com"
    return messaggio

async def invia_telegram():
    bot = Bot(BOT_TOKEN)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 WhatsApp", url="https://wa.me/393511937470")],
        [InlineKeyboardButton("🛒 Visita Shop", url="https://www.bigtelemarketing.com")]
    ])
    await bot.send_message(
        chat_id=CHANNEL_USERNAME,
        text=genera_messaggio(),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True
    )

def invia_whatsapp():
    msg = genera_messaggio().replace("*", "")
    url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json"
    data = {
        "To": TWILIO_TO,
        "From": TWILIO_FROM,
        "Body": msg
    }
    res = requests.post(url, data=data, auth=(TWILIO_SID, TWILIO_TOKEN))
    print("WhatsApp:", res.status_code, res.text)

async def main():
    await invia_telegram()
    invia_whatsapp()

if __name__ == "__main__":
    asyncio.run(main())
