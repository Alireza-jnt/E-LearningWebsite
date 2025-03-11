import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from course.models.course_models import Author

user_model = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # role = serializers.SerializerMethodField() # many=True, read_only=True, source='get_role'
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {
        #     'password': {'write_only': True, 'min_length': 5}
        # }


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = '__all__'  # ['username', 'email', 'password', 'password2', 'gender' ,'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'read_only': True},
            'mobile': {'read_only': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        # Check if the username contains only English letters, numbers, and underscores
        elif not re.match(r'^[A-Za-z0-9_]+$', attrs['username']):
            raise serializers.ValidationError(
                "Username can only contain English letters, numbers, and underscores.")
        # Ensure no spaces in username
        elif ' ' in attrs['username']:
            raise serializers.ValidationError("Username cannot contain spaces.")

        # Check if the username contains at least 3 words
        elif len(attrs['username'].split('_')) < 3:
            raise serializers.ValidationError("Username must contain at least 3 words separated by underscores.")

        return attrs

    def create(self, validated_data):
        default_role = Role.objects.get(id=3)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            role=default_role
        )
        return user

    def update(self, instance, validated_data):
        # 🔹 Prevent email or mobile update directly
        if 'email' in validated_data or 'mobile' in validated_data:
            raise serializers.ValidationError(
                "You cannot directly update your email or mobile. A request for approval has been sent."
            )
        return super().update(instance, validated_data)


class UserCourseRegistrationSerializer(serializers.Serializer):
    class Meta:
        model = User,
        fields = '__all__'  # ['username', 'email', 'password', 'password2', 'gender' ,'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'read_only': True},
            'mobile': {'read_only': True},
        }


class UserProfileSerializer(serializers.ModelSerializer):
    street_number = serializers.CharField(source='userinformation.street_number', required=False, allow_null=True)
    street_name = serializers.CharField(source='userinformation.street_name', required=False, allow_null=True)
    state = serializers.CharField(source='userinformation.state', required=False, allow_null=True)
    profile_picture = serializers.ImageField(source='userinformation.profile_picture', required=False, allow_null=True)
    dark_mode = serializers.BooleanField(source='userinformation.dark_mode', required=False)
    language = serializers.CharField(source='userinformation.language', required=False)
    author_bio = serializers.CharField(source='author.bio', required=False, allow_null=True, read_only=True)
    author_approval_status = serializers.CharField(source='author.approval_status', required=False, read_only=True)
    author_rejection_reason = serializers.CharField(source='author.rejection_reason', required=False, read_only=True)
    role_name = serializers.CharField(source='role.role_name', read_only=True)

    class Meta:
        model = User
        fields = [
            'last_login', 'is_superuser', 'is_staff', 'username',
            'first_name', 'email', 'mobile', 'is_deleted', 'is_active',
            'last_name', 'role', 'role_name', 'street_number', 'street_name',
            'state', 'profile_picture', 'dark_mode', 'language',
            'author_bio', 'author_approval_status', 'author_rejection_reason'
        ]
        read_only_fields = ['email', 'mobile', 'is_superuser', 'is_staff',
                            'is_deleted', 'is_active', 'role', 'last_login']

    def update(self, instance, validated_data):
        # Handle UserInformation fields
        user_info_data = {}
        for field in ['street_number', 'street_name', 'state', 'profile_picture', 'dark_mode', 'language']:
            if f'userinformation.{field}' in validated_data:
                user_info_data[field] = validated_data.pop(f'userinformation.{field}')

        if user_info_data:
            user_info, created = UserInformation.objects.get_or_create(user=instance)
            for field, value in user_info_data.items():
                setattr(user_info, field, value)
            user_info.save()

        # Handle Author fields if user is an author
        if hasattr(instance, 'author') and 'author.bio' in validated_data:
            instance.author.bio = validated_data.pop('author.bio')
            instance.author.save()

        # Update User fields
        return super().update(instance, validated_data)