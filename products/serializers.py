from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField()
    price = serializers.FloatField()
    image = serializers.ImageField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.price = validated_data.get('price',instance.price)
        instance.save()
        return instance

    