from django.shortcuts import render
from prague.models import Toilet, Review
from prague.forms import ReviewForm
from django.shortcuts import redirect
from django.db.models import Q

def index(request):
    wc_list = Toilet.objects.all()
    return render(request, 'prague/index.html', context={'wc_list': wc_list})

def toilet_list(request):
    wc_list = Toilet.objects.exclude(Q(address__isnull=True) | Q(address='Public WC') | Q(address__iregex=r'^\s*$'))
    return render(request, 'prague/toilet_list.html', context={'wc_list': wc_list})

def toilet_detail(request, slug):
    toilet = Toilet.objects.get(slug=slug)
    reviews = Review.objects.filter(toilet=toilet).order_by('-date_posted')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.toilet = toilet
            review.save()
            return redirect('prague:toilet_detail', slug=slug)

    else:
        form = ReviewForm()

    context = {
        'toilet': toilet,
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'prague/toilet_detail.html', context)

def free_toilets(request):
    toilets = Toilet.objects.filter(price='zdarma')
    return render(request, 'prague/free_toilets.html', context={'wc_list': toilets})
