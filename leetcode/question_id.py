import requests

title_slug = input("Enter the title slug: ")

url = "https://leetcode.com/graphql"

params = {
    "query": """
        query questionTitle($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionFrontendId
            }
        }
    """,
    "variables": {"titleSlug": f"{title_slug}"},
    "operationName": "questionTitle"
}

# Make the request
response = requests.post(url, json=params)

# Check the response status code
if response.status_code == 200:
    # Request was successful
    json = response.json()['data']

    print(json['question']['questionFrontendId'])
    # Return the link
else:
    # Request failed
    print("Error: Failed to reach leetcode.com")