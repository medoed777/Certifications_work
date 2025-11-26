from rest_framework import serializers

from network.models import NetworkNode, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = "__all__"
        read_only_fields = ["debt_to_supplier"]

    def update(self, instance, validated_data):
        validated_data.pop("debt_to_supplier", None)
        return super().update(instance, validated_data)
