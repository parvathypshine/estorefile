from rest_framework import serializers
from api.models import Reviews,Books,Cart
from django.contrib.auth.models import User
class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    author=serializers.CharField()
    publisher=serializers.CharField()
    qty=serializers.IntegerField()

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get("name")
        instance.author = validated_data.get("author")
        instance.price = validated_data.get("price")
        instance.publisher = validated_data.get("publisher")
        instance.qty = validated_data.get("qty")
        instance.save()
        return instance

    def validate(self, data):
        qty = data.get("qty")
        price = data.get("price")

        if qty not in range(50, 1000):
            raise serializers.ValidationError("invalid qty")
        if price not in range(50, 1000):
            raise serializers.ValidationError("invalid price")
        return data
        # price=data.get("price")


class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"
            # ["book","user","comment","rating"]
        # exclude=("created_date",)

        # def validate(self,data):
        #     qty=data.get("qty")
        #     if qty not in range(50,1000):
        #         raise serializers.ValidationError("invalid qty")
        #     if price not in range(50,1000):
        #         raise serializers.ValidationError("invalid price")
        #     return data
        #     # price=data.get("price")
#  viewset and modelview set put and post is not working.... 21 and 22 date vheck

#check put method of viewset
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name',"username",'email','password']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class CartSerializer(serializers.ModelSerializer):
        book=serializers.CharField(read_only=True)
        user=serializers.CharField(read_only=True)
        status=serializers.CharField(read_only=True)
        class Meta:
            model=Cart
            fields=['book','user','status']