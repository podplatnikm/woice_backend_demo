import factory.django
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f"franc_rozman_stane_{n}")
    email = factory.Sequence(lambda n: f"zaho_{n}@nkmaribor.si")
