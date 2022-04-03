from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Courses, User,CoursesInstances
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from .serializer import CourseSerializer,CourseInstanceSerializer,CourseNamesSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import ensure_csrf_cookie






# Create your views here.
def home(request):
    context = {}
    return render(request,'baseapp/home.html',context)

@api_view(('GET',))
def getcourses(request):
    # data= Courses.objects.all().distinct()
    # data = Courses.objects.distinct()
    # data = Courses.objects.values('pk','courseName','courseFee','courseTeacher','student').distinct()
    # print(data)
    # data = Courses.objects.all().distinct('courseName').order_by('courseName')

    # data = Courses.objects.values().distinct()

    data = CoursesInstances.objects.all()
    serializer = CourseInstanceSerializer(data,many=True)
    return Response(serializer.data)

@ensure_csrf_cookie
def LoginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('baseapp:home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('baseapp:welcome')
        else:
            messages.error(request,'Username or password does not exist')
    context = {'page':page}
    return render(request,'baseapp/register_login.html',context)

def LogoutPage(request):
    logout(request)
    return redirect('baseapp:login')

def register(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = User.objects.create(username=username,email=email,password=password1)
        user.set_password(password1)
        user.save()
        return redirect('baseapp:welcome')

        # form = NewUserForm(request.POST)
        # if form.is_valid():
        #     user = form.save()
        #     login(request,user)
        #     return redirect('baseapp:welcome')
        # else:
        #     messages.error(request,'Unsuccessful registration, Invalid information')
        #     print(form.errors)
    # form = NewUserForm()            
    # return render(request,'baseapp/register_login.html',{'form':form})
    return render(request,'baseapp/register_login.html',{})

@login_required(login_url='baseapp:login')
@ensure_csrf_cookie
def welcome(request):
    userId = request.user.id
    print(userId)
    # courses = Courses.objects.filter(student = userId)
    
    context = {'request':request}
    return render(request,'baseapp/welcome.html',context)  
    
# @method_decorator(csrf_exempt, name='dispatch')
class CourseView(APIView):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(CourseView, self).dispatch(request, *args, **kwargs)

    def post(self,request):
        userID = request.user.id
        request.data['student'] = userID
        data = request.data
        serializer = CourseSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self,request):
        userID = request.user.id
        print(userID)
        data = Courses.objects.filter(student = userID)
        serializer  = CourseSerializer(data,many = True)
      
        return Response(serializer.data)




@api_view(('GET',))
def getCourseNames(request):
    userID = request.user.id
    coursenames = Courses.objects.filter(student = userID).values('courseName')
    # lis = []
    # for i in coursenames:
    #     print(i['courseName'])
    #     lis.append(i['courseName'])
        
    serializer  = CourseNamesSerializer(coursenames,many = True)

    return Response(serializer.data)


# @api_view(('POST',))
# @csrf_exempt
# def postCourse(request):
#     userID = request.user.id
#     request.data['student'] = userID
#     data = request.data
#     serializer = CourseSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)
