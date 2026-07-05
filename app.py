from flask import Flask, render_template

# Create Flask application
app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Services Page
@app.route("/services")
def services():
    return render_template("services.html")

# Portfolio Page
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

# Pricing Page
@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Login Page
@app.route("/login")
def login():
    return render_template("login.html")

# Register Page
@app.route("/register")
def register():
    return render_template("register.html")

# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# AI Prediction Page
@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

# Prediction Result Page
@app.route("/result")
def result():
    return render_template("result.html")

# Admin Page
@app.route("/admin")
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)