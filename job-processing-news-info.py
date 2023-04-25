import csv
import boto3
import requests

from datetime import date
from bs4 import BeautifulSoup

S3_BUCKET = 'parcial-2-big-data'
date_day = date.today()

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

def extraerTiempo(file):
    
    contenido = s3.get_object(Bucket=S3_BUCKET, Key=file)["Body"].read() 
    soup = BeautifulSoup(contenido, 'html.parser')

    headers='titulo,categoria,link\n'
    
    for articles in soup.find_all('article'):
        for links in articles.find_all('a',class_='title page-link'):
            try:
              link='"'+links["href"]+'"'
              #print(link)
              categoria='"'+link.split('/')[1]+'"'
              #print(categoria)
              titulo='"'+(links.text)+'"'
              headers+=f'{titulo},{categoria},{link}\n'
            except:
                ...
             

    url="headlines/final/periodico=eltiempo/year="+str(date_day.year)+"/month="+str(date_day.strftime('%m'))+"/day="+str(date_day.strftime('%d'))+"/elTiempo"
    s3_resource.Object(S3_BUCKET, url+'{}.csv'.format(date_day.strftime('%Y-%m-%d'))).put(Body=headers)
 
def extraerEspectador(file):
    contenido = s3.get_object(Bucket=S3_BUCKET, Key=file)["Body"].read() 
    soup = BeautifulSoup(contenido, 'html.parser')
    
    headers='titulo,categoria,link\n'

    for articles in soup.find_all('h2',class_='Card-Title Title Title'):
      for links in articles.find_all('a'):
        try:
          link=links["href"]
          categoria=link.split('/')[1]
          titulo=((link.replace('-',' ')).replace(categoria,'')).replace('/','')
          headers+=f'{titulo},{categoria},{link}\n'
        except:
          ...
    url="headlines/final/periodico=elespectador/year="+str(date_day.year)+"/month="+str(date_day.strftime('%m'))+"/day="+str(date_day.strftime('%d'))+"/elEspectador"
    s3_resource.Object(S3_BUCKET, url+'{}.csv'.format(date_day.strftime('%Y-%m-%d'))).put(Body=headers)

extraerTiempo("headlines/raw/eltiempo-"+str(date_day.year)+"-"+str(date_day.strftime('%m'))+"-"+str(date_day.strftime('%d'))+".html")
extraerEspectador("headlines/raw/elespectador-"+str(date_day.year)+"-"+str(date_day.strftime('%m'))+"-"+str(date_day.strftime('%d'))+".html")