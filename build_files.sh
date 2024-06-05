# Install dependencies
pip install -r requirements.txt

# Run Python commands
python manage.py collectstatic --noinput
python manage.py migrate