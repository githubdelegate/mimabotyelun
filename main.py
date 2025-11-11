from fastapi import FastAPI, Request
from telebot import TeleBot, types
import os

TOKEN = "8475017908:AAEgbsEg4kqt8afUXGRds6sKfOcEZX4C0cQ"
bot = TeleBot(TOKEN)

app = FastAPI()

# -------------------------
# 消息处理函数
# -------------------------
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "你好，我是mimabot机器人！")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.send_message(message.chat.id, "嘻嘻")

# -------------------------
# Webhook 接口
# -------------------------
@app.post(f"/webhook/{TOKEN}")
async def telegram_webhook(request: Request):
    json_data = await request.json()
    bot.process_new_updates([types.Update.de_json(json_data)])
    return {"ok": True}



# -------------------------
# 设置 Webhook 的路由
# -------------------------
@app.get("/set_webhook")
def set_webhook():
    # Vercel 部署后的 URL，需要改成你自己的
    vercel_url = "https://your-app.vercel.app"
    url = f"{vercel_url}/webhook/{TOKEN}"
    if bot.set_webhook(url):
        return {"status": "Webhook set", "url": url}
    else:
        return {"status": "Failed to set webhook"}


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/chat")
def read_chat():
    return {"Hello": "Chat"}

# 如果你需要加更多路由，就在这儿扩展，就跟搭积木似的

# 这块儿加给Vercel用的，就跟点火启动似的
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)