from django.db import models


class Projects(models.Model):
    # project name
    name = models.CharField(max_length=255, null=False)
    # project description
    description = models.CharField(max_length=255, null=False)

    def __str__(self):
      return "{} - {}".format(self.name, self.description)
