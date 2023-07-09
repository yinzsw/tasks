from task import *
from util import *


def main():
    environment = Environment()
    email_sender = EmailSender(environment.smtp)

    for task in environment.tasks:
        task_templates = []

        if task.sock_boom:
            msg = SockBoom(task.sock_boom.user, task.sock_boom.passwd).start()
            print(msg)
            task_templates.append(TaskTpl("SockBoom", msg))
            if task.sock_boom.extra_notice:
                email_sender.send(EmailTpl(task_templates, True), task.sock_boom.extra_notice)
        if task.hua_mi:
            msg = HuaMi(task.hua_mi.user, task.hua_mi.passwd, task.hua_mi.step_range).start()
            print(msg)
            task_templates.append(TaskTpl("HuaMi", msg))
        email_sender.send(EmailTpl(task_templates), task.notice)


if __name__ == '__main__':
    main()
