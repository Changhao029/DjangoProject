import json

from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from rest_framework.response import Response
from mysite import models


# class IndexView(View):
#     """
#
#     """
#     def get(self, request, *args, **kwargs):
#         data = [
#             {"id": 1, "title": "welcome", "content": "welcome to the sudoku"},
#             {"id": 2, "title": "welcome", "content": "welcome to the sudoku"},
#             {"id": 3, "title": "welcome", "content": "welcome to the sudoku"},
#             {"id": 4, "title": "welcome", "content": "welcome to the sudoku"},
#             {"id": 5, "title": "welcome", "content": "welcome to the sudoku"},
#         ]
#         return JsonResponse(data, safe=False)


class IndexView(APIView):
    """

    """
    def get(self, request, *args, **kwargs):
        data = [
            {"id": 1, "title": "welcome", "content": "welcome to the sudoku"},
            {"id": 2, "title": "welcome", "content": "welcome to the sudoku"},
            {"id": 3, "title": "welcome", "content": "welcome to the sudoku"},
            {"id": 4, "title": "welcome", "content": "welcome to the sudoku"},
            {"id": 5, "title": "welcome", "content": "welcome to the sudoku"},
        ]
        return Response(data)


# def index(request):
#     data = [
#         {"id": 1, "title": "welcome", "content": "welcome to the sudoku"},
#         {"id": 2, "title": "welcome", "content": "welcome to the sudoku"},
#         {"id": 3, "title": "welcome", "content": "welcome to the sudoku"},
#         {"id": 4, "title": "welcome", "content": "welcome to the sudoku"},
#         {"id": 5, "title": "welcome", "content": "welcome to the sudoku"},
#     ]
#     return JsonResponse(data, safe=False)


class DrfCateView(APIView):
    def post(self, request, *args, **kwargs):
        print(json.loads(request.body.decode('utf-8')))
        # in the rest framework, request.data = json.loads(request.body.decode('utf-8'))
        print(request.data)
        # print(request.POST)
        # name = request.POST.get('name')
        # print(name)
        # models.Category.objects.create(title=name)
        return Response("successful")

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            queryset = models.Category.objects.all().values('id', 'title')
            data_list = list(queryset)
            return Response(data_list)
        else:
            queryset = models.Category.objects.filter(id=id).first()
            return Response(model_to_dict(queryset))

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        models.Category.objects.filter(id=id).delete()
        return Response("successful")

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id')
        models.Category.objects.filter(id=id).update(**request.data)
        return Response("successful")



class DrfInfoView(APIView):
    def post(self, request, *args, **kwargs):
        return Response("successful")