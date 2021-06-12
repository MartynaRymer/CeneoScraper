# CeneoScraper
## Etap 1 - Pobranie składowych pojedynczej opinii o wybranym produkcie z serwisu [Ceneo.pl](https:www.ceneo.pl)
* Pobranie kodu pojedynczej strony z opiniami o wskazanym produkcie
* Analiza kodu HTML pojedynczej opinii

+--------------+------------+--------------+----------+\
|Składowa opnii|Selektor CSS|Nazwa zmiennej|Typ danych|\
+:=============+:===========+:=============+:=========+\
|Opinia|div.js_product-review|opinion|dict|\
+--------------+------------+--------------+----------+\
|Identyfikator opinii|`["data-entry-id"]`|opinion_id|int|\
+--------------+------------+--------------+----------+\
|Autor|span.user-post__author-name|author|str|\
+--------------+------------+--------------+----------+\
|Rekomendacja|span.user-post__author-recomendation|recomm|bool|\
+--------------+------------+--------------+----------+\
|Liczba gwiazdek|span.user-post__score-count|stars|float|\
+--------------+------------+--------------+----------+\
|Treść|div.user-post__text|content|str|\
+--------------+------------+--------------+----------+\
|Lista zalet|review-feature__col:has(> div.review-feature__title--positives) > .review-feature__item\|pros|\[str\]||\
||review-feature__col:has(> div[class*="positives") > review-feature__item\||||\
||div.review-feature__title--positives ~ review-feature__item|||\
+--------------+------------+--------------+----------+\
|Lista wad|div.review-feature__title--negatives ~ .review-feature__item\|cons|\[str\]|\
+--------------+------------+--------------+----------+\
|Dla ilu osób użyteczna|button.vote-yes`["data-total-vote"]`|useful|int|\
+--------------+------------+--------------+----------+
|Dla ilu osób nieużyteczna|button.vote-no`["data-total-vote"]`|useless|int|
+--------------+------------+--------------+----------+\
|Czy opinia potwierdzona zakupem|div.review-pz|purchased|bool|\
+--------------+------------+--------------+----------+\
|Data wystawienia opinii|span.user-post__published > time:nth-child(1)`["datetime"]`|publish_date|datetime|\
+--------------+------------+--------------+----------+\
|Data zakupu produktu|span.user-post__published > time:nth-child(2)`["datetime"]`|purchase_date|datetime|\
+--------------+------------+--------------+----------+

* Pobranie poszczególnych składowych pojedynczej opinii do indywidualnych zmiennych
* Zdefiniowanie funkcji do pobierania elementów struktury HTML  z uwzględnieniem obsługi błędów

## Etap 2 - Pobranie wszystkich opinii o produkcie
* Zdefiniowanie słownika do przechowywania składowych pojedynczej opinii
* Zdefiniowanie listy do przechowywania wszystkich opinii o produkcie
* Dodanie pętli przechodzących po wszystkich opiniach z pojedynczej strony
* Dodanie pętil przechodzącej po wszystkich stronach z opiniami o produkcie
* Eksport opinii o produkcie do pliku .json

## Etap 3 - Refaktoryzacja kodu
* Parametryzacja kodu produktu, o którym pobierane są opinie
* Użycie słownika składowych opinii oraz wyrażania słownikowego (dictionary comprehension) do utworzenia słownika ze składowymi pojedynczej opinii

## Etap 4 - Analiza opinii pobranych dla pojedynczego produktu
* Wyliczenie podstawowych statystyk o opiniach
* Rysowanie histogramu częstości poszczególnych ocen (gwiazdek)
* Rysowanie udziału rekomendacji w zbiorze opinii

