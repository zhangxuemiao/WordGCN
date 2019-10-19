import os
import socket


class _SettingManager(object):
    def __init__(self):
        self.PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))  # __file__是相对路径

        hostname = socket.gethostname()
        print('Program running on machine:', hostname)
        self.hostname = hostname

        if hostname == 'medical':  # on medical gpu server
            self.base_data_dir = '/home/xuemiao/dataset/data'
        elif hostname == 'g105e1901560':  # on sense local machine
            self.base_data_dir = '/home/SENSETIME/zhangxuemiao/dataset/data'
        elif hostname == 'Lab.lan' or hostname == 'Lab.local':  # on mac develop machine
            self.base_data_dir = '/Users/lab/dataset/data'
        else:
            raise ValueError('Unknown machine!')


# 全局唯一配置管理访问器
settings = _SettingManager()
