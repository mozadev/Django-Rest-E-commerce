from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):

        #custom validation
        if 'ce' in value:
            raise serializers.ValidationError("This name is not allowed")
           
        return value
    
    def validate_email(self, value):
        #custom validation
        if value == '':
            raise serializers.ValidationError("This have to indicate an email")
        
        return value

    def validate(self, data):
        return data

    def create(self, validated_data):
        return User.objects.create(** validated_data) 
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance
      
    





    