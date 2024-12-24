from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simulated Database
messages = []

# Keywords to Detect
sensitive_keywords = ["confidential", "password", "account"]

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    subject = data.get("subject", "")
    content = data.get("content", "")
    recipient = data.get("recipient", "")

    is_sensitive = any(keyword in content.lower() for keyword in sensitive_keywords)

    message = {"subject": subject, "content": content, "recipient": recipient, "sensitive": is_sensitive}
    messages.append(message)

    if is_sensitive:
        return jsonify({"message": "Sensitive content detected!", "status": "alert"})
    return jsonify({"message": "Message sent successfully!", "status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
