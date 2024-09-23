from flask import Blueprint
from models import UserModel
from exts import db
bp = Blueprint("user",__name__,url_prefix='/user')


@bp.route('/addUser')
def addUser(uid,name):
    users = UserModel.query.all()
    count = UserModel.query.count()
    num = 0
    for user in users:
        if user.u_id == uid:
            break
        else:
            num = num + 1
    if num == count:
        user_dao = UserModel(u_id=uid, u_name=name)
        db.session.add(user_dao)
        db.session.commit()
