from tkinter import *
from tkinter import filedialog 
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.font as font
from PIL import Image
from PIL import ImageTk
from Object_detection_image import detect
import time
import numpy as np
import cv2
import os
#from db_conn import get_details
import datetime



#tkinter Frontend

#home logo displayed
#home = Toplevel() # create the window
home = ThemedTk(theme="breeze")


#home.transient([root]) 

#opens the image ,resizes it and places it on the window
path =Image.open("C:/tensorflow1/models/research/object_detection/capcoplogo.png")
re_image = path.resize((600, 600), Image.ANTIALIAS)
home_img = ImageTk.PhotoImage(re_image)
home_label = Label(home,image=home_img)
home_label.image = home_img

#Places the home window in the center of the any computer screen
hl=600
wl=600

widthl = home.winfo_screenwidth()
heightl= home.winfo_screenheight()

x_coordinate = (widthl/2) - (wl/2)
y_coordinate = (heightl/2) - (hl/2)

home.geometry("%dx%d+%d+%d" % (wl,hl,x_coordinate,y_coordinate))

#actually puts the window on the screen
home_label.pack()

#destroys the window after 5000 mill seconds(5 secs)

home.after(3000,lambda:home.destroy())

home.mainloop()


#changes the theme and also changes fonts of different labels based on the variable used.
root = ThemedTk(theme="breeze")
myFont = font.Font(family='Helvetica', size=15, weight='bold')


#title of root window
root.title("Cam Cop")
root.iconbitmap('C:/tensorflow1/models/research/object_detection/capfinal.ico')

#size window
width_value = root.winfo_screenwidth()
height_value = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(width_value,height_value))

#First label
label1 = Label(root, text="Enter image:",font=myFont)
label1.place(x=1130,y=40)


def click1():
    # gives the location of the images
    global label_filedialog
    filename = filedialog.askopenfilename(initialdir ="/", title="Select Image", filetype=(("png files","*.png"),("jpeg files","*.jpeg"),("jpg files","*.jpg")))
    click1.img1 = filename
    label_filedialog = Label(root, text="")
    label_filedialog.place(x=1150,y=80)
    label_filedialog.configure(text=filename)

    if filename == "":
        label_filedialog.destroy()
        addButton['state'] = NORMAL
        
    else:
       addButton['state'] = DISABLED
       
        
       img =cv2.imread(filename)
       #adj_img = cv2.rectangle(img,(100,100),(300,300),(0,255,0),3)
       # changes the color channel
       image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

       
       #converts to tk image and resizes the image so it can fit in the tkinter frame
       image_Pil = Image.fromarray(image)
       resize_image = image_Pil.resize((1080, 700), Image.ANTIALIAS)
       tkImage = ImageTk.PhotoImage(resize_image)

       #displays on window
       click1.label_img = Label(frame,image=tkImage)
       click1.label_img.image = tkImage
       click1.label_img.pack()


def detector():
    global label_img
    #runs the detect function from Object_detection_image
    detect(click1.img1)
    
    img =cv2.imread(detect.img_scan)
    #adj_img = cv2.rectangle(img,(100,100),(300,300),(0,255,0),3)
    # changes the color channel
    image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

       
    #converts to tk image and resizes the image so it can fit in the tkinter frame
    image_Pil = Image.fromarray(image)
    resize_image = image_Pil.resize((1080, 700), Image.ANTIALIAS)
    tkImage = ImageTk.PhotoImage(resize_image)

    #removes previous image
    click1.label_img.destroy()

    #recreates the label that was destroyed/delected
    click1.label_img = ''
    
    #displays scanned image on window
    detector.label_img = Label(frame,image=tkImage)
    detector.label_img.image = tkImage
    detector.label_img.pack()

def reset():
    #remove label in the window
    label_filedialog.destroy()
    if click1.label_img != '':
        click1.label_img.destroy()
    elif detector.label_img !='':
        detector.label_img.destroy()
        

    addButton['state'] = NORMAL



