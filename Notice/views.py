from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import Notice


def notice_list(request):
    notice = Notice.objects.all()
    return render(request, 'notice/notice_list.html', {
        'notice': notice
    })



class NoticeDetail(View):
    def get(self, request, pk, *args, **kwargs):
        notice = Notice.objects.get(pk=pk)

        context = {
            'notice': notice,
        }

        return render(request, 'notice/notice_detail.html', context)
