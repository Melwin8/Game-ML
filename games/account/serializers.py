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

# class QuestionSerializer(serializers.Serializer):
#     LEVEL_CHOICES = [
#         ('beginner', 'Beginner'),
#         ('medium', 'Medium'),
#         ('expert', 'Expert'),
#     ]

#     id = serializers.IntegerField()
#     question = serializers.CharField()
#     level = serializers.ChoiceField(choices=LEVEL_CHOICES)
#     game_state = serializers.BooleanField(default=True)

#     def create(self, validated_data):
#         # Not needed for a serializer without a model
#         pass

#     def update(self, instance, validated_data):
#         # Not needed for a serializer without a model
#         pass

#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         if ret.get('game_state', False):  # Check if game_state is True
#             ret['level'] = self.fields['level'].disabled  # Disable the level field
#         return ret
    
# class AnswerSerializer(serializers.Serializer):
#     answer = serializers.CharField(max_length=100)    


class LevelChoiceSerializer(serializers.Serializer):
    level_choices = [
        ("beginner", "Beginner"),
        ("medium", "Medium"),
        ("expert", "Expert"),
    ]
    level = serializers.ChoiceField(choices=level_choices)

class AnswerSerializer(serializers.Serializer):
    answer = serializers.CharField(max_length=255)
    start_quiz = serializers.BooleanField(default=True)
    
# class ScoreSerializer(serializers.Serializer):
#     score = serializers.IntegerField()


class BoggleInputSerializer(serializers.Serializer):
    player_words = serializers.CharField(max_length=255)
