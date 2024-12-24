from django.shortcuts import render

# Create your views here.

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('images')  # 获取批量上传的图片
        if not files:
            return Response({"detail": "No images uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        image_instances = []
        for file in files:
            image_instance = Image(image=file)
            image_instance.save()
            image_instances.append(image_instance)

        serializer = ImageSerializer(image_instances, many=True)  # many=True 表示这是一个包含多个对象的列表，序列化器将会处理列表中的每个 Image 实例。
        return Response(serializer.data, status=status.HTTP_201_CREATED)

def upload_page(request):
    return render(request, 'upload.html')
    # return render(request, 'upload/templates/upload.html')