from flask import Blueprint
from models import CpuModel
from exts import db
bp = Blueprint("cpu",__name__,url_prefix='/cpu')

class Cpu:
    def __init__(self, count,freq,utilization,uuid):
        self.count = count
        self.freq = freq
        self.utilization = utilization
        self.uid = uuid

    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"


@bp.route('/getCpuByUid')
def getCpuByUid(uid):
    return CpuModel.query.filter_by(u_id=uid).first()


@bp.route('/addCpu')
def addCpu(cpu,uid):
    cpu_dao = CpuModel(cpu_count=cpu.get('cpu_count'), cpu_freq=cpu.get('cpu_freq'),
                       cpu_utilization=cpu.get('cpu_utilization'), u_id=uid)
    db.session.add(cpu_dao)
    db.session.commit()
