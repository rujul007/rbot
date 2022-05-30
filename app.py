from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")
    response = MessagingResponse()
    response.message(f"माझ्याी संपर्क  धन्यवाद. तुम्ही पाठवले आहे '{text}' या क्रमांकावरून {number[-10:]}")
    return str(response)


if __name__ == "__main__":
    app.run()
