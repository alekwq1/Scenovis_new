/* Rezerwowe przekierowanie "/" → /pl/ lub /en/ (?lang=en ze starych linków). Zachowuje #kotwicę.
   Na Cloudflare robi to Worker (301) — ten plik działa tylko na innym hostingu lub w podglądzie. */
(function () {
  var l = new URLSearchParams(location.search).get('lang') === 'en' ? '/en/' : '/pl/';
  location.replace(l + location.hash);
})();
