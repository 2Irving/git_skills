import cv2
import socket
import zlib
LCD_WIDTH = 240
LCD_LENGTH = 280
SOCKET_MODE = 'UDP'
server = ('192.168.101.183',3333)

def socket_cilent(ip):
    global client
    #TCP
    if SOCKET_MODE == 'TCP':
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #连接客户端地址 ip=(port,host)
        if(client.connect_ex(ip) == 0):
            print("connect to server",ip)

    #UDP
    if SOCKET_MODE == 'UDP':
        client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



def resize_img(image,width,length):
    if(width > LCD_WIDTH or length > LCD_LENGTH):
        if(width <= length):#横
            image = cv2.resize(image,(280,int(width*(280/length))))
    return image
    # if(image_width > image_length):#竖
    #     cv2.resize(image,())

def toarray_rgb565(img_arr):
    img_arr = cv2.cvtColor(img_arr,cv2.COLOR_BGR2BGR565)
    img_arr = img_arr[:,:,(1,0)]
    return img_arr

if __name__=="__main__":
    socket_cilent(server)
    image = cv2.imread('tst.png')
    image_width = image.shape[0]
    image_length = image.shape[1]
    image_dimension = image.shape[2]

    #图像缩放并且转为rgb565的图像矩阵
    image = resize_img(image,image_width,image_length)
    image_565 = toarray_rgb565(image)

    #转字节传输
    img_bytestream = image_565.tobytes()
    print("bytestream:",type(img_bytestream),len(img_bytestream),"B")

    #压缩字节流，减小开销，到接收端再解压
    compress_bytestream = zlib.compress(img_bytestream)
    print("compress_bytestream:",type(compress_bytestream),len(compress_bytestream),"B")

    #TCP
    #面向连接的，可靠的，点对点，字节流传输，自有阻塞机制
    if SOCKET_MODE == 'TCP':
        client.send(b'start')
        client.send(compress_bytestream)
        client.send(b'end') #截止符
    #UDP
    #无连接的，不可靠的，多对多，数据报文传输，不带阻塞机制，自己实现
    if SOCKET_MODE == 'UDP':
        client.sendto(b'start',server)

        for i in range(0,int(len(compress_bytestream)/1024)):
            client.sendto(compress_bytestream[i*1024:(i+1)*1024],server) #UDP需要自己拆包
            print("pack",i*1024,(i+1)*1024)
            #阻塞 等待接收端成功再发送
            while(1):
                if client.recvfrom(1024):
                    break

        client.sendto(b'end',server) #截止符



    cv2.imshow("im",image)
    cv2.waitKey()