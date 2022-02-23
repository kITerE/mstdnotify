notifications=$(python3 mstdnotify.py --server_url $1 --token $2 --exclude follow --exclude favourite --exclude reblog --exclude poll --exclude pleroma:emoji_reaction)

[ -z "$notifications" ] || echo "To: $3\nSubject: Pleroma notifications\nContent-Type: text/plain; charset="utf-8"\n\n$notifications" | sendmail -t
