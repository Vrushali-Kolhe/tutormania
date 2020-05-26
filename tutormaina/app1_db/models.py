from django.db import models
from datetime import datetime


class Department(models.Model):
    department_name = models.CharField(max_length=200)
    department_slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = "departments"

    def __str__(self):
        return self.department_name


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_outcome = models.CharField(max_length=200)
    course_slug = models.SlugField(max_length=200)
    course_credit = models.IntegerField()
    department_name = models.ForeignKey(Department, default=1, verbose_name = "department", on_delete=models.SET_DEFAULT)


    class Meta :
        verbose_name_plural = "courses"

    def __str__(self):
        return self.course_name


class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_info = models.CharField(max_length=200)
    author_slug = models.SlugField(max_length=200)
    course_name = models.ForeignKey(Course, default=1, verbose_name="course", on_delete=models.SET_DEFAULT)
    department_name = models.ForeignKey(Department, default=1, verbose_name="department", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "authors"

    def __str__(self):
        return self.author_name


class Topic(models.Model):
    topic_title = models.CharField(max_length=200)
    topic_content = models.TextField()
    topic_slug = models.SlugField(max_length=200)
    topic_published = models.DateTimeField("date published", default= datetime.now())
    topic_summary = models.CharField(max_length=200)
    author_name = models.ForeignKey(Author, default=1, verbose_name="author", on_delete=models.SET_DEFAULT)
    course_name = models.ForeignKey(Course, default=1, verbose_name="course", on_delete=models.SET_DEFAULT)


    def __str__(self):
        return self.topic_title
