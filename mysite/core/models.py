from django.contrib.auth.models import User # thêm cái này để reference tới class user
from django.db import models

class Race(models.Model):
    # Fields
    name = models.CharField(blank=False,max_length=100) # Tên giải
    date = models.DateField(blank=False) #ngày xảy ra sự kiện
    info = models.TextField(blank=True) #thông tin giải

    
    # Metadata
    class Meta:
        ordering = ['-date'] # Sắp xếp theo thời gian

    # Methods
    def __str__(self):
        return self.name + '@' + self.date.strftime('%A %b %d %Y') # Có thể phải format lại date cho dễ nhìn


class Racer(models.Model):
    # Fields
    name = models.CharField(blank=False,max_length=100) # Tên vận động viên/team
    avatar = models.ImageField() # hình đại diện
    info = models.TextField(blank=True) # thông tin giới thiệu
    target = models.DurationField(blank=False) # thời gian dự kiến hoàn thành race (format timedelta), sẽ bị refator qua joinrace khi nâng cấp

    # Methods
    def __str__(self):
        return self.name

class Wager(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    race = models.ForeignKey('Race', models.SET_NULL, blank=True, null=True)
    racer1 = models.ForeignKey('Racer', on_delete=models.CASCADE, related_name='topdog_racer') 
    racer2 = models.ForeignKey('Racer', on_delete=models.CASCADE, null=True, blank=True, related_name='underdog_racer')
    content = models.TextField()

    # Methods
    def __str__(self):
        return self.name


class Bet(models.Model):
    PLACE_CHOICES = [
        ('t', 'Favorite Dog'),
        ('u', 'Outsider'),
    ]
    STATUS_CHOICES = [
        ('i', 'Initializing'),
        ('d', 'Done'),
        ('c', 'Cancelled'),
    ]

    # Fields
    player = models.ForeignKey(User, on_delete=models.CASCADE) 
    stake = models.TextField()
    place = models.CharField(max_length=1, choices=PLACE_CHOICES, default='t')
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='i')

    # Methods
    def __str__(self):
        return ""