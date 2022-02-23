import requests

from html.parser import HTMLParser


def _request(method, url, params=None):
    r = method(url, params=params)
    r.raise_for_status()
    return r.json()


class _TextHarvester(HTMLParser):
    def __init__(self):
        super().__init__()
        self.collected = []

    def handle_data(self, data):
        self.collected.append(data.strip())


def main(server_url, token, excludes):
    session = requests.Session()
    session.headers.update(Authorization='Bearer ' + token)

    params = dict()
    if excludes:
        params['exclude_types[]'] = excludes

    while True:
        notifications = _request(session.get, server_url + '/api/v1/notifications', params=params)
        if not notifications:
            break

        for notification in notifications:
            acct = (notification.get('account') or {}).get('acct') or '?'
            status_url = (notification.get('status') or {}).get('url') or ''
            print('{} {} {}'.format(acct, notification['type'], status_url))

            in_reply_to_id = (notification.get('status') or {}).get('in_reply_to_id')
            if in_reply_to_id:
                in_reply_to = _request(session.get, server_url + '/api/v1/statuses/' + in_reply_to_id)
                print('reply to ' + in_reply_to.get('url'))

            content = (notification.get('status') or {}).get('content')
            if content:
                harvester = _TextHarvester()
                harvester.feed(content)
                print(' '.join(i for i in harvester.collected if i))

            print()
            _request(session.post, server_url + '/api/v1/notifications/' + notification['id'] + '/dismiss')


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Read and dismiss Mastodon (Pleroma) notifications')
    parser.add_argument('--server_url', required=True, help='server base URL, for example: https://mastodon.example')
    parser.add_argument('--token', required=True, help='user token (read:notifications read:statuses write:notifications), details: https://docs.joinmastodon.org/client/authorized/#flow')
    parser.add_argument('--exclude', action='append', default=[], help='types to exclude (may be several)')
    args = parser.parse_args()
    main(args.server_url, args.token, args.exclude)

