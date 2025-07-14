from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/register-step1', methods=['POST'])
def register_step1():
    data = request.get_json()
    employee_id = data.get('employee_id')
    national_id = data.get('national_id')

    return jsonify({
        "message": "ثبت‌نام مرحله اول موفق بود",
        "employee_id": employee_id,
        "national_id": national_id
    })
