
# 1 When a user press add education button , 
# the system should create a new entry in the education table with the user_uid and composite_cv_id.

import sys 
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.models import (
    CVLookup , Education , EmploymentHistory , EmploymentReferences , Skills , UserLanguages , WebsiteSocialLinks 
)
from database.sqlserver import get_db 

from faker import Faker




def get_lookup_by_uid(uid):
    db = next(get_db())
    lookup = db.query(CVLookup).filter(CVLookup.user_uid == uid).first()
    db.close()
    return lookup



def create_education_entry():
    lookup = get_lookup_by_uid('154b20df-a3da-497b-86c7-e8cd66520bdb')
    composite_cv_id = lookup.composite_cv_id
    # create education model entry
    education = Education(
        composite_cv_id_reference=composite_cv_id,
        school='University of Pretoria',
        degree='Bachelor of Science',
        description='I am a student of the University of Pretoria',
        start_date='2019-01-01',
        end_date='2019-12-31',
        user_uid = '154b20df-a3da-497b-86c7-e8cd66520bdb'
        
    )

    db = next(get_db())
    db.add(education)
    db.commit()
    db.close()
    pass





# create_education_entry()

def create_employment_history_entry():
    lookup = get_lookup_by_uid('154b20df-a3da-497b-86c7-e8cd66520bdb')
    composite_cv_id = lookup.composite_cv_id
    # create employment model entry
    employment = EmploymentHistory(
        composite_cv_id_reference=composite_cv_id,
        user_uid = lookup.user_uid,
        job_title='Software Developer',
        employer='University of Pretoria',
        start_date = '2019-01-01',
        end_date = '2019-12-31',
        city = 'Cape Town',
        
    )

    db = next(get_db())
    db.add(employment)
    db.commit()
    db.close()
    pass

# create_employment_history_entry()


def create_employment_reference_entity():

    faker = Faker()
    full_name = faker.name()
    email = faker.email()
    phone_number = faker.phone_number()
    company = faker.company()


    lookup = get_lookup_by_uid('154b20df-a3da-497b-86c7-e8cd66520bdb')
    composite_cv_id = lookup.composite_cv_id
    # create employment reference model entry
    employment_reference = EmploymentReferences(
        user_uid = lookup.user_uid,
        composite_cv_id_reference = composite_cv_id,
        reference_full_name = full_name,
        company = company,
        reference_phone_number = phone_number,
        reference_email=email)
    
    db = next(get_db())
    db.add(employment_reference)
    db.commit()
    db.close()
    pass





def create_skills_entry():
    lookup = get_lookup_by_uid('154b20df-a3da-497b-86c7-e8cd66520bdb')
    composite_cv_id = lookup.composite_cv_id
    # create skills model entry
    skills = Skills(
        composite_cv_id_reference=composite_cv_id,
        user_uid = lookup.user_uid,
        skill_name='Python')
    

    db = next(get_db())
    db.add(skills)
    db.commit()
    db.close()
    pass



def create_languages_entry():
    lookup = get_lookup_by_uid('154b20df-a3da-497b-86c7-e8cd66520bdb')
    composite_cv_id = lookup.composite_cv_id
    # create languages model entry
    languages = UserLanguages(
        composite_cv_id_reference=composite_cv_id,
        user_uid = lookup.user_uid,
        user_language_label='English')
    

    db = next(get_db())
    db.add(languages)
    db.commit()
    db.close()
    pass


# create WebsiteSocialLinks entry
def create_website_social_links_entry():
    lookup = get_lookup_by_uid('154b20df-a3da-497b-86c7-e8cd66520bdb')
    composite_cv_id = lookup.composite_cv_id
    # create website social links model entry
    website_social_links = WebsiteSocialLinks(
        composite_cv_id_reference=composite_cv_id,
        user_uid = lookup.user_uid,
        label='Facebook',
        link='https://www.facebook.com/')
    

    db = next(get_db())
    db.add(website_social_links)
    db.commit()
    db.close()
    pass


create_education_entry()
create_employment_history_entry()
create_website_social_links_entry()
create_languages_entry()
create_skills_entry()
create_employment_reference_entity()




























