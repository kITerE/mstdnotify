notifications=$(python3 mstdnotify.py --server_url $1 --token $2 --exclude follow --exclude favourite --exclude reblog --exclude poll --exclude pleroma:emoji_reaction)
[ -z "$notifications" ] || echo "$notifications" | sendmail -t $3
