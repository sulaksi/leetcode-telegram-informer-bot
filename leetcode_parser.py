import json

import requests


BASE_URL = "https://leetcode.com/graphql"

data = {
    "operationName": "getUserProfile",
    "variables": {
        "username": None
    },
    "query": "query getUserProfile($username: String!) {\n  allQuestionsCount {\n    difficulty\n    count\n    __typename\n  }\n  matchedUser(username: $username) {\n    username\n    socialAccounts\n    githubUrl\n    contributions {\n      points\n      questionCount\n      testcaseCount\n      __typename\n    }\n    profile {\n      realName\n      websites\n      countryName\n      skillTags\n      company\n      school\n      starRating\n      aboutMe\n      userAvatar\n      reputation\n      ranking\n      __typename\n    }\n    submissionCalendar\n    submitStats: submitStatsGlobal {\n      acSubmissionNum {\n        difficulty\n        count\n        submissions\n        __typename\n      }\n      totalSubmissionNum {\n        difficulty\n        count\n        submissions\n        __typename\n      }\n      __typename\n    }\n    badges {\n      id\n      displayName\n      icon\n      creationDate\n      __typename\n    }\n    upcomingBadges {\n      name\n      icon\n      __typename\n    }\n    activeBadge {\n      id\n      __typename\n    }\n    __typename\n  }\n}\n"
}

headers = {
    "Content-Type": "application/json"
}


def get_profile(username):
    data['variables']['username'] = username

    response = requests.post(BASE_URL, data=json.dumps(data), headers=headers)
    response_data = response.json()['data']
    user_data = response_data['matchedUser']
    profile = user_data['profile']
    submissions = user_data['submitStats']['acSubmissionNum']

    profile = {
        "username": user_data['username'],
        "points": user_data['contributions']['points'],
        "realName": profile['realName'],
        "ranking": profile['ranking'],
        "total": submissions[0]['count'],
        "easy": submissions[1]['count'],
        "medium": submissions[2]['count'],
        "hard": submissions[3]['count']
    }

    return profile
