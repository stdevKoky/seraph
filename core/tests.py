from django.test import TestCase
from .models import Type 
#from ..archangel.wsgi import *
# Create your tests here.

##List
#query = Type.objects.all()
#print(query)


## Insert
#t = Type()
#t.name = "Developoer"
#t.save()

#Type(name="Koky").save()

##Edit
#t = Type.objects.get(id=1)
#t.name = "Developer"
#print(t.name)
#t.save()

##Delete
#t = Type.objects.get(id=2)
#t.delete()


##Filter
objs = Type.objects.filter(name__icontains="Y")
print(objs)
