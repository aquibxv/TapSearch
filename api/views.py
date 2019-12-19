from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
import pdfkit
from api.Index import InvertedIndex
from api.pdfParser import parser
from api.pdfMiner import pdfparser
from api.models import PDF

# Create your views here
index_obj = InvertedIndex()

def index(request):
    if request.method == 'POST':
        # fetching the input document and parsing it
        lines = request.POST.get('document')
        docs = []
        
        for line in lines.split("\n\n"):
            docs.append(line)

        for doc in docs:
            for term in doc.split():
                index_obj.add_term_occurrence(term, doc)

        # fetching the PDF file and parsing it
        pdf = request.FILES.get('myFile') or None

        if pdf != None:    
            # parsing the pdf to string
            lines = pdfparser(pdf)
            docs = []

            # saving the pdf in db
            name = str(pdf)
            pdf = PDF.objects.create(name=name, pdf_file=pdf)
            pdf.save()
        
            for line in lines.split("\n\n"):
                docs.append(line)

            for doc in docs:
                for term in doc.split():
                    index_obj.add_term_occurrence(term, name)

        return redirect('index')

    else:
        return render(request, 'pages/index.html')

def search(request):
    if request.method == 'POST':
        
        # create an empty result list to store all the documets
        result = []
        pdfs = []
        pdfObject = PDF.objects.all()
        

        # fetch the token from input
        token = request.POST.get('token')

        # returns a Counter Object
        docs = index_obj.get_documents(token)
        
        if docs:
            # append the documents into a result list
            for doc in docs:

                # restricting the results to only top 10
                if len(result) > 10 and len(pdfs) > 10:
                    break

                #check if the name is a pdf name
                try:
                    pdf = PDF.objects.get(name=doc)
                except ObjectDoesNotExist:
                    pdf = None
                
                if (pdf != None):
                    pdfs.append(pdf)
                else:
                    result.append(doc)

            context = {
                'documents' : result,
                'pdfs' : pdfs,
            }

            return render(request, 'pages/search.html', context)
        elif docs == None:
            context = {
                'documents' : 0
            }
            return render(request, 'pages/search.html', context)

    else:
        return render(request, 'pages/search.html')

def clear(request):
    index_obj.clear()
    PDF.objects.all().delete()
    return render(request, 'pages/clear.html')