import os
import json
from dotenv import load_dotenv


class SmtpConf:
    def __init__(self, conf: dict):
        self.host = conf.get('host')
        self.port = conf.get('port')
        self.username = conf.get('username')
        self.password = conf.get('password')


class SockBoomConf:
    def __init__(self, conf: dict):
        self.user = conf.get('user')
        self.passwd = conf.get('passwd')
        self.extra_notice: list[str] = conf.get('extra_notice')


class HuaMiConf:
    def __init__(self, conf: dict):
        self.user = conf.get('user')
        self.passwd = conf.get('passwd')
        self.step_range: list[int, int] = conf.get('step_range')


class TaskConf:
    def __init__(self, conf: dict):
        self.notice: list[str] = conf.get('notice')
        self.sock_boom = conf.get('sock_boom') and SockBoomConf(conf.get('sock_boom'))
        self.hua_mi = conf.get('hua_mi') and HuaMiConf(conf.get('hua_mi'))


class Environment:
    def __init__(self):
        load_dotenv()

        environ = os.environ
        smtp = environ.get("SMTP")
        tasks = environ.get("TASKS")

        self.smtp = SmtpConf(json.loads(smtp))
        self.tasks = [TaskConf(task) for task in json.loads(tasks or "[]")]