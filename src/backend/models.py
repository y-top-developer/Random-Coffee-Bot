import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, create_engine

Base = declarative_base()
engine = create_engine('sqlite:///db.db?check_same_thread=False')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    state = Column(Integer, default=0)
    language_code = Column(String, nullable=False)
    telegram_id = Column(String, nullable=False)
    name = Column(String, default='', nullable=False)
    link = Column(String, default='', nullable=False)
    work = Column(String, default='', nullable=False)
    about = Column(String, default='', nullable=False)
    companies = Column(String, default='', nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)

    def __repr__(self):
        return (f'<User {self.id} state:{self.state} telegram_id:{self.telegram_id} telegram_id:{self.created_at}>')


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String, default='', nullable=False, unique=True)
    password = Column(String, nullable=False, unique=True)
    company_admin = Column(String, default='', nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)

    def __repr__(self):
        return (f'<Company {self.id} name:{self.name} company_admin:{self.company_admin} created_at:{self.created_at}>')


class Pair(Base):
    __tablename__ = 'pair'

    id = Column(Integer, primary_key=True)
    user_a = Column(String, nullable=False)
    user_b = Column(String, nullable=False)
    company = Column(String, nullable=False)
    paired_at = Column(DateTime, nullable=False)
    created_at = Column(
        DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now, nullable=False)

    def __repr__(self):
        return (f'<Pair {self.id} user_a:{self.user_a} user_b:{self.user_b} paired_at:{self.paired_at}>')


Base.metadata.create_all(engine)
