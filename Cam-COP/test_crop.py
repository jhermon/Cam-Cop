import cv2
import pytesseract
import numpy as np
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#global call so it can be used in capFrontend.py. This variable is reassigned in the read_plate()


def read_plate(image):
    image = cv2.imread(image)
    image = cv2.resize(image, (500, 200))

    x = image.shape[1]
    y = image.shape[0]
    image = image[40:165, 30:470]


    #cv2.imshow('test',image)
    #cv2.waitKey(0)
    #image = cv2.GaussianBlur(image, (9,9), 0)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray,11, 62, 62)
    #gray = cv2.Canny(gray,170,200)


    _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    #cv2.imshow('test',binary_image)
    
    n_white_pix = np.sum(binary_image == 255)
    n_black_pix = np.sum(binary_image == 0)

    
    if n_black_pix>=n_white_pix:
        
        binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    #cv2.imshow('n', binary_image)
    #cv2.waitKey(0)
    try:
        
        text1 = pytesseract.image_to_string(binary_image, lang='eng', config='--psm 6')
    

        text1 = text1.split(' ')
        
        numbers = ''.join(i for i in text1[0] if i.isalnum())
        #print(numbers)
        if len(numbers)>4:
            numbers = numbers[1:]
            
            
        else:
            pass
        
        letters = ''.join(i for i in text1[1] if i.isalnum())
        #print(letters)
        if len(letters)>2 and int(letters)==False:
            letters = letters[:-1]
            
            
        else:
            pass

        plate = numbers + letters
        

        if len(plate)<6:
            plate = 'Unable to read license plate'
        else:
            pass
        
        #print(plate)
        return plate
    except Exception:
        error = 'Unable to read license Plate'
        return error


#read_plate(r'C:\Users\Jhermon\Desktop\plot23.jpeg')
#read_plate(r'C:\Users\Jhermon\Desktop\plot6.jpeg')
#read_plate(r'C:\Users\Jhermon\Desktop\plot8.jpeg')
#read_plate(r'C:\Users\Jhermon\Desktop\plot7.jpeg')
#read_plate(r'C:\Users\Jhermon\Desktop\pot4.jpeg')
#read_plate(r'C:\Users\Jhermon\Desktop\croptest5.jpg')
#read_plate(r'C:\Users\Jhermon\Desktop\sub.jpeg')
#read_plate(r'C:\Users\Jhermon\Desktop\lastman.jpeg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\pot2.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\pot1.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\late1.jpeg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\late2.jpeg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\late3.jpeg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\late4.jpeg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\DC 1973.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\2781 GJ.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\3029 HN.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\6053 GX.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\6181 HB.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\9441 FU.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\9707 JE.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\7888 AD.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\4747 GB.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\4446 EX.jpg')
#read_plate(r'C:\tensorflow1\models\research\object_detection\cropped-images\DC 1973.jpg')

#get_details(read_plate(r'C:\Users\Jhermon\Desktop\Img (306).jpeg'))




    





