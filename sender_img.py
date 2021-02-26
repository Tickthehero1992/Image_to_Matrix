import os
import serial

default_path="CreatedText_Arial._10_C"
default_ser_name="/dev/ttyACM0"
"""
Протокол 1 байт- функция, 1 - байт тип, 2-байта размер.
остальное данные
0х01 - передать символ, тип - код символа
0х02 - передать лого на чб, тип - номер лого 
0х03 - передача лого на кчб, тип - номер лого
0х04 - передача кнопокб тип - 00 - да, 01 - нет
"""
class sendes:
 def __init__(self,path,ser_name):
   self.path=path
   self.ser=serial.Serial(ser_name, 115200, timeout=1)
   
 def send_to_com(self,name_file):
  fl=open(os.path.join(self.path,name_file),mode='r', encoding='utf8')
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
  if(len(name_file[:-2])==2):
     name=ord(name_file[0].encode('cp1251'))
  return array_size, array, name, name_file[0]
     
 def write_characters(self):
   for name in os.listdir(self.path):
    #print(name)
    size,array,name_code,name=self.send_to_com(name)
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
    #print(ss)
    self.ser.write(bytearray(ss)) 
    #while(self.check()==False):
    #  pass
    x=input("Ready:")
    if(x=="exit"):
     break
     
     
 def check(self):
  if(self.ser.read()):
   return True
  else:
   return False
     
cl=sendes(default_path,default_ser_name)     
cl.write_characters()
