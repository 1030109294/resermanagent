from flask import Blueprint
from models import DiskModel
from exts import db
bp = Blueprint("disk",__name__,url_prefix='/disk')

@bp.route('/getDisk')
def getDisk():
    pass


@bp.route('/getDiskByUid')
def getDiskByUid(uid):
    return DiskModel.query.filter_by(u_id=uid).first()


@bp.route('/addDisk')
def addDisk(disk,uid):
    print(disk)
    disk_dao = DiskModel(d_total=disk.get('disk_total'), d_used=disk.get('disk_used'),
                       d_utilization=disk.get('disk_utilization'), u_id=uid,d_free=disk.get('disk_free'))
    db.session.add(disk_dao)
    db.session.commit()


