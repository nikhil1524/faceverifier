from rest_framework import serializers


class UploadedImageSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    clientId = serializers.IntegerField()
    apiKey = serializers.CharField(max_length=25)
    image = serializers.FileField()
    class Meta:
        fields = ('pk', 'clientId', 'apiKey','image' )
