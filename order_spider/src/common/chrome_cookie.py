# coding: GB18030

"""
���ԣ�http://www.redicecn.com/html/Python/20141204/480.html
�Ȱ�װEditThisCookie�����360�����ò��Ҳ֧��������������Ҫ�ɼ�����վ����ɵ�¼�Ȳ��������EditThisCookieͼ�꣬
�������������ť�����Ҽ�ͷ������ǰҳ�棨��վ����Cookies�ͱ����Ƶ��������ˣ�JSON��ʽ�ģ�����ճ����cookies.txt�ļ�����á�
��������ش��룬��cookies.txt������ݼ��ص�Python��CookieJar�У�
"""

import json
import cookielib

def read_chrome_cookie(cookie_file):
    """��ȡʹ��EditThisCookie������chrome��cookie
    """
    cookie_jar = cookielib.MozillaCookieJar()
    cookies = open(cookie_file).read()
    for cookie in json.loads(cookies):
        cookie_jar.set_cookie(cookielib.Cookie(version=0, name=cookie['name'], value=cookie['value'], port=None, port_specified=False, domain=cookie['domain'], domain_specified=False, domain_initial_dot=False, path=cookie['path'], path_specified=True, secure=cookie['secure'], expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False))    
    # cookie_jar���Ѿ������˵�ǰҳ���Cookie�����ˣ�Enjoy!
    return cookie_jar
