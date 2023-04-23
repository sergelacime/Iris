# import openai
# import os 

# API_KEY = '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'
# os.environ["OPENAI_API_KEY"] = "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"
# openai.api_key = os.environ["OPENAI_API_KEY"]
# model_id = 'whisper-1'

# media_file_path = 'test1.mp3'
# media_file = open(media_file_path, 'rb')

# response = openai.Audio.transcribe(
#     api_key=API_KEY,
#     model=model_id,
#     file=media_file
# )
# print(response.data['text'])

# from pydub import AudioSegment
# import os


# # Chemin du fichier audio à découper
# file_path = "test2.flac"


# # Taille maximale de chaque morceau (en mégaoctets)
# max_size = 5 #(paramétrage)


# # Charge le fichier audio
# audio = AudioSegment.from_file(file_path, format="flac")


# # Calcul le nombre de segments à créer
# num_segments = len(audio) // (max_size * 1024 * 1024) + 1


# # Découpe le fichier audio en segments
# for i in range(num_segments):
#     start_time = i * max_size * 1000 * 1000
#     end_time = (i + 1) * max_size * 1000 * 1000
#     segment = audio[start_time:end_time]
#     segment.export(f"segment_{i}.flac", format="flac")


# from pydub import AudioSegment
# import math
# import os

# # Définir la taille maximale de chaque segment en Mo
# max_segment_size = 3000

# # Définir le chemin complet du fichier audio
# audio_path = os.path.join("test2.flac")

# # Charger le fichier audio
# audio_file = AudioSegment.from_file(audio_path)

# # Calculer la durée totale de l'audio en millisecondes
# total_duration = len(audio_file)

# print(total_duration)

# # Définir le nombre total de segments nécessaires
# total_segments = math.ceil(total_duration / (max_segment_size * 1000))

# Découper l'audio en segments de taille maximale de 20 Mo
# for i in range(total_segments):
#     start_time = i * max_segment_size * 1000
#     end_time = min((i + 1) * max_segment_size * 1000, total_duration)
#     segment = audio_file[start_time:end_time]

#     # Sauvegarder chaque segment en tant que fichier audio séparé
#     segment_path = os.path.join(f"fichier_audio_segment_{i}.wav")
#     segment.export(segment_path, format="wav")

# from pydub import AudioSegment
# from pydub.utils import make_chunks
# import os

# # Charge le fichier audio
# audio = AudioSegment.from_file("test3.mp3", format="mp3")
# taille_fichier = os.path.getsize("test3.mp3")
# # Comprime le fichier audio
# compression_rate = 32 # taux de compression en kbps
# audio.export("compressé32.mp3", format="mp3", bitrate=f"{compression_rate}k")

# # Supprime le fichier audio original (optionnel)
# #os.remove("chemin/vers/fichier/audio.wav")
# import openai
# import os
# openai.api_key = "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"

# texte = "Bonjour DG. Bonjour, il y a dit Sandrine ou Echofine? Bon, bonjour Sandrine. D'accord, donc vous êtes allé pour Ville et on en profite pour faire une petite interview. Donc deux ans après le début d'une économisation des marchés financiers à l'École centrale, quels sont en quelques chiffres ou indicateurs les réalisations qui ont été faites jusqu'ici? Bon, je dirais même que nous sommes déjà à plus de deux ans de la fusion, parce que la fusion est intervenue, elle a été réalisée en 2019, nous sommes en 2023. Donc, quel est le bilan qu'on peut en faire aujourd'hui? C'est que la fusion a été serrée, c'est-à-dire en deux phases. Donc une première phase qui était le rapprochement institutionnel et physique des structures qui étaient là, ça concernait les deux entreprises de marché, donc il y avait la BVMAC à Libreville et la DSX à Douala. Donc ces deux entités ont fusionné avec un siège qui était fixé à Douala. Après, il y a les deux régulateurs dont la COSUMAF et la Commission des marchés financiers du Cameroun qui ont fusionné aussi avec un siège à Libreville. Après, les dépositaires centraux aussi ont fusionné et cette mission a été confiée à la Banque centrale qui a tissé le transitoire pour deux ans. Donc théoriquement, c'est en 2023 qu'une société privée doit être créée pour pouvoir assurer ces missions de dépositaires centrales qui quitteraient donc la Banque centrale à BAC, mais qui restera néanmoins banque de règlement. Donc la deuxième phase qui a été engagée après l'année 2020, après que ces rapprochements physiques aient eu lieu, est une phase qui concerne beaucoup plus davantage la dynamisation des différents structures qui ont été unifiées. On est en train de s'orienter sur la recherche de la viabilité. Donc la viabilité de la COSUMAF, la viabilité de la BVMAC, la viabilité aussi des dépositaires centrales. Donc sur cette phase-là, en ce qui nous concerne, nous sommes BVMAC et on va beaucoup plus s'appesantir sur cette structure-là. Il y a un business plan qui a été élaboré avec un diagnostic, c'est-à-dire des faiblesses sur le plan institutionnel, sur le plan marketing, sur le plan de la profondeur du marché, sur le plan des ressources humaines, sur le plan juridique, sur un ensemble de volets. Et donc ce diagnostic-là a amené aussi à des pistes de solutions, à des pistes de réformes, et parmi lesquelles il y a le renforcement des fonds propres. Donc il faut remettre l'institution à flot, le recrutement de nouveaux cadres, de personnes qualifiées pour pouvoir occuper un certain nombre de postes, mais également l'approfondissement même des deux compartiments, du compartiment action et le compartiment obligataire. Donc si je m'arrête un peu sur ce dernier point, les États ont accepté de jouer le jeu, c'est-à-dire en montrant un petit peu la voie au secteur privé. Le marché, c'est le marché du secteur privé, mais les États ont, dans un premier temps, accepté, c'est-à-dire de céder des participations de leurs portefeuilles, et aujourd'hui nous comptabilisons sur les six États de la CEMAC, cinq ont déjà répondu et ont donné des entités. Certains en ont donné quatre, d'autres étaient en ont donné trois, et globalement nous avons 17 entreprises qui ont été listées, et parmi les 17, il y a deux qui sont déjà cotées en bourse aujourd'hui. Donc c'est un processus qui est aussi la caractéristique de la manifestation même de la volonté politique, parce qu'on avait souvent tendance, à penser dans notre zone, que la volonté politique était un peu absente pour doter notre espace économique d'un marché de capitaux viables. Donc ça c'est dans les réformes, dans la deuxième phase, mais également au niveau de la BVMAC, vous êtes certainement au courant de ça, aujourd'hui nous sommes en train de faire l'action sur le renforcement des fonds propres. Donc la BVMAC va augmenter son capital social de 3 milliards et demi, après que certains actionnaires aient renoncé à des créances qu'ils avaient vis-à-vis de l'institution pour plus d'un milliard et demi, et donc cela va être consolidé en fonds propres, ça va "
# taille_morceau = 200

# morceaux = []
# debut_morceau = 0
# fin_morceau = taille_morceau

# while debut_morceau < len(texte):
#     morceaux.append(texte[debut_morceau:fin_morceau])
#     debut_morceau += taille_morceau
#     fin_morceau += taille_morceau

# for i in morceaux:
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         # messages=[
#         #     {"role": "system", "content": "you are the professional writers"},
#         #     {"role": "user", "content": "rewrite me :"+i}
#         # ])
#         messages=[
#             {"role": "system", "content": "Tu es un journaliste professionnel"},
#             {"role": "user", "content": "reformulle dans un français beau, correct et fluide:"+i}
#         ])
#     print(completion["choices"][0]["message"]["content"])
#     # gpt = gpt + " " + completion.choices[0].text

# a = "mp3"

# for i in ['m4a', 'mp3', 'webm', 'mp4', 'mpga', 'wav', 'mpeg']:
#     if a == i:
#         print("ok")
#         break
#     else:
#         print("merde")

# import PyPDF2

# from PyPDF2 import PdfReader

# reader = PdfReader("Biomasse.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()

# print(text)

# import docx

# doc = docx.Document('Biomasse.docx')
# text = []

# for paragraph in doc.paragraphs:
#     text.append(paragraph.text)

# print('\n'.join(text))

# from transformers import pipeline

