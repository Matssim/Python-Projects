from django.db import models

# Creates model of University Campuses
class UniversityCampus(models.Model):
    name = models.CharField(max_length=100, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    # Ties the input id to the auto-generated primary key, so the user can assign
    # an id without corrupting the database
    id = models.IntegerField(primary_key=True)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the campus name to display in the browser.
        # The if statement makes sure to only add 'Campus' to the name if it's
        # not already in the name input
        if 'campus' or 'Campus' in self.name:
            display_campus = '{0.name}'
        else:
            display_campus = '{0.name} Campus'
        return display_campus.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campuses"