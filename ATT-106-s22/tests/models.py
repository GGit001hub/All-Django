from django.db import models

# Create your models here.

holati = (
    ('active',"Ko'riladigan"),
    ('deactive',"Yashirish")
)

javoblar = (
    ('variant1','1-variant'),
    ('variant2','2-variant'),
    ('variant3','3-variant'),
)

class Test(models.Model):
    questions = models.TextField(verbose_name="Savol uchun")
    variant1 = models.CharField(max_length=200,verbose_name="1-variant")
    variant2 = models.CharField(max_length=200,verbose_name="2-variant")
    variant3 = models.CharField(max_length=200,verbose_name="3-variant")


    true_question = models.CharField(max_length=200,choices=javoblar,verbose_name="To'g'ri javob")
    status = models.CharField(max_length=60,choices=holati,verbose_name="Holati")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.true_question

