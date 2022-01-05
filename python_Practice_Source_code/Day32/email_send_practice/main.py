# ---------------------------- Demo1：SMTP示例 ------------------------------- #
# 本例中新申请了一个 gmail 测试用账户
# 账号：jackma22336677@gmail.com
# 密码：4$dbxxr#i!HtN3G9
# 但是本例还是不能正常运行，执行发送邮件的命令。代码应该没有问题，可能是因为 google 账号安全机制，没有细深究。
# 更新，指定587端口号之后便正常工作了，非常棒！

# import smtplib
#
# my_email = "jackma22336677@gmail.com"
# password = "4$dbxxr#i!HtN3G9"
# to_email = "jackma22336677@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=to_email,
#                         msg="Subject:Hello There!\n\nThis is the body of my Email."
#                         )
# print("Email send!")

# ---------------------------- Demo2：Datetime示例 ------------------------------- #
# import datetime as dt
#
# now = dt.datetime.now()
# print(now, type(now))  # now 是个 datetime 格式的对象
# year = now.year
# print(year)
# day_of_week = now.weekday()
# print(day_of_week)  # 注：周一为0，周二为1
#
# date_of_birth = dt.datetime(year= 1995, month=6, day=23)  # 创建一个 datetime 对象
# print(date_of_birth)

# ---------------------------- Demo3：周一励志邮件 Demo ------------------------------- #
# 本例还是不能正常运行，执行发送邮件的命令。代码应该没有问题，可能是因为 google 账号安全机制，没有细深究。
# import smtplib
# import datetime as dt
# import random
#
# MY_EMAIL = "jackma22336677@gmail.com"
# MY_PASSWORD = "4$dbxxr#i!HtN3G9"
# TO_EMAIL = "dongweisp@gmail.com"
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 2:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             to_addrs=TO_EMAIL,
#                             msg=f"Subject:Monday Motivation\n\n{quote}"
#                             )

# ---------------------------- Demo4：从网上找到的例子 ------------------------------- #
# 这是一段从网上找到的代码，可以正常运行。
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# mail_content = '''Hello,
# This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
# Thank You
# '''
#
# sender_address = 'jackma22336677@gmail.com'
# sender_pass = '4$dbxxr#i!HtN3G9'
# receiver_address = 'jackma22336677@gmail.com'
# #Setup the MIME
# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
# #The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'plain'))
# #Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
# session.starttls() #enable security
# session.login(sender_address, sender_pass) #login with mail_id and password
# text = message.as_string()
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('Mail Sent')