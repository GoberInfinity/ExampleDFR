import factory

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False

class DataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.Data'
        django_get_or_create = ('transaction_id',)

    transaction_id = factory.Faker('uuid4')
    transaction_date = factory.Faker('date')
    transaction_amount = factory.Faker('pyint')
    client_id = factory.Faker('pyint')
    client_name = factory.Faker('name')
