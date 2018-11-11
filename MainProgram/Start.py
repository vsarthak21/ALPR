import os
import time
import pyrebase
import datetime
import videosplit
import Main
import base64
import cv2
import json
from io import BytesIO
from PIL import Image

config = {
    'apiKey': "AIzaSyCAxWkvFUGnQ69_s3s9iNH90VSnRDo6Efo",
    'authDomain': "vision-5334f.firebaseapp.com",
    'databaseURL': "https://vision-5334f.firebaseio.com",
    'projectId': "vision-5334f",
    'storageBucket': "vision-5334f.appspot.com",
    'messagingSenderId': "45558056742"
}

firebase = pyrebase.initialize_app(config)

try:
    db = firebase.database()
except:
    print("Unable to connect to the database")


# db.child("users").child('4JEMFBw3wodPSv0B1zTKHIIj1Iy1').update(
#     {"vehicles": {
#         "lnlfkdn": {
#             "vehicleData": {
#                 "vehicleUrl": "abc",
#                 "challanAmount": "1000",
#                 "numberOfChallans": "1",
#                 "plateUrl": "abc",
#                 "regNo": "abc",
#                 "vName": "lnlfkdn"
#             }
#         }
#     }
#     }
# )
# db.child("users").child('4JEMFBw3wodPSv0B1zTKHIIj1Iy1').child(
#     '-LR1Ul18jvB9DBdxPjJt').remove()
# data = db.child("users").child('4JEMFBw3wodPSv0B1zTKHIIj1Iy1').get()
# print(data.val())


if __name__ == '__main__':
    name = str(input('Enter the name of the video: '))
    print(name)
    (vdolength, totalFrames) = videosplit.Launch(str(name))
    print(vdolength, totalFrames)
    # The name of the folder to store the frames of the video
    os.chdir('data')

    result = {}
    result_imag = {}
    # startTime = datetime.now()
    startTime = time.time()
    for f in os.listdir('.'):
        pred, img = Main.main(f)
        if pred in result.keys():
            result[pred] = result[pred] + 1
        elif pred != ' ':
            result[pred] = 1
            result_imag[pred] = img

    # endTime = datetime.now()
    endTime = time.time()
    # Sort the list of number plates by the frequency of their occurance
    l = {x: y for y, x in result.items()}
    r = list(sorted(l.keys()))
    print(l, r)
    index = r[len(r)-1]
    plate = l[index]
    img = result_imag[plate]
    executionTime = "{0:.2f}".format(endTime - startTime)
    print('The name plate is :', plate, ' frequency is: ', result[plate])
    try:
        img = Image.fromarray(img, 'RGB')
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        myimage = buffer.getvalue()
        image_str = base64.b64encode(myimage)
    except:
        print("Problem in displaying license plate")
    print('execution time is : ' + executionTime)

    os.chdir('..')
    licensePlatePath = './LicensePlates/'+name.split('.')[0]+'.jpg'

    with open("/home/sarthak/Desktop/ALPR/data/frame0.jpg", "rb") as f:
        vehicle_str = base64.b64encode(f.read())

    # try:
    #     cv2.imwrite(licensePlatePath, img)
    # except:
    #     print("Problem in writing license plate image")

    # # If u want to see the freqiencies for predictions then uncomment the below 2 lines.
    # """
    # for i in result.keys():
    #     print(i, ' : ', result[i])
    # """
    # # Store the result into mongodb
    # try:
    #     col = mongo_connection()
    #     dict = {}
    #     dict['date and time'] = time.ctime()
    #     dict['video'] = name
    #     dict['video length'] = vdolength
    #     dict['image'] = plate
    #     dict['Total Frames in video'] = totalFrames
    #     dict['execution_time'] = executionTime
    #     dict['frequency ratio'] = "{0:.2f}".format(result[plate] / len(result))

    #     col.insert(dict)
    # except Exception as e:
    #     print(e)


db.child("users").child('FZoKe9vd9wTRbGqXd9JDzBWlnwG3').child("vehicles").update(
    {plate:
        {"vehicleData": {
            "vehicleUrl": vehicle_str.decode("utf-8"),
            "challanAmount": "1000",
            "numberOfChallans": "1",
            "plateUrl": image_str.decode("utf-8"),
            "regNo": plate,
            "vName": "abcd"}
         }
     }
)


data = db.child("users").child('FZoKe9vd9wTRbGqXd9JDzBWlnwG3').child(
    'vehicles').get()
print(data.val())
