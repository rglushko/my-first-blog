from django.core.management.base import BaseCommand
from certificates.models import Certificate
import pandas as pd

class Command(BaseCommand):
    help = 'Load data from Excel file into the database'

    def handle(self, *args, **kwargs):
        excel_file = 'data 1.xlsx'
        df = pd.read_excel(excel_file, engine='openpyxl')
        for _, row in df.iterrows():
            Certificate.objects.create(
                serial_number=row['Serial Number'],
                article_number=row['Article Number'],
                date_end=row['Date End'],
                name_pump=row['Name pump'],
                wc_number=row['WC Number'],
                name_partner=row['Name partner'],
                pin=row['PIN'],
            )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))