from PIL import Image, ImageDraw, ImageFont
import sys
import os
import string

text_dir="CreatedText"
font_dir='fonts'

all_string="абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_\+[](){}"
class CreatorText():
  def __init__(self, path_dir, font_path, size, fontName):
    self.size=size    
    self.fontName=fontName
    self.font=ImageFont.truetype(font_path, self.size)
    self.path_dir=path_dir+'_'+self.fontName+'_'+str(self.size)
    if (os.path.exists(self.path_dir)==False):
       os.makedirs(self.path_dir)
              
  def __create_one_img__(self,name):
    img=Image.new('RGB',(int(1*self.size),int(self.size)),color='white')
    draw=ImageDraw.Draw(img)
    draw.text((int(self.size*0.1),-int(self.size*0.1)-1),name,fill='black',font=self.font, align='center')
    #img.show()
    path=self.path_dir+'/'+name+'.jpg'
    img.save(path)
    
  def create_all_symblos(self):
    for n in all_string:
      self.__create_one_img__(n)
    
    
crT=CreatorText(path_dir=text_dir,font_path=font_dir+'/times-new-roman.ttf', size=12, fontName="TimesNewRoman")
crT.create_all_symblos()
