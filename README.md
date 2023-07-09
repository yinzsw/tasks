# TASKS

### 支持任务

- [x] SockBoom
  > [SockBoom](https://www.sockboom.com) 每日签到领取流量
- [x] HuaMi
  > 小米运动步数修改(微信, 支付宝, QQ)

### 配置文件(Github Actions secrets)

##### SMTP邮箱配置

Name: SMTP | Secret: 见表格和例子

| 键        | 描述        |
|----------|-----------|
| host     | smtp host |
| port     | smtp port |
| username | 用户名       |
| password | 密码        |

```json
{
  "host": "smtp.qq.com",
  "port": 465,
  "username": "example@qq.com",
  "password": "example password"
}
```

##### 任务配置

Name: SMTP | Secret: 见表格和例子

| 键                      | 描述          |
|------------------------|-------------|
| notice                 | 需要发送通知的邮箱列表 |
| sock_boom              | SockBoom配置  |
| sock_boom.user         | 用户登录邮箱      |
| sock_boom.passwd       | 用户登录密码      |
| sock_boom.extra_notice | 需要额外通知的邮箱   |
| hua_mi                 | HuaMi配置     |
| hua_mi.user            | 用户登录邮箱或手机号  |
| hua_mi.passwd          | 用户登录密码      |
| hua_mi.step_range      | 步数范围        |

```json
[
  {
    "notice": [
      "notice@qq.com"
    ],
    "sock_boom": {
      "user": "user@qq.com",
      "passwd": "user passwd",
      "extra_notice": [
        "extra_notice@qq.com"
      ]
    },
    "hua_mi": {
      "user": "email or phone",
      "passwd": "user passwd",
      "step_range": [
        222222,
        666666
      ]
    }
  }
]
```