from django.shortcuts import render
from .models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer


# serializer 사용밥
# GET: 첫번째 parameter로 db에서 넘어오는 django 객체를 넘겨줌
# POST: 유저가 보낸 데이터를 data parameter로 넘겨줌
@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            return Response({"created": True})
        else:
            return Response(serializer.errors)


# {
#     "name": "Category from DRF",
#     "kind": "rooms"
# }


@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
