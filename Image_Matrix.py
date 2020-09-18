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
   fl.write("const unsigned char gImage_2[11040]={\n")
   iter=0
   st="0x"
   for i in range(self.img_width):
    for j in range(self.img_height-1,-1,-1):
     #print(i)
     #print(j)
     a=self.pix[i,j][0]
     b=self.pix[i,j][1]
     c=self.pix[i,j][2]
     S= (a+b+c)//3
     if(S>192):
        st=st+"F"
     if(S>128 and S<=192):
       st=st+"C"
     if(S>=64 and S<=128):
       st=st+"8"
     if(S<64):
       st=st+"0"
     if(iter%2==1):
      fl.write(st)
      fl.write(',')
      st="0x"
     iter=iter+1
     if(iter%16==15):
      fl.write('\n')
      
   """for i in range(self.img_height):
     for j in range(self.img_width):
       	  a=self.pix[j,i][0]
          b=self.pix[j,i][1]
          c=self.pix[j,i][2]
          S= (a+b+c)//3
          fl.write(str(hex(S)))
          fl.write(',')
          if(j%16==15):
           fl.write('\n')
          self.draw.point((i,j), (S,S,S))"""
   

   self.Image.show()
   fl.write("};")


img=ImageMatrix("pug.jpg", 104, 212)    
img.make_gray()  
     

