from abc_api_base import APIBase

BASE_URL = 'https://api.genderize.io/'

class APIGenderize(APIBase):
    def __init__(self, params, timeout=10):
        super().__init__(BASE_URL, params, timeout)

    def call_api(self):
        self.__data = self.get_api()
        return self.status, self.message

    def __str__(self):
        data = self.__data
        probabilitypercent = data["probability"] * 100
        ret = f'\n{data['name']} is {probabilitypercent}% percent likely to be a {data['gender']}.'
        
        return ret
