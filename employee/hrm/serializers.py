from rest_framework import serializers
from hrm.models import users


class UsersSerializer(serializers.ModelSerializer):

	class Meta:
		model=users
		#fields=('name','employee_id')
		fields='__all__'