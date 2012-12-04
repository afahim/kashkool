from django.db import models

class Media(models.Model):
	media = models.FileField(upload_to='wall/uploads/')
	fileType = models.CharField(max_length=20)
	mimeType = models.CharField(max_length=20)
	title = models.CharField(max_length=200)
	timestamp = models.DateTimeField()
	popularity = models.IntegerField()

class Tag(models.Model):
	tag = models.CharField(max_length=200)

class Relation(models.Model):
	media = models.ForeignKey(Media)
	tag = models.ForeignKey(Tag)

class Comment(models.Model):
	media = models.ForeignKey(Media)
	text = models.TextField()
	timestamp = models.DateTimeField()


