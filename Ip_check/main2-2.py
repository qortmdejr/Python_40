import socket

hostName = socket.gethostname(); # gethostname 은 로컬호스트의 이름을 리턴
in_addr1 = socket.gethostbyname(hostName); # ethostbyname 은 컴퓨터의 이름이나 도메인이름을 사용하여 ip주소를 리턴

print(in_addr1);

in_addr2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
in_addr2.connect(("www.google.co.kr", 443));
print(in_addr2.getsockname()[0]);
