from  Image_Matrix import ImageMatrix
import os

default_in_folder="ASCII"
default_folder_out="ASCII_C"

def create_c():
 list_files=os.listdir(default_in_folder)
 if(os.path.exists(default_folder_out)==False):
  os.makedirs(default_folder_out)
 width=8
 height=12
 for l in list_files:
  name_path=default_in_folder+'/'+l
  name_out=default_folder_out+'/'+l[:-3]+'.c'
  img_crt=ImageMatrix(name_path,width, height,name_out)
  img_crt.make_black()
  
  
  
  

create_c()



