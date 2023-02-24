import json
import requests
import csv


payload = {
    'operationName': "hackathonProjects",
    'query': "query hackathonProjects {\n  hackathonVote {\n    status\n    projects {\n      projectName\n      description\n      logo\n      votedCount\n      link3Handle\n      __typename\n    }\n    __typename\n  }\n}\n",
    'variables': {},
}


def get_projects():
    response = requests.post('https://api.cyberconnect.dev/', json=payload)
    data = response.json()
    # print(data)
    return data['data']['hackathonVote']['projects']


projects = get_projects()


with open('Data.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
    fieldnames = ['Rank', 'Name', 'Votes']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for index, project in enumerate(projects):
        name = project['projectName']
        rank = index
        votes = project['votedCount']

        writer.writerow({
            'Rank': rank,
            'Name': name,
            'Votes': votes
        })

        print({
            'Rank': rank,
            'Name': name,
            'Votes': votes
        })