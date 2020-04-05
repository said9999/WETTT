from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import get_sqlconfig

class DAO:
    def __init__(self, user, pwd, host, db):
        self._engine = create_engine("mysql://{}:{}@{}/{}".format(
            user, pwd, host, db), echo=True, pool_size=10)
        self._engine.connect()
        
        self.Session = sessionmaker(bind=self._engine)
    
    def get_random_choice(self, mall, cusine, promo_bank, is_hala, is_vege):
        pass

dao_obj = None

def get_dao():
    global dao_obj
    if not dao_obj: 
        sql_config = get_sqlconfig()
        dao_obj = DAO(sql_config.username, sql_config.pwd, sql_config.host, sql_config.db)

    return dao_obj
        





