from django.db import models

#Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class UserModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    reputation = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Users'



class QuestionModel(models.Model):
    title = models.TextField()
    description = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='question_images', null=True, blank=True)
    votes = models.IntegerField(default=0)
    is_answered = models.BooleanField(default=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Questions'


class AnswerModel(models.Model):
    description = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='answer_images', null=True, blank=True)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    is_accepted = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return (self.description[:50] + '...')
    
    class Meta:
        verbose_name_plural = 'Answers'



