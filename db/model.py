from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Mall(Base):
    __tablename__ = 'malls'

    mid = Column(Integer, primary_key=True)
    name = Column(String)
    district = Column(String)
    address = Column(String)
    description = Column(String)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    rid = Column(Integer, primary_key=True)
    mid = Column(Integer)
    name = Column(String)
    cuisine = Column(String)
    is_halal = Column(String)
    is_veg = Column(String)
    unit = Column(String)
    phone = Column(String)
    hours = Column(String)
    description = Column(String)
    website = Column(String)
    pic_url = Column(String)
    ad = Column(String)
    rating = Column(Float)

class Promotion(Base):
    __tablename__ = 'promotions'

    pid = Column(Integer, primary_key=True)
    rid = Column(Integer)
    bank = Column(String)
    card = Column(String)
    promo = Column(String)

"""
create table cuisine_types(
cid int primary key,
cuisine_type text)
"""
class CuisineType(Base):
    __tablename__ = 'cuisine_types'

    cid = Column(Integer, primary_key=True)
    cuisine_type = Column(String) 