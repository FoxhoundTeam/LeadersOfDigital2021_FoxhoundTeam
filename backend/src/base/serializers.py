import json
from math import sqrt

from src.base.models import (
    Level,
    Task,
    TaskAttempt,
    Test,
    TestAttempt,
    TeoryInfo,
)
from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class TrackPoint:
    def __init__(
            self,
            x,
            y,
            z,
            time
    ):
        self.x = x
        self.y = y
        self.z = z
        self.time = time

    @staticmethod
    def from_dict(dict_obj: dict) -> 'TrackPoint':
        x = dict_obj['x']
        y = dict_obj['y']
        z = dict_obj['z']
        time = dict_obj['t']
        return TrackPoint(
            x=x,
            y=y,
            z=z,
            time=time
        )


class Result:
    def __init__(
            self,
            marks,
            Rras,
            Tras,
    ):
        self.marks = marks
        self.Rras = Rras
        self.Tras = Tras


class Criteria:
    def __init__(
            self
    ):
        self.x = None
        self.y = None
        self.z = None
        self.time = None
        self.command = None
        self.radius = None
        self.type = None

    @staticmethod
    def from_dict(dict_obj: dict) -> 'Criteria':
        obj = Criteria()
        obj.x = dict_obj.get('x')
        obj.y = dict_obj.get('y')
        obj.z = dict_obj.get('z')
        obj.time = dict_obj.get('t')
        obj.command = dict_obj.get('command')
        obj.radius = dict_obj.get('r')
        obj.type = dict_obj.get('type')
        return obj


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
            'user',
        ]

    def create(self, validated_data):

        task = Task.objects.get(pk=validated_data['task_id'])

        data = task.task_value  # то с чем сравнивать

        data_to_score = validated_data['track']  # пользовательский трек

        tracks = []
        criterials = []
        results = []
        for track in data_to_score:
            tracks.append(TrackPoint.from_dict(track))

        for criteria in data:
            criterials.append(Criteria.from_dict(criteria))

        for criteria in criterials:
            if criteria.type == 'waypoint' and criteria.time is not None:
                for track in tracks:
                    lenght = sqrt((criteria.x - track.x) ** 2 + (criteria.y - track.y) ** 2)
                    if lenght <= criteria.radius * 2 and criteria.time <= track.time * 1.5:
                        Rras = (lenght / criteria.radius) - 1

                        if Rras < 0:
                            Kr = 1
                        elif Rras > 1:
                            Kr = 0
                        else:
                            Kr = Rras

                        Tras = ((lenght / criteria.radius) - 0.5) * 2

                        if Tras < 0:
                            Tr = 1
                        elif Rras > 1:
                            Tr = 0
                        else:
                            Tr = Tras
                        results.append(Result(10 * Kr * Tr, Kr, Tr))
                        break
            if criteria.type == 'waypoint_command' and criteria.time is not None:
                for track in tracks:
                    lenght = sqrt((criteria.x - track.x) ** 2 + (criteria.y - track.y) ** 2)
                    if lenght <= criteria.radius * 2 and criteria.time <= track.time * 1.5 and criteria.command is not None:
                        Rras = (lenght / criteria.radius) - 1

                        if Rras < 0:
                            Kr = 1
                        elif Rras > 1:
                            Kr = 0
                        else:
                            Kr = Rras

                        Tras = ((lenght / criteria.radius) - 0.5) * 2

                        if Tras < 0:
                            Tr = 1
                        elif Rras > 1:
                            Tr = 0
                        else:
                            Tr = Tras
                        results.append(Result(10 * Kr * Tr, Kr, Tr))
                        break
        score = sum([i.marks for i in results])
        validated_data['score'] = score

        return super().create(validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['track'] = json.loads(instance.track)
        return data


class TestSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()

    class Meta:
        model = Test
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['data'] = instance.data_value
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context['view'].action == 'list':
            self.fields.pop('data')


class UserSerializer(UserDetailsSerializer):
    class Meta:
        fields = list(UserDetailsSerializer.Meta.fields) + ['is_admin']
        model = UserDetailsSerializer.Meta.model


class TeoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = TeoryInfo


class TestAttemptSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        fields = '__all__'
        model = TestAttempt


class ChartSerializer(serializers.Serializer):
    dt_from = serializers.DateField()
    dt_to = serializers.DateField()
