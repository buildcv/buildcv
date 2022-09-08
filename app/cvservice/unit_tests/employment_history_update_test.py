
import json
import sys 
import os 

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.sqlserver import get_db 


from data.models import EmploymentHistory , User



def update_employment_history_job_title(composite_cv_id_reference , job_title):

    db = next(get_db())
    data = db.query(EmploymentHistory).filter(EmploymentHistory.composite_cv_id_reference == composite_cv_id_reference)
    data.update({EmploymentHistory.job_title: job_title})
    db.commit()
    db.close()

   
    pass

def update_employment_history_company_name(composite_cv_id_reference , employer):
        
    db = next(get_db())
    data = db.query(EmploymentHistory).filter(EmploymentHistory.composite_cv_id_reference == composite_cv_id_reference)
    data.update({EmploymentHistory.employer: employer})
    db.commit()
    db.close()
        
        
    pass

def update_employment_history_start_date(composite_cv_id_reference , start_date):
    db = next(get_db())
    data = db.query(EmploymentHistory).filter(EmploymentHistory.composite_cv_id_reference == composite_cv_id_reference)
    data.update({EmploymentHistory.start_date: start_date})
    db.commit()
    db.close()
                
                
    pass


def update_employment_history_end_date(composite_cv_id_reference , end_date):
    db = next(get_db())
    data = db.query(EmploymentHistory).filter(EmploymentHistory.composite_cv_id_reference == composite_cv_id_reference)
    data.update({EmploymentHistory.end_date: end_date})
    db.commit()
    db.close()
                
                
    pass
def update_employment_history_city(composite_cv_id_reference , city):
    db = next(get_db())
    data = db.query(EmploymentHistory).filter(EmploymentHistory.composite_cv_id_reference == composite_cv_id_reference)
    data.update({EmploymentHistory.city: city})
    db.commit()
    db.close()
                
                
    pass

       

update_employment_history_job_title('7gw9XjCdylXNe7eXoulitzVkaRq2_rand_ClaSzo' , 'New Job Title')
update_employment_history_company_name('7gw9XjCdylXNe7eXoulitzVkaRq2_rand_ClaSzo' , 'New Company Name')
update_employment_history_start_date('7gw9XjCdylXNe7eXoulitzVkaRq2_rand_ClaSzo' , '2019-01-02')
update_employment_history_end_date('7gw9XjCdylXNe7eXoulitzVkaRq2_rand_ClaSzo' , '2019-01-02')
update_employment_history_city('7gw9XjCdylXNe7eXoulitzVkaRq2_rand_ClaSzo' , 'New City')

