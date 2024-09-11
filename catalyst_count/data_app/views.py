from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CSVUploadForm
from .models import CompanyData
from .tasks import process_csv

def upload_file(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            file_path = f'media/{csv_file.name}'
            with open(file_path, 'wb+') as f:
                for chunk in csv_file.chunks():
                    f.write(chunk)
            process_csv.delay(file_path)
            return redirect('query')
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})

def query_data(request):
    companies = CompanyData.objects.all()
    count = companies.count()
    return render(request, 'query.html', {'count': count})
