from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client

def jr():
    global web
    web = Chrome()
    web.get('http://192-168-100-208.webvpn.shxj.edu.cn:8118/ams/front/login.do')
    #因为此网站证书不安全需要进行继续前往和进行登录上海行健vpn才可以进入
    web.find_element(By.XPATH,'//*[@id="details-button"]').click()
    web.find_element(By.XPATH,'//*[@id="proceed-link"]').click()
    time.sleep(2)
    web.find_element(By.XPATH,'//*[@id="Calc"]/div[1]/div[1]/div/div[1]/input').send_keys('20204040019')
    web.find_element(By.XPATH,'//*[@id="loginPwd"]').send_keys('101790')
    web.find_element(By.XPATH,'//*[@id="Calc"]/div[3]/span/div[1]').click()
    web.find_element(By.XPATH,'//*[@id="Calc"]/div[4]/button').click()
    #测试资产管理系统
    # 测试用例
    time.sleep(2)
    test=[['qweq','eqweq','wqeqwe'],['25','20204040019','20204040019'],['25','20204040019','123456']]
    for item in test:
        #使用超级鹰来识别验证码
        img = web.find_element(By.XPATH,'//*[@id="vericode_img"]').screenshot_as_png
        chaojiying = Chaojiying_Client('2205952729', 'wsx520580', '933478')
        dic = chaojiying.PostPic(img,1004)
        yzm = dic['pic_str']
        web.find_element(By.XPATH,'//*[@id="taskId"]').send_keys(item[0])
        web.find_element(By.XPATH,'//*[@id="loginName"]').send_keys(item[1])
        web.find_element(By.XPATH,'//*[@id="password"]').send_keys(item[2])
        web.find_element(By.XPATH,'//*[@id="vericode"]').send_keys(yzm)
        web.find_element(By.XPATH,'//*[@id="fmedit"]/div[7]/button').click()
        try:
            err = web.find_element(By.XPATH,'//*[@id="error_msg"]').text
        except:
            web.back()#如果没有报错成功进入则返回登录界面
            err = "成功"
        print('任务ID:{} 用户名:{} 密码:{} err:{}'.format(item[0],item[1],item[2],err))
        time.sleep(3)
        web.refresh()#刷新页面

if __name__ == '__main__':
    jr()


