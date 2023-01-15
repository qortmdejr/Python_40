import smtplib
from email.mime.text import MIMEText

send_email = "tmdejrtodn@naver.com"
send_pwd = "qortmdejr123"

recv_email = "wndeldtmdejr@naver.com"

smtp_name = "smtp.naver.com"
smtp_port = 587;


text = """
파이썬 메일 보내기
"""

msg = MIMEText(text);

msg['Subject'] = "파이썬 메일"
msg['From'] = send_email;
msg['To'] = recv_email;
print(msg.as_string());


s = smtplib.SMTP( smtp_name , smtp_port);
s.starttls();
s.login(send_email , send_pwd);
s.sendmail(send_email, recv_email, msg.as_string());
s.quit();



