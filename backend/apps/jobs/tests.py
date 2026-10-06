import pytest
from django.contrib.auth import get_user_model
from .models import Job,Application
@pytest.mark.django_db
def test_duplicate_application_is_blocked():
    u=get_user_model().objects.create_user(username='test',password='x'); j=Job.objects.create(user=u,company='Acme',title='Engineer',description='Python')
    Application.objects.create(user=u,job=j)
    with pytest.raises(Exception): Application.objects.create(user=u,job=j)
