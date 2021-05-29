#自定义fabfile文件如下
#/root/fab.py
from fabric.api import *
"""
Fabric是一个Python的库，它提供了丰富的同SSH交互的接口，可以用来在本地或远程机器上自动化、流水化地执行Shell命令。因此它非常适合用来做应用的远程部署及系统维护。"""
#local_node和remote_node都可以为多个
local_node = ['127.0.0.1']
remote_node = ['10.116.97.30']
#定义local和remote角色
env.roledefs['local'] = local_node
env.roledefs['remote'] = remote_node
#定义用户名
env.user = 'root'
#定义密码
env.password = 'xxx'

#不同的角色执行不同的命令
@roles('local')
def test_local():
    #run命令在roles为local的主机上执行命令"hostname"
    run("hostname")

@roles('remote')
def test_remote():
    run("hostname")
