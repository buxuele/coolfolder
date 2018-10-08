import zmail


mail_content = {
    'subject': 'ok***test',
    'content': 'love zmail ,for human beings!',
    'attachments': 'D:/Pictures/unfinished/a.jpg',
}

mail = zmail.encode_mail(mail_content)

server = zmail.server('bao****le@163.com', '*****')

server.send_mail('296*****9@qq.com', mail)
# server.send_mail(['2***59@qq.com',        'someoneelse@qq.com'], mail)


