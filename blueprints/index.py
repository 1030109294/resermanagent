from flask import Blueprint,Flask,request,jsonify
import blueprints.user as userDb
import blueprints.cpu as cpuDb
import blueprints.disk as diskDb
import blueprints.memory as memoryDb

bp = Blueprint("index",__name__,url_prefix='/')

@bp.route('/')
def index():
    return 'index.html'


@bp.route('/data', methods=['POST'])
def receive_data():
    # 假设我们接收JSON格式的数据
    data_list = request.get_json()
    cpu = data_list.get('cpu')
    disk = data_list.get('disk')
    user = data_list.get('user')
    memory = data_list.get('memory')
    uid = user.get('uid')
    name = user.get('name')

    #添加用户信息
    userDb.addUser(uid, name)

    #添加cpu信息
    cpuById = cpuDb.getCpuByUid(uid)
    if cpuById == None:
        cpuDb.addCpu(cpu,uid)

    # 添加disk信息
    diskById = diskDb.getDiskByUid(uid)
    if diskById == None:
        diskDb.addDisk(disk, uid)

    # 添加memory信息
    memoryById = memoryDb.getMemoryByUid(uid)
    if memoryById == None:
        memoryDb.addmemory(memory, uid)

    # 这里可以根据需要对数据进行处理
    return jsonify({"status": "success", "message": "Data received successfully"}), 200


