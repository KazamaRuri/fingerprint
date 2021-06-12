import binascii
import serial
import serial.tools.list_ports
import time

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
    return data

def GetImage(serial):
    command = 'EF 01 FF FF FF FF 01 00 03 01 00 05'
    mess = bytes.fromhex(command)
    serial.write(mess)
    time.sleep(1)
    data = recv(serial)
    data_con = str(binascii.b2a_hex(data))[20:22]
    return data_con

def GenChar(serial):
    command = 'EF 01 FF FF FF FF 01 00 04 02 01 00 08'
    mess = bytes.fromhex(command)
    serial.write(mess)
    time.sleep(1)
    data = recv(serial)
    data_con = str(binascii.b2a_hex(data))[20:22]
    return data_con

def Search(serial):
    command = 'EF 01 FF FF FF FF 01 00 08 04 01 00 00 00 64 00 72'
    mess = bytes.fromhex(command)
    serial.write(mess)
    time.sleep(1)
    data = recv(serial)
    data_con = str(binascii.b2a_hex(data))
    return data_con

def Enroll(serial):
    command = 'EF 01 FF FF FF FF 01 00 03 10 00 14'
    mess = bytes.fromhex(command)
    serial.write(mess)
    time.sleep(1)
    data = recv(serial)
    data_con = str(binascii.b2a_hex(data))
    return data_con

def Identify(serial):
    command = 'EF 01 FF FF FF FF 01 00 03 11 00 15'
    mess = bytes.fromhex(command)
    serial.write(mess)
    time.sleep(1)
    data = recv(serial)
    data_con = str(binascii.b2a_hex(data))
    return data_con

def DeletChar(serial):
    command = 'EF 01 FF FF FF FF 01 00 07 0c 00 00 00 00 00 00' # page number sum
    mess = bytes.fromhex(command)
    serial.write(mess)
    time.sleep(1)
    data = recv(serial)
    data_con = str(binascii.b2a_hex(data))[20:22]
    return data_con

# if __name__ == '__main__':
#     serial = serial.Serial('/dev/ttyUSB0', 57600, timeout=0.5)
#     if serial.isOpen() :
#         print("识别器已开启 模式：注册")
#         while True:
#             data_GetImage = GetImage()
#             if(data_GetImage == '02'):
#                 print("请按住识别器")
#             elif(data_GetImage == '00'):
#                 print("识别成功")
#                 data_GenChar = GenChar()
#                 if(data_GenChar == '00'):
#                     print("已生成特征")
#                     data_Search = Search()
#                     if(data_Search[20:22] == '00'):
#                         print("该用户已存在")
#                         print("用户：",data_Search[22:26])
#                         print("相似度：",data_Search[26:30])
#                     else:
#                         print("开始注册")
#                         data_Enroll = Enroll()
#                         if(data_Enroll[20:22] == '00'):
#                             print("用户：",data_Enroll[22:26])
#                         else:
#                             print("注册失败，请重试")
#                 else:
#                     print("gen nosuccess")
#             else:
#                 print("不成功")
#     else :
#         print("open failed")