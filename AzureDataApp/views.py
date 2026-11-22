from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'account/home.html')

def FileStorage(request):
    return render(request, 'account/explore.html')

def ExploreDb(request):
    return render(request, 'account/databases.html')

def Trans(request):
    return render(request, 'account/transactionaldb.html')

def Analytic(request):
    return render(request, 'account/analytical.html')

def Databricks(request):
    return render(request, 'account/databricks.html')

    