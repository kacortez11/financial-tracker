from rest_framework.serializers import ModelSerializer

from api.users.models import User


class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

	def create(self, validated_data):
		instance = super().create(validated_data)
		instance.username = validated_data.get('username')
		instance.first_name = validated_data.get('first_name').capitalize()
		instance.last_name = validated_data.get('last_name').capitalize()
		if validated_data.get('display_name') == '':
			instance.display_name = self._build_display_name(
				instance.first_name,
				instance.last_name
			)
		else:
			instance.display_name = validated_data.get('display_name')
		instance.save()

		return instance

	def update(self, instance, validated_data):
		instance.username = validated_data.get('username', instance.username)
		instance.first_name = validated_data.get(
			'first_name',
			instance.first_name
		).capitalize()
		instance.last_name = validated_data.get(
			'last_name',
			instance.last_name
		).capitalize()
		if validated_data.get('display_name') == '':
			instance.display_name = self._build_display_name(
				instance.first_name,
				instance.last_name
			)
		else:
			instance.display_name = validated_data.get('display_name')
		instance.save()

		return instance

	@staticmethod
	def _build_display_name(_fn, _ln):
		return f"{_fn.capitalize()} {_ln.capitalize()}"
