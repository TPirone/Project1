from flask import Blueprint, request, session
from service.user_service import UserService
from exceptions.user_registration import UserRegisterError
from exceptions.user_not_found import UserNotFound
from exceptions.login_error import LoginError
from model.user import User

user_control = Blueprint('user_control', __name__)
user_service = UserService()

@user_control.route('/user/<userid>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        return user_service.get_user_by_id(user_id)
    except UserNotFound as e:
        return {
            "message": str(e)
        }, 404
@user_control.route('/loginstatus', methods=['GET'])
def loginstatus():
    if session.get('user_info') is not None:
        return {
            "message": "You are currently logged in", "logged_in_user": session.get('user_info')
        }, 200
    else:
        return {
            "message" : "You are currently not logged in"
        }, 200
@user_control.route('/login', methods=['POST'])
def login():
    login_body_dict = request.get_json()
    username = login_body_dict['username']
    password = login_body_dict['password']
    try:
        user_dict = user_service.login(username, password)
        session['user_info'] = user_dict
        return user_dict, 200
    except LoginError as e:
        return {
            "message":str(e)
        }, 400
@user_control.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return {
        "message": "You've been logged out"
    }, 200
@user_control.route('/user', methods=['POST'])
def add_user():
    user_body_dict = request.get_json()
    user_object = User(None, user_body_dict['username'], user_body_dict['password'], user_body_dict['first_name'], user_body_dict['last_name'], user_body_dict['phone_number'], user_body_dict['email_address'], user_body_dict['role'])
    try:
        added_user = user_service.add_user(user_object), 201
    except UserRegisterError as e:
        return {
            "messages": e.messages
        }
    return added_user, 201
@user_control.route('/user/<user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    try:
        user_body_dict = request.get_json()
        return user_service.update_user_by_id(User(user_id, user_body_dict['username'], user_body_dict['password'], user_body_dict['first_name'], user_body_dict['last_name'],
                                                   user_body_dict['phone_number'], user_body_dict['email_address'], user_body_dict['role']))
    except UserNotFound as e:
        return{
            "message": str(e)
        }, 404