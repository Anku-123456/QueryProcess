from celery import shared_task
from .models import CompanyData
import csv

@shared_task
def process_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            CompanyData.objects.create(
                name=row[0],
                sector=row[1],
                revenue=row[2]
            )
