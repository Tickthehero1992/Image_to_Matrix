import random
from PIL import Image,ImageDraw
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', action='store', help='This is the path')
parser.add_argument ('-o', '--output', action='store', help='This is output file')
parser.add_argument('-w', '--width', action='store', help='This is the width')
parser.add_argument('-l', '--height', action='store', help='This is the height')
parser.add_argument ('-t', '--type', action='store', help='This is the type of transformation')


class ImageMatrix():
  def __init__(self,path,width,height,path_out="file_data.c"):
     self.path=path
     self.Image=Image.open(self.path)
     self.height=height
     self.width=width
     self.Image=self.Image.resize((height,width))
     self.img_width=self.Image.size[0]
     self.img_height=self.Image.size[1]     
     self.draw=ImageDraw.Draw(self.Image)
     self.pix=self.Image.load()
     self.path_out=path_out

  def make_gray(self):
   fl=open(self.path_out, mode='w', encoding='utf-8')
   array_size=self.img_width*self.img_height/2
   st_to_write="const unsigned char gImage_2["+str(int(array_size))+"]={\n"
   fl.write(st_to_write)
   iter=0
   st="0x"
   for i in range(self.img_width):
    for j in range(self.img_height-1,-1,-1):
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
      
   self.Image.show()
   fl.write("};")

  def make_red(self):
   fl=open(self.path_out, mode='w', encoding='utf-8')
   array_size=self.img_width*self.img_height/8
   st_to_write="const unsigned char gImage_BW["+str(int(array_size))+"]={\n"
   fl.write(st_to_write)
   iter=0
   st="0x"
   B=0
   for i in range(self.img_width-1,-1,-1):
    for j in range(self.img_height):
     a=self.pix[i,j][0]
     b=self.pix[i,j][1]
     c=self.pix[i,j][2]
     S= (a+b+c)//3
     if(S>128):
      #st=st+'0'
      B=(B<<1)|1
     else:
      B=B<<1
      #st=st+'0'
     if(iter%8==7):
      fl.write(str(B))
      fl.write(',')
      st='0x'
      B=0
     iter=iter+1
     if(iter%128==15):
      fl.write('\n')
   fl.write("};\n\n")
   st_to_write="const unsigned char gImage_R["+str(int(array_size))+"]={\n"
   fl.write(st_to_write)
   iter=0
   st="0x"
   B=0
   for i in range(self.img_width-1,-1,-1):
    for j in range(self.img_height):
     a=self.pix[i,j][0]
     b=self.pix[i,j][1]
     c=self.pix[i,j][2]
     if a>128 and b<128 and c<128:
       B=B<<1
       #st=st+'F'
     else:
       B=B<<1|1 
       #st=st+'F'
     if(iter%8==7):
      fl.write(str(B))
      fl.write(',')
      st='0x'
      B=0   
     iter=iter+1
     if(iter%128==15):
      fl.write('\n')
     #self.draw.point((i,j),fill=(b,a,c))
   #self.Image.show()
   fl.write("};\n\n")   
   fl.close() 
   
  def make_black(self):
   fl=open(self.path_out, mode='w', encoding='utf-8')
   array_size=self.img_width*self.img_height/8
   st_to_write="const unsigned char gImage_BW["+str(int(array_size))+"]={\n"
   fl.write(st_to_write)
   iter=0
   st="0x"
   B=0
   for i in range(self.img_width):
    for j in range(self.img_height):
     a=self.pix[i,j][0]
     b=self.pix[i,j][1]
     c=self.pix[i,j][2]
     S= (a+b+c)//3
     if(S>128):
      #st=st+'0'
      B=(B<<1)|1
     else:
      B=B<<1
      #st=st+'0'
     if(iter%8==7):
      fl.write(str(B))
      fl.write(',')
      st='0x'
      B=0
     iter=iter+1
     if(iter%128==15):
      fl.write('\n')
   fl.write("};\n\n")
   fl.close() 
   
  def make_black_partial(self):
   fl=open(self.path_out, mode='w', encoding='utf-8')
   array_size= self.img_width*self.img_height/8 if ((self.img_width*self.img_height)%8) else (int(self.img_width*self.img_height/8))+1
   
   st_to_write="const unsigned char gImage_BW["+str(int(array_size))+"]={\n"
   fl.write(st_to_write)
   iter=0
   st="0x"
   B=0
   #Width = (width % 8 == 0)? (width / 8 ): (width/ 8 + 1);
   dev=self.img_width/8 if (self.img_width%8==0) else (int(self.img_width/8) +1) 
   it=0
   for i in range(self.img_width):
    for j in range(self.img_height-1,-1,-1):
     a=self.pix[i,j][0]
     b=self.pix[i,j][1]
     c=self.pix[i,j][2]
     S= (a+b+c)//3
     if(S>128):
      #st=st+'0'
      B=(B<<1)|1
     else:
      B=B<<1
      #st=st+'0'
     if(iter%8==7):
      fl.write(str(B))
      fl.write(',')
      st='0x'
      B=0
     iter=iter+1
     if(iter%128==15):
      fl.write('\n')
   fl.write("};\n\n")
   fl.close() 

"""
img=ImageMatrix("wr.jpeg", 128, 296)    
img.make_red()  
"""
if __name__=="__main__":     
	#print(parser.parse_args().path)
        if(type(parser.parse_args().output)==str):
           out=parser.parse_args().output
        else:
           out="file_data.c"
        img=ImageMatrix(parser.parse_args().path, int(parser.parse_args().width), int(parser.parse_args().height),out)
        if(parser.parse_args().type=="g"):
         img.make_gray() 
        if (parser.parse_args().type=="r"):
         img.make_red()
        if (parser.parse_args().type=="b"):
         img.make_black()
        if (parser.parse_args().type=='p'):
         img.make_black_partial()
