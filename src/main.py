from flask import Flask
from routes.auth import auth_bp  # چون توی src هستی، این مسیر درسته

app = Flask(__name__)
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return 'سیستم مدیریت غذای شرکت فعال است.'

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
