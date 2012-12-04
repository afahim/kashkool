from django.http import HttpResponse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.http import Http404
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import simplejson
import re
from wall.models import *

import datetime

def index(request):
    media_list = Media.objects.all().order_by('popularity') 
    return render_to_response('wall/index.html',{'media_list': media_list})

def uploader(request):
    return render_to_response('wall/uploader.html')

@csrf_exempt
def add(request):
    try:
        fType = request.FILES['file'].content_type
        if re.match("image", fType):
            imgVid = "image"
        elif re.match("video", fType):
            imgVid = "video"
        else:
            imgVid = "garbage"
        uploadedFile = Media(media=request.FILES['file'],\
        fileType = imgVid,\
        mimeType=fType,\
        title = request.POST['title'],\
        timestamp = datetime.datetime.now(),\
        popularity=1)
        uploadedFile.save()
        received_list = request.POST['tags']
        print str(received_list)
        tags_list = simplejson.loads(received_list)
        for received_tag in tags_list:
            if Tag.objects.filter(tag=received_tag.lower()):
                matched_tag = Tag.objects.get(tag=received_tag.lower())
            else:
                matched_tag = Tag(tag=received_tag.lower())
                matched_tag.save()
            new_relation = Relation(media=uploadedFile,tag=matched_tag)
            new_relation.save()
    except MultiValueDictKeyError:
         return HttpResponseRedirect(reverse('wall.views.uploader'))
    else:
        return HttpResponseRedirect(reverse('wall.views.index'))

def getMedia(request,mediaid):
    e = Media.objects.get(id=mediaid)
    return HttpResponse(e.media, mimetype=e.mimeType)

def zoomBox(request, mediaid):
    comment_list = Comment.objects.all();
    return render_to_response('wall/comments.html',{'comment_list': comment_list})

def vote(request, mediaid):
    current_media = Media.objects.get(id=mediaid)
    current_media.popularity += 1
    current_media.save()
    return HttpResponse("Popularized!")

def wallReturn(request, tag, pageid):
    limit = int(pageid) * 10
    json_list = list()
    if tag == "":
        json_list = Media.objects.all()
        for element in json_list:
            element.media =  "/wall/" + str(element.id) + "/getMedia/"
    else:
        search_word = tag.lower()
        if Tag.objects.filter(tag=search_word):
                    matched_tag = Tag.objects.get(tag=search_word)
                    relation_list = Relation.objects.filter(tag=matched_tag)
                    for relation in relation_list:
                        media_element = Media.objects.get(id=relation.media_id)
                        media_element.media = "/wall/" + str(media_element.id) + "/getMedia/"
                        json_list.append(media_element)
    if len(json_list) > 0: 
        json_list = json_list[limit:limit+10]
    serialized_list = serializers.serialize('json', json_list)
    return HttpResponse(serialized_list)
	
def randomTags(request):
    tag_list = Tag.objects.order_by('?')[0:5]
    return render_to_response('wall/tagslist.html',{'tag_list': tag_list})

@csrf_exempt
def comment(request, mediaid):
    try:
        current_pic = Media.objects.get(id=mediaid)
    except ObjectDoesNotExist:
        raise Http404
    c = Comment(media=current_pic,
                text=request.POST['text'],\
                timestamp = datetime.datetime.now())
    c.save()
    return HttpResponseRedirect("Commented!")

