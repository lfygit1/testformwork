"""
# file:     Base/utils.py
# 读取-配置文件.ini
# 打包zip文件
"""

import sys
import argparse
from pathlib import Path
# 获取当前文件的父目录的父目录（项目根目录）
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
# print(sys.path)

from configparser import RawConfigParser
from Base.basePath import BasePath



def read_config_ini(config_path):
    """ 读取-配置文件.ini """
    config = RawConfigParser()    # 创建RawConfigParser对象
    config.read(config_path, encoding='utf-8')
    return config

def write_config_ini(config_path, section, option, value):
    """ 写入-配置文件.ini """
    config = RawConfigParser()    
    config.read(config_path, encoding='utf-8')
    config.set(section, option, value)
    with open(config_path, 'w', encoding='utf-8') as f:
        config.write(f)


def main():
    config = read_config_ini(BasePath.CONFIG_FILE)
    print(config['客户端自动化配置']['confidence'])

if __name__ == '__main__':
    main()