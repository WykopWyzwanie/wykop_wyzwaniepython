#### \#wyzwaniepython Zadanie 01


A ankiecie wygrała 3 opcja więc oto pierwsze zadanie w historii **#wyzwaniepython**

![Przykład](https://raw.githubusercontent.com/qofnaught/wykop_wyzwaniepython/master/edycja1/przyklad.png)

    Otrzymujesz katalog zawierający 1000 plików o losowych nazwach które są wypełnione
    3 losowymi znakami. Twoim zadaniem jest:
    Wersja łatwa
     - Odczytać rok i miesiąc modyfikacji pliku
     - skopiowac wszystkie pliki z danego roku do do jednego katalogu a poźniej to samo dla miesięcy
    Wersja trudna
     - To co łatwa
     - Znaleźć wszystkie duplikaty.

##### Przydatne biblioteki:
* time
* os.path

Czas na wykonanie to 2 tygodnie tj. **do 17.07.2016**. Wtedy też opublikujemy wpis, gdzie będziecie mogli wstawić link do swojego programu. Nie publikujcie proszę wcześniej rozwiązań, bo zepsujecie zabawę.

##### Linki:
* [Pliki testowe](https://github.com/qofnaught/wykop_wyzwaniepython/blob/master/edycja1/test.zip)
* [Github](https://github.com/qofnaught/wykop_wyzwaniepython/tree/master/edycja1)
* [Spam lista](http://mirkolisty.pvu.pl/list/qIRpnpHg3WM8YOv5)

***

#### Skrypt generujący testy
Skrypt **gf.py** tworzy **k** (**k** jest podawane jako argument linii komend) plików o losowych czasach dostępu do modyfikacji w
katalogu, w którym został wywołany. Ponadto wypełnia pliki losową zawartością,
generując duplikaty, które rozwiązanie zadania w wersji trudniejszej powinno
wykryć.

Przykład użycia (tworzy 10 plików):

    python gf.py 10

Plik **test.zip** zawiera przykładowe dane testowe (1000 plików umieszczonych w katalogu **tst/**).

#### Powodzenia!
