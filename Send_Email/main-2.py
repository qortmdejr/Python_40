import  smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


send_email = "tmdejrtodn@naver.com"
send_pwd = "qortmdejr123"

recv_mail = "wndeldtmdejr@naver.com"

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart();

msg['Subject'] = "첨부파일 테스트"
msg['From'] = send_email;
msg['To'] = recv_mail;

text = """
첨부파일 테스트
"""

contentPart = MIMEText(text);
msg.attach(contentPart);

etc_file_path = '첨부파일.txt'

with open(etc_file_path, 'rb') as f:
    etc_part = MIMEApplication(f.read());
    etc_part.add_header('Content-Disposition', 'attachment', filename = '첨부파일.txt');
    msg.attach(etc_part);

s = smtplib.SMTP(smtp_name, smtp_port);
s.starttls();
s.login(send_email, send_pwd);
s.sendmail(send_email, recv_mail, msg.as_string());
s.quit();

