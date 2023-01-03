from currency_converter import CurrencyConverter

cc = CurrencyConverter(); # 객체 생성

print(cc.convert(1000,'EUR','USD')); # 환율 변경
print(cc.currencies); # 지원 통화 확인

# #ECB 은행의 최신 환율 정보 업데이트
cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc.convert(1, 'USD', 'KRW'));