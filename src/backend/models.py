import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, create_engine, create_engine

Base = declarative_base()
engine = create_engine('sqlite:///db.db?check_same_thread=False')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
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
        return (f'<User {self.id} {self.telegram_id} {self.created_at}>')


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String, default='', nullable=False)
    company_admin = Column(String, default='', nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)

    def __repr__(self):
        return (f'<Company {self.id} {self.name} {self.company_admin} {self.created_at}>')


class Pair(Base):
    __tablename__ = 'pair'

    id = Column(Integer, primary_key=True)
    user_a = Column(String, nullable=False)
    user_b = Column(String, nullable=False)
    paired_at = Column(DateTime, nullable=False)
    created_at = Column(
        DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now, nullable=False)

    def __repr__(self):
        return (f'<Pair {self.id} {self.user_a} {self.user_b} {self.paired_at}>')
