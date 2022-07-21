import psycopg
from model.user import User


def get_all_users(self):
    with psycopg.connect(host="127.0.0.1", port="5432", user="postgres", dbname="Project1",
                         password="Starwars14!") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            list_users = []
            for users in cur:
                user_id = users[0]
                username = users[1]
                password = users[2]
                first_name = users[3]
                last_name = users[4]
                gender = users[5]
                phone_number = users[6]
                email_address = users[7]
                role = users[8]
                my_user_object = User(user_id, username, password, first_name, last_name, gender, phone_number,
                                      email_address, role)
                list_users.append(my_user_object)
            return list_users

def get_user_by_username_and_password(self, username, password):
    with psycopg.connect(host="127.0.0.1", port="5432", user="postgres", dbname="Project1",
                         password="Starwars14!") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE username = %s and password = %s", (username, password))
            user_info = cur.fetchone()
            if user_info is None:
                return None
            user_id = users[0]
            username = users[1]
            password = users[2]
            first_name = users[3]
            last_name = users[4]
            gender = users[5]
            phone_number = users[6]
            email_address = users[7]
            role = users[8]

            return User(user_id, username, password, first_name, last_name, gender, phone_number, email_address, role)
        