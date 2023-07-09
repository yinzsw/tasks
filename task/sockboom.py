import requests
from task.runner import Runner


class SockBoom(Runner):
    BASE_URL = "https://sockboom.com"

    def __init__(self, email, passwd):
        self.email = email
        self.passwd = passwd
        self.common_headers = {
            "Origin": SockBoom.BASE_URL,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/114.0.0.0 Safari/537.36 "
        }
        self.session = requests.session()

    def login(self):
        login_url = f"{self.BASE_URL}/auth/login"
        headers = {"Referer": f"{self.BASE_URL}/auth/login", **self.common_headers}
        data = {"email": self.email, "passwd": self.passwd, "code": ""}

        self.session.post(login_url, headers=headers, data=data, timeout=5)

    def logout(self):
        checkin_url = f"{self.BASE_URL}/user/logout"
        headers = {"Referer": f"{self.BASE_URL}/user", **self.common_headers}
        self.session.get(checkin_url, headers=headers, timeout=5)

    def checkin(self):
        checkin_url = f"{self.BASE_URL}/user/checkin"
        headers = {"Referer": f"{self.BASE_URL}/user", **self.common_headers}

        login_response = self.session.post(checkin_url, headers=headers, timeout=5)
        login_response_body = login_response.json()
        return login_response_body['msg']

    def start(self):
        try:
            self.login()
            msg = self.checkin()
            self.logout()
            return f"签到: {msg}"
        except:
            return "签到失败"
