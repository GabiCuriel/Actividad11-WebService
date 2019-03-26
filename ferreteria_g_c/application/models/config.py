import web

db_host = 'localhost'
db_name = 'ferreteria_g_c'
db_user = 'gabi'
db_pw = 'gabi.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )