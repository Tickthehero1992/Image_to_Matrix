This is program for transformation image to matrix for Displays GDE Type, with reverse sequence:
Address X increment, Y decrement, adress counter update X direction
using:
python Image_Matrix.py -p path_name -w width_size_pixel -l height_size_pixel 
-t type_of_transformation -o output_file.c

transformation types:
-g - 4 color - grayscale,
-r - 3 color: white/black/red


for g-type will create file file_data.h
for r-type will create file file_data_red.h


text_creator.py - создает текстовые изображения для дальнейшего его перевода в массивы с помощью asci_creator.py



sender_img.py- файл для записи данных в ПЗУ платы БУИ. На стм32 должен быть запущен драйвер https://gitlab.codemaster.pro/a.gorshkov/eeepromdownloader

Как работать с sender_img.py с аргументом -t отправляете 
erase - отчистка памяти стм32
characters - запись символов из  Created_Text_Arial...
black- запись логотипов из logo_bw
red - запись логотипов для красного logo_rbw
button -запись кнопок

если ничего не отправить. то по очереди запишет все.
