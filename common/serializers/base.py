from rest_framework import serializers

from common.utils import validate_using_model_clean


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        abstract = True
        read_only_fields = ["id", "created_at", "updated_at"]
        fields = read_only_fields

    def validate(self, attrs):
        """
        model validation for serializer.
        """
        validated_attrs = super(BaseModelSerializer, self).validate(attrs)
        instance = getattr(self, "instance", None)
        return validate_using_model_clean(
            validated_attrs, instance, self.Meta.model, self._get_m2m_fields()
        )

    def _get_m2m_fields(self):
        """
        Should return m2m fields in the model.
        Used for validating values with model validation rules
        """
        return []
