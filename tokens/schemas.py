from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenObtainPairResponseSerializer(TokenObtainPairSerializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
