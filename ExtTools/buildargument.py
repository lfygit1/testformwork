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

def write_config_ini(config_path, *args, **kwargs):
    """ 写入-配置文件.ini """
    config = RawConfigParser()    
    config.read(config_path, encoding='utf-8')
    
    for key, value in kwargs.items():
        print("qqqqqqqqqqqqqqqq", key, value)


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
    parser.add_argument('-srnginx', '--send_report_nginx', type=str)
    
    args = parser.parse_args()

    config_args = {    
        'NGINX_HOST': args.nginx_host,
        'NGINX_PORT': args.nginx_port,
        'NGINX_USER': args.nginx_user,
        'NGINX_ALLURE_PATH': args.nginx_allure_path,
        'AUTO_TYPE': args.auto_type,
        'REPORT_TYPE': args.report_type,
        'DATA_DRIVER_TYPE': args.data_driver_type,
        'TEST_PROJECT': args.test_project,
        'TEST_URL': args.test_url,
        'SEND_REPORT_NGINX': args.send_report_nginx
    }
    print(config_args)

    write_config_ini(config_path=BasePath.CONFIG_FILE, **config_args)
    

if __name__ == '__main__':
    main()