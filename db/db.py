import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .model import Mall, Restaurant, Promotion
from config import get_sqlconfig

class DAO:
    def __init__(self, user, pwd, host, db):
        self._engine = create_engine("mysql://{}:{}@{}/{}".format(
            user, pwd, host, db), echo=True, pool_size=10)
        self._engine.connect()
        
        self.Session = sessionmaker(bind=self._engine)

    def get_mall(self, mall_name):
        '''

        :param mall_name:
        :return: mall_id if found, None if not found
        '''
        session = self.Session()
        result = (session.query(Mall)
              .filter(Mall.name == mall_name).all())
        if result is not None and len(result) == 1:
            return result[0]
        else:
            return None
    
    def get_random_choice(self, mall_id, cuisine=None, promo_bank=None, is_hala=None, is_vege=None):
        '''
            return None if not found
            return [Mall, Restaurant, [Promotion]] if found
        '''
        session = self.Session()
        hala = "Y" if is_hala else "N"
        vege = "Y" if is_vege else "N"
        q = (session.query(Mall,Restaurant)
            .filter(Mall.mid == Restaurant.mid)
            .filter(Mall.mid == mall_id))
        
        if cuisine:    
            q = q.filter(Restaurant.cuisine == cuisine)
        
        if promo_bank:    
            q = q.filter(Promotion.bank == promo_bank)
        
        if is_hala is not None:
            q = q.filter(Restaurant.is_halal == hala)
        
        if is_vege is not None:
            q = q.filter(Restaurant.is_veg == vege)
        
        ret = q.all()

        if len(ret) == 0:
            return None
        
        ret = ret[random.randint(0, len(ret)-1)]
        mall = ret[0]
        res = ret[1]

        promotions = (session.query(Promotion)
            .filter(Promotion.rid == res.rid).limit(5).all())
        
        return (mall, res, promotions)
    
    def get_ads(self, recommend_rest_id, mall_id):
        # default to 5
        number_of_ads = 5

        session = self.Session()
        all_promotion_restaurants = (session.query(Restaurant)
         .filter(Restaurant.mid == mall_id)
        .filter(Restaurant.rid != recommend_rest_id)
        .filter(Restaurant.ad == 'Y')
        .all())

        return random.sample(all_promotion_restaurants, min(len(all_promotion_restaurants), number_of_ads))


dao_obj = None

def get_dao():
    global dao_obj
    if not dao_obj: 
        sql_config = get_sqlconfig()
        dao_obj = DAO(sql_config.username, sql_config.pwd, sql_config.host, sql_config.db)

    return dao_obj

def to_dict(obj):
    """
    convert object to python dict
    """
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

def format_restaurant(input_rest, input_promo):
    if input_promo:
        promotion = [to_dict(p) for p in input_promo]
        for p in promotion:
            p['id'] = str(p['pid'])
            del p['pid']
            del p['rid']
    else:
        promotion = []

    resturant = to_dict(input_rest)
    resturant['promotions'] = promotion
    resturant['id'] = str(resturant['rid'])
    resturant['is_halal'] = (resturant['is_halal'] == 'Y')
    resturant['is_veg'] = (resturant['is_veg'] == 'Y') 
    del resturant['rid']
    del resturant['mid']
    del resturant['ad']
    del resturant['rating']

    return resturant

def format_mall(input_mall):
    mall = to_dict(input_mall)
    del mall['mid']
    return mall
