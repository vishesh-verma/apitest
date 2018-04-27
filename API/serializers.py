from rest_framework import serializers
from API.models import ideator, LANGUAGE_CHOICES, STYLE_CHOICES

class ideatorSerializer(serializers.ModelSerializer):
      class Meta:
           model=ideator
           fields=('id','name','email', 'title','description')

      def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return ideator.objects.create(**validated_data)

      def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
