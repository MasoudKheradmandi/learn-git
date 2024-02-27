from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog,Tag
from rest_framework import serializers,status


class ApiIndexView(APIView):
    
    class SerializerInput(serializers.ModelSerializer):
        name = serializers.CharField(max_length=250)
        category = serializers.CharField(max_length=20)
        text = serializers.CharField(max_length=450)
        
    def get(self,request):
        ...
    
    def post(self,request):
        data = Blog.objects.create(name='masoud',category=1,text='Hi')
        serializers = self.SerializerInput(data)
        return serializers.data
    
    


class ApiTag(APIView):
    class InputSerializerTag(serializers.Serializer):
        tag_name = serializers.CharField(max_length=250)

    class SerializerOutput(serializers.Serializer):
        tag_name = serializers.CharField(max_length=250)


    def get(self,request):
        tag = Tag.objects.all()
        serializer = self.SerializerOutput(tag,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.InputSerializerTag(data=request.data)

        if serializer.is_valid():
            tag_name = serializer.validated_data['tag_name']

            Tag.objects.create(tag_name = tag_name)

            return Response({'messages':'its successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def create(self,validated_data):
        return Tag.objects.create(**validated_data)