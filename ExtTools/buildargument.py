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
    parser = argparse.ArgumentParser(
        description='构建参数配置工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
                    示例:
                    python buildargument.py --env test
                    python buildargument.py --config ./config.ini --env prod
                '''
    )
    
    parser.add_argument('-nghost', '--nginx_host', type=str, help='nginx的IP地址')
    parser.add_argument('-ngport', '--nginx_port', type=str)
    parser.add_argument('-nguser', '--nginx_user', type=str)
    parser.add_argument('-ngpath', '--nginx_allure_path', type=str)
    parser.add_argument('-auto', '--auto_type', type=str)
    parser.add_argument('-report', '--report_type', type=str)
    parser.add_argument('-ddtype', '--data_driver_type', type=str)
    parser.add_argument('-project', '--test_project', type=str)
    parser.add_argument('-url', '--test_url', type=str)
    
    args = parser.parse_args()
    
    print(
    f"nginx_host: {args.nginx_host}\n"
    f"nginx_port: {args.nginx_port}\n"
    f"nginx_user: {args.nginx_user}\n"
    f"nginx_allure_path: {args.nginx_allure_path}\n"
    f"auto_type: {args.auto_type}\n"
    f"report_type: {args.report_type}\n"
    f"data_driver_type: {args.data_driver_type}\n"
    f"test_project: {args.test_project}\n"
    f"test_url: {args.test_url}"
)
    

if __name__ == '__main__':
    main()