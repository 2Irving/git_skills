import cv2
from datetime import datetime
LCD_WIDTH = 240
LCD_LENGTH = 280
#start = datetime.now()
#end = datetime.now()
# print(end-start)

def resize_img(image,width,length):
    if(width > LCD_WIDTH or length > LCD_LENGTH):
        if(width <= length):#横
            image = cv2.resize(image,(280,int(width*(280/length))))
    return image
    # if(image_width > image_length):#竖
    #     cv2.resize(image,())

def toarray_rgb565(img_arr):
    img_arr = cv2.cvtColor(img_arr,cv2.COLOR_BGR2BGR565)
    return img_arr

    
image = cv2.imread('rtt.jpg')
image_width = image.shape[0]
image_length = image.shape[1]
image_dimension = image.shape[2]
#print(image.shape[0], image.shape[1])

image = resize_img(image,image_width,image_length)
cv2.imshow("im",image)

image_565 = toarray_rgb565(image)

byte_array = image_565.tobytes()
print(byte_array.hex())
cv2.waitKey()