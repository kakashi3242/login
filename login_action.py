#coding=utf8

import urllib.request
import urllib.parse
import http.cookiejar
import time
import json
import login_log


def login(usr, psw):
    startTime = time.time()
    # login_log.logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    # login_log.logger.info(usr + ' start login at ' + str(startTime))
    # logging.warning(loginName + ' start login.')
    # print(loginName + ' start login.')
    # print('Login start at ' + str(startTime))
    # login_log.logger.info('Login start at ' + str(startTime))
    cj = http.cookiejar.CookieJar()
    url_login = "http://test.pluspre.1course.cn/UserService/Login"
    form_login = {"loginName":usr, "password":psw, "school": "hz"}
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36 QQBrowser/4.1.4132.400')]
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url_login,urllib.parse.urlencode(form_login).encode(encoding='UTF8'))
    # req.add_header("Referer","http://xxoo.com")
    resp = urllib.request.urlopen(req)
    msg = resp.read().decode('utf8')
    # print(msg)
    message = json.loads(msg)

    # print(message['status'])
    # print(type(message['status']))

    if message['status'] == 1:
        endTime = time.time()
        spendTime = endTime - startTime
        # login_log.logger.info(usr + ' login done.')
        # login_log.logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        login_log.logger.info(usr + ' login spends ' + str(spendTime) + ' seconds.')
        # login_log.logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print('Done')
        # print('Login done at ' + str(endTime))
        # print('It spends ' + str(spendTime) + ' second.')
    else:
        endT = time.time()
        spendT = endT - startTime
        login_log.logger.error('Reason: ' + message['message'])
        login_log.logger.warning(usr + ' Login false at ' + str(endT))
        login_log.logger.info('It spends ' + str(spendT) + ' seconds.' + '\n')
        # login_log.logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(time.ctime() + ' Login false.')
        # print('Reason: ' + message['message'])

    # for cookie in cj:
    #     print(cookie.name,':',cookie.value)

# usr = 'a1'
# psw = '123456'
#
# login(usr,psw)

