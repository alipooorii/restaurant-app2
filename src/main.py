from flask import Flask
from routes.auth import auth_bp
from database.db import init_db

app = Flask(__name__)
init_db()
app.register_blueprint(auth_bp)

@app.route("/")
def index():
    return "سیستم مدیریت غذای شرکت فعال است."

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
