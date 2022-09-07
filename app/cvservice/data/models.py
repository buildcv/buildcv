


from datetime import datetime
import sys 
import os 



from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime , Date , PrimaryKeyConstraint
from sqlalchemy.orm import relationship

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()





class CVLookup(Base):
    __tablename__ = 'cv_lookup'
    user_uid = Column(String(130),ForeignKey('users.uid'), primary_key=True)
    composite_cv_id = Column(String(130), primary_key=True)
    users = relationship("User", back_populates="cvlookups")
    
    



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(60), nullable=False)
    registration_date = Column(Date, nullable=False)
    uid = Column(String(130), nullable=False)
    email = Column(String(30), nullable=False)
    cvlookups = relationship("CVLookup", back_populates="users")



# create table query : 

'''


create table resume.dbo.education (
  id int not null,
  user_uid varchar(120),
  composite_cv_id_reference varchar(130),
  school varchar(100),
  degree varchar(100),
  description varchar(512),
  start_date date,
  end_date date,
  foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)
);
GO



'''

# convert sql query into education model :
class Education(Base):
    __tablename__ = 'education'

    # id = Column(Integer, autoincrement=True)
    user_uid = Column(String(130), primary_key=True,nullable=False)
    composite_cv_id_reference = Column(String(130), ForeignKey('cv_lookup.composite_cv_id'), nullable=False , primary_key=True)
    school = Column(String(100), nullable=False)
    degree = Column(String(100), nullable=False)
    description = Column(String(512), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    # cvlookups = relationship("CVLookup", back_populates="Education")
    PrimaryKeyConstraint (user_uid, composite_cv_id_reference)


# convert sql query into employment history 

'''
create table employment_history
(
    id                        int identity,
    user_uid                  varchar(120),
    composite_cv_id_reference varchar(130)
        references cv_lookup,
    job_title                 varchar(200),
    employer                  varchar(200),
    start_date                date,
    end_date                  date,
    city                      varchar(100)
)
go


'''
class EmploymentHistory(Base):
    __tablename__ = 'employment_history'

    # id = Column(Integer, autoincrement=True)
    user_uid = Column(String(130), primary_key=True,nullable=False)
    composite_cv_id_reference = Column(String(130), ForeignKey('cv_lookup.composite_cv_id'), nullable=False , primary_key=True)
    job_title = Column(String(200), nullable=False)
    employer = Column(String(200), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    city = Column(String(100), nullable=False)
    PrimaryKeyConstraint (user_uid, composite_cv_id_reference)


# convert sql query into employment references

'''
create table resume.dbo.employment_references (
  id int not null,
  user_uid varchar(120),
  composite_cv_id_reference varchar(130),
  reference_full_name varchar(60),
  company varchar(60),
  reference_phone_number varchar(20),
  reference_email varchar(60),
  foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)
);
GO




'''


class EmploymentReferences(Base):
    __tablename__ = 'employment_references'

    # id = Column(Integer, autoincrement=True)
    user_uid = Column(String(130), primary_key=True,nullable=False)
    composite_cv_id_reference = Column(String(130), ForeignKey('cv_lookup.composite_cv_id'), nullable=False , primary_key=True)
    reference_full_name = Column(String(60), nullable=False)
    company = Column(String(60), nullable=False)
    reference_phone_number = Column(String(50), nullable=False)
    reference_email = Column(String(60), nullable=False)
    PrimaryKeyConstraint (user_uid, composite_cv_id_reference)



# convert sql query into skills

'''
create table resume.dbo.skills (
  id int not null,
  user_uid varchar(120),
  composite_cv_id_reference varchar(130),
  skill_name varchar(60),
  foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)
);
GO



'''
class Skills(Base):
    __tablename__ = 'skills'

    # id = Column(Integer, autoincrement=True)
    user_uid = Column(String(130), primary_key=True,nullable=False)
    composite_cv_id_reference = Column(String(130), ForeignKey('cv_lookup.composite_cv_id'), nullable=False , primary_key=True)
    skill_name = Column(String(60), nullable=False)
    PrimaryKeyConstraint (user_uid, composite_cv_id_reference)

# convert sql query into user_languages 

'''
create table resume.dbo.user_languages (
  id int not null,
  user_uid varchar(120),
  composite_cv_id_reference varchar(130),
  user_language_label varchar(50),
  cv_t_reference varchar(150),
  foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)
);
GO


'''
class UserLanguages(Base):
    __tablename__ = 'user_languages'

    # id = Column(Integer, autoincrement=True)
    user_uid = Column(String(130), primary_key=True,nullable=False)
    composite_cv_id_reference = Column(String(130), ForeignKey('cv_lookup.composite_cv_id'), nullable=False , primary_key=True)
    user_language_label = Column(String(50), nullable=False)
    PrimaryKeyConstraint (user_uid, composite_cv_id_reference)



# convert sql query into website_social_links

'''
create table resume.dbo.website_social_links (
  id int not null,
  user_uid varchar(120),
  composite_cv_id_reference varchar(130),
  label varchar(50),
  link varchar(200),
  foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)
);
GO



'''
class WebsiteSocialLinks(Base):
    __tablename__ = 'website_social_links'

    # id = Column(Integer, autoincrement=True)
    user_uid = Column(String(130), primary_key=True,nullable=False)
    composite_cv_id_reference = Column(String(130), ForeignKey('cv_lookup.composite_cv_id'), nullable=False , primary_key=True)
    label = Column(String(50), nullable=False)
    link = Column(String(200), nullable=False)
    PrimaryKeyConstraint (user_uid, composite_cv_id_reference)