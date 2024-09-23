from flask import Blueprint

bp = Blueprint("Gpu",__name__,url_prefix='/gpu')

@bp.route('/getGpu')
def getGpu():
    pass