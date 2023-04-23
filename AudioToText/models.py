from django.db import models
from django.core.files.storage import default_storage
from django.db.models import FileField
import re
from django.utils.text import slugify
from django.utils.deconstruct import deconstructible
import datetime
from django.contrib.auth.models import User

# Create your models here.
class RenamedAudioFileField(FileField):
    
    @deconstructible
    def generate_filename(self, instance, filename):
        filename = slugify(filename)
        ext = filename.split('.')[-1]
        new_filename = f"{instance.pk}Iris.{ext}"
        return super().generate_filename(instance, new_filename+".mp3")
        # """
        # Generate a filename for the file.
        # """
        # ext = self.get_ext(filename)
        # filename = re.sub(f'Iris{instance.id}.{ext}')
        # return default_storage.get_available_name(filename)


class Audio(models.Model):
    filename = models.CharField(max_length=100, default="audioIris")
    date = models.DateField(default=datetime.datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file = RenamedAudioFileField()
    
    
    class Meta:
        verbose_name_plural = 'Audio'

    def __str__(self):
        return self.filename


class TextGen(models.Model):
    text = models.TextField()
    date = models.DateField(default=datetime.datetime.now)
    Audio = models.ForeignKey(Audio,on_delete=models.CASCADE,verbose_name="Audio")

    class Meta:
        verbose_name_plural = 'TextGen'

    def __str__(self):
        return self.Audio.filename



