
import sys 
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.models import CVLookup , User

from database.sqlserver import get_db 



from get_user_test import get_random_user
from utils.generic_utils import create_random_string 


# get 50 users 


def create_cv_lookup():
    user = get_random_user()
    composite_cv_id = user.uid + create_random_string()
    user_uid = user.uid
    cv_lookup = CVLookup(
        composite_cv_id=composite_cv_id,
        user_uid=user_uid)

    db = next(get_db())
    db.add(cv_lookup)
    db.commit()
    db.close()


    


create_cv_lookup()




















