import configparser

class SQLConfig:
    def __init__(self, host, pwd, port, username, db):
        self.host = host 
        self.pwd = pwd
        self.port = port
        self.username = username
        self.db = db

sql_cfg = None
def get_sqlconfig():
    global sql_cfg
    if not sql_cfg:
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        print(config)
        sql_cfg = SQLConfig(config['sql']['host'], config['sql']['password'],
            config['sql']['port'], config['sql']['user'], config['sql']['dbname'])

    return sql_cfg

