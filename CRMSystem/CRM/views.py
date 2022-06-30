from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegisterSerializer, UserSerializer,EnquiryFormSerializer
from .models import EnquiryForm, User,claimedEmployee
from django.contrib.auth import login
from django.shortcuts import render, redirect 
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.http import HttpResponseRedirect,HttpResponse
from knox.views import LoginView as KnoxLoginView
from django.contrib import messages
from rest_framework import serializers
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data
        })
class EnquiryAPI(generics.GenericAPIView):
    serializer_class = EnquiryFormSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        enquiry = serializer.save()
        return Response({
        "enquiry": EnquiryFormSerializer(enquiry, context=self.get_serializer_context()).data
        })
global us
def login(request):
    global p2
    if request.method == 'POST':
        email = request.POST['email']
        password =request.POST['password']
        x=User.objects.all()
        for i in x:
            p2=0
            if i.username==email and i.password==password:
                p1=1
                us=i.username
                return redirect('home')
        if(p2!=1):
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
    
    return render(request, "accounts/login.html")

def home(request):
    enquiry = EnquiryForm.objects.all()
    print(enquiry)
    return render(request,'accounts/home.html',{'enquiry':enquiry})

def hide(request):
    if request.method == 'POST':
        id = request.POST['id']
    ins = EnquiryForm.objects.get(Id=id)
    print(ins,"0000")
    p = claimedEmployee(cuser=ins)
    print(p)
    p.save()
    ins.delete()
    enquiry = EnquiryForm.objects.all()
    return render(request,'accounts/home.html',{'enquiry':enquiry})


    







