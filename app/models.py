from django.db import models

class drink(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    # this adds name to the object, orginally if you would create a new record in the model using admin panel, the name would be 'app_name object 1' but now since we use def __str__(self): return self.name, we get the name we input as the object name. Very useful