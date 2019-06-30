# Generate Annotations JSON Format for CreateML with Python

Python script which generates annotations in JSON format required for training object detection models using CreateML.

CreateML requires a list of dictionaries with information about the selected bounding boxes: center and size (height and width) of the bounding box.


![annotations](https://user-images.githubusercontent.com/41980160/60399956-b2af1700-9b32-11e9-990d-c0dc039273ad.png)


## Code Description

The following code shows how to draw bounding boxes using matplotlib library. Functions 'line_select_callback', 'toggle_selector', 'onkeypress' where found on the matplotlib documentation. It allow us to iterate over the images of a folder, draw bounding boxes and get the corresponding top left and bottom right coordinates of the drawn bounding box.

```
import os
import cv2
import json
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
image_folder = 'path_to_image_folder'
annotations = []
tl_list = []
br_list = []
def line_select_callback(clk, rls):                                                                        
    global tl_list                                                                     
    global br_list                                                                 
    tl_list.append((int(clk.xdata), (int(clk.ydata))))                                
    br_list.append((int(rls.xdata), (int(rls.ydata))))
def toggle_selector(event):                                                         
    toggle_selector.RS.set_active(True)
def onkeypress(event):
    global tl_list
    global br_list
    global img
    if event.key == 'q':
       generate_json(tl_list, br_list)
       tl_list = []                                                                  
       br_list = []
       img = None
```

The 'generate_json' function uses the top left and bottom right coordinates to compute the center, heigth and width of the bounding box. Also it declares the corresponding dictionaries to generate the annotations. Once created the dictionary, it is appended to a global list called 'annotations' which stores the dictionaries of all the iterated images.

```
def generate_json(tl_list, br_list):
    image_dict = {"image":'', "annotations":[]}
    label_dict = {"label":'', "coordinates":{}}
    coord_dict = {"x":int, "y":int, "width":int, "heigth":int}
    center_x = int(abs((tl_list[0][0] - br_list[0][0])/2)) +     
    int(tl_list[0][0])
    center_y = int(abs((tl_list[0][1] - br_list[0][1])/2)) +  
    int(tl_list[0][1])
    width = int(abs(tl_list[0][0] - br_list[0][0]))
    height = int(abs(tl_list[0][1] - br_list[0][1]))
    coord_dict['x'] = center_x
    coord_dict['y'] = center_y
    coord_dict['width'] = width
    coord_dict['heigth'] = heigth
    label_dict['label'] = name_class
    label_dict['coordinates'] = coord_dict
    image_dict['image'] = image_name
    image_dict['annotations'] = label_dict
    annotations.append(image_dict)
```

The main function, create a list of all the files contained on the 'path_folder' and iterates over the images, calls the other functions and generates the JSON file containing a list of dictionaries of all the images.

```
if __name__ == '__main__':
   image_name = ''
   name_class = ''
   file_names = os.listdir(image_folder)
   for file_name in file_names:
       image_name = file_name
       if image_name[0] != '.':     
          name_class, sep, tail = image_name.partition('_')
          dir_file = os.path.abspath(os.path.join(image_folder,    
                                                    file_name))
          fig, ax = plt.subplots(1)      
          image = cv2.imread(dir_file)     
          image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
          ax.imshow(image)
          toggle_selector.RS = RectangleSelector(
                 ax, line_select_callback,
                 drawtype='box', useblit=True,
                 button=[1], minspanx=5, minspany=5,
                 spancoords='pixels', interactive=True
          )
   
          bbox = plt.connect('key_press_event', toggle_selector) 
          key = plt.connect('key_press_event', onkeypress)
          plt.show()
   json_file = json.dumps(annotations)
   with open('path_save_directory/annotations.json', 'w') as f:
   f.write(json_file)
```


## Run Script

Pass the path to the images folder (image_folder = 'path_to_image_folder'). Each image must be named with the corresponding class in order to detect the label, example: 'dog_01.jpg'.

![folder_exm](https://user-images.githubusercontent.com/41980160/60400005-7af49f00-9b33-11e9-854b-700d0bedf4aa.png)

Run generate_json.py script

Code will iterate over all the images contained on the images folder.

Now, you must draw the bounding box over the interest object. Once you are confident about the drawn bounding box, press "q" to generate and store the corresponding dictionary and continue the process with the next image.

![bb](https://user-images.githubusercontent.com/41980160/60400013-9f507b80-9b33-11e9-9627-bf4b68558a1a.png)

A list containing the dictionaries of all images will be generated.

![dict](https://user-images.githubusercontent.com/41980160/60400020-b68f6900-9b33-11e9-94f7-b794d1dfb74f.png)

Finally a JSON file will be generated.

![json_file](https://user-images.githubusercontent.com/41980160/60400025-cc9d2980-9b33-11e9-9c7e-3afe755b6384.png)


### Open and Iterate JSON file

Run open_json_file.py

This script opens and iterates over the list containing the image dictionaries. This script also shows how to access the the list elements and the corresponding dictionaries.

It prints:
List length (number of contained dictionaries)
Image dictionary
Label dictionary
Coordinates dictionary

Thanks for reading! :D
