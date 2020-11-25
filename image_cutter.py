from PIL import Image,ImageDraw
import os
import sys

default_path_in="ascii.jpg"
default_dir_out="ASCII"

class ImageCutter():
  def __init__(self,path=default_path_in,path_out=default_dir_out):
     self.path=path
     self.Image=Image.open(self.path)
     self.draw=ImageDraw.Draw(self.Image)
     self.pix=self.Image.load()
     self.path_out=path_out
     self.width_tr=20
     self.width_td=20
     self.tr=52
     self.td=34
     if(os.path.exists(self.path_out)==False):
      os.makedirs(self.path_out)
         
  def cutter(self):
   #self.Image.show()
   left=0
   top=0
   
   left=left+10
   bottom=self.td
   for i in range(15):
    if(i==0):
     top=34
    else:
     top=bottom
    bottom=(i+2)*self.td
    if(i<4):
     bottom=bottom-3
    right=self.tr-20
    
    im4=self.Image.crop((left,top,right, bottom))
    im4.save("ASCII/"+"img"+str(i)+".jpg")
   
      
      
  
  
  
img_cutter=ImageCutter()
img_cutter.cutter()
     
