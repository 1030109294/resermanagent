#数据库配置
#MYSQL所在的主机名
HOSTNAME ="127.0.0.1"
#MYSQL监听的端口号，默认3306
PORT = '3306'
#连接MYSQL的用户名:读者用自己设置的
USERNAME ="root"
#连接MYSQL的密码、读者用自己的
PASSWORD ="123456"
#MYSQL上创建的数据库名称
DATABASE ="servermanagement"
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD, HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI



