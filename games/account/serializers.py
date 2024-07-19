from rest_framework import serializers
from .models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from .gaming import question


class CustomUserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password','password_confirmation')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        try:
            CustomUser.objects.get(email=data['email'])
            raise serializers.ValidationError({'email':'Email already exists.'})
        except ObjectDoesNotExist:
            pass

        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({'password_confirmation':"Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation', None)
        user = CustomUser.objects.create_user(**validated_data)
        return user

    
    
class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': {'Custom message':' No active account found with the given credentials'},
        'blank_username': 'Custom message: Please fill in all required fields.',
    }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # adding custom claims
        token['current_user'] = user.username
        token['is_superuser'] = user.is_superuser
        # print(token)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user.is_superuser==False:
            data["is_superuser"] = user.is_superuser
            data["current_user"] = user.username
    
            return data
        else:
            raise serializers.ValidationError("Only commom users are allowed to log in here.")


class LevelChoiceSerializer(serializers.Serializer):
    level = serializers.ChoiceField(choices=[('beginner', 'Beginner'), ('medium', 'Medium'), ('expert', 'Expert')])

class AnswerSerializer(serializers.Serializer):
    answer = serializers.CharField(max_length=255, required=True)

class BoggleGameSerializer(serializers.Serializer):
    guessed_words = serializers.ListField(child=serializers.CharField(max_length=50), allow_empty=False)


class WordShuffleSerializer(serializers.Serializer):
    difficulty = serializers.ChoiceField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], required=True)
    guess = serializers.CharField(max_length=100, required=False)
    original_word = serializers.CharField(max_length=100, required=False)
    shuffled_word = serializers.CharField(max_length=100, required=False)
    level = serializers.IntegerField(required=False)
    score = serializers.IntegerField(required=False)
    message = serializers.CharField(max_length=255, required=False)
    
class TranslateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000)
    target_language = serializers.CharField(default='en')     