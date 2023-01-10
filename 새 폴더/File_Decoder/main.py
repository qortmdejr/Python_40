import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len+1):
        to_attempt = itertools.product(passwd_string, repeat=len); # itertools.product 두개 이상의 집합 끼리의 데카르트 곱을 계산하여 iterator 형태로 반환
        for attempt in to_attempt:                                 # A = [1,2,3] list(itertools.product(A, repeat=2))
            passwd = ''.join(attempt);                             # >>>> [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
            print(' '.join(passwd));
            try:
                zFile.extractall(pwd=passwd.encode());   # extractall(압축해제할 경로)로 이용되며, 해당 압축파일을 해당 경로에 모두 압축해제를 시켜준다.
                print(f"비밀번호는 {passwd} 입니다.");       # 당연히 경로를 지정하지 않으면, 현재 작업디렉토리에 바로 압축이 해제된다.
                return 1;                               # encode() 문자열을 인코딩
            except:
                pass

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

zFile = zipfile.ZipFile(r'/Users/seungdeok/Desktop/python_40/File_Decoder/test1234.zip');

min_len = 1;
max_len = 4;

unzip_result = un_zip(passwd_string, min_len, max_len, zFile);

if unzip_result == 1:
    print("암호찾기 성공");
else:
    print("암호찾기 실패");
