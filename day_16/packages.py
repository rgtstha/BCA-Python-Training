import requests

API_URL = 'https://api.adviceslip.com/advice'

def get_advice():
   response =  requests.get(API_URL)
#    print(response.status_code)
   
   if response.status_code == 200:
      data = response.json()

      advice =  data['slip']['advice']
      return advice
   
   else:
      return 'Something went wrong'

random_advice =  get_advice()

print(random_advice)