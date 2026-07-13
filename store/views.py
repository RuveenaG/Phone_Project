from django.shortcuts import render


def storehome(request):
    return render(request, 'store/storehome.html', {})

def aboutus(request):
    return render(request, 'store/aboutus.html', {})

def reviews(request):
    return render(request, 'store/reviews.html', {})

def campaign (request):
    return render(request, 'store/campaign.html', {})