import pyrebase

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


data = db.child("users").child('FZoKe9vd9wTRbGqXd9JDzBWlnwG3').child(
    'vehicles').get()
print(data.val())