# # Charger le modèle de question-réponse de BERT
# question_answerer = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

# # Texte à analyser
# context = """Le plan de classement est un outil de gestion qui regroupe les documents par sujets, 
# selon une hiérarchie logique basée sur les principales activités d'un organisme.
# Dans StarsGED, le plan de classement est organisé en arborescence sous forme de 
# dossiers de l’explorateur de Windows, et chaque dossier de l’arborescence 
# représente une série du plan de classement. Chaque série du plan de classement
# peut contenir des dossiers de rangements dans lesquels sont rangées les archives"""

# # Poser une question sur le texte
# question = "comment est organiser Le plan de classement?"

# # Obtenir la réponse à la question
# answer = question_answerer(question=question, context=context)

# # Afficher la réponse
# print(answer)

import openai
openai.api_key = "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" # Remplacez YOUR_API_KEY par votre clé API GPT-3

# Fonction pour découper un texte en morceaux
def split_text(text, max_tokens):
    words = text.split()
    chunks = []
    current_chunk = ""
    for word in words:
        if len(current_chunk) + len(word) < max_tokens:
            current_chunk += f" {word}"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = f"{word}"
    chunks.append(current_chunk.strip())
    return chunks

# Fonction pour répondre à une question à partir d'une liste de contextes

def answer_question(contexts, question):
    answer=" "
    for context in contexts:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"""ROLE: Tu es un assistant QA. Ton rôle est d'aider les utilisateurs a trouver la bonne réponse.
            FONCTIONNEMENT:
                Voici un texte {answer} .{context}.
                Tu dois analyser ce texte pour répondre à cette question {question}.

                
                2 Verifie que la question est en rapport avec ce text
                    - Si OUI Alors:
                        - construit la réponse 
                        - reformule la reponse
                    - Si Non Alors:
                        - Si la question est en rapport avec ton fonctionnement alors:
                            - tu ne dit :  Désolé, cette question n'a rien a voir avec le texte
                        - Si Non alors:
                            - tu ne dit :  Désolé, cette question n'a rien a voir avec le texte
            ATTENTION:
                - Tu ne dois pas répondre a une question qui est en dehors de ce contexte.
                - Tu dois être gentil avec le user.
                - évite de dire que tu avais déja répondu à une question
                - Tu dois répondre de façon formelle sans t'excuser d'avoir fait une erreure
                
            Réponse :
        """,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        answer = response.choices[0].text.strip()
        if "Désolé" in answer:
            answer=" "
            continue
            
        else:
            break
    return answer

# Exemple d'utilisation
text = """Le plan de classement est un outil de gestion qui regroupe les documents par sujets, 
selon une hiérarchie logique basée sur les principales activités d'un organisme.
Dans StarsGED, le plan de classement est organisé en arborescence sous forme de 
dossiers de l’explorateur de Windows, et chaque dossier de l’arborescence 
représente une série du plan de classement. Chaque série du plan de classement
peut contenir des dossiers de rangements dans lesquels sont rangées les archives
Le calendrier de conservation est l’ensemble des règles de conservation qui 
régissent le cycle de vie des archives d’une administration. Une règle de 
conservation décrit le cycle de vie d’une archive en terme de durée légale de 
conservation obligatoire à sortie d’un sort final.
Chaque archive qui entre dans StarGED suit donc le cycle de vie de la règle de 
conservation qui lui est attribuée. Quand une archive arrive au terme de son cycle, 
le système le signale à l’archiviste et lui indique le sort final à appliquer à cette 
archive.
Une règle de conservation se définit par les éléments suivants :
 Un code de la règle en général alpha numérique
 Un libellé ou nom de la règle
 Une description, commentaire ou observation de la règle
 Une DUA (Durée d’Utilité Administrative) en général en année
 Un sort final de la règle (qui dit ce que deviendra l’archive sur laquelle est 
appliquée cette règle quand la DUA est terminée
"""
question = "la superficie du togo ? "

max_tokens = 1024
chunks = split_text(text, max_tokens)
answer = answer_question(chunks, question)
if answer:
    print(f"Réponse : {answer}")
else:
    print("Impossible de trouver une réponse dans le texte.")
