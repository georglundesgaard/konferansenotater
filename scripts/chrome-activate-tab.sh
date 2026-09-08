#!/usr/bin/env bash
# Aktiverer Chrome-fanen hvis URL inneholder argumentet, og henter vinduet fram. CDP-klikk (computer-verktøyet)
# når bare den aktive fanen, så dette må kjøres før kopieringsklikket i Vimeo-flyten.
# Bruk: scripts/chrome-activate-tab.sh <url-del>   f.eks. scripts/chrome-activate-tab.sh vimeo.com/1223281331
set -euo pipefail
frag=${1:?bruk: $0 <url-del>}
osascript - "$frag" <<'APPLESCRIPT'
on run argv
  set frag to item 1 of argv
  tell application "Google Chrome"
    repeat with w in windows
      set i to 1
      repeat with t in tabs of w
        if URL of t contains frag then
          set active tab index of w to i
          set index of w to 1
          activate
          return "aktivert: " & (URL of t)
        end if
        set i to i + 1
      end repeat
    end repeat
  end tell
  return "ikke funnet: " & frag
end run
APPLESCRIPT
