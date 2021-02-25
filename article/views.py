from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from article.forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.


def articles(request):
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})




def index(request):
   

    return render(request,"index.html")




def about(request):
    return render(request,"about.html")   


@login_required(login_url="user:login")
def dashboard(request):
    artcle = Article.objects.filter(author=request.user)
    context={
        "article":artcle
    }
    return render(request,"dashboard.html",context)


@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm()
    if request.method=="POST":
        form = ArticleForm(request.POST,request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            
            article.author = request.user
            article.save()

            messages.success(request,"Makale başarıyla oluşturuldu")
            return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})   



def details(request,id):
    article = get_object_or_404(Article,id = id)
    comment = article.comments.all()
    return render(request,"details.html",{"article":article,"comment":comment})    

@login_required(login_url="user:login")
def delete(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()  
    messages.success(request,"Makale Başarıyla Silindi") 
    return redirect("article:dashboard")

@login_required(login_url="user:login")
def uptade(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("article:dashboard")
    return render(request,"uptade.html",{'form': form})    



def comment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("name")
        comment_content = request.POST.get("comment")
        
        newComment = Comment()
        newComment.author=article
        newComment.comment_content=comment_content
        newComment.comment_author=comment_author
        newComment.article = article

        newComment.save()
    return redirect(reverse("article:details",kwargs={"id":id}))