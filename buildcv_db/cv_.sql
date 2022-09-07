create table users (
    id integer identity (1,1),
    name varchar(60) not null ,
    registration_date date not null ,
    uid varchar(130) not null primary key ,
    email varchar(30) not null ,

)

GO
create table cv_lookup
(
    id              integer identity (1,1),
    user_uid        varchar(130) not null,
    user_cv_count   integer      not null,
    composite_cv_id varchar(130) not null
    primary key (composite_cv_id),
    foreign key (user_uid) references users (uid)
)


GO


create table website_social_links
(
    id                        integer identity (1,1),
    user_uid                  varchar(130),
    composite_cv_id_reference varchar(130),
    label                     varchar(50),
    link                      varchar(200),
    foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)

)

GO

create table skills
(
    id                        integer identity (1,1),
    user_uid                  varchar(130),
    composite_cv_id_reference varchar(130),
    skill_name                varchar(60),
    foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)


)


GO


create table user_languages
(

    id                        integer identity (1,1),
    user_uid                  varchar(130),
    composite_cv_id_reference varchar(130),
    user_language_label                  varchar(50),
    cv_t_reference            varchar(150),
    foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)


)

GO

create table employment_references
(
    id                        integer identity (1,1),
    user_uid                  varchar(130),
    composite_cv_id_reference varchar(130),
    reference_full_name       varchar(60),
    company                   varchar(60),
    foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)


)


GO

create table employment_history
(
    id                        integer identity (1,1),
    user_uid                  varchar(130),
    composite_cv_id_reference varchar(130),
    job_title                 varchar(200),
    employer                  varchar(200),
    start_date                date,
    end_date                  date,
    city                      varchar(100),
    foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)


)

GO

create table education
(
    id                        integer identity (1,1),
    user_uid                  varchar(130),
    composite_cv_id_reference varchar(130),
    school                    varchar(100),
    degree                    varchar(100),
    description               varchar(512),
    start_date                date,
    end_date                  date,
    foreign key (composite_cv_id_reference) references cv_lookup (composite_cv_id)


)

GO


