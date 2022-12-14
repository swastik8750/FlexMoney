from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import EnrolledBatches, User
from django.shortcuts import render,redirect, HttpResponse
from .serializers import EnrolledBatchesSerializer, UserSerializer
from django.contrib import messages
from datetime import datetime,date
def current_age(bday,d):
    bday = str(bday)
    bday = datetime.strptime(bday, '%Y-%m-%d')
    temp= int(d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))
    # print(temp)
    if temp<=0:
        return 0
    else:
        return temp
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,'signup.html')

def signupuser(request):
    if request.method=='POST':
        fname = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        dob = request.POST.get('dob')
        print(dob)
        phone = request.POST.get('phone')
        
        if password != cpassword:
            messages.error(request,'Both Password are different')
            return redirect('signupuser')

        if User.objects.filter(email=email).exists():
            print("error")
            messages.error(request,'USER ALREADY EXIST! Please Login')
            mess = {'abcd':'USER ALREADY EXIST! Please Login'}
            return redirect('signupuser')
        else:
            obj = User.objects.create_user(username=email,email=email,password=password, name=fname, dob=dob,phone=phone)
            obj.save()
            obj2= User.objects.get(email =email)
            print(obj2.dob)
            user=authenticate(username=email,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                return redirect('userlogin')
    else:
        return redirect('index')

def signinuser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method=='POST':
            username= request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,'Username or Password is Incorrect')
                return redirect('userlogin')
        return render(request,'login.html')
    


def enrollnow(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method=='POST':
        if not request.user.is_authenticated:
            return redirect('index')
        user = User.objects.get(username=request.user)

        batch = request.POST.get('batch')
        date = request.POST.get('date')
        date = str(date)
        date = datetime.strptime(date, '%Y-%m-%d')
        if current_age(user.dob,date)<18 or current_age(user.dob,date)>65:
            messages.error(request,"You are not in the age of 18-65 on "+ str(date))
            return redirect('dashboard')
        enrolledbatches = EnrolledBatches.objects.filter(user=user)
        print(enrolledbatches)
        flag=0
        for x in enrolledbatches:
            if x.month.month==date.month and x.month.year==date.year:
                flag=1
                messages.error(request,'You are already enrolled for the selected month')
                break       
        if flag==0:
            obj = EnrolledBatches(user=user,batch=batch,month=date)
            obj.save()
        return redirect('dashboard')

def dashboard(request):
    if request.user.is_authenticated:
        enrolled_batches = EnrolledBatches.objects.filter(user = request.user)
        context  = {'enrolled_batched':enrolled_batches}
        for x in enrolled_batches:
            print(x.batch)
            print(x.month)
        print(context)
        return render(request, 'dashboard.html',{'enrolled_batched':enrolled_batches})
    return redirect('index')

def logoutuser(request):
    logout(request)
    return redirect('index')


# Create API views for Enpoint calling.
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def loginuser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.data['name'],
                password=serializer.data['password']
            )
            if user is not None:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {'error': 'Invalid credentials'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def generate_auth_token(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )

def enrolled_batches(request):
    if request.method == 'GET':
        enrolled_batches = EnrolledBatches.objects.all()
        serializer = EnrolledBatchesSerializer(enrolled_batches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)