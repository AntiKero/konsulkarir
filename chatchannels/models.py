from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Chat(models.Model):
    participant1 = models.OneToOneField(User, related_name='user1', on_delete=models.DO_NOTHING)
    participant2 = models.OneToOneField(User, related_name='user2', on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{}".format(self.pk)

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author', on_delete=models.DO_NOTHING)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, blank=False, default="", on_delete=models.DO_NOTHING)

    def last_10_messages():
        currentroom = Chat.objects.get
        return Message.objects.order_by('timestamp').all()[:10]


    def __str__(self):
        return self.contact.user.username



