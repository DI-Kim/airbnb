from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer
from categories.models import Category


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(
                AmenitySerializer(amenity).data,
            )
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(
            amenity,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(
                AmenitySerializer(updated_amenity).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 유저가 검증되었다면
        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                #! category
                # category는 serializer에서 검증을 해주지 않기 때문에 직접 해야한다.
                category_pk = request.data.get("category")
                # pk가 없다면(category를 입력하지 않음) raise error
                if not category_pk:
                    raise ParseError("Category is required.")
                try:
                    # category를 가져옴
                    category = Category.objects.get(pk=category_pk)
                    # category가 experience라면 raise error
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError("Category kind should be 'rooms'")
                # 카테고리가 존재하지 않으면 raise error
                except Category.DoesNotExist:
                    raise ParseError("Category not found")

                #! save()안에 파라미터를 넣어주면, serializer에서 create 함수의 validated_data 파라미터에 포함된다.(이는 put에서 불러오는 update 함수도 마찬가지)
                room = serializer.save(
                    #! user
                    owner=request.user,
                    category=category,
                )

                #! amenities
                # ManyToManyField와 Foriegn Key와는 저장(삭제) 방법이 다르다.
                # amenities를 추가하기 전에 이미 방은 만들어진다. amenity에 문제가 발생하면 parseError로 이후의 모든 amenity가 저장이 안되는데 이에 대한 해결책
                # 1. 문제가 있는 amenity만 제외하고 저장한다.
                # 2. 룸을 삭제하고(room.delete() user가 처음부터 다시 방을 만들도록 시킨다.
                amenities = request.data.get("amenities")
                for amenity_pk in amenities:
                    try:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                    except Amenity.DoesNotExist:
                        raise ParseError(f"Amenity with pk {amenity_pk} not found")
                    room.amenities.add(amenity)

                serializer = RoomDetailSerializer(room)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)
