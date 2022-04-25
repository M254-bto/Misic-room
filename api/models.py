from django.db import models
import string, random


#code generator
def random_code():

        length = 6
        while True:
            code = "".join(random.choices(string.ascii_uppercase, k = length))
           
            return code


class Room(models.Model):
    
    code = models.CharField(max_length=10, default="random_code()", null=False, unique=True)
    host = models.CharField(max_length=100, null=False, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(default=1, null=False)
    created = models.DateField(auto_now_add=True)
