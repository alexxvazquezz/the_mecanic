from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import User

bp = Blueprint('profile', __name__)

@bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    data = request.get_json()
    username = data.get('username')

    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400
    
    user.username = username
    db.session.commit()

    return jsonify({'message': 'Profile updates successfully'}), 200