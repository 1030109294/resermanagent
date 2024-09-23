from flask import Blueprint
from models import MemoryModel
from exts import db

bp = Blueprint("memory",__name__,url_prefix='/memory')

@bp.route('/getMemoryByUid')
def getMemoryByUid(uid):
    return MemoryModel.query.filter_by(u_id=uid).first()

@bp.route('/addMemory')
def addmemory(memory, uid):
    print(memory)
    disk_dao = MemoryModel(m_total=memory.get('memory_total'), m_used=memory.get('memory_used'),
                         m_utilization=memory.get('memory_utilization'), u_id=uid, m_free=memory.get('memory_free'))
    db.session.add(disk_dao)
    db.session.commit()
