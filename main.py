from flask import Flask
from data import db_session
from sqlalchemy import orm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_mission_1.db")
    # капитан
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    # колонист 1
    user_1 = User()
    user_1.name = "Kate"
    user_1.surname = "Scott"
    user_1.age = 25
    user_1.position = "chief officer"
    user_1.speciality = "it engineer"
    user_1.address = "module_1"
    user_1.email = "kate_scott@mars.org"
    user_1.hashed_password = "chief"
    # колонист 2
    user_2 = User()
    user_2.name = "Mike"
    user_2.surname = "Bishop"
    user_2.age = 30
    user_2.position = "third officer"
    user_2.speciality = "support engineer"
    user_2.address = "module_1"
    user_2.email = "mike_bishop@mars.org"
    user_2.hashed_password = "third"
    # колонист 3
    user_3 = User()
    user_3.name = "Ginny"
    user_3.surname = "Mickaelson"
    user_3.age = 22
    user_3.position = "second officer"
    user_3.speciality = "сombat systems engineer"
    user_3.address = "module_1"
    user_3.email = "ginny_mick@mars.org"
    user_3.hashed_password = "sec"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user_1)
    db_sess.add(user_2)
    db_sess.add(user_3)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()