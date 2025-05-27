import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from datetime import datetime

BOT_TOKEN = '7996855061:AAFz6yh7CDhtRIRkhA0vSXjBJkcTIOBHXrE'
CHANNEL_USERNAME = '@consulenteperilrisparmio'

# Offerte aggiornate da www.bigtelemarketing.com
prodotti = [
    {
        "categoria": "📱 Smartphone",
        "nome": "Xiaomi Redmi 14C 8+256GB",
        "prezzo": "99,99€ (anziché 169,00€)",
        "link": "https://www.bigtelemarketing.com/shop/p/xiaomi-redmi-14c",
        "img": "https://www.bigtelemarketing.com/_files/ugd/0ca1a1_5b0f2e3b1e4a4a1cbdcb5c837e93c9f3~mv2.jpg"
    },
    {
        "categoria": "📺 TV & Audio",
        "nome": "Smart TV VOV 32'' HD Android",
        "prezzo": "109,99€ (anziché 149,99€)",
        "link": "https://www.bigtelemarketing.com/shop/p/smart-tv-vov-32",
        "img": "https://www.bigtelemarketing.com/_files/ugd/0ca1a1_e2d67b5569cf48a2b7c20714b57b51d7~mv2.jpg"
    },
    {
        "categoria": "☕ Caffè & Cucina",
        "nome": "Macchina da Caffè Faber a Cialde",
        "prezzo": "109,99€ (anziché 149,99€)",
        "link": "https://www.bigtelemarketing.com/shop/p/macchina-caffe-faber",
        "img": "https://www.bigtelemarketing.com/_files/ugd/0ca1a1_4537d8f01675467a8ef9e92d124b46e0~mv2.jpg"
    }
]

async def invia_telegram():
    bot = Bot(BOT_TOKEN)
    for prodotto in prodotti:
        caption = (
            f"*{prodotto['categoria']}*\n\n"
            f"📦 {prodotto['nome']}\n"
            f"💰 *{prodotto['prezzo']}*\n"
            f"👉 [Acquista ora]({prodotto['link']})\n\n"
            f"🕒 Promo automatica del {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💬 WhatsApp", url="https://wa.me/393511937470")],
            [InlineKeyboardButton("🛒 Visita lo Shop", url="https://www.bigtelemarketing.com")]
        ])
        await bot.send_photo(
            chat_id=CHANNEL_USERNAME,
            photo=prodotto['img'],
            caption=caption,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard
        )

if __name__ == "__main__":
    asyncio.run(invia_telegram())
