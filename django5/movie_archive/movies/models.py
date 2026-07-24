from django.db import models

from django.contrib.auth.models import User

class Movies(models.Model):
    title = models.CharField('Назва фільму',max_length=50)
    author = models.CharField('Режисер',max_length=30)
    description = models.TextField('Опис фільму')
    year = models.IntegerField('Рік випуску')
    genre = models.CharField('Жанр',max_length=30)
    poster = models.ImageField(blank=True,null=True,upload_to='media/')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(blank=True,null=True,max_length=400)
    avatar = models.ImageField(upload_to='avatars/',blank=True)
    avatar_color = models.CharField(max_length=8,default='#2b5ce6')
    def __str__(self):
        return f'Профіль {self.user.username}'
    def get_initials(self):
        fn = self.user.first_name
        ln = self.user.last_name
        if fn and ln:
            return f'{fn[0]}{ln[0]}'.upper()
        return self.user.username[:2].upper()
class Comment(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Коментар від {self.author.username} до {self.movie.title}"