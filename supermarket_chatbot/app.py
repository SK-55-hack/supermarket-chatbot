from flask import Flask, render_template, request, session, redirect, url_for
from chatbot import SupermarketChatbot

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure key

# Initialize chatbot instance
chatbot = SupermarketChatbot()

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            # Get bot response
            bot_reply = chatbot.get_response(user_input)
            # Store conversation in session
            session["chat_history"].append(("You", user_input))
            session["chat_history"].append(("Bot", bot_reply))
            session.modified = True
        return redirect(url_for("index"))

    return render_template("index.html", chat_history=session["chat_history"])

@app.route("/reset")
def reset():
    session.pop("chat_history", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
