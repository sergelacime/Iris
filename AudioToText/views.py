from django.shortcuts import render,redirect
from .models import *
from report.models import *
from report.views import fonction_report
from Iris.settings import *
from django.core.files.storage import FileSystemStorage
import shutil, os
import openai
from pydub import AudioSegment
import datetime
from django.http import JsonResponse

from report.views import cut

# Create your views here.

def home(request):
    return render(request, "index.html")


def home2(request):
    a,b=1,0
    audio = Audio.objects.filter(user_id=request.user.id)
    
    if request.method=="POST":
        audio_file = request.FILES.get('file')
        d = datetime.datetime.now()
        audioC = Audio.objects.create(filename=str(d.minute)+"_"+audio_file.name,user=request.user,file=audio_file)
        audioC.save()
        # print(request.POST.get('file'))
        return redirect("New")
    if request.user.username == "" :
        a = 1
    
    return render(request, "index2.html",{'a':a,'b':b,'audio':audio})

def new(request):
    a,b=1,0
    audio = Audio.objects.filter(user_id=request.user.id).last
    if request.user.username == "" :
        a = 1
    if request.method=="POST":
        la = request.POST.get('la')
        print(la)
        return render(request, "home.html",{'audio':audio,'a':a,'b':b})
    return render(request, "home.html",{'audio':audio,'a':a,'b':b})



# def cut(response,seg):
#     texte = response
#     taille_morceau = int(seg)

#     morceaux = []
#     debut_morceau = 0
#     fin_morceau = taille_morceau

#     while debut_morceau < len(texte):
#         morceaux.append(texte[debut_morceau:fin_morceau])
#         debut_morceau += taille_morceau
#         fin_morceau += taille_morceau
        
#     return morceaux


def executer_fonction(request):
    valeur = request.GET.get('valeur')
    r = "report"
    if r in valeur :
        val = valeur.split(".")
        if val[0] == "report":
           report = Report.objects.filter(user_id=request.user.id).last()
           exec = fonction_report(report,val[1])
           result = exec
           return JsonResponse({"resultat": result})
    else:
        # ... Faites le traitement avec la valeur ici ...
        audio = Audio.objects.filter(user_id=request.user.id).last()
        compression_rate = 16
        ext = audio.filename.split(".")
        tmp = ext[-1:]
        ex = str(tmp[0])
        for i in ['m4a', 'mp3', 'webm', 'mp4', 'mpga', 'wav', 'mpeg']:
            if ex == i:
                try:
                    audioC = AudioSegment.from_file(audio.file.url[1:], format=ex)
                        # taux de compression en kbps
                    audioC.export("Iris"+audio.filename, format=ex, bitrate=f"{compression_rate}k")
                except:
                    pass

        model_id = 'whisper-1'
        # media_file_path = audio.file.url[1:]
        media_file_path = "Iris"+audio.filename
        media_file = open(media_file_path, 'rb')

        response = openai.Audio.transcribe(
            api_key=openai.api_key,
            model=model_id,
            file=media_file,
            response_format='text',
            language=valeur
        )
        # print(response)
        try : 
            try:
                completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tu es un journaliste professionnel"},
                    {"role": "user", "content": "réécris en langage '"+valeur+"' dans un langage beau, correct et fluide le texte :"+response},
                    # {"role": "assistant", "content": desc},
                ]
                )
                gpt = completion["choices"][0]["message"]["content"]
                
            except:
                # texte = response
                # taille_morceau = 200

                # morceaux = []
                # debut_morceau = 0
                # fin_morceau = taille_morceau

                # while debut_morceau < len(texte):
                #     morceaux.append(texte[debut_morceau:fin_morceau])
                #     debut_morceau += taille_morceau
                #     fin_morceau += taille_morceau
                
                morceaux = cut(response,200)
                gpt=""
                for i in morceaux:
                    completion = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        # messages=[
                        #     {"role": "system", "content": "you are the professional writers"},
                        #     {"role": "user", "content": "rewrite me :"+i}
                        # ])
                        messages=[
                            {"role": "system", "content": "Tu es un journaliste professionnel"},
                            {"role": "user", "content": "réécris en langage '"+valeur+"' dans un langage beau, correct et fluide le texte :"+i},
                            # {"role": "assistant", "content": desc},
                        ])
                    gpt = gpt + " " + completion["choices"][0]["message"]["content"]
                
            textBd = TextGen.objects.create(Audio=audio,text=gpt)
            textBd.save()
            os.remove("Iris"+audio.filename)
            # resultat = "Langage : " + valeur + "\n " + textBd.text
            resultat = "Langage : " + valeur + "\n " +  textBd.text
            return JsonResponse({"resultat": resultat})
        except:
            try:
                resultat = "Langage : " + valeur + "\n " + textBd.text
            except:
                gpt = " Error !!!"
                textBd = TextGen.objects.create(Audio=audio,text=gpt)
                resultat =  "Langage : " + valeur + "\n " + textBd.text
            os.remove("Iris"+audio.filename)
            return JsonResponse({"resultat": resultat})
 
 

def voir_text(request):
    valeur = request.GET.get('valeur')
    try:
        v = valeur.split(".")
        print(v[0],v[1])
        if v[0] == "report":
            try:
                print(valeur)
                text = Resume.objects.get(Report_id=int(v[1]))
                resultat = text.text
            except:
                resultat="empty "
            return JsonResponse({"resultat": resultat})
    except : 
        try:
            text = TextGen.objects.get(Audio_id=int(valeur))
            resultat = text.text
        except:
            resultat="empty "
        return JsonResponse({"resultat": resultat})
 
