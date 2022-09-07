
import json
import sys 
import os 

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.sqlserver import get_db 


from data.models import Education , User


def update_education_school_name(composite_cv_id_reference , school_name):

    db = next(get_db())
    # update education
    data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)

    # update school name
    data.update({Education.school: school_name , Education.composite_cv_id_reference: composite_cv_id_reference})
    db.commit()
    db.close()

  
    pass 



update_education_school_name('7gw9XjCdylXNe7eXoulitzVkaRq2_rand_hZaRlF' , 'new school name')




