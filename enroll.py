import fingerprint
import binascii
import serial
import serial.tools.list_ports
import time

fp = fingerprint

serial = serial.Serial('/dev/ttyUSB0', 57600, timeout=0.5)
if serial.isOpen() :
    print("识别器已开启 模式：注册")
    while True:
        data_GetImage = fp.GetImage(serial)
        if(data_GetImage == '02'):
            print("请按住识别器")
        elif(data_GetImage == '00'):
            print("识别成功")
            data_GenChar = fp.GenChar(serial)
            if(data_GenChar == '00'):
                print("已生成特征")
                data_Search = fp.Search(serial)
                if(data_Search[20:22] == '00'):
                    print("该用户已存在")
                    print("用户：",data_Search[22:26])
                    print("相似度：",data_Search[26:30])
                else:
                    print("开始注册")
                    data_Enroll = fp.Enroll(serial)
                    if(data_Enroll[20:22] == '00'):
                        print("用户：",data_Enroll[22:26])
                    else:
                        print("注册失败，请重试")
            else:
                print("gen nosuccess")
        else:
            print("不成功")
else :
    print("open failed")