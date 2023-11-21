
def mail():
        # smtplib 用于邮件的发信动作
    import smtplib
    # email 用于构建邮件内容
    from email.mime.text import MIMEText


    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '3562230984@qq.com'
    password = 'kvzgvkntrfiqdafg'
    

    # 收信方邮箱
    to_addr = '981011972@qq.com'

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText('my first email send by python','plain','utf-8')


    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server,465)

    server.login(from_addr, password)

    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()

