import os
import serial
import time
import argparse
default_path="CreatedText_Arial._10_C"
default_ser_name="/dev/ttyACM0"
default_logos_dir="logo_bw"
default_logos_red_dir="logo_rbw"
default_buttons_dir= "buttons"

parser = argparse.ArgumentParser()
parser.add_argument ('-t', '--type', action='store', help='This is the type of operation', default=None)

"""
Протокол 1 байт- функция, 1 - байт тип, 2-байта размер.
остальное данные
0х01 - передать символ, тип - код символа
0х02 - передать лого на чб, тип - номер лого 
0х03 - передача лого на кчб, тип - номер лого
0х04 - передача кнопок тип - 00 - да, 01 - нет, 02 - скрин вкл/выкл, 03 - перезагрузка
"""
class sendes:
 def __init__(self,path_char=None,ser_name=None,path_bw=None,path_rbw=None, path_btn=None):
   self.my_path=os.path.realpath(__file__)[:-len("sender_img.py")]
   self.path=os.path.join(self.my_path,path_char)
   self.path_bw=os.path.join(self.my_path,path_bw)
   self.path_rbw=os.path.join(self.my_path,path_rbw)
   self.path_btn=os.path.join(self.my_path,path_btn)
   self.ser=serial.Serial(ser_name, 115200, timeout=1)
   
 def send_to_com(self,name_file,path):
  fl=open(os.path.join(path,name_file),mode='r', encoding='utf8')
  l=fl.readline()
  n_ent=l.find("[")
  n_ext=l.find("]")
  array_size=int(l[n_ent+1:n_ext])
  array=[]
  for l in fl.readlines():
     for n in l.split(','):
      if((n!='\n') and (n.find('}')==-1)):
       array.append(n)
  #array.pop()
  name=name_file
  if(len(name_file[:-2])==2):
     name=ord(name_file[0].encode('cp1251'))
  return array_size, array, name, name_file[0]
     
 def write_characters(self):
   self.ser.flush()
   for name in os.listdir(self.path):
    print(name)
    size,array,name_code,name=self.send_to_com(name,self.path)
    size=size.to_bytes(1,byteorder='little')
    name_code=name_code.to_bytes(1, byteorder='big')
    st=b"\x01"+name_code+size
    self.ser.write(st)
    while(self.check()==False):
      pass
    ss=[] 
    for ar in array:
      ss.append(int(ar))
    #ss=str()
    print(len(ss))
    self.ser.write(bytearray(ss)) 
    while(self.check()==False):
      pass
   
    time.sleep(1)
    #break
    
 def write_bw_logo(self):
     Id=1
     for name in os.listdir(self.path_bw):
      #print(name)
      size,array,name_code,names=self.send_to_com(name,self.path_bw)
      #print(array)
      size=size.to_bytes(2,byteorder='little')
      st=b"\x02"+Id.to_bytes(1,byteorder='big')+size
      Id=Id+1
      self.ser.write(st)
      while(self.check()==False):
       pass
      ss=[] 
      for ar in array:
       ss.append(int(ar))
      #print(st)
      self.ser.write(bytearray(ss)) 
      while(self.check()==False):
       pass
     
     
     
 def send_to_com_red(self,name_file):
  fl=open(os.path.join(self.path_rbw,name_file),mode='r', encoding='utf8')
  l=fl.readline()
  n_ent=l.find("[")
  n_ext=l.find("]")
  array_size=int(l[n_ent+1:n_ext])
  array=[]
  for l in fl.readlines():
     for n in l.split(','):
      if (n.find('}')!=-1) or (n.find('{')!=-1):
       pass
      else:
       if(n!='\n'):
        array.append(n)
  array.pop()
  return len(array), array
 
 def write_rbw(self):
  Id=1
  for name in os.listdir(self.path_rbw):
    self.send_to_com_red(name)
    size, array = self.send_to_com_red(name)
    #print(array)
    #print(size)
    #break
    size=size.to_bytes(2,byteorder='little')
    st=b"\x03"+Id.to_bytes(1,byteorder='big')+size
    Id=Id+1
    self.ser.write(st)
    while(self.check()==False):
     pass
    ss=[] 
    for ar in array:
     ss.append(int(ar))
    #print(st)
    self.ser.write(bytearray(ss)) 
    while(self.check()==False):
       pass
       
 def write_btn(self):
  for name in os.listdir(self.path_btn):
    size,array,name_code,names=self.send_to_com(name,self.path_btn)
    #print(name_code)
    Id=0
    if(name_code=="cancel.c"):
     Id=3
    if(name_code=="yes.c"):
     Id=4
    if(name_code=="OFF.c"):
     Id=2
    if(name_code=="reboot.c"):
     Id=1
    #print(name_code)
    size=size.to_bytes(2,byteorder='little')
    st=b"\x04"+Id.to_bytes(1,byteorder='big')+size
    #print(st)
    self.ser.write(st)
    while(self.check()==False):
     pass
    ss=[] 
    for ar in array:
     ss.append(int(ar))
      #print(st)
    self.ser.write(bytearray(ss)) 
    while(self.check()==False):
       pass
    
         
       
       
 def erasing(self):
    st=b"\x05\x08\x07\x02"
    self.ser.write(st)
    while(self.check()==False):
     pass
    st=b"\x05\x08\x07\x02\x03\x93"
    self.ser.write(st)
    while(self.check()==False):
     pass
     
 def reboot(self):
    st=b"\x06\x08\x07\x02"
    self.ser.write(st)
    self.ser.close()
    sys.exit(0)
  
 def check(self):
  OK=self.ser.read(size=2).decode()
  if(OK=="OK"):
   print(OK)
   return True
  else:
   return False
     
cl=sendes(default_path,default_ser_name,default_logos_dir,default_logos_red_dir,default_buttons_dir)     

if __name__=="__main__":    
 if(parser.parse_args().type==None):
  print("start erase")
  cl.erasing()
  print("start character write")
  cl.write_characters()
  print("start bw logs")
  cl.write_bw_logo()
  print("start rbd logs")
  cl.write_rbw()
  print("start btns")
  cl.write_btn()
  print("start reboot")
  cl.reboot()
 if(parser.parse_args().type=='erase'):
  cl.erasing()
 if(parser.parse_args().type=='characters'):
  cl.write_characters()
 if(parser.parse_args().type=='black'):
  cl.write_bw_logo()
 if(parser.parse_args().type=='red'):
  cl.write_rbw()
 if(parser.parse_args().type=='buttons'):
   cl.write_btn()

