from flask_sqlalchemy import SQLAlchemy
#这个文件解决循环引用的问题  第三方插件
db = SQLAlchemy()