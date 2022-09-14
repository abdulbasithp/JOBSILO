from django.db import models


class EducationLevel(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class EducationCourse(models.Model):
    level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class EducationSpecialisation(models.Model):
    course = models.ForeignKey(EducationCourse, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
