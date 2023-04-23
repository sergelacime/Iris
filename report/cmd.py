import subprocess

# Exécute les commandes "ls" et "pwd" et récupère la sortie dans la variable "output"

def execBuild(fileurl):
    subprocess.check_output(["export OPENAI_API_KEY=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 ; export TRANSFORMERS_CACHE=home/cime/Iris/pdf2gpt-index-main ; export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python ; python3 /home/cime/Iris/pdf2gpt-index-main/main.py  build-index --path2pdf_file "+fileurl+" --model_name 'Sahajtomar/french_semantic' explore-index --top_k 7"], shell=True)

def execExplore():
    output = subprocess.check_output(["python3 /home/cime/Iris/pdf2gpt-index-main/main.py explore-index --top_k 7 "], shell=True)

    # Affiche la sortie sur la console
    print(output)
