from django.db import models
import uuid

class School(models.Model):
     id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
     school_name = models.TextField(max_length=30)
     admin_name = models.TextField(max_length=30)
     admin_email = models.TextField(max_length=30)
     
     def __str__(self):
        return self.school_name # this 'name' field must be exist in your model.