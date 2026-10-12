# Scenovis — strona firmowa

Wersja 2 z 12.10.2026: HTML, CSS, JavaScript i lokalne grafiki.
Bez instalowania pakietów i bez procesu budowania.

## Edycja
Otwórz ten folder w Visual Studio Code.
- index.html — układ i treść startowa.
- site.css — podstawowe style.
- refinements.css — aktualne kolory, typografia, karty, responsywność i poprawki przewijania; ładowany po site.css.
- site.js — słowniki PL/EN/RU, nawigacja, animacje i formularz.
- assets/ — grafiki i portret Aleksa.

Treści tłumaczone zmieniaj również w obiekcie DICT w site.js — skrypt wstawia je po uruchomieniu strony.
Podgląd: otwórz index.html lub użyj Live Server w VS Code.

## GitHub → Netlify
1. Rozpakuj ZIP i umieść zawartość tego folderu w głównym katalogu repozytorium.
2. Zrób commit i push do GitHub tak jak zwykle.
3. Połącz repozytorium z Netlify albo użyj istniejącego połączenia.
4. Base directory: puste. Build command: puste. Publish directory: .
Plik netlify.toml zawiera katalog publikacji. Jeśli istniejące repo ma konfigurację innego frameworka, usuń stary build command w ustawieniach Netlify i upewnij się, że publikujesz katalog tej strony.

## Kontakt
Telefon: +48 666 895 060
E-mail: malyshkogrodno@gmail.com
Formularz przygotowuje wiadomość w WhatsApp lub programie pocztowym.
Nie wysyła jej sam i nie zapisuje danych. Nie jest formularzem Netlify Forms.

## Materiały
Portret Aleksa jest zachowany z zaakceptowanej wersji. Zdjęcie Lizy pozostaje do uzupełnienia.
Ilustracje produktów i stoiska są oznaczone na stronie jako koncepcje AI.
Paczka nie zawiera danych logowania, historii repozytorium ani konfiguracji hostingu ChatGPT.

## Aktualizacja istniejącego repozytorium
Podmień pliki tej strony zawartością ZIP, w tym nowy refinements.css.
Zachowaj swój folder .git i ewentualne własne pliki niezwiązane ze stroną.
Następnie:

```bash
git add index.html site.css refinements.css site.js assets README.md netlify.toml
git commit -m "Czytelniejsze UI i poprawione przewijanie Scenovis"
git push
```

## Sprawdzenie po wdrożeniu
Kliknij kolejno Oferta, Przykłady, Jak pracujemy, O nas i Kontakt; nagłówki powinny znaleźć się pod paskiem menu.
Sprawdź też bezpośrednie otwarcie adresu z #services, powrót logo na górę, menu telefonu oraz zmianę PL/EN/RU.
Na telefonie długie sekcje przewijają się naturalnie: treści nie są obcinane, aby wymusić jeden ekran.
Formularz nie otwiera automatycznie klawiatury po wybraniu usługi.
