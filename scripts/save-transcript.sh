#!/usr/bin/env bash
# Lagrer transkripsjonen som ligger på utklippstavlen (etter kopieringsklikket i Vimeo-flyten) med header,
# og verifiserer at innholdet ser ut som «hh:mm:ss tekst»-linjer. Verifiser på innhold, ikke bytelengde.
# Bruk: scripts/save-transcript.sh <utfil> <tittel> <video-url> [språk]
set -euo pipefail
out=${1:?bruk: $0 <utfil> <tittel> <video-url> [språk]}; title=${2:?tittel}; url=${3:?video-url}; lang=${4:-ukjent}
body=$(pbpaste)
first=$(printf '%s\n' "$body" | head -1)
if ! printf '%s' "$first" | grep -Eq '^[0-9]{2}:[0-9]{2}:[0-9]{2} '; then
  echo "FEIL: utklippstavlen starter ikke med en cue-linje: «${first:0:80}»" >&2; exit 1
fi
{ printf '# %s\n# Video: %s · Språk: %s\n\n' "$title" "$url" "$lang"; printf '%s\n' "$body"; } > "$out"
n=$(printf '%s\n' "$body" | wc -l | tr -d ' ')
echo "$n linjer → $out"; echo "$first"
