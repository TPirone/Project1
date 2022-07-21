import psycopg
from model.user import User


class UserDao:

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
                    phone_number = users[5]
                    email_address = users[6]
                    role = users[7]
                    my_user_object = User(user_id, username, password, first_name, last_name, phone_number,
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
                user_id = user_info[0]
                username = user_info[1]
                password = user_info[2]
                first_name = user_info[3]
                last_name = user_info[4]
                phone_number = user_info[5]
                email_address = user_info[6]
                role = user_info[7]

                return User(user_id, username, password, first_name, last_name, phone_number, email_address, role)

    def get_user_by_email(self, email_address):
        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres", dbname="Project1",
                             password="Starwars14!") as conn:
            with conn.cursor() as cur:
                cur.excute("SELECT * FROm users WHERE email_address = %s", (email_address,))

                user_info = cur.fetchone()

                if user_info is None:
                    return None

                user_id = user_info[0]
                username = user_info[1]
                password = user_info[2]
                first_name = user_info[3]
                last_name = user_info[4]
                phone_number = user_info[5]
                email_address = user_info[6]
                role = user_info[7]

                return User(user_id, username, password, first_name, last_name, phone_number, email_address, role)

    def get_user_by_username(self, username):
        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres", dbname="Project1",
                             password="Starwars14!") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE username = %s", (username,))
                user_info = cur.fetchone()

                if user_info is None:
                    return None
                user_id = user_info[0]
                username = user_info[1]
                password = user_info[2]
                first_name = user_info[3]
                last_name = user_info[4]
                phone_number = user_info[5]
                email_address = user_info[6]
                role = user_info[7]
                return User(user_id, username, password, first_name, last_name, phone_number, email_address, role)

    def add_user(self, user_object):
        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres", dbname="Project1",
                             password="Starwars14!") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *",
                            user_object.username, user_object.password, user_object.first_name, user_object.last_name,
                             user_object.phone_number, user_object.email_address, user_object.role)
                user_that_was_inserted = cur.fetchone()
                conn.commit()
                return User(user_that_was_inserted[0], user_that_was_inserted[1], user_that_was_inserted[2],
                            user_that_was_inserted[3], user_that_was_inserted[4], user_that_was_inserted[5], user_that_was_inserted[6])
