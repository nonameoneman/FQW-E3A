from django.db import models

# Create your models here.

class news(models.Model):
    title = models.CharField(("Заголовок"), max_length=50)
    text = models.TextField(("Текст новости"))
    date_of_pub = models.DateField(("Дата публикации"), auto_now=False, auto_now_add=True)
    advisor = models.ForeignKey("app_users.Advisor", verbose_name=("Советник"), on_delete=models.CASCADE)
    hide = models.BooleanField(("Скрыть новость"), default=False)
    
    class Meta:
        verbose_name = ("Новость")
        verbose_name_plural = ("Новости")
        ordering = ['date_of_pub',]
        
    