from flask import Flask, render_template, request
import pickle
from extract_features import extract_features_from_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    reason = ""
    if request.method == "POST":
        url = request.form["url"]
        features = extract_features_from_url(url)

        # Manual rule-based prediction
        reasons = []

        if features[1] == 0:
            reasons.append("Website does not use HTTPS (secure connection missing).")
        if features[2] == 1:
            reasons.append("URL contains '@' symbol (commonly used in phishing).")
        if features[3] == 1:
            reasons.append("URL is unusually long (can hide malicious parts).")
        if features[4] == 1:
            reasons.append("URL contains words like 'login' or 'secure' to mislead users.")
        if features[0] == 1:
            reasons.append("URL mimics well-known domains (e.g., facebook.com).")

        # If any reason exists, flag as phishing
        if reasons:
            prediction = 1  # Phishing
            reason = " | ".join(reasons)
        else:
            prediction = 0  # Safe

    return render_template("index.html", prediction=prediction, reason=reason)

if __name__ == "__main__":
    app.run(debug=True,port=1000)
