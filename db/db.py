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
    
    def get_random_choice(self, mall, cuisine=None, promo_bank=None, is_hala=None, is_vege=None):
        '''
            return None if not found
            return (Mall, Restaurant, Promotion) if found
        '''
        session = self.Session()
        hala = "Y" if is_hala else "N"
        vege = "Y" if is_vege else "N"
        q = (session.query(Mall,Restaurant,Promotion)
            .filter(Mall.mid == Restaurant.mid)
            .filter(Promotion.rid == Restaurant.rid)
            .filter(Mall.name == mall))
        
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
        
        return ret[random.randint(0, len(ret)-1)]
            
dao_obj = None

def get_dao():
    global dao_obj
    if not dao_obj: 
        sql_config = get_sqlconfig()
        dao_obj = DAO(sql_config.username, sql_config.pwd, sql_config.host, sql_config.db)

    return dao_obj
        





