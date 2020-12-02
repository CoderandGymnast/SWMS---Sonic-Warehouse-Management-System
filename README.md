# QR/Bar Decoder:

## I. Guides:
### I.1. Django setup for Socket.IO:
* [WSGI](https://github.com/miguelgrinberg/python-socketio/blob/master/examples/server/wsgi/django_example/django_example/wsgi.py).

## II. Errors: 
1. "RuntimeError: You need to use the eventlet server. See the Deployment secti
on of the documentation for more information.":

2. "GET http://...:.../socket.io/EIO=3&transport=polling&t=142197415699051 404 (NOT FOUND)":
**Reason**: Must set up the Socket.IO server at the file **wsgi.py**.

3. "...\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type bytes is not JSON serializable":
**Reason**: 
```python
# Socket.IO could not read the return value of "pyzbar.decode(image)".
if barcodes:
	sio.emit("Barcodes", {"data": barcodes})
```

4. "TypeError: 'set' object is not subscriptable":
**Reason**:
```python
static_files = {  
	f"{re.sub(r'/$', '', settings.STATIC_URL)}",
}
```

**Solution**: 
```python
static_files = {  
	f"{re.sub(r'/$', '', settings.STATIC_URL)}": settings.STATIC_ROOT,
}
```

5. "django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.":
**Reason**: Issue this command in the default Python console.
```python
from django.contrib.auth.models import User
```
**Solution**: 
```commandline
python manage.py shell
```
```python
from django.contrib.auth.models import User
```

6. "Reverse for 'login' not found. 'login' is not a valid view function or pattern name.":
**Reason**: 
```python
path('accounts/login/', views.LoginView.as_view())
```
**Solution**: 
```python
path('accounts/login/', views.LoginView.as_view(), name="login")
```

7. Could not play videos created by OpenCV: 
**Reason**: Video - Writing thread is corrupted.

## III. Tricks: 
1. Remove permissions: 
```python
for p in Permission.objects.filter(name__startswith="CRUD"):
    p.delete()
```

## IV. Design References: 
1. [freshdesignweb.com](https://freshdesignweb.com/free-css-tables/)
