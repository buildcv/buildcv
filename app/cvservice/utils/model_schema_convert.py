import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from data.models import User , Education
from schemas.education import  EducationSchema 


def education_schema_to_model(education: EducationSchema):
    print(education)
    education_model  = Education(
        user_uid=education.user_uid,
        composite_cv_id_reference=education.composite_cv_id_reference,
        school=education.school,
        degree=education.degree,
        description=education.description,
        start_date=education.start_date,
        end_date=education.end_date
    )
    return education_model








