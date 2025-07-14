from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from models.user import User
from database.db import SessionLocal
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os

auth_bp = Blueprint("auth", __name__)
SECRET_KEY = "secret-key"

@auth_bp.route("/api/auth/register-step1", methods=["POST"])
def register_step1():
    data = request.get_json()
    employee_id = data.get("employee_id")
    national_id = data.get("national_id")

    db: Session = SessionLocal()
    user = db.query(User).filter_by(employee_id=employee_id, national_id=national_id).first()
    if user:
        return jsonify({"message": "تأیید شد"}), 200
    return jsonify({"message": "اطلاعات نادرست است"}), 400

@auth_bp.route("/api/auth/register-step2", methods=["POST"])
def register_step2():
    data = request.get_json()
    employee_id = data.get("employee_id")
    password = data.get("password")

    db: Session = SessionLocal()
    user = db.query(User).filter_by(employee_id=employee_id).first()
    if user and password:
        user.password = generate_password_hash(password)
        db.commit()
        return jsonify({"message": "ثبت‌نام کامل شد"}), 200
    return jsonify({"message": "خطا در ثبت‌نام"}), 400

@auth_bp.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    employee_id = data.get("employee_id")
    password = data.get("password")

    db: Session = SessionLocal()
    user = db.query(User).filter_by(employee_id=employee_id).first()

    if user and check_password_hash(user.password, password):
        token = jwt.encode({
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8)
        }, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"message": "ورود ناموفق"}), 401