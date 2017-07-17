#! python3
#coding:utf-8

import itchat
from itchat.content import *

user_name_list = []
#注册群消息（本注册函数仅支持文本消息）
# @itchat.msg_register(TEXT, isGroupChat = True)
# def text_reply(msg):
#     print(msg['isAt'])#返回是否艾特自己
#     print(msg['ActualNickName'])#返回微信昵称（群昵称）
#     print(msg['Content'])#返回文字内容（貌似支持表情）
#     if (msg['ActualNickName'] == 'yourname'):
#         temp = str(msg['Content'])
#         username = itchat.search_chatrooms(name='qunming')
#         user = username[0]['UserName']
#         itchat.send(temp,toUserName=user)

@itchat.msg_register([PICTURE,RECORDING,TEXT,MAP,CARD,NOTE,SHARING,ATTACHMENT,VIDEO])
#注册接受消息类型;    图片    录音      文字 位置名片 通知 分享    文件       视频
def simple_reply(msg):
    global i
    if msg['Type'] == TEXT:
        if (user_name_list.count(msg['FromUserName'])==0):
            user_name_list.append(msg['FromUserName'])
            itchat.send_msg('这个微信手机上没卡[捂脸]，如果着急可以添加我另一个微信:17640226057，晚上回来才能收到消息[机智]', toUserName=msg['FromUserName'])
        elif (user_name_list.count(msg['FromUserName'])>0 and user_name_list.count(msg['FromUserName'])<10):
            user_name_list.append(msg['FromUserName'])
            itchat.send_msg('再发一条我也看不到，因为这是自动回复，[嘿哈]' , toUserName=msg['FromUserName'])
        elif (user_name_list.count(msg['FromUserName'])>=10):
            pass
        # if msg['Text']  == '1':
        #     itchat.send_msg('aaaa',toUserName=msg['FromUserName'])
        # itchat.send_msg('说出来你可能不信，但这是一条自动回复',toUserName=msg['FromUserName'])
        # ReplyContent = 'i receive message:' + msg['Content']
    elif msg['Type'] == PICTURE:
        if (user_name_list.count(msg['FromUserName'])==0):
            user_name_list.append(msg['FromUserName'])
            itchat.send_msg('这个微信手机上没卡[捂脸]，如果着急可以添加我另一个微信:17640226057，晚上回来才能收到消息[机智]', toUserName=msg['FromUserName'])
        elif (user_name_list.count(msg['FromUserName'])>0 and user_name_list.count(msg['FromUserName'])<10):
            user_name_list.append(msg['FromUserName'])
            itchat.send_msg('再发一条我也看不到，因为这是自动回复，[嘿哈]' , toUserName=msg['FromUserName'])
        elif (user_name_list.count(msg['FromUserName'])>=10):
            pass
    #     # ReplyContent = 'i receive picture:' + msg['FileName']
    elif msg['Type'] == RECORDING:
        if (user_name_list.count(msg['FromUserName'])==0):
            user_name_list.append(msg['FromUserName'])
            itchat.send_msg('这个微信手机上没卡[捂脸]，如果着急可以添加我另一个微信:17640226057，晚上回来才能收到消息[机智]', toUserName=msg['FromUserName'])
        elif (user_name_list.count(msg['FromUserName'])>0 and user_name_list.count(msg['FromUserName'])<10):
            user_name_list.append(msg['FromUserName'])
            itchat.send_msg('再发一条我也看不到，因为这是自动回复，[嘿哈]' , toUserName=msg['FromUserName'])
        elif (user_name_list.count(msg['FromUserName'])>=10):
            pass
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

# 获取自己的用户信息，返回自己的属性字典
# itchat.search_friends()
# 获取特定UserName的用户信息
# itchat.search_friends(userName='@abcdefg1234567')
# 获取任何一项等于name键值的用户
# itchat.search_friends(name='littlecodersh')
# 获取分别对应相应键值的用户
# itchat.search_friends(wechatAccount='littlecodersh')
# 三、四项功能可以一同使用
# itchat.search_friends(name='LittleCoder机器人', wechatAccount='littlecodersh')

# itchat.send('Hello, filehelper', toUserName='filehelper')

# itchat.auto_login(hotReload=True)

#使用命令行二维码
itchat.auto_login(enableCmdQR=True,hotReload=True)

itchat.run()