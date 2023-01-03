import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len+1):
        to_attempt = itertools.product(passwd_string, repeat=len);
        for attempt in to_attempt:
            passwd = ''.join(attempt);
            print(' '.join(passwd));
            try:
                zFile.extractall(pwd=passwd.encode());
                print(f"비밀번호는 {passwd} 입니다.");
                return 1;
            except:
                pass

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

zFile = zipfile.ZipFile(r'/Users/seungdeok/Desktop/python_40/File_Decoder/test1234.zip');

min_len = 1;
max_len = 4;

unzip_result = un_zip(passwd_string, min_len, max_len, zFile);

if unzip_result ==1:
    print("암호찾기 성공");
else:
    print("암호찾기 실패");
