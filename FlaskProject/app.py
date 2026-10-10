from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        send_email(name, email, message)

        return render_template("contact.html", success=True)

    return render_template("contact.html")


def send_email(name, email, message):
    msg = EmailMessage()
    msg["Subject"] = "New Contact Form Submission"
    msg["From"] = "kmblueman@icloud.com"
    msg["To"] = "kmblueman@icloud.com"

    msg.set_content(f"""
Name: {name}
Email: {email}

Message:
{message}
""")

    # iCloud SMTP
    smtp_server = "smtp.mail.me.com"
    smtp_port = 587
    smtp_user = "kmblueman@icloud.com"
    smtp_pass = "lxnj-rekb-owad-kdji"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/services")
def services():
    return render_template("services.html")


