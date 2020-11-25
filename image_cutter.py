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
     self.td=30
     if(os.path.exists(self.path_out)==False):
      os.makedirs(self.path_out)
         
  def cutter(self):
   #self.Image.show()
   left=0
   top=0
   
   left=left+10
   """top=top+self.td+10
   right=self.tr-20
   bottom=2*self.td
   im1=self.Image.crop((left,top,right, bottom))
   #im1.show()
   im1.save("ASCII/"+"img.jpg")
   
   top=bottom+10
   right=self.tr-20
   bottom=3*self.td
   im2=self.Image.crop((left,top,right, bottom))
   #im2.show()
   im2.save("ASCII/"+"img2.jpg")
   
   top=bottom+10
   right=self.tr-20
   bottom=4*self.td+10
   im3=self.Image.crop((left,top,right, bottom))
   #im2.show()
   im3.save("ASCII/"+"img3.jpg")
   
   
   top=bottom+10
   right=self.tr-30
   bottom=5*self.td+10
   im4=self.Image.crop((left,top,right, bottom))
   #im2.show()
   im4.save("ASCII/"+"img4.jpg")
   
   
   top=bottom+10
   right=self.tr-20
   bottom=6*self.td+20
   im4=self.Image.crop((left,top,right, bottom))
   im4.save("ASCII/"+"img5.jpg")
   
   
   
   top=bottom+10
   right=self.tr-20
   bottom=7*self.td+20
   im4=self.Image.crop((left,top,right, bottom))
   im4.save("ASCII/"+"img6.jpg")
   
   
   top=bottom+10
   right=self.tr-20
   bottom=8*self.td+20
   im4=self.Image.crop((left,top,right, bottom))
   im4.save("ASCII/"+"img7.jpg")
   """
   for i in range(15):
    if(i==0):
     top=top+self.td+10
    if(0<i<4):
     top=bottom+10
    if(7>i>=4):
      top=bottom+10
    if(i>=7):
     top=bottom+15
      
    if(7>i>=4):
     bottom=(i+2)*self.td
    if(4>i>1):
     bottom=(i+2)*self.td
    if(i<=1):
      bottom=(i+2)*self.td
    if(i>=7):
     bottom=(i+2)*self.td
     
    right=self.tr-20
    
    im4=self.Image.crop((left,top,right, bottom))
    im4.save("ASCII/"+"img"+str(i)+".jpg")
   
      
      
  
  
  
img_cutter=ImageCutter()
img_cutter.cutter()
     
