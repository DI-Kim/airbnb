from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(read_only=True)

    # **validation_data는
    # {"name": "Category from DRF", "kind": "rooms"} 딕셔너리를
    # name='Category from DRF'
    # kind='rooms'
    # 로 바꿔줌
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # get 은 {} 에서 쓰이는 메소드로 첫번째 parameter를 key로 찾지 못하면 두번째 parameter의 값을 반환
        instance.name = validated_data.get("name", instance.name)
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()
        return instance
