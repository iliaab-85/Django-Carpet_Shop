from rest_framework import serializers
from Store.models import Add_Product
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Add_Product
        fields = "__all__"