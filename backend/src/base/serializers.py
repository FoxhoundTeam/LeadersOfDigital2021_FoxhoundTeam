import json
from src.base.models import (
    Level, 
    Task,
    TaskAttempt,
    Test,
    TestTask,
    TestAttempt,
    TeoryInfo,
    UserAnswer,
)
from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class TaskSeializer(serializers.ModelSerializer):
    task = serializers.JSONField()
    level = LevelSerializer(read_only=True)
    level_id = serializers.IntegerField()
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['task'] = instance.task_value
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context['view'].action == 'list':
            self.fields.pop('task')

class TaskAttemptSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    score = serializers.FloatField(read_only=True)
    track = serializers.JSONField()
    class Meta:
        model = TaskAttempt
        fields = [
            'id',
            'type',
            'dttm_start',
            'dttm_end',
            'task_id',
            'track',
            'score',
        ]

    def create(self, validated_data):

        task = Task.objects.get(pk=validated_data['task_id'])

        data = task.task_value # то с чем сравнивать

        data_to_score = validated_data['track'] # пользовательский трек

        score = 0 # сюда записать результат сравнения


        validated_data['score'] = score

        return super().create(validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['track'] = json.loads(instance.track)
        return data

class TestSerializer(serializers.ModelSerializer):
        model = Test
        fields = '__all__'
    
class UserSerializer(UserDetailsSerializer):
    class Meta:
        fields = list(UserDetailsSerializer.Meta.fields) + ['is_admin']
        model = UserDetailsSerializer.Meta.model

class TeoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TeoryInfo

class ChartSerializer(serializers.Serializer):
    dt_from = serializers.DateField()
    dt_to = serializers.DateField()