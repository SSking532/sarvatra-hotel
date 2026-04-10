from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# ✅ ALL RESPONSES (40+ QUESTIONS)
def chatbot(user_input):

    if not user_input:
        return "Please type something 🙂"

    user_input = user_input.lower()

    # greetings
    if 'bye' in user_input or 'exit' in user_input:
        return "Goodbye! Have a luxurious day ✨"

    elif 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
        return "Hello! Welcome to Sarvatra Hotel 😊"

    # rooms & booking
    elif 'room types' in user_input:
        return "We have Deluxe, Executive, and Presidential Suites."

    elif 'rooms' in user_input or 'room' in user_input:
        return "We offer Deluxe, Suite, and Luxury rooms."

    elif 'price' in user_input or 'cost' in user_input:
        return "Prices range from ₹3000 to ₹15000 per night."

    elif 'booking' in user_input:
        return "You can book rooms directly on our website."

    elif 'reservation' in user_input:
        return "Reservations can be made online or by calling us."

    elif 'availability' in user_input:
        return "Please provide dates to check availability."

    # check-in/out
    elif 'checkin' in user_input or 'check-in' in user_input:
        return "Check-in time is 12 PM."

    elif 'checkout' in user_input or 'check-out' in user_input:
        return "Check-out time is 11 AM."

    elif 'early checkin' in user_input:
        return "Early check-in depends on availability."

    elif 'late checkout' in user_input:
        return "Late checkout may be available on request."

    # facilities
    elif 'wifi' in user_input:
        return "Free high-speed WiFi is available."

    elif 'parking' in user_input:
        return "Free secure parking is available 🚗"

    elif 'pool' in user_input:
        return "Yes, we have a luxury swimming pool 🏊"

    elif 'gym' in user_input:
        return "Yes, we have a fully equipped gym 💪"

    elif 'spa' in user_input:
        return "Relax with our premium spa services 🧖"

    elif 'restaurant' in user_input:
        return "We have a multi-cuisine restaurant 🍽️"

    elif 'bar' in user_input:
        return "Yes, we have a premium bar 🍷"

    elif 'laundry' in user_input:
        return "Laundry service is available."

    elif 'room service' in user_input:
        return "24/7 room service is available."

    # food
    elif 'food' in user_input:
        return "We serve Indian, Chinese, and Continental cuisines."

    elif 'breakfast' in user_input:
        return "Complimentary breakfast is included."

    elif 'menu' in user_input:
        return "You can view the menu at the restaurant or via room service."

    # location
    elif 'location' in user_input:
        return "We are located in the heart of the city."

    elif 'address' in user_input:
        return "Sarvatra Hotel, City Center, India."

    elif 'airport' in user_input:
        return "Airport is 30 minutes away."

    elif 'transport' in user_input:
        return "We provide cab and travel assistance."

    elif 'parking space' in user_input:
        return "Ample parking space available."

    # policies
    elif 'cancel' in user_input:
        return "Free cancellation within 24 hours of booking."

    elif 'refund' in user_input:
        return "Refunds are processed within 5-7 days."

    elif 'id proof' in user_input:
        return "Valid ID proof is required at check-in."

    elif 'pets' in user_input:
        return "Sorry, pets are not allowed."

    elif 'smoking' in user_input:
        return "Smoking rooms are available on request."

    # hotel info
    elif 'owner' in user_input:
        return "Sarvatra is owned by Shaury Industries."

    elif 'about' in user_input:
        return "Sarvatra is a luxury hotel offering world-class hospitality."

    elif 'luxury' in user_input:
        return "We provide premium luxury services ✨"

    elif 'facilities' in user_input:
        return "We offer spa, gym, pool, restaurant and more."

    elif 'rating' in user_input:
        return "We are rated 5⭐ by our guests."

    # contact
    elif 'contact' in user_input or 'phone' in user_input:
        return "Call us at +91 9876543210"

    elif 'email' in user_input:
        return "Email us at sarvatra@gmail.com"

    elif 'thanks' in user_input or 'thank you' in user_input:
        return "You're welcome 😊"

    # fallback
    else:
        return "I'm not sure 🤔 Try asking about rooms, price, or facilities."

 #🔥 SERVE CSS + IMAGES (IMPORTANT)
@app.route("/<path:filename>")
def serve_files(filename):
    return send_from_directory('.', filename)


# CHAT API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")

    response = chatbot(user_input)

    return jsonify({"response": response})


if __name__ == "__main__":
    print("Chatbot running at http://127.0.0.1:5000")
    app.run(debug=True)