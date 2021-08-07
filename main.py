import smtplib

my_mail = ""
password = ""

# connection = smtplib.SMTP("smtp.gmail.com")
# # secures the connection
# connection.starttls()
# connection.login(user=my_mail, password=password)
# connection.sendmail(
#     from_addr=my_mail,
#     to_addrs="",
#     msg="Subject:Hello\n\nThis is the body of my email."
# )
# connection.close()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs="",
        msg="Subject:Hello\n\nThis is the body of my email."
    )



