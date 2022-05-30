from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://dbuser:dbpass@cluster0.jrbed.mongodb.net/?retryWrites=true&w=majority")

db = cluster["shop"]
users = db["users"]
orders = db["orders"]

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")
    res = MessagingResponse()
    user = users.find_one({"number": number})
    print (text)
    if bool(user) == False:
        msg = res.message("नमस्कार, वॉर्ड7शी संपर्क साधल्याबद्दल धन्यवाद \n तुम्ही खालीलपैकी एक पर्याय निवडू शकता \n\n टाईप करा 1️⃣ माझ्याबद्दल जाणून घेण्यासाठी \n 2️⃣ माझ्याशी संपर्क साधण्यासाठी \n 3️⃣ माझ्या ताज्या बातम्या जाणून घेण्यासाठी \n 4️⃣ माझ्या विकासाच्या बातम्या जाणून घेण्यासाठी \n 5️⃣ माझ्या भविष्यातील योजना जाणून घेण्यासाठी ")
        msg.media("https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.majhimarathi.com%2Fwp-content%2Fuploads%2F2020%2F02%2FAjit-Pavar.jpg&imgrefurl=https%3A%2F%2Fwww.majhimarathi.com%2Fajit-pawar-biography-in-marathi%2Fajit-pavar%2F&tbnid=b1wdOf292g5U1M&vet=12ahUKEwjgvdfMjvr3AhW3i9gFHWcSA-4QMygsegUIARClAg..i&docid=owuDQR3XX8xjUM&w=700&h=500&q=ajit%20pawar%20images&ved=2ahUKEwjgvdfMjvr3AhW3i9gFHWcSA-4QMygsegUIARClAg")
        users.insert_one({"number": number, "status": "main", "messages": []})
    elif user["status"] == "main":
        try:
            option = int(text)
        except:
            res.message("कृपया वैध प्रतिसाद प्रविष्ट करा")
            return str(res)

        if option == 1:
            msg = res.message("अजित अनंतराव पवार हे एक भारतीय राजकारणी आणि राष्ट्रवादी काँग्रेस पार्टी (NCP) चे सदस्य आहेत. ते भारतीय ज्येष्ठ राजकीय नेते आणि राष्ट्रवादी काँग्रेसचे अध्यक्ष शरद पवार यांचे पुतणे आहेत. बारामती मतदारसंघातून ते विधानसभेचे सदस्य म्हणून निवडून आले")
            msg.media("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flickr.com%2Fphotos%2Fvivek_morepatil%2F11511268065&psig=AOvVaw1RMvj4fGwVV79GXze23Xis&ust=1653551995961000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCPDevrmX-vcCFQAAAAAdAAAAABAF")
        elif option == 2:
            res.message("तुम्ही माझ्याशी \n\n फोन:9175634856 किंवा \n ईमेल:ward7@gmail.com \n द्वारे संपर्क साधू शकता")
        elif option == 3:
            res.message("ुणे : तीक्ष्ण वळणे न सुटल्यास सिंहगड किल्ल्यावर जाणारी ई-बस सेवा बंद ठेवण्यास आपण पुणे महानगर परिवहन महामंडळ लिमिटेड (पीएमपीएमएल) आणि वन अधिकाऱ्यांना सांगितले असल्याचे उपमुख्यमंत्री अजित पवार यांनी सोमवारी सांगितले.")

        elif option == 4:
            res.message("या माध्यमातून शेतकऱ्‍यांची गुणवत्तापूर्ण उत्पादनं आता ग्राहकांना उपलब्ध होणार आहेत. सध्या मॅाल संस्कृती पुढे येत असून या संस्कृतीत शेतकऱ्‍यांची कृषी उत्पादनं टिकून ग्राहकांमध्ये विश्वासार्हता निर्माण होणं गरजेचं आहे.")
        elif option == 5:
            res.message("महाराष्ट्र सरकार मुंबईतील वांद्रे परिसरात सर्व समाजातील विद्यार्थ्यांसाठी सर्वात मोठे वसतिगृह उभारणार आहे, असे राज्याचे उपमुख्यमंत्री अजित पवार यांनी रविवारी नाशिकमध्ये मुलींच्या वसतिगृहाचे लोकार्पण करताना सांगितले")
        else:
            res.message("कृपया वैध प्रतिसाद प्रविष्ट करा")
        if text == int(text):
            res.message("तुम्ही खालीलपैकी एक पर्याय निवडू शकता \n\n टाईप करा 1️⃣ माझ्याबद्दल जाणून घेण्यासाठी \n 2️⃣ माझ्याशी संपर्क साधण्यासाठी \n 3️⃣ माझ्या ताज्या बातम्या जाणून घेण्यासाठी \n 4️⃣ माझ्या विकासाच्या बातम्या जाणून घेण्यासाठी \n 5️⃣ माझ्या भविष्यातील योजना जाणून घेण्यासाठी")
    users.update_one({"number": number}, {"$set": {"status": "main"}})


if __name__ == "__main__":
    app.run()
