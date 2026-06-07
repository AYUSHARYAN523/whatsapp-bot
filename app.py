from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp():
    incoming = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    if 'hi' in incoming or 'hello' in incoming:
        msg.body("Hey Ayush! 👋 Main tumhara WhatsApp AI bot LIVE ho gaya. Ab kaam kar raha hun!")
    else:
        msg.body(f"Tumne bola: {incoming}")
    
    return str(resp)

@app.route("/")
def home():
    return "Bot is running!"
