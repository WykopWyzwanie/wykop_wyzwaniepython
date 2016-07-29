## [\#wyzwaniepython](http://www.wykop.pl/tag/wyzwaniepython/) Zadanie 03

W ankiecie wygrała propozycja **nr 1.** i nad tym zadaniem będziemy pracować przez
następne **pięć dni**:

### Łatwa
Propozycja:
"Konsolowy eksplorator plików (poruszanie się folderach,
wyświetlanie informacji o plikach, może jakieś kopiowanie, usuwanie,
tworzenie folderów)."

* przydatna biblioteka **shutil** [Python 2](https://docs.python.org/2.7/library/shutil.html) 
[Python 3](https://docs.python.org/3/library/shutil.html)

Stworzymy po prostu pseudokonsolę, czyli program, który w pętli będzie wczytywał polecenia
na plikach oraz odpowiednio na nie reagował.

#### Polecenia do obsłużenia:
 - `pwd` - wraca napis zawierający pełną ścieżkę bezwzględną do aktualnego katalogu
 - `cd <nazwa_katalogu>` - przechodzi do katalogu `<nazwa_katalogu>` (zmienia aktualny katalog,
czyli ten wskazywany przez `pwd`)
 - `cp <sciezka1> <sciezka2>` - kopiuje **plik** lub **katalog** ze `<sciezka1>` do `<sciezka2>`
 - `mv <sciezka1> <sciezka2>` - przenosi **plik** lub **katalog** ze `<sciezka1>` do `<sciezka2>`
 - `info <sciezka1>` - zwraca informacje o **pliku** lub **katalogu** z `<sciezka1>` (format niżej)
 - `ls` - wyświetla zawartość aktualnego (czyli zwracanego przez polecenie `pwd`) **katalogu**
 - `rm <sciezka>` - usuwa **plik** lub **katalog** spod `<sciezka>`
 - `touch <sciezka>` - tworzy **pusty** plik pod `<sciezka>`

#### Format polecenia `info`
Polecenie `info` powinno wyświetlać następujące informacje:
* typ - plik/katalog/inny
* ścieżkę bezwzględną podanego **pliku** lub **katalogu**
* pełny (tzn. w przypadku katalogu sumaryczny rozmiar całej jego zawartości) rozmiar w bajtach **pliku** lub **katalogu**
* **[w przypadku katalogów]** liczbę plików (czyli bez katalogów) znajdujących się wewnątrz
* czas zwracany przez **os.path.getctime()**
* czas zwracany przez **os.path.getmtime()**


Przykład dla **katalogu** `dir1`:
```
typ: katalog
sciezka: /home/raw/docs/dir1
rozmiar: 5813B
liczba_plikow: 31
ctime: 2016-05-28
mtime: 2015-11-03
```

#### Wymagania
 * rozwiązanie **musi** zawierać funkcję `parse(cmd, \*args, \*\*kwargs)`, która będzie interpretowała polecenie podane jako `cmd`
   z argumentami występującymi po nim oraz w przypadku poleceń wypisujących informacje (`pwd`, `ls`, `info`) zwróci napis je
   je zawierający; w przypadku pozostałych poleceń wykona związane z nimi akcje i zwróci **None** - pozwoli to wygodnie
   testować podsyłane rozwiązania i je ujednolici

### Trudna
Graficzny eksplorator plików (biblioteka do wyboru: pyQt/tkinter/pyGTK/ncurses), pozwalający wykonać takie akcje jak
eksplorator z wersji łatwej.

===

### Czas na wykonanie
**5 dni, do 03.08.2016 (ok. 22:00)**

===

Tak jak poprzednio, prosimy o niepublikowanie wcześniej rozwiązań, ale
zachęcamy do pytania o pomoc w tagu [#wyzwaniepythonpomoc](http://www.wykop.pl/tag/wyzwaniepythonpomoc/)
(jeśli coś jest dla Was niejasne w treści zadania, pytajcie i o to).

### Linki:
* [Spam lista](http://mirkolisty.pvu.pl/list/qIRpnpHg3WM8YOv5)

## Powodzenia!