#USING OFFLINE DATABASE
'''def detector():
    global label_img
    #runs the detect function from Object_detection_image
    detect(click1.img1)
    
    img =cv2.imread(detect.img_scan)
    #adj_img = cv2.rectangle(img,(100,100),(300,300),(0,255,0),3)
    # changes the color channel
    image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

       
    #converts to tk image and resizes the image so it can fit in the tkinter frame
    image_Pil = Image.fromarray(image)
    resize_image = image_Pil.resize((1080, 700), Image.ANTIALIAS)
    tkImage = ImageTk.PhotoImage(resize_image)

    #removes previous image
    click1.label_img.destroy()

    #recreates the label that was destroyed/delected
    click1.label_img = ''
    
    #displays scanned image on window
    detector.label_img = Label(frame,image=tkImage)
    detector.label_img.image = tkImage
    detector.label_img.pack()
    if len(detect.plate) != 6:
        detector.label_plate = Label(root,text=detect.plate)
        detector.label_plate.place(x=1150,y=180)
        detector.label_plate.config(font=('Courier',20))
    else:
        
        detector.label_plate = Label(root,text=detect.plate)
        detector.label_plate.place(x=1150,y=180)
        detector.label_plate.config(font=('Courier',44))
        #this function queries the database
        
        get_details(detect.plate)
        if type(get_details.lst[0]) == str:
            #adding result of database to the window
            #header of driver details
            detector.label_header = Label(root,text='Driver Info')
            detector.label_header.place(x=1150,y=240)
            detector.label_header.config(font=('Courier',25,'bold'))
            #print firstname
            detector.label_firstname = Label(root, text= 'Firstname: ' + get_details.lst[0])
            detector.label_firstname.place(x=1150,y=270)
            detector.label_firstname.config(font=('Courier',15))
            #print lastname
            detector.label_lastname = Label(root, text= 'Lastname: ' + get_details.lst[1])
            detector.label_lastname.place(x=1150,y=300)
            detector.label_lastname.config(font=('Courier',15))
            #print gender
            detector.label_gender = Label(root, text= 'Gender: ' + get_details.lst[2])
            detector.label_gender.place(x=1150,y=330)
            detector.label_gender.config(font=('Courier',15))
            #print TRN
            detector.label_TRN = Label(root, text= 'TRN: ' + get_details.lst[3])
            detector.label_TRN.place(x=1150,y=360)
            detector.label_TRN.config(font=('Courier',15))
            #print address
            detector.label_address = Label(root, text= 'Address:')
            detector.label_address2 = Label(root, text= get_details.lst[4])
            detector.label_address.place(x=1150,y=390)
            detector.label_address.config(font=('Courier',15, 'bold'))
            detector.label_address2.place(x=1150,y=420)
            detector.label_address2.config(font=('Courier',15))
            #print DOB
            dob = get_details.lst[5].strftime('%m/%d/%Y')
            detector.label_DOB = Label(root, text= 'DOB: ' + dob)
            detector.label_DOB.place(x=1150,y=450)
            detector.label_DOB.config(font=('Courier',15))
            #print car brand
            detector.label_car_brand = Label(root, text= 'Car brand: ' + get_details.lst[6])
            detector.label_car_brand.place(x=1150,y=480)
            detector.label_car_brand.config(font=('Courier',15))
            #print car color
            detector.label_car_color = Label(root, text= 'Car color: ' + get_details.lst[7])
            detector.label_car_color.place(x=1150,y=510)
            detector.label_car_color.config(font=('Courier',15))
            #year made
            detector.label_year_made = Label(root, text= 'Year made: ' + get_details.lst[8])
            detector.label_year_made.place(x=1150,y=540)
            detector.label_year_made.config(font=('Courier',15))
            #year purchased
            detector.label_year_purchased = Label(root, text= 'Year purchased: ' + get_details.lst[9])
            detector.label_year_purchased.place(x=1150,y=570)
            detector.label_year_purchased.config(font=('Courier',15))
        else:
            get_details(detect.plate)
            detector.label_match = Label(root, text='Possible match found: ' + get_details.lst[0][1] + '\n' + str(get_details.lst[0][0]) + '% match')
            detector.label_match.place(x=1150,y=240)
            detector.label_match.config(font=('Courier',15))


def reset():
    #remove label in the window
    label_filedialog.destroy()
    if click1.label_img != '':
        click1.label_img.destroy()
    elif detector.label_img !='' and len(detect.plate) == 6:
        detector.label_img.destroy()
        detector.label_plate.destroy()
        detector.label_header.destroy()
        detector.label_firstname.destroy()
        detector.label_lastname.destroy()
        detector.label_gender.destroy()
        detector.label_TRN.destroy()
        detector.label_address.destroy()
        detector.label_address2.destroy()
        detector.label_DOB.destroy()
        detector.label_car_brand.destroy()
        detector.label_car_color.destroy()
        detector.label_year_made.destroy()
        detector.label_year_purchased.destroy()
        
    elif detector.label_img !='' and len(detect.plate) != 6:
        detector.label_img.destroy()
        detector.label_plate.destroy()
    else:
        detector.label_match.destroy()

    addButton['state'] = NORMAL'''


#create button
addButton = ttk.Button(root, text="Choose image",command=click1)
#addButton['font'] = myFont
addButton.place(x=1260,y=40)

#scan image
scanButton = ttk.Button(root, text="Scan image",command=detector)
scanButton.place(x=1150,y=140)

# reset button
resetButton = ttk.Button(root, text="Reset",command=reset)
#resetButton['font'] = myFont
resetButton.place(x=1280,y=140)

# frame
frame = LabelFrame(root, padx=2, pady=2)
label_dummy =Label(frame)
label_dummy.pack()
frame.place(x=10,y=40,width=1100, height=720)




root.mainloop()

