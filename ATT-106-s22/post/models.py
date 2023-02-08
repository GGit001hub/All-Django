from django.db import models

# Create your models here.

fanlar = (
    ("talim","Ta'lim.Y.K"),
    ("texnika","Texnik.T.A.T"),
    ("oliy_math","Oliy matematika"),
    ("inglis","Inglis-tili"),
    ("russ","Rus-tili"),
)

yulduz = (
    ('one',"⭐"),
    ('two',"⭐⭐"),
    ('three',"⭐⭐⭐"),
    ('four',"⭐⭐⭐⭐"),
    ('five',"⭐⭐⭐⭐⭐"),
)


holati = (
    ('active',"Activ"),
    ('deactive',"Activ Emas"),
    ('delete',"O'chirish")
)



class Teacher(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ism familya")
    photo = models.ImageField(upload_to="teacher_photo",verbose_name="Rasm uchun")
    subject = models.CharField(max_length=80,choices=fanlar,verbose_name="Fanlar")
    stars = models.CharField(max_length=100,choices=yulduz,verbose_name="Yulduzlari")
    status = models.CharField(max_length=90,choices=holati,verbose_name="Holati")

    created_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# upload_to="teacher_photo\%Y\%m",  -  Bu har oyda yuklangan rasmni alohida faylga saqlaydi

class Student(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ism familya")
    photo = models.ImageField(upload_to="student_photo",verbose_name="Ism familya")
    stars = models.CharField(max_length=100,choices=yulduz,verbose_name="Yulduzlari")
    status = models.CharField(max_length=90,choices=holati,verbose_name="Holati")

    created_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name