import sys 
import os 

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from data.models import CVLookup  , User

from faker import Faker



def create_user():
    fake = Faker()
    user = User(
        name=fake.name(),
        email=fake.email(),
        registration_date=fake.date_between(start_date='-30y', end_date='today'),
        uid=fake.uuid4()
    )
    return user




def create_random_users(count):
    users = []
    for i in range(count):
        users.append(create_user())
    return users


create_random_users(100)

