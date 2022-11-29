import bs4 as bs
import requests
import pandas
from ontario.celery import app
from .models import DemandReport


@app.task(ignore_result=True)
def fetch_ontario_csv():
    # get last csv url
    url = 'http://reports.ieso.ca/public/Demand'
    r = requests.get(url)
    html = r.text

    soup = bs.BeautifulSoup(html, 'html.parser')
    links_with_text = []

    for a in soup.find_all('a', href=True):
        if a.text:
            links_with_text.append(a['href'])

    last_href = links_with_text[-1]
    csv_url = url + '/' + last_href

    # read csv demand
    csv_table = pandas.read_csv(csv_url, skiprows=3)
    # save csv demand in db
    for index, row in csv_table.iterrows():
        # save DemandReport
        demand_report_value = {
            'date': pandas.to_datetime(row['Date']),
            'hour': row['Hour'],
            'market_demand': row['Market Demand'],
            'ontario_demand': row['Ontario Demand']
        }
        try:
            demand_report = DemandReport.objects.get(date=row['Date'], hour=row['Hour'])
            for key, value in demand_report_value.items():
                setattr(demand_report, key, value)
            demand_report.save()
        except DemandReport.DoesNotExist:
            demand_report = DemandReport(**demand_report_value)
        demand_report.save()

