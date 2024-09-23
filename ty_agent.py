import psutil
import platform
import gpustat
import requests
import os
import getpass
import win32security
import ntsecuritycon as con
import win32api
import sys
import time

def send_data_to_server(data):
    url = 'http://10.190.79.213:8000/data'
    headers = {
    'Content-Type': 'application/json'
}
    response = requests.post(url, json=data,headers=headers)
    print(response)
def get_current_user_sid():
    # 打开当前进程的访问令牌
    token = win32security.OpenProcessToken(win32api.GetCurrentProcess(), con.TOKEN_READ)
    # 获取令牌中的用户信息
    user_info = win32security.GetTokenInformation(token, con.TokenUser)
    # SID存储在用户信息的第一个元素中
    user_sid = user_info[0]
    # 将SID转换为字符串形式以便打印
    sid_string = win32security.ConvertSidToStringSid(user_sid)
    # 释放令牌句柄
    win32api.CloseHandle(token)
    return sid_string
def get_system_info():
    if sys.platform == "linux":
        #Linux环境下获取用户名和SID
        username = os.getlogin()
        #获取当前用户的UID
        uid = os.getuid()
    else:
        # Windows环境下获取用户名和SID
        # 获取当前用户的UID
        uid = get_current_user_sid()
        # 获取当前用户名
        username = getpass.getuser()
    print(username)
    print(uid)

    # 获取操作系统信息
    os_info = f"操作系统: {platform.system()}, {platform.release()}, {platform.version()}"
    print(os_info)
    # 获取CPU信息
    cpu_count = psutil.cpu_count(logical=False)  # 物理核心数
    cpu_freq = psutil.cpu_freq().max  # CPU最大频率
    cpu_utilization = psutil.cpu_percent(interval=0.1) #CPU利用率
    cpu_info = f"CPU核心数: {cpu_count}, 最大频率: {cpu_freq} MHz，cpu利用率：{cpu_utilization}%"
    print(f'CPU信息')
    print(cpu_info)

    # 获取硬盘信息
    disk_usage = psutil.disk_usage('/')  # 假设我们关心根目录的磁盘使用情况
    disk_total = disk_usage.total / (1024 ** 3)
    disk_used = disk_usage.used / (1024 ** 3)
    disk_free = disk_usage.free/ (1024 ** 3)
    disk_utilization = disk_usage.percent
    disk_info = f"根目录磁盘: 总大小 {disk_total:.2f} GB, 使用中: {disk_used:.2f} GB ({disk_utilization}%)"
    print(f'硬盘信息')
    print(disk_info)

    #获取内存信息
    memory = psutil.virtual_memory()
    memory_total = memory.total / (1024 ** 3)
    memory_available = memory.available / (1024 ** 3)
    memory_utilization = memory.percent
    memory_used = memory.used / (1024 ** 3)
    memory_free = memory.free / (1024 ** 3)
    print(f"内存信息：")
    print(f"总内存: {memory_total:.2f} GB")
    print(f"可用内存: {memory_available:.2f} GB")
    print(f"使用率: {memory_utilization}%")
    print(f"已用内存: {memory_used:.2f} GB")
    print(f"空闲内存: {memory_free:.2f} GB")

    # 创建一个GPUStatCollection对象，用于查询GPU信息
   # gpu_stats = gpustat.GPUStatCollection.new_query()


    # 遍历所有的GPU
    # for gpu in gpu_stats:
    #     # 获取GPU的索引
    #     index = gpu.index
    #     # 获取GPU的名称
    #     name = gpu.name
    #     # 获取GPU的利用率
    #     utilization = gpu.utilization
    #     # 获取GPU已使用的内存
    #     memory_used = gpu.memory_used
    #     # 获取GPU的总内存
    #     memory_total = gpu.memory_total
    #     # 计算内存利用率（注意：这里假设memory_total和memory_used的单位相同）
    #     memory_util = memory_used / memory_total * 100 if memory_total > 0 else 0
    #     print(f"GPU信息：")
    #     print(f"GPU {index}:")
    #     print(f"  GPU型号: {name}")
    #     print(f"  利用率: {utilization}%")
    #     print(f"  已用内存: {memory_used} / {memory_total} GB")
    #     print(f"  内存利用率: {memory_util:.2f}%")

    data = {
        'os': {'os_name': platform.system()},
        'cpu': {'cpu_count': cpu_count, 'cpu_freq': cpu_freq, 'cpu_utilization': cpu_utilization},
        'disk': {'disk_used': disk_used, 'disk_total': disk_total, 'disk_utilization': disk_utilization,'disk_free': disk_free},
        'memory': {'memory_total': memory_total, 'memory_available': memory_available, 'memory_utilization': memory_utilization,
                   'memory_used': memory_used,'memory_free': memory_free},
        'user': {'name': username,'uid': uid}
    }

    send_data_to_server(data)

def my_method():
    print("方法被执行了，当前时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
    # 在这里添加你的方法逻辑

if __name__ == '__main__':
    #while True:  # 无限循环
        get_system_info()  # 调用方法
        #time.sleep(5)  # 暂停5秒


