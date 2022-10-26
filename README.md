# test_oblig3
---------------------Løsningmetode-----------------------

Først, fra min github-konto opprettet jeg et github-depot kalt test_oblig3.
Så opprettet jeg en tom mappe på datamaskinen min som kalt oblig_3.
Etter det åpnet jeg kommandolinjen for å konfigurere prosjektets arbeidsmiljø, og et virtuelt arbeidsmiljø ble aktivert.

       ------- Microsoft Windows [Version 10.0.22621.675]
                 (c) Microsoft Corporation. Med enerett.

                C:\Users\radwa\Desktop\Oblig_3\test_oblig3>python -m venv venv

                C:\Users\radwa\Desktop\Oblig_3\test_oblig3>venv\Scripts\activate.bat

                 (venv) C:\Users\radwa\Desktop\Oblig_3\test_oblig3>
                 -----------------------------------------------------------------------------------------

Så kjørte jeg pycharm og åpnet prosjektet for å begynne å lage og utføre forretningskrav for push-operasjon og teste koden i github.
Jeg opprettet leap_year Python-filen og programlogikken "def isLeapYear(year)" som i oblig 2.

-------Installere avhengigheter Start push-prosessen for testen----
  pip install flake8 pytest pytest-cov
og 
  pip freeze > requirements.txt
  
Etter at installasjonen er fullført, lager jeg en Python-testfil kalt "test_leap_year" som i oblig 2
brukte jeg:
  pytest -v --cov
Jeg kjørte den i terminalen for å gjøre alle kodetestene.

----- innstillere continuous integration pipeline-----------

Jeg opprettet circleci-mappen og laget en konfigurasjonsfil inne i den kalt config.yml
Så startet jeg push til github fra terminalen, i henhold til følgende trinn
    git add test_leap_year.py
    git commit  -m "test" 
    git push
    
Så åpnet jeg github og satte inn Actions innstillingene for å se testprosessene som blir push til github
Fra da fungerte alt inkludert push- og test operasjoner.

    
