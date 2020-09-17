import random
from PIL import Image,ImageDraw

class ImageMatrix():
  def __init__(self,path,width,height):
     self.path=path
     self.Image=Image.open(self.path)
     self.height=height
     self.width=width
     self.Image=self.Image.resize((height,width))
     self.img_width=self.Image.size[0]
     self.img_height=self.Image.size[1]     
     self.draw=ImageDraw.Draw(self.Image)
     self.pix=self.Image.load()
     

  def make_gray(self):
   fl=open("file_data.h", mode='w', encoding='utf-8')
   fl.write("const unsigned char gImage_2[22408]={")
   for i in range(self.img_width):
      for j in range(self.img_height):
          a=self.pix[i,j][0]
          b=self.pix[i,j][1]
          c=self.pix[i,j][2]
          S= (a+b+c)//3
          self.draw.point((i,j), (S,S,S))
          #fl.write(str(S))
          """
          if(i!=self.img_width-1) and (j!= self.img_height-1):
           fl.write(', ')
          elif(i==self.img_width-1) and (j==self.img_height-1):
           fl.write('\n')
          else:
           fl.write(', ')
          if (j%15==1 and j!=1):
           fl.write('\n')"""
   for i in range(self.img_height):
     for j in range(self.img_width):
       	  a=self.pix[j,i][0]
          b=self.pix[j,i][1]
          c=self.pix[j,i][2]
          S= (a+b+c)//3
          if(S<64):
           fl.write("0x00, 0x00, 0x00,0x00")
          if(S>=64 and S<128):
           fl.write("0xC0, 0xC0, 0xC0, 0xC0")
          if(S>=128 and S<=192):
           fl.write("0xCC, 0xCC,0xCC, 0xCC")
          if(S>192):
           fl.write("0xFF,0xFF,0xFF,0xFF")
          fl.write(', ')
          if(j%16==0 and j>0):
           fl.write('\n')
  

          
   self.Image.show()
   fl.write("};")


img=ImageMatrix("gray.jpg", 212, 104)    
img.make_gray()  
     

