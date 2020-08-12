from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Company(models.Model):
    user = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    website = models.CharField(max_length=200, blank=True)
    company_size = models.IntegerField()
    industry = models.CharField(max_length=200)
    overview = models.TextField()

    def __str__(self):
        return self.name
    

class Specialization(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    

class Vacancy(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='vacancy_posts')
    specialization = models.ForeignKey(Specialization, on_delete=models.DO_NOTHING,related_name='vacancy')
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING,related_name='vacancy')
    salary = models.IntegerField()
    area = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    description = models.TextField()
    experience_required = models.IntegerField()
    picture =  models.ImageField(upload_to='jobportal/%Y/%m/%d/')
    created_on = models.DateTimeField(auto_now_add=True)
    expired_on = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title