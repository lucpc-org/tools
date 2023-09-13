import requests

class Problem:
    def easy(self):
        self.difficulty = "EASY"
        return self

    def medium(self):
        self.difficulty = "MEDIUM"
        return self

    def hard(self):
        self.difficulty = "HARD"
        return self

    def get_problem_link(self) -> str:
        url = "https://leetcode.com/graphql"

        # We need a query string for the leetcode api
        params = {
            "query": """
                query randomQuestion($categorySlug: String, $filters: QuestionListFilterInput) {
                    randomQuestion(categorySlug: $categorySlug, filters: $filters) {
                        titleSlug
                    }
                }
            """,
            # Here we set the filter based on the difficulty
            "variables": {"categorySlug": "", "filters": {"difficulty": f"{self.difficulty}"}},
            "operationName": "randomQuestion",
        }

        # Make the request
        response = requests.post(url, json=params)

        # Check the response status code
        if response.status_code == 200:
            # Request was successful
            # Return the link
            return f"https://leetcode.com/problems/{response.json()['data']['randomQuestion']['titleSlug']}"
        else:
            # Request failed
            return "Error: Failed to reach leetcode.com"
