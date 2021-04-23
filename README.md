#Generátor překladů pro TC Manager
Generátor vytváří adresář `_locales` se všemi potřebnými překlady pro rozšíření TC Manager.

Autor: Aleš Postulka - xpostu03@stud.fit.vutbr.cz

## Použití

### Virtuální prostředí
```shell
python3 -m venv venv
source venv/bin/activate
```

### Instalace závislostí
```shell
pip install -r requirements.txt
```

### Spuštění
```shell
python3 generate-locales.py
```