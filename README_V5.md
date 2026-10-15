# Scenovis V5 — formularz kontaktowy i prywatność

## Zmiany
- Krótki formularz: telefon **lub** e-mail (jedno wymagane pole), opcjonalna wiadomość, jeden przycisk „Wyślij zapytanie”.
- Temat oferty jest wpisywany do ukrytego pola, kiedy ktoś przechodzi do kontaktu z wybranej usługi.
- Formularz przygotowany pod **Netlify Forms** z polem `form-name`, `data-netlify="true"` i niewidocznym honeypotem antyspamowym.
- Strona obsługuje PL/EN, także teksty o błędach, potwierdzeniu i informację prawną.
- Dodano `privacy.html`, a w indeksie okno z tą samą polityką, otwierane z formularza i stopki.
- Brak zewnętrznych skryptów analitycznych/cookies marketingowych w kodzie dostarczonej witryny. Zapisywana jest preferencja językowa (`localStorage`).

## Wysyłanie z Netlify — wymagane kroki
1. Opublikuj zawartość ZIP na swojej stronie Netlify (np. przez GitHub tak jak wcześniej).
2. Panel Netlify > **Forms** > **Enable form detection**. Jeśli dopiero włączasz tę funkcję, zrób ponowny deploy.
3. Sprawdź, czy w **Forms** pojawia się formularz `scenovis-contact`.
4. Panel Netlify > **Forms** > **Submission notifications** > **Add notification** > e-mail, wpisz swój docelowy adres. Zgłoszenia będą też w panelu Forms.
5. Przetestuj na opublikowanej domenie dwa zapytania: z numerem telefonu i z e-mailem. Sprawdź, czy zgłoszenie jest widoczne w Netlify Forms i czy dotarło powiadomienie na adres.

**Uwaga:** pojedynczy plik podglądu `SCENOVIS_podglad_v5.html` i testowanie na `localhost` **nie wysyłają** żadnych danych. Wyświetlają stosowny komunikat. Wysyłka w produkcji wymaga hostingu obsługującego Netlify Forms. Jeśli hosting zostanie przeniesiony na Cloudflare Workers, należy podmienić obsługę backendową formularza.

## RODO / dane firmy — DO UZUPEŁNIENIA PRZED PUBLIKACJĄ
W `privacy.html` oraz dialogu w `index.html` jest celowo oznaczone pole na **pełną nazwę administratora danych i adres**. Nie wpisano fikcyjnej firmy ani adresu. Uzupełnij i zweryfikuj dane firmy (w razie potrzeby także inne wymagane dane działalności), podmiot przetwarzający, lokalizację przetwarzania i okres retencji. Sprawdź, czy tekst odpowiada faktycznemu sposobowi działania firmy i dostawców. Na razie polityka jest projektem, **nie gotową opinią prawną**.

Jeśli później dodasz Google Analytics, Meta Pixel, YouTube osadzone, marketingowe cookies lub inne niekonieczne technologie, przeanalizuj obowiązek uzyskania zgody i zaktualizuj informację cookies.

## Modyfikacja formularza
- HTML: `index.html`, sekcja `#contact`.
- Wysłanie / walidacja: `site.js` — `submitEnquiry`, `validContact`.
- Style: `refinements.css` (na końcu pliku).
- Polityka: `privacy.html` oraz treść okna polityki w `index.html` (obie wersje PL/EN).
