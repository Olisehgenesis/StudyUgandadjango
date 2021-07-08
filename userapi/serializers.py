from rest_framework import serializers
from userapi.models import User, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('title', 'dob', 'email', 'school', 'level', 'phone')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

def create(self, validated_data):
    profile_data = validated_data.pop('profile')
    password = validated_data.pop('password')
    user = User(**validated_data)
    user.set_password(password)
    user.save()
    UserProfile.objects.create(user=user, **profile_data)
    return user

def update(self, instance, validated_data):
    profile_data = validated_data.pop('profile')
    profile = instance.profile

    instance.email = validated_data.get('email', instance.email)
    instance.save()

    profile.title = profile_data.get('title', profile.title)
    profile.dob = profile_data.get('dob', profile.dob)
    profile.email = profile_data.get('email', profile.email)
    profile.school = profile_data.get('school', profile.school)
    profile.level = profile_data.get('level', profile.level)
    profile.phone = profile_data.get('phone', profile.phone)
    profile.save()
    return instance