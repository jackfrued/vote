from rest_framework import serializers

from polls.models import Subject, Teacher


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('no', 'name')


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        exclude = ('subject', )
