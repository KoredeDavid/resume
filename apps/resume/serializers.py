from rest_framework import serializers

class MailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    from_email = serializers.EmailField(max_length=250)
    content = serializers.CharField(max_length=2000)



