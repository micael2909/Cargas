from . import models
from django.shortcuts import render

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Archivo(
            Titulo = fileTitle,
            ArchivoSubido = uploadedFile
        )
        document.save()

    documents = models.Archivo.objects.all()

    return render(request, "cabeceras/Carga-Archivos.html", context = {
        "files": documents
    })