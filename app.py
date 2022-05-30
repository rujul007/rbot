from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/", methods=['post'])
def reply():
    print ("1")
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")
    response = MessagingResponse()
    print("2")
    response.message(f"माझ्याशी संपर्क  धन्यवाद. तुम्ही पाठवले आहे '{text}' या क्रमांकावरून {number[-10:]}")
    print("3")
    return str(response)


if __name__ == "__main__":
    app.run()
