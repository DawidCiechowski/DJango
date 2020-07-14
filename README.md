# Personal Blog using DJango

## Table of Contents

- [ Introduction ](#intro)
- [ Technologies ](#tech)
- [ How It works](#how)

<a name="intro"></a>
## Introduction

A project revolving around learning the basics of HTML and DJango framework for website development and back-end handling. Project also uses BootStrap to make the general
outlook of the website look better.

<a name="tech"></a>
##Technologies

- Python
- DJango Framework
- BootStrap
- HTML
- CSS

<a name="how"></a>
##How it works

By downloading the repository, the personal development server can be run via DJango Framework. 

DJango Framework must be available in order to ensure that the website will run.

To downlaod it run:

```
$ python -m pip install django
```
Pip will automatically download all the necessary dependencies, which will be necessary for running django applications on your computer.

DJango uses it's own internalised model for handling the backend of the applciation, redirects, admin handling and databases, hence the engienieer using it will have easier time
developing the website. 

### Handling Views

By using DJango built in features, the rendering and routing has been made quite easy by defining a list of [ URL patterns ](#urls), with associated [ functions ](#funcs) that
define an action, which should be taken upon routing to new URL.

<a name="urls"></a>
URL Patterns

```
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]
```

<a name="funcs"></a>
Example Functions

```
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')
```

### Database and Models

By default DJango framework use SQLite as the database, which can of course be changed. In order to interact with the database, a [ model ](#model) can be created to define the fields, 
which will represent the scope of particular model. 

```
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length = 2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
```
