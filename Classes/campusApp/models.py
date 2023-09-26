from django.db import models


# Create your models here.
# creates model of university classes
class UniversityCampus(models.Model):
    # campus name (string value)
    Campus_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    # state (string value)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    # campus id (integer value)
    Campus_id = models.IntegerField(default="", blank=True, null=False)

    # creates model manager
    object = models.Manager()

    # displays the object output values in the form of a string
    def __str__(self):
        # returns the input value of the campus and state
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.Campus_Name}: {0.State}'
        return display_campus.format(self)

    # removes added 's' that Django adds to te model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
