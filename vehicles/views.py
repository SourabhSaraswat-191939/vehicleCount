from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pyrebase

config = {
    "apiKey": "AIzaSyCb_nVRQBwoj6Xw-sGwVRybTh-DSsd7Fr8",
    "authDomain": "vehiclecount-57233.firebaseapp.com",
    "projectId": "vehiclecount-57233",
    "storageBucket": "vehiclecount-57233.appspot.com",
    "databaseURL": "https://vehiclecount-57233-default-rtdb.firebaseio.com",
    "messagingSenderId": "734332040551",
    "appId": "1:734332040551:web:9e90b96ffa81b178b3abc2",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

class vehicleData(APIView):
    def post(self,request):
        # name = database.child('data').child('name').get().val()
        # department = database.child('data').child('department').get().val()
        # branch = database.child('data').child('branch').get().val()
        database.child('data').push(data=request.data)
        return Response({"msg":"Your data is successfully saved on Server","status":status.HTTP_200_OK})
        
    def get(self,request):
        all =  database.child('data').get().val()
        return Response(all)