from django.db import models


#  this class gives the component names and cost of each component
class RecipeName(models.Model):
    recipe_type = models.CharField(default="NORR", max_length=16)
    ref_number = models.CharField(max_length=16)
    rank = models.CharField(max_length=16)
    component_1 = models.CharField(max_length=16)
    component_2 = models.CharField(max_length=16)
    component_3 = models.CharField(max_length=16)
    component_4 = models.CharField(max_length=16)
    component_5 = models.CharField(max_length=16)
    component_6 = models.CharField(max_length=16)
    cost_component_1 = models.FloatField()
    cost_component_2 = models.FloatField()
    cost_component_3 = models.FloatField()
    cost_component_4 = models.FloatField()
    cost_component_5 = models.FloatField()
    cost_component_6 = models.FloatField()

    def __str__(self):
        return f"{self.recipe_type} {self.ref_number}"