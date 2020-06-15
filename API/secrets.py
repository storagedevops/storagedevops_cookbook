from dotenv import load_dotenv   #for python-dotenv method
import os


load_dotenv()                    #for python-dotenv method

user_name = os.environ.get('USER')
password = os.environ.get('PASSWORD')

print(user_name,password)
