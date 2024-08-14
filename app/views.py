from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Professor,Course,Room,Group,Class,Year_student
from .serializer import ProfessorSerializer , CourseSerializer ,RoomSerializer,GroupSerializer ,ClassSerializer ,Year_studentSerializer
from rest_framework.response import Response


class RoomView(APIView):
    def get(self,request):
        output = [{'name':output.name}
                  for output in Room.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


#############################################################################


class CourseView(APIView):
    def get(self,request):
        output = [{'name':output.name,
                   'year':output.year}
                  for output in Course.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


#######################################################################
class ProfessorView(APIView):
    def get(self,request):
        output = [{'first_name':output.first_name,
                   'last_name':output.last_name,
                   'email':output.email,
                   'email_second':output.email_second,
                   'password':output.password
                   }
                  for output in Professor.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
##################################################################3



class GroupView(APIView):
    def get(self,request):
        output = [{'name':output.name,
                   'size':output.size}
                  for output in Group.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


#############################################################################

class ClassView(APIView):
    def get(self,request):
        output = [{'professor':output.professor,
                   'course ':output.course ,
                   'duration':output.duration,
                   'group ':output.group,
                   'lab':output.lab,
                   'session':output.session}
                  for output in Class.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer = ClassSerializer (data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



#############################################################################


class Year_studentView(APIView):
    def get(self,request):
        output = [{'name_collage':output.name_collage,
                   'current_year ':output.current_year

                   }
                  for output in Year_student.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer = Year_studentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
######################################################################################
class courseview2(APIView):
    def get(self,request):
        output = [{'name':output.name,
                   'year':output.year,
                    'professor':output.professor,
                   'session':output.session,
                   'Mr':output.Mr,
                   'duration':output.duration}
                  for output in Course.objects.all()]
        return Response(output)
    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
   
