import argparse
import requests


def main():
    parser =argparse.ArgumentParser(description='GitHub User Activity Tracker CLI')
    subparser = parser.add_subparsers(dest='command')

    #Create the parser for the "github-activity" command

    github_activity_parser = subparser.add_parser('github-activity', help='Track GitHub User Activity')
    github_activity_parser.add_argument('username', type=str, help='GitHub Username')

    args = parser.parse_args()

    if args.command == 'github-activity':
        track_github_activity(args.username)
    else:
        parser.print_help()


def track_github_activity(username):
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)
    events = response.json()

    if response.status_code != 200:
        print('Error fetching data')
        return
    elif response.status_code == 200:
        print("Output:")
        for event in events:
            if event['type'] == 'PushEvent':
                if event.get('payload')['size'] == 1:
                    print(f"- Pushed 1 commit to {event.get('repo')['name']}")
                else:
                    print(f"- Pushed {event.get('payload')['size']} commits to {event.get('repo')['name']}")
            elif event['type'] == 'WatchEvent':
                print(f"- Starred {event.get('repo')['name']}")
            elif event['type'] == 'CreateEvent':
                print(f"- Created {event.get('repo')['name']}")
            elif event['type'] == 'IssuesEvent':
                print(f"- Opened an issue in {event.get('repo')['name']}")
            elif event['type'] == 'PullRequestEvent':
                print(f"- Opened a pull request in {event.get('repo')['name']}")
            elif event['type'] == 'DeleteEvent':
                print(f"- Deleted {event.get('repo')['name']}")
            elif event['type'] == 'ForkEvent':
                print(f"- Forked {event.get('repo')['name']}")
            elif event['type'] == 'PublicEvent':
                print(f"- Made {event.get('repo')['name']} public")
            else:
                print(f"- Event type {event['type']} not supported")
    else:
        print(f'Error fetching data{response.status_code}')


if __name__ == '__main__':
    main()