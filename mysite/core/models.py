from django.contrib.auth.models import User # thêm cái này để reference tới class user
from django.db import models

# Chốt, không cần sửa
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
        return self.name + '@' + self.date.strftime('%A %b %d %Y') 

# Chốt, class
class Racer(models.Model):
    # Fields
    name = models.CharField(blank=False,max_length=100) # Tên vận động viên/team
    avatar = models.ImageField(blank=True, null=True) # hình đại diện
    info = models.TextField(blank=True) # thông tin giới thiệu

    # Methods
    def __str__(self):
        return self.name

class Bet(models.Model):
    STATUS_CHOICES = [
        ('i', 'Initializing'),
        ('d', 'Done'),
        ('c', 'Cancelled'),
    ]
    # Fields
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Player')  # người cá đầu tiên
    opponent = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='Opponent') # Người theo 
    content = models.TextField(default="")

    race = models.ForeignKey('Race', models.SET_NULL, blank=True, null=True) # giải
    racer1 = models.ForeignKey('Racer', on_delete=models.CASCADE, null=True, blank=True, related_name='topdog_racer') # vận động viên liên quan đến độ
    racer2 = models.ForeignKey('Racer', on_delete=models.CASCADE, null=True, blank=True, related_name='underdog_racer') # vận động viên đối đầu nếu là kèo hơn thua
    
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='i') 
    
    # Methods
    def __str__(self):
        return self.content

