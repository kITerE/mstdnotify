# mstdnotify.py

Command line utility: read(and dismiss) new [Mastodon](https://joinmastodon.org/) ([Pleroma](https://pleroma.social/)) notifications.

## Usage mstdnotify.py

Required [requests library](https://docs.python-requests.org/).

Read mention notifications for [Pleroma](https://pleroma.social/) user:
```
python3 mstdnotify.py --server_url https://pleroma.example --token <USER_TOKEN> --exclude follow --exclude favourite --exclude reblog --exclude poll --exclude pleroma:emoji_reaction
```

Obtain USER\_TOKEN: https://docs.joinmastodon.org/client/authorized/#flow

Required scope: `read:notifications` `read:statuses` `write:notifications`

#  pleroma\_sendmail\_mention.sh

Sending new mention notifications using `sendmail`.

## Usage pleroma\_sendmail\_mention.sh

```
pleroma_sendmail_mention.sh https://pleroma.example <USER_TOKEN> user@example.net
```

