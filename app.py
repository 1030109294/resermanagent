from flask import Flask,request,jsonify
from sqlalchemy import  text
import config
from exts import db
from blueprints.cpu import bp as cpu_bp
from blueprints.gpu import bp as gpu_bp
from blueprints.disk import bp as disk_bp
from blueprints.memory import bp as memory_bp
from blueprints.user import bp as user_bp
from blueprints.index import bp as index

from models import CpuModel
from models import GpuModel
from models import MemoryModel
from models import DiskModel

from flask_migrate import Migrate

app = Flask(__name__)


#绑定配置文件
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(cpu_bp)
app.register_blueprint(gpu_bp)
app.register_blueprint(disk_bp)
app.register_blueprint(memory_bp)
app.register_blueprint(user_bp)
app.register_blueprint(index)

migrate = Migrate(app,db)


if __name__ == '__main__':
    app.run()
