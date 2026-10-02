import requests


class UsersAPI:

    def __init__(self, base_url):

        self.base_url = base_url

    def get_user(self, user_id):

        return requests.get(
            f"{self.base_url}/api/users/{user_id}",
            timeout=10
        )

    def get_users(self, page=2):

        return requests.get(
            f"{self.base_url}/api/users",
            params={"page": page},
            timeout=10
        )

    def create_user(self, name, job):

        return requests.post(
            f"{self.base_url}/api/users",
            json={
                "name": name,
                "job": job
            },
            timeout=10
        )

    def update_user(
        self,
        user_id,
        name,
        job
    ):

        return requests.put(
            f"{self.base_url}/api/users/{user_id}",
            json={
                "name": name,
                "job": job
            },
            timeout=10
        )

    def delete_user(self, user_id):

        return requests.delete(
            f"{self.base_url}/api/users/{user_id}",
            timeout=10
        )
