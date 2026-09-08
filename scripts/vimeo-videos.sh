#!/usr/bin/env bash
# Lister de nyeste videoene på en Vimeo-bruker/kanal, headless, via det gamle Simple API-et.
# API-et gir 20 per side og maks 3 sider (de 60 nyeste). Profilsiden er JS-rendret og ubrukelig for curl.
# Bruk: scripts/vimeo-videos.sh <bruker> [sider=3]     f.eks. scripts/vimeo-videos.sh javazone
# Utskrift: <url> TAB <opplastet> TAB <tittel>, nyeste først.
set -euo pipefail
user=${1:?bruk: $0 <vimeo-bruker> [sider=3]}
pages=${2:-3}
for p in $(seq 1 "$pages"); do
  curl -sf "https://vimeo.com/api/v2/${user}/videos.json?page=${p}" \
    | jq -r 'if type=="array" then .[] | "\(.url)\t\(.upload_date)\t\(.title)" else empty end' || break
done
