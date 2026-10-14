# Scenovis — strona firmowa

Aktualizacja z 14.10.2026: HTML, CSS, JavaScript i lokalne grafiki.
Bez instalowania pakietów i bez procesu budowania.

## Edycja
Otwórz ten folder w Visual Studio Code.
- index.html — układ i treść startowa.
- site.css — podstawowe style.
- refinements.css — aktualne kolory, typografia, karty, responsywność i poprawki przewijania; ładowany po site.css.
- site.js — słowniki PL/EN/RU, nawigacja, animacje i formularz.
- assets/ — grafiki i portrety Aleksa oraz Lizy.

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
Portret Aleksa jest zachowany z zaakceptowanej wersji. Dodano dostarczony portret Lizy. Kadrowanie dopasowano w CSS, bez zmiany pliku źródłowego i twarzy.
Ilustracje produktów i stoiska są oznaczone na stronie jako koncepcje AI.
Paczka nie zawiera danych logowania, historii repozytorium ani konfiguracji hostingu ChatGPT.

## Aktualizacja istniejącego repozytorium
Podmień pliki tej strony zawartością ZIP, w tym nowy refinements.css.
Zachowaj swój folder .git i ewentualne własne pliki niezwiązane ze stroną.
Następnie:

```bash
git add index.html site.css refinements.css site.js assets README.md netlify.toml
git commit -m "Dodaj portret Lizy i dopracuj sekcję zespołu"
git push
```

## Sprawdzenie po wdrożeniu
Kliknij kolejno Oferta, Przykłady, Jak pracujemy, O nas i Kontakt; nagłówki powinny znaleźć się pod paskiem menu.
Sprawdź też bezpośrednie otwarcie adresu z #services, powrót logo na górę, menu telefonu oraz zmianę PL/EN/RU.
Na telefonie długie sekcje przewijają się naturalnie: treści nie są obcinane, aby wymusić jeden ekran.
Formularz nie otwiera automatycznie klawiatury po wybraniu usługi.

## Zmiany 14.10.2026
- Zdjęcie Lizy zamiast inicjału, dopasowane kadrowanie obu portretów.
- Szersze portrety na komputerze i pełne karty na telefonie.
- Czytelniejsze opisy zespołu i większe przyciski tematów zapytania.
- Escape zamyka menu i przywraca fokus; etykiety menu PL/EN/RU.
- Weryfikacja statyczna plików i składni JavaScript. Podgląd przeglądarkowy nie był dostępny w tym środowisku.

Aktualizacja zespołu: imiona Aleks i Liza, linki LinkedIn, opisy obowiązków w PL/EN/RU.

Oferta obejmuje organizację całych wydarzeń i wsparcie klientów zagranicznych w Polsce. Formularz rozróżnia obsługę stoiska i organizację wydarzenia. Treści PL/EN/RU.
