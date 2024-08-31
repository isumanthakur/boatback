import os
import django
from django.contrib.auth import get_user_model

# Set up the Django settings environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobnb_backend.settings')

# Set up Django
django.setup()

# Create superuser
User = get_user_model()

if not User.objects.filter(username='testadmin').exists():
    User.objects.create_superuser('testadmin', 'admintest@example.com', 'testadminpassword123')
    print('Superuser created.')
else:
    print('Superuser already exists.')
