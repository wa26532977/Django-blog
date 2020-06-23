from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    public_date = models.DateTimeField(blank=True, null=True)

    # when user decide to publish the post the public date will create
    def public(self):
        self.public_date = timezone.now()
        self.save()

    def approve_comments(self):
        print(self.comments)
        return self.comments.filter(approved_comment=True)

    # go to the post_detail url after user create the post
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title}, {self.author},"


class Comment(models.Model):
    post = models.ForeignKey("blog.Post", related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    # go the main post page after comment post
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return f"{self.text}, {self.author}"
