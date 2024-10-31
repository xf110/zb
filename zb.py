import requests
from bs4 import BeautifulSoup
import re

def extract_ip_ports():
    url = 'http://www.foodieguide.com/iptvsearch/hoteliptv.php'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'REFERER=30273563; ckip1=116.117.106.155|116.117.106.144|59.42.60.249|60.255.47.174|58.20.77.74|222.218.158.86|27.185.1.27|175.0.35.92; ckip2=119.41.37.132|46.180.108.130|178.163.61.132|222.80.12.231|115.239.104.249|123.101.98.200|178.163.37.84|202.103.213.75; REFERER2=Game; REFERER1=Over',
        'Origin': 'http://www.foodieguide.com',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.foodieguide.com/iptvsearch/hoteliptv.php',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36'
    }

    data = {
        'saerch': '广东电信',
        'Submit': '+',
        'city': 'HeZhou',
        'address': 'Ca94122'
    }

    response = requests.post(url, headers=headers, data=data, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    ip_ports = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+)', soup.text)

    return ip_ports

if __name__ == '__main__':
    ip_ports = extract_ip_ports()
    with open('ip_ports.txt', 'w') as f:
        for ip_port in ip_ports:
            f.write(f"{ip_port}\n")
