from rest_framework import serializers
from .models import listItem


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = listItem
		fields = ('id','title','content', 'status')