import os
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector                                    


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
    if event.key == 'q':
        generate_json(tl_list, br_list)                                                          
        tl_list = []                                                              
        br_list = []


def generate_json(tl_list, br_list):
    image_dict = {"image":'', "annotations":[]}
    label_dict = {"label":'', "coordinates":{}}
    coord_dict = {"x":int, "y":int, "width":int, "height":int}

    center_x = int(abs((tl_list[0][0] - br_list[0][0])/2)) + int(tl_list[0][0])
    center_y = int(abs((tl_list[0][1] - br_list[0][1])/2)) + int(tl_list[0][1])

    width = int(abs(tl_list[0][0] - br_list[0][0]))
    height = int(abs(tl_list[0][1] - br_list[0][1]))  

    coord_dict['x'] = center_x
    coord_dict['y'] = center_y
    coord_dict['width'] = width
    coord_dict['height'] = height

    label_dict['label'] = name_class
    label_dict['coordinates'] = coord_dict

    image_dict['image'] = file_name
    image_dict['annotations'].append(label_dict)                               

    annotations.append(image_dict)


#Main
image_folder = 'path_to_image_folder'  
file_name = ''
name_class = ''
rotation = ''

annotations = [] 
tl_list = []
br_list = []
file_names = os.listdir(image_folder)

for file_name in file_names:
    if file_name[0] != '.':
        name_class, sep, tail = file_name.partition('_')
        dir_file = image_folder + '/' + file_name

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

print('Number of Processed Images:', len(annotations))

json_file = json.dumps(annotations)
with open('save_directory/Annotations.json', 'w') as f:
    f.write(json_file)
