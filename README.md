# CeneoScraper
## Etap 1 - Pobranie składowych pojedynczej opinii o wybranym produkcie z serwisu [Ceneo.pl](https:www.ceneo.pl)
* Pobranie kodu pojedynczej strony z opiniami o wskazanym produkcie
* Analiza kodu HTML pojedynczej opinii

+--------------+------------+--------------+----------+
|Składowa opnii|Selektor CSS|Nazwa zmiennej|Typ danych|
+:=============+:===========+:=============+:=========+
|Opinia|.js_product-review|opinion||
+--------------+------------+--------------+----------+
|Identyfikator opinii|`["data-entry-id"]`|opinion_id||
+--------------+------------+--------------+----------+
|Autor|.user-post__author-name|author||
+--------------+------------+--------------+----------+
|Rekomendacja|.user-post__author-recomendation|recomm||
+--------------+------------+--------------+----------+
|Liczba gwiazdek|.user-post__score-count|stars||
+--------------+------------+--------------+----------+
|Treść|.user-post__text|content||
+--------------+------------+--------------+----------+
|Lista zalet|review-feature__col:has(> div.review-feature__title--positives) > review-feature__item\|pros|||
||review-feature__col:has(> div[class*="positives") > review-feature__item\||||
||div.review-feature__title--positives ~ review-feature__item|||
+--------------+------------+--------------+----------+
|Lista wad|div.review-feature__title--negatives ~ review-feature__item\|cons||
+--------------+------------+--------------+----------+
|Dla ilu osób użyteczna|button.vote-yes`["data-total-vote"]`|useful||
+--------------+------------+--------------+----------+
|Dla ilu osób nieużyteczna|button.vote-no`["data-total-vote"]`|useless||
+--------------+------------+--------------+----------+
|Czy opinia potwierdzona zakupem|div.review-pz|purchased||
+--------------+------------+--------------+----------+
|Data wystawienia opinii|span.user-post__published > time:nth-child(1)`["datetime"]`|publish_date||
+--------------+------------+--------------+----------+
|Data zakupu produktu|span.user-post__published > time:nth-child(2)`["datetime"]`|purchase_date||
+--------------+------------+--------------+----------+