#! python3
#coding:utf-8

import itchat
from itchat.content import *

user_name_list = []

@itchat.msg_register([PICTURE,RECORDING,TEXT,MAP,CARD,NOTE,SHARING,ATTACHMENT,VIDEO])
#注册接受消息类型;    图片    录音      文字 位置名片 通知 分享    文件       视频
def simple_reply(msg):
    global i
    if msg['Type'] == TEXT:
        if (user_name_list.count(msg['FromUserName'])==0):
            user_name_list.append(msg['FromUserName'])
            itchat.send_msg('你好，我是孟凡宇的助理，孟凡宇正在复习，如果本条信息很紧急请致电17640226057', toUserName=msg['FromUserName'])
        elif (user_name_list.count(msg['FromUserName'])>0 and user_name_list.count(msg['FromUserName'])<10):
            user_name_list.append(msg['FromUserName'])
            itchat.send_msg('又见面了' , toUserName=msg['FromUserName'])
        elif (user_name_list.count(msg['FromUserName'])>=10):
            pass
        # if msg['Text']  == '1':
        #     itchat.send_msg('aaaa',toUserName=msg['FromUserName'])
        # itchat.send_msg('说出来你可能不信，但这是一条自动回复',toUserName=msg['FromUserName'])
        # ReplyContent = 'i receive message:' + msg['Content']
    # elif msg['Type'] == PICTURE:
    #     # ReplyContent = 'i receive picture:' + msg['FileName']
    # elif msg['Type'] == RECORDING:
    #
    # elif msg['Type'] == VIDEO:
    #
    # elif msg['Type'] == RECORDING:
    #
    # elif msg['Type'] == RECORDING:
    #
    # elif msg['Type'] == RECORDING:

        # itchat.send_msg('nice', toUserName='filehelper')
    # print("someone send to me " )


# itchat.send('Hello, filehelper', toUserName='filehelper')

itchat.auto_login(hotReload=True)

itchat.run()