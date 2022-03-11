from django.shortcuts import render
from dashboard.models import Hash
# Create your views here.

def hashinfo(request):
    hashed_info = Hash.objects.all()
    # .get() for a specific id
    print('Myoutput ',hashed_info)
    return render(request,'dashboard/hash_details.html',{'dash':hashed_info})
     