from typing import Dict


def validate_using_model_clean(attrs: Dict, instance, model, m2m_fields=None):
    if m2m_fields is None:
        m2m_fields = []

    attrs_without_m2m = attrs.copy()
    for m2m_field in m2m_fields:
        if attrs_without_m2m.get(m2m_field, None) is not None:
            attrs_without_m2m.pop(m2m_field)

    if instance is None:
        # api is called to CREATE model instance
        model_instance = model(**attrs_without_m2m)
        model_instance.clean()
    else:
        # api si called to UPDATE model instance
        model_instance = instance
        [setattr(instance, x, attrs_without_m2m[x]) for x in attrs_without_m2m]
        model_instance.clean()

    return attrs
