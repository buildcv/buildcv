
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
    # print data
    data.update({Education.school: school_name})
    db.commit()
    db.close()

  
    pass 

def update_education_description(composite_cv_id_reference , description):
    db = next(get_db())
    data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
    data.update({Education.description: description})
    db.commit()
    db.close()
    pass


def update_education_start_date(composite_cv_id_reference , start_date):
    db = next(get_db())
    data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
    data.update({Education.start_date: start_date})
    db.commit()
    db.close()
    pass




def delete_education_school_name(composite_cv_id_reference):
    db = next(get_db())
    data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
    data.update({Education.school: None})
    db.commit()
    db.close()
    pass


def delete_education_degree(composite_cv_id_reference):
    db = next(get_db())
    data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
    data.update({Education.degree: None})
    db.commit()
    db.close()
    pass


def delete_education_description(composite_cv_id_reference):
    db = next(get_db())
    data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
    data.update({Education.description: None})
    db.commit()
    db.close()
    pass


def delete_education_start_date(composite_cv_id_reference):
    db = next(get_db())
    data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
    data.update({Education.start_date: None})
    db.commit()
    db.close()
    pass


def delete_education_end_date(composite_cv_id_reference):
    db = next(get_db())
    data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
    data.update({Education.end_date: None})
    db.commit()
    db.close()
    pass


def delete_education(composite_cv_id_reference):
    db = next(get_db())
    data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
    data.delete()
    db.commit()
    db.close()
    pass






