import win32gui
import win32con
import win32clipboard as w
import time
import datetime
import random
i=0
name=['丁欣怡!! ','丁丁妞妞!!!','丁宝/qq/qq','徐子!','徐徐']
word=['最漂亮!!/qq/qq','2022财源滚滚！/cp/cp','今天也加油加油呀！/cy/cy','虎年虎虎生威！/hb/hb','全世界最棒！/cy/cy']
# word =['最漂亮/qq/qq','/dk徐子想丁丁妞妞啦！/dk','丁欣怡全世界最棒！/cy/cy','虎年虎虎生威我的漂亮宝！！/hb/hb'
# ,'/bp2022新年快乐妞妞/bp','恭喜发财！/cp/cp财源滚滚','相信丁欣怡/fendou']
def send_qq(to_who,msg):  #粘贴剪切板内容并回车
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    #打开剪贴板
    w.OpenClipboard()
    #清空剪贴板
    w.EmptyClipboard()
    #设置剪贴板内容
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    #获取剪贴板内容
    date = w.GetClipboardData()
    #关闭剪贴板
    w.CloseClipboard()
    # 将消息写到剪贴板
    qq = win32gui.FindWindow('TXGuiFoundation', to_who)  # 获取qq窗口句柄
    if qq == 0:
        print('未找到窗口！')
      #显示窗口
    win32gui.ShowWindow(qq,win32con.SW_SHOW)
    #把剪切板内容粘贴到qq窗口
    win32gui.SendMessage(qq, win32con.WM_PASTE, 0, 0)
    # 模拟按下回车键  https://docs.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-sendmessage
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0) #WM_KEYDOWN 按下一个键
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0) #WM_KEYUP释放一个键

while(1):
    if(datetime.datetime.now().hour==17 and datetime.datetime.now().minute==30 and datetime.datetime.now().second==0):
        i=0
        while(i<10):#条
            if(i==0):
                time.sleep(3)
                send_qq('小怡宝贝','今天是'+time.strftime("%Y年%m月%d日", time.localtime())+'很高兴为丁丁和徐徐服务/cy/cy/cy')
                send_qq('小怡宝贝','为您下午5点'+str(datetime.datetime.now().minute)+'分播报祝福!')
                #send_qq('小怡宝贝',"徐徐复读机很高兴为丁丁服务/cy/cy/cy")
            else:
                com=[random.choice(word)+random.choice(name),random.choice(name)+random.choice(word)]
                send_qq('小怡宝贝',random.choice(com))
                #send_qq('AZ、',random.choice(word))
            time.sleep(1)
            i=i+1

    # else: 
    #     print(datetime.datetime.now().second)
    #     time.sleep(1)