from django.db import models

# Create your models here.
Type_Choices = {
    ('n/a','N/A'),
    ('image',"IMAGE"),
    ('stl', 'STL'),
}
class File(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=6, choices=Type_Choices, default='N/A')
    file = models.FileField(upload_to='Files/files/')


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def name(self):
        return os.path.basename(self.File.name)
