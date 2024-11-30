import os

path = 'C:/Users/FenixDev02/Downloads/DiretorioIdiota';

#Bom, se for considerar que a função primariamente roda a O(n), cada diretório ira rodar a O(m), sendo m o total de nomes em determinado diretório.
#Consequentemente todas as chamadas são O(n), sendo n o numero de arquivos em cada diretório.

def readFilesRecursevly(path):
    for item in os.listdir(path):
        print(item);
        itemPath = path + "/" + item;
        if(bool(os.path.isfile(itemPath)) == False):
            readFilesRecursevly(itemPath);
    return;

readFilesRecursevly(path);