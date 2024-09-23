from datetime import datetime

from exts import db

class CpuModel(db.Model):
    __tablename__ = 'cpu'
    cpu_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    cpu_count = db.Column(db.Integer, nullable=True)
    cpu_freq = db.Column(db.Float, nullable=True)
    cpu_utilization = db.Column(db.Float, nullable=True)
    join_time = db.Column(db.DateTime,default=datetime.now)
    u_id = db.Column(db.String(128), db.ForeignKey('user.u_id'))
class DiskModel(db.Model):
    __tablename__ = 'disk'
    d_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    d_total = db.Column(db.Float, nullable=True)
    d_used = db.Column(db.Float, nullable=True)
    d_free = db.Column(db.Float, nullable=True)
    d_utilization = db.Column(db.Float, nullable=True)
    join_time = db.Column(db.DateTime,default=datetime.now)
    u_id = db.Column(db.String(128), db.ForeignKey('user.u_id'))
class GpuModel(db.Model):
    __tablename__ = 'gpu'
    g_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    g_name = db.Column(db.String(128), nullable=True)
    g_memory_total = db.Column(db.Float, nullable=True)
    g_memory_used = db.Column(db.Float, nullable=True)
    g_memory_free = db.Column(db.Float, nullable=True)
    g_utilization = db.Column(db.Float, nullable=True)
    g_count = db.Column(db.Integer, nullable=True)
    join_time = db.Column(db.DateTime,default=datetime.now)
    u_id = db.Column(db.String(128), db.ForeignKey('user.u_id'))
class MemoryModel(db.Model):
    __tablename__ = 'memory'
    m_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    m_total = db.Column(db.Float, nullable=True)
    m_used = db.Column(db.Float, nullable=True)
    m_free = db.Column(db.Float, nullable=True)
    m_utilization = db.Column(db.Float, nullable=True)
    join_time = db.Column(db.DateTime,default=datetime.now)
    u_id = db.Column(db.String(128), db.ForeignKey('user.u_id'))

class UserModel(db.Model):
    __tablename__ = 'user'
    u_id = db.Column(db.String(128), primary_key=True)
    u_name = db.Column(db.String(128), nullable=True)
    join_time = db.Column(db.DateTime,default=datetime.now)

    def get(cls, u_id):
        return cls.query.get(u_id)