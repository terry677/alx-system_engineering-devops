from fabric.api import *

env.use_ssh_config = True

def connect():
    env.hosts = ['web1', 'web2']

def copy():
    put('signature.key')

def copy1():
    put('user.sql')

def create_user():
    run("cat user.sql | sudo mysql")
