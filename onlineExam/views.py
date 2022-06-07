from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from gradesApp.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from deepface import DeepFace
import cv2
from PIL import Image


def FirstPage(request):
    return render(request, 'onlineExam/firstPage.html', context={})



@login_required
def FaceRecognition(request):
    current_user = UserProfile.objects.get(user=request.user)

    x = 'media/' + str(current_user.profile_pic)
    print(x)

    img1 = cv2.imread(x)

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Face Recognition")

    img_counter = 0
    res = 0

    while True:
        ret, frame = cam.read()

        if not ret:
            print("Failed to capture image")
            break

        cv2.imshow("test", frame)

        k = cv2.waitKey(1)

        if k%256 == 27:
             print("escape hit")
             break


        elif k%256 == 32:
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            img_counter+=1

            img2 = cv2.imread(img_name)


            result = DeepFace.verify(img1, img2)
            res = result['distance']

            if result['distance']<0.30:
                print(result['distance'])
                print("Matched")
            else:
                print(result['distance'])
                print("Not Matched")

    cam.release()

    verified = False

    if res<=0.3:
        verified = True

    return render(request, 'onlineExam/verifiedPage.html', context={
        'current_user': current_user,
        'result': res,
        'verified': verified
    })
