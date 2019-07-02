import os
import cv2
import json
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector                                    # global constants

image_folder = 'path_to_image_folder'  #where images are

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
        tl_list = []                                                                #empty all lists
        br_list = []
        img = None


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

    image_dict['image'] = image_name
    image_dict['annotations'].append(label_dict) 

    annotations.append(image_dict)


if __name__ == '__main__':
    image_name = ''
    name_class = ''
    file_names = os.listdir(image_folder)

    print(file_names)

    for file_name in file_names:
        image_name = file_name
        if image_name[0] != '.':                                                        #When copy and page images inside a folder a '.DS_Store' file is generated, then this file must not be read
            name_class, sep, tail = image_name.partition('_')
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
    with open('path_to_save_directory/annotations.json', 'w') as f:
        f.write(json_file)
