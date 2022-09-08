
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

def update_education_degree_name(composite_cv_id_reference , degree_name):
    
        db = next(get_db())
        # update education
        data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
        # print data
        data.update({Education.degree: degree_name})
        db.commit()
        db.close()
    
    
        pass

def update_education_description(composite_cv_id_reference , description):
        
            db = next(get_db())
            # update education
            data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
            # print data
            data.update({Education.description: description})
            db.commit()
            db.close()
        
        
            pass


def update_education_start_date(composite_cv_id_reference , start_date):
            
                db = next(get_db())
                # update education
                data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
                # print data
                data.update({Education.start_date: start_date})
                db.commit()
                db.close()
            
            
                pass

def update_education_end_date(composite_cv_id_reference , end_date):
 db = next(get_db())
 data = db.query(Education).filter(Education.composite_cv_id_reference == composite_cv_id_reference)
 data.update({Education.end_date: end_date})
 db.commit()
 db.close()
                    
                    
                            


update_education_school_name('7gw9XjCdylXNe7eXoulitzVkaRq2_rand_ClaSzo' , 'new school name')
update_education_degree_name('7gw9XjCdylXNe7eXoulitzVkaRq2_rand_ClaSzo' , 'new degree name')
update_education_description('7gw9XjCdylXNe7eXoulitzVkaRq2_rand_ClaSzo' , 'new description')
update_education_start_date('7gw9XjCdylXNe7eXoulitzVkaRq2_rand_ClaSzo' , '2020-01-01')



def update_education(education: Education):
    db = next(get_db())
    db.query(Education).filter(Education.composite_cv_id_reference == education.composite_cv_id_reference).update(education.dict())
    db.commit()
    db.close()

edu = Education(
    composite_cv_id_reference='7gw9XjCdylXNe7eXoulitzVkaRq2_rand_ClaSzo',
    school='New Degree ',
    degree='new degree name',
    description='new description',
    start_date='2020-01-01',
    end_date='2020-01-01'
)

def update_education(education: Education):
    db = next(get_db())
    db.query(Education).filter(Education.composite_cv_id_reference == education.composite_cv_id_reference).update(education.dict())
    db.commit()
    db.close()


