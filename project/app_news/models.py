from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(("Заголовок"), max_length=50)
    text = models.TextField(("Текст новости"))
    date_of_pub = models.DateField(("Дата публикации"), auto_now=False, auto_now_add=True)
    advisor = models.ForeignKey("app_users.Advisor", verbose_name=("Советник"), on_delete=models.PROTECT)
    hide = models.BooleanField(("Скрыть новость"), default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("Новость")
        verbose_name_plural = ("Новости")
        ordering = ['date_of_pub',]
        
    