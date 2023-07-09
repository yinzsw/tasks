from typing import List
from email.message import EmailMessage
from smtplib import SMTP_SSL
from jinja2 import Environment, FileSystemLoader
from util.env import SmtpConf


class TaskTpl:
    def __init__(self, topic, msg):
        self.topic = topic
        self.msg = msg


class EmailTpl:
    def __init__(self, tasks: List[TaskTpl], is_extra_notice=False):
        self.tasks = [vars(task) for task in tasks]
        self.is_extra_notice = is_extra_notice

    def get_params(self):
        return vars(self)


class EmailSender:
    def __init__(self, conf: SmtpConf):
        self.conf = conf

    def send(self, contents: EmailTpl, receivers: list):
        html_content = Environment(loader=FileSystemLoader('.')) \
            .get_template('./templates/scheduled-tasks.html') \
            .render(contents.get_params())

        msg = EmailMessage()
        msg['Subject'] = '定时任务执行结果通知'
        msg['From'] = self.conf.username
        msg['To'] = ",".join(receivers)
        msg.set_content(html_content, subtype='html')

        with SMTP_SSL(host=self.conf.host, port=self.conf.port, timeout=5) as smtp:
            smtp.login(self.conf.username, self.conf.password)
            smtp.send_message(msg)
