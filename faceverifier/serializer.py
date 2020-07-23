from rest_framework import serializers


class UploadedImageSerializer(serializers.Serializer):
    email_Id = serializers.CharField(max_length=50)
    client_Id = serializers.IntegerField()
    apiKey = serializers.CharField(max_length=25)
    image = serializers.FileField()
    class Meta:
        fields = ('pk', 'clientId', 'apiKey', 'image')
