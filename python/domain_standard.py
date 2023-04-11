"""
在url链接中提取出域名信息
"""
from tld import get_tld

domain = "www.test.com"
result = get_tld(domain, as_object=True, fix_protocol=True)
domain = result.fld # .fld全域名 .subdomain域名前缀 .tld域名内容 .domain域名后缀
print(domain)