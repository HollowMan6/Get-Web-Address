# 获取 Web VPN 地址

[![last-commit](https://img.shields.io/github/last-commit/HollowMan6/Get-Web-VPN-Address)](../../graphs/commit-activity)
![Python package](https://github.com/HollowMan6/Get-Web-VPN-Address/workflows/Python%20package/badge.svg)

[![Followers](https://img.shields.io/github/followers/HollowMan6?style=social)](https://github.com/HollowMan6?tab=followers)
[![watchers](https://img.shields.io/github/watchers/HollowMan6/Get-Web-VPN-Address?style=social)](../../watchers)
[![stars](https://img.shields.io/github/stars/HollowMan6/Get-Web-VPN-Address?style=social)](../../stargazers)
[![forks](https://img.shields.io/github/forks/HollowMan6/Get-Web-VPN-Address?style=social)](../../network/members)

[![Open Source Love](https://img.shields.io/badge/-%E2%9D%A4%20Open%20Source-Green?style=flat-square&logo=Github&logoColor=white&link=https://hollowman6.github.io/fund.html)](https://hollowman6.github.io/fund.html)
[![GPL Licence](https://img.shields.io/badge/license-GPL-blue)](https://opensource.org/licenses/GPL-3.0/)
[![Repo-Size](https://img.shields.io/github/repo-size/HollowMan6/Get-Web-VPN-Address.svg)](../../archive/master.zip)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/HollowMan6/Get-Web-VPN-Address.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/Get-Web-VPN-Address/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/HollowMan6/Get-Web-VPN-Address.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/HollowMan6/Get-Web-VPN-Address/context:python)

(English version is down below)

[Python库依赖](../../network/dependencies)

Python生成URL对应的Web VPN地址。

适用于`北京网瑞达科技有限公司`的Web VPN地址的获取。在[兰州大学Web VPN](https://vpnx.lzu.edu.cn/)界面通过了测试。

可以通过本程序来方便地使用校园网代理，进行爬虫。

爬虫使用示例：

该程序通过Web VPN爬取base_url中的内容。使用时需要事先登录你的Web VPN页面并获取到登陆界面的cookies中`remember_token`项的值填入下面程序中。

```python
import Get_Web_VPN_Address
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

base_url = "https://www.baidu.com"
vpn_host = "https://vpnx.lzu.edu.cn"
remember_token = ""
cookie = {"remember_token": remember_token}
vpn_url = vpn_host + Get_Web_VPN_Address.encrypUrl("https", base_url)
response = requests.get(url=vpn_url, cookies=cookie,verify=False)
print(response.text)

```

## 链接

* [Get Web VPN Address 脚本](Get_Web_VPN_Address.py)

# Get Web VPN Address

[Python library dependency](../../network/dependencies)

Generate Web VPN address of the specified URL in python.

Suitable for `北京网瑞达科技有限公司` Web VPN. Tested on [Lanzhou University Web VPN](https://vpnx.lzu.edu.cn/).

This program can be used to crawl through campus network VPN.

Web Crawler example:

Crawl `base_url` through web VPN. Before using, you need to log in to your web VPN page and get the cookies record `remember_token` in the login page and then fill the variable below.

```python
import Get_Web_VPN_Address
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

base_url = "https://www.baidu.com"
vpn_host = "https://vpnx.lzu.edu.cn"
remember_token = ""
cookie = {"remember_token": remember_token}
vpn_url = vpn_host + Get_Web_VPN_Address.encrypUrl("https", base_url)
response = requests.get(url=vpn_url, cookies=cookie,verify=False)
print(response.text)

```

## Links

* [Get Web VPN Address Script](Get_Web_VPN_Address.py)
