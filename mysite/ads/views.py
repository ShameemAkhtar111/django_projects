# Create your views here.
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from ads.models import Ad, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from ads.forms import CreateForm
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from ads.forms import CommentForm


class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "myarts/Ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "ads/ad_detail.html"
    def get(self, request, pk) :
        x = get_object_or_404(Ad, id=pk)
        comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'ad' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class AdCreateView(LoginRequiredMixin, View):
    model = Ad
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')
    # List the fields to copy from the Ad model to the Ad form
    #fields = ['title', 'price', 'text']
    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)

class AdUpdateView(LoginRequiredMixin, View):
    model = Ad
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')
    #fields = ['title', 'price', 'text']
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']
    def get(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        ad = form.save(commit=False)
        ad.save()

        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=f)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        forum = self.object.ad
        return reverse('ads:ad_detail', args=[forum.id])

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response
