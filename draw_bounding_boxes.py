import os
import re
import cv2
import csv
import json
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector                                    # global constants

image_folder = ''                                                                   #where images are
class_names_txt = ''
save_json_dir = ''

annotations = [] 
tl_list = []
br_list = []


def line_select_callback(clk, rls):                                                 #clk: click event
    global tl_list                                                                  #top left pixel positions
    global br_list                                                                  #button rigth pixel positions
    tl_list.append((int(clk.xdata), (int(clk.ydata))))                              #click first on the left corner
    br_list.append((int(rls.xdata), (int(rls.ydata))))  


def toggle_selector(event):                                                         #matplotlib function: draw rectangole selector
    toggle_selector.RS.set_active(True)


def onkeypress(event):
    global tl_list
    global br_list 
    global img
    if event.key == 'q':
        generate_json(tl_list, br_list)
        tl_list = []                                                                #empty every list
        br_list = []
        img = None


def get_label(file_name):
    name_label = ''
    file_name = re.sub('\.jpg$', '', file_name)

    with open(class_names_txt, 'r') as labels:  
        class_names = csv.reader(labels)
        for row in class_names:
            if row[0] == file_name:
                name_label = row[1]

    return(name_label)


def generate_json(tl_list, br_list):
    image_dict = {"image":'', "annotations":[]}
    label_dict = {"label":'', "coordinates":{}}
    coord_dict = {"x":int, "y":int, "width":int, "heigth":int}

    center_x = int(abs((tl_list[0][0] - br_list[0][0])/2)) + int(tl_list[0][0])
    center_y = int(abs((tl_list[0][1] - br_list[0][1])/2)) + int(tl_list[0][1])

    width = int(abs(tl_list[0][0] - br_list[0][0]))
    heigth = int(abs(tl_list[0][1] - br_list[0][1]))  

    coord_dict['x'] = center_x
    coord_dict['y'] = center_y
    coord_dict['width'] = width
    coord_dict['heigth'] = heigth

    label_dict['label'] = get_label(image_name)
    label_dict['coordinates'] = coord_dict

    image_dict['image'] = image_name
    image_dict['annotations'] = label_dict

    annotations.append(image_dict)


image_name = ''
file_names = os.listdir(image_folder)

for file_name in file_names:
    image_name = file_name
    if len(image_name) > 10:
        dir_file = os.path.abspath(os.path.join(image_folder, file_name))

        fig, ax = plt.subplots(1)                                                   #figure axis
        image = cv2.imread(dir_file)                                                #get path to the image      
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,                                     #button=[1] left mouse click
            spancoords='pixels', interactive=True
        )
                                                                                    #connect events - key_button + function
        bbox = plt.connect('key_press_event', toggle_selector)                      #connect evento press key to the function toggle
        key = plt.connect('key_press_event', onkeypress)
        plt.show()

for i in annotations:
    print(i)
print('\n')
print(annotations)

json_file = json.dumps(annotations)
with open(save_json_dir, 'w') as f:
    f.write(json_file)