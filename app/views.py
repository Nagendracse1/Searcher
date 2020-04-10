from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from .models import *
from .forms import *
from .scrap import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def app_searcher(request):

    if request.method == "POST":

            form = SearcherApp(request.POST)

            if form.is_valid():

                name = form.cleaned_data['name']
                appl_id = form.cleaned_data['appl_id']

                app_store = apple_store(name, appl_id)

                return JsonResponse(app_store)


            else:
                form = SearcherGoogle(request.POST)

                if form.is_valid():
                    package_name = form.cleaned_data['package_name']

                    play_store = google_play(package_name)
                    print('-----------*******------------')
                    return JsonResponse(play_store)

    else:
        g_form = SearcherGoogle()
        a_form = SearcherApp()
        return render(request,'App_searcher.html',{'a_form': a_form, 'g_form': g_form})




def keyword_finder(request):

    if request.method == "POST":

        url = request.POST.get('url')
        print(url)


        for u in Db_finder.objects.all():
            if u.url == url:
                c_key = u.keyword.split(',')

                print('---------------=====+++++')
                d={}
                rec_key = set()

                for j in Db_finder.objects.all():
                    c = 0
                    tk=[]
                    for i in c_key:
                        if i in j.keyword.split(','):
                            c += 1
                            d[j.url] = j.keyword


                    if c>=3:
                        print(j.keyword.split(','))
                        for mm in j.keyword.split(','):
                            if mm  in c_key:
                                continue

                            rec_key.add(mm)

                a={'d':str(d),'rec_key':str(list(rec_key))}
                return JsonResponse(a)

        keyword = key_find(url)
        if keyword == 'Invalid URL':
            print('=-=-=-=-=-=-')
            return JsonResponse({'invalid':"Invalid URL"})

        else:
            c_key = keyword.split(',')

            print('---------------=====+++++')
            d = {}
            rec_key = set()

            for j in Db_finder.objects.all():
                c = 0
                tk = []
                for i in c_key:
                    if i in j.keyword.split(','):
                        c += 1
                        d[j.url] = j.keyword

                if c >= 3:
                    print(j.keyword.split(','))
                    for mm in j.keyword.split(','):
                        if mm in c_key:
                            continue

                        rec_key.add(mm)

            a = {'d': str(d), 'rec_key': str(list(rec_key))}
            var_url = Db_finder(url=url, keyword=keyword)
            var_url.save()

            return JsonResponse(a)

    return render(request, 'Keyword_finder.html')