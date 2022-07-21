import re
from dao.user_dao import UserDao
from exceptions.user_registration import UserRegisterError
from exceptions.login_error import LoginError
from exceptions.user_not_found import UserNotFound

class UserService:
    def __init__(self):
        self.user_dao = UserDao()
    def login(self, username, password):
        user_object = self.user_dao.get_user_by_username_and_pasword(username, password)
        return user_object.to_dict()
    def add_user(self, user_object):
        # username registration
        user_register_error = UserRegisterError()
        if not user_object.username.isalnum():
            user_register_error.messages.append("Username can only contain alphabetical and numerical characters")
        if len(user_object) < 6 or len(user_object) > 20:
            user_register_error.messages.append("Username can only be greater than 6 or less than 20 characters")
        if self.user_dao.get_user_by_username(user_object.username) is not None:
            user_register_error.messages.append("Username is already taken. Please create another")
        if user_object.username == '':
            user_register_error.append("Username can't be blank")
        # password registration
        alphabetical_characters = "abcdefghijklmnopqrstuvwxyz"
        special_characters = "!@#$%^&*)("
        numeric_characters = "1234567890"

        lower_alpha_count = 0
        upper_alpha_count = 0
        special_character_count = 0
        numeric_character_count = 0
        for char in user_object.password:
            if char in alphabetical_characters:
                lower_alpha_count += 1
            if char in alphabetical_characters.upper():
                upper_alpha_count += 1
            if char in special_characters:
                special_character_count += 1
            if char in numeric_characters:
                numeric_character_count =+ 1
        if lower_alpha_count == 0:
            user_register_error.messages.append("Password must contain at least 1 lowercase letter")
        if upper_alpha_count == 0:
            user_register_error.messages.append("Password must contain at least 1 uppercase letter")
        if special_character_count == 0:
            user_register_error.messages.append("Password must contain at least 1 special character '(!@#$%^&*())'")
        if numeric_character_count == 0:
            user_register_error.messages.append("Password must contain at least 1 number")
        if len(user_object.password) < 6 or len(user_object.password) > 20:
            user_register_error.messages.append("Password must be greater than 6 characters or less than 20 characters")
        if len(user_object.password) != lower_alpha_count + upper_alpha_count + special_character_count + numeric_character_count:
            user_register_error.messages.append("Password can only contain alphabetical, numerical, and special characters")
        if user_object.password == '':
            user_register_error.messages.append("Password cannot be blank")
        # first name registration
        if not user_object.first_name.isalpha():
            user_register_error.messages.append("First name can only contain alphabetical characters")
        if user_object.first_name == '':
            user_register_error.messages.append("First name cannot be blank")
        # last name registration
        if not user_object.last_name.isalpha():
            user_register_error.messages.append("Last name can only contain alphabetical characters")
        if user_object.last_name == '':
            user_register_error.messages.append("Last name cannot be blank")
        # email address registration
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', user_object.email_address):
            user_register_error.messages.append("Email address can only be of the format <username>@<domain>")
        if self.user_dao.get_user_by_email(user_object.email_address) is not None:
            user_register_error.messages.append("Email address is already in use")
        if user_object.email_address == '':
            user_register_error.messages.append("Email address cannot be blank")
        # phone number registration
        if not re.fullmatch("\d{3}-\d{3}-\d{4}", user_object.phone_number):
            user_register_error.messages.append("Phone number can only be of the format XXX-XXX-XXXX")
        if user_object.phone_number == '':
            user_register_error.messages.append("Phone number cannot be blank")

        if len(user_register_error.messages) > 0:
            raise user_register_error

        added_user_obj = self.user_dao.add_user(user_object)

        return added_user_obj.to_dict()

    def update_user_by_id(self, user_object):
        updated_user_object = self.user_dao.update_user_by_id(user_object)
        if updated_user_object is None:
            raise UserNotFound(f"User with id {user_object.id} was not found")
        return updated_user_object.to_dict()


