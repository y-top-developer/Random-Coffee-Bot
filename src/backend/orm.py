import logging
from sqlalchemy.orm import sessionmaker

from backend.models import User, Company, Pair, engine

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

session = sessionmaker(engine)()

# user


def get_user(user_id):
    user = (
        session.query(
            User
        )
        .filter(
            User.telegram_id == user_id,
        )
        .first()
    )
    return user


def set_user(user_id):
    session.add(User(
        language_code='en',
        telegram_id=user_id,
    ))
    session.commit()


def set_user_field(user_id, key, value):
    (
        session.query(
            User
        )
        .filter(
            User.telegram_id == user_id,
        )
        .update(
            {key: value}
        )
    )
    session.commit()

# company


def get_company(company_name):
    company = (
        session.query(
            Company
        )
        .filter(
            Company.name == company_name,
        )
        .first()
    )
    return company


def get_company_by_password(password):
    company = (
        session.query(
            Company
        )
        .filter(
            Company.password == password,
        )
        .first()
    )
    return company


def set_company_field(company_name, key, value):
    (
        session.query(
            Company
        )
        .filter(
            Company.name == company_name,
        )
        .update(
            {key: value}
        )
    )
    session.commit()

# pair
