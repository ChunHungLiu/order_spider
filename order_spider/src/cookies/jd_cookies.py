# coding: GB18030
from common import chrome_cookie
from conf import project_paths


def get_cookiejar():
    """��ȡ������cookie jar
    """
    ckjar = chrome_cookie.read_chrome_cookie(project_paths.JD_COOKIE_FILE)
    return ckjar