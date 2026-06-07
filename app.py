from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    
    if msg.lower() in ["hi", "hello", "hey"]:
        reply = "Hey Ayush! 👋 Main tumhara WhatsApp AI bot LIVE ho gaya. Kuch bhi pucho!"
    else:
        reply = f"Tumne bola: '{msg}'\n\nBot working 100% ✅"
    
    resp.message(reply)
    return str(resp)

@app.route("/")
def home():
    return "WhatsApp Bot is Running"
