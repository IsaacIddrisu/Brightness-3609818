#importing Pillow library
import PIL
#importing necessary tools for image enhancement from the Piloow library
from PIL import Image, ImageEnhance

#opening the photo and storing in pic variable.
pic=Image.open('burnRM.jpg')
#Setting an enhancer type and storing in brightening variable
brightening= ImageEnhance.Brightness(pic)
#setting brigtening factoor
factor=2.5
#applying factor to the photo and storing as pic_output
pic_output= brightening.enhance(factor)
#saving new photo
pic_output.save("newPic.jpg")


