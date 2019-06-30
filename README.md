# Generate Annotations JSON Format for CreateML with Python

Python script which generates annotations in JSON format required for training object detection models using CreateML.

CreateML requires a list of dictionaries with information about the selected bounding boxes: center and size (height and width) of the bounding box.


![annotations](https://user-images.githubusercontent.com/41980160/60399956-b2af1700-9b32-11e9-990d-c0dc039273ad.png)


## Code Description

The following code shows how to draw bounding boxes using matplotlib library. Functions 'line_select_callback', 'toggle_selector', 'onkeypress' where found on the matplotlib documentation. It allow us to iterate over the images of a folder, draw bounding boxes and get the corresponding top left and bottom right coordinates of the drawn bounding box.

Detailed description on: https://medium.com/@eriksols/generate-annotations-json-format-for-createml-apple-with-python-90fc848cd439?postPublishedType=repub


## Run Script

Pass the path to the images folder (image_folder = 'path_to_image_folder'). Each image must be named with the corresponding class in order to detect the label, example: 'dog_01.jpg'.

![folder_exm](https://user-images.githubusercontent.com/41980160/60400005-7af49f00-9b33-11e9-854b-700d0bedf4aa.png)

### Run generate_json.py script

Code will iterate over all the images contained on the images folder.

Now, you must draw the bounding box over the interest object. Once you are confident about the drawn bounding box, press "q" to generate and store the corresponding dictionary and continue the process with the next image.

![bb](https://user-images.githubusercontent.com/41980160/60400013-9f507b80-9b33-11e9-9627-bf4b68558a1a.png)

A list containing the dictionaries of all images will be generated.

![dict](https://user-images.githubusercontent.com/41980160/60400020-b68f6900-9b33-11e9-94f7-b794d1dfb74f.png)

Finally a JSON file will be generated.

![json_file](https://user-images.githubusercontent.com/41980160/60400025-cc9d2980-9b33-11e9-9c7e-3afe755b6384.png)


### Open and Iterate JSON file

#### Run open_json_file.py

This script opens and iterates over the list containing the image dictionaries. This script also shows how to access the the list elements and the corresponding dictionaries.

It prints:
List length (number of contained dictionaries)
Image dictionary
Label dictionary
Coordinates dictionary

![res](https://user-images.githubusercontent.com/41980160/60400071-7d0b2d80-9b34-11e9-825d-0fecb61c483b.png)


That's all! :D
