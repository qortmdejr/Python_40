import requests
import re

url ="https://www.hani.co.kr/arti/society/society_general/1075274.html";

headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
}

response = requests.get(url, headers = headers);

results = re.findall(r'[\w\.-]+@[\w\.-]+', response.text);

results = list(set(results));

print(results);


