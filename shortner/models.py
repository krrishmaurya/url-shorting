from django.db import models

 

class Url(models.Model):
    # to take link as an input i.e take url that ha to be shorten 
    link=models.CharField(max_length=10000) 
    # to return the uuid 
    uuid=models.CharField(max_length=100)



# create superuser so that u can manage your database
# after making migration create super user  then go admin.py