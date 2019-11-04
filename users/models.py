# Authors; Yaseen Hull, Laeeq Diedericks, Thobeka Gumede
# Project; Capstone SITPG
# Date; September 2019

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
# Create your models here.

COUNTRY = (
    ('Algeria', 'Algeria'),
    ('Angola', 'Angola'),
    ('Argentina', 'Argentina'),
    ('Australia', 'Australia'),
    ('Austria', 'Austria'),
    ('Botswana', 'Botswana'),
    ('Brazil', 'Brazil'),
    ('Burundi', 'Burundi'),
    ('Cameroon', 'Cameroon'),
    ('Canada', 'Canada'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Chile', 'Chile'),
    ('Congo', 'Congo'),
    ('Costa Rica', 'Costa Rica'),
    ('Democratic Republic of Congo (DRC)', 'Democratic Republic of Congo (DRC)'),
    ('Ecuador', 'Ecuador'),
    ('Egypt', 'Egypt'),
    ('Ethiopia', 'Ethiopia'),
    ('Eritrea', 'Eritrea'),
    ('France', 'France'),
    ('Gabon', 'Gabon'),
    ('Ghana', 'Ghana'),
    ('Germany', 'Germany'),
    ('Guinea', 'Guinea'),
    ('Guyana', 'Guyana'),
    ('India', 'India'),
    ('Iran', 'Iran'),
    ('Ireland', 'Ireland'),
    ('Israel', 'Israel'),
    ('Italy', 'Italy'),
    ('Ivory Coast', 'Ivory Coast'),
    ('Kenya', 'Kenya'),
    ('Lesotho', 'Lesotho'),
    ('Liberia', 'Liberia'),
    ('Madagascar', 'Madagascar'),
    ('Malawi', 'Malawi'),
    ('Mali', 'Mali'),
    ('Mauritius', 'Mauritius'),
    ('Mexico', 'Mexico'),
    ('Morocco', 'Morocco'),
    ('Mozambique', 'Mozambique'),
    ('Namibia', 'Namibia'),
    ('New Zealand', 'New Zealand'),
    ('Nigeria', 'Nigeria'),
    ('Pakistan', 'Pakistan'),
    ('Peru', 'Peru'),
    ('Portugal', 'Portugal'),
    ('Romania', 'Romania'),
    ('Russian Federation', 'Russian Federation'),
    ('Rwanda', 'Rwanda'),
    ('Sierra Leone', 'Sierra Leone'),
    ('South Africa', 'South Africa'),
    ('Spain', 'Spain'),
    ('Sudan', 'Sudan'),
    ('Swaziland', 'Swaziland'),
    ('Tanzania', 'Tanzania'),
    ('Tunisia', 'Tunisia'),
    ('Uganda', 'Uganda'),
    ('United States of America', 'United States of America'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
    ('Other', 'Other')
)

PREVIOUS_DEGREE = (('Diplôme d’Études Supérieures - Algeria', 'Diplôme d’Études Supérieures - Algeria'),
                   ('Magister - Algeria', 'Magister - Algeria'),
                   ('Bacharel - Angola', 'Bacharel - Angola'),
                   ('licenciado - Angola', 'licenciado - Angola'),
                   ('Doutorado - Angola', 'Doutorado - Angola'),
                   ('Titulo - Argentina', 'Titulo - Argentina'),
                   ('Titulo de Maestría - Argentina', 'Titulo de Maestría - Argentina'),
                   ('Bachelor degree - Australia', 'Bachelor degree - Australia'),
                   ('Bachelor degree (Honours) - Australia', 'Bachelor degree (Honours) - Australia'),
                   ('Masters degree - Australia', 'Masters degree - Australia'),
                   ('Fachhochschuldiplom - Austria', 'Fachhochschuldiplom - Austria'),
                   ('Bachelor degree - Austria', 'Bachelor degree - Austria'),
                   ('Masters degree - Austria', 'Masters degree - Austria'),
                   ('Bachelor degree - Botswana', 'Bachelor degree - Botswana'),
                   ('Masters degree - Botswana', 'Masters degree - Botswana'),
                   ('Titulo de Bacharel - Brazil', 'Titulo de Bacharel - Brazil'),
                   ('Titulo de Mestre - Brazil', 'Titulo de Mestre - Brazil'),
                   ('Diplôme de Licence - Burundi', 'Diplôme de Licence - Burundi'),
                   ('Diplôme d’Etudes Approfondies - Burundi', 'Diplôme d’Etudes Approfondies - Burundi'),
                   ('Bachelor degree - Cameroon', 'Bachelor degree - Cameroon'),
                   ('Maîtrise - Cameroon', 'Maîtrise - Cameroon'),
                   ('Diplôme d’Études Approfondies - Cameroon', 'Diplôme d’Études Approfondies - Cameroon'),
                   ('Bachelor degree - Canada', 'Bachelor degree - Canada'),
                   ('Bachelor degree (Honours) - Canada', 'Bachelor degree (Honours) - Canada'),
                   ('Masters degree - Canada', 'Masters degree - Canada'),
                   ('Licence - Central African Republic', 'Licence - Central African Republic'),
                   ('Maîtrise - Central African Republic', 'Maîtrise  - Central African Republic'),
                   ('Licence - Chad', 'Licence - Chad'),
                   ('Maitrise - Chad', 'Maitrise - Chad'),
                   ('Diplôme d’Etudes Approfondies - chad', 'Diplôme d’Etudes Approfondies - Chad'),
                   ('Grado de Licenciado - Chile', 'Grado de Licenciado - Chile'),
                   ('Magister - Chile', 'Magister - Chile'),
                   ('Licenciado - Colombia', 'Licenciado - Colombia'),
                   ('Magíster - Colombia', 'Magíster - Colombia'),
                   ('Licence - Congo', 'Licence - Congo'),
                   ('Maîtrise - Congo', 'Maîtrise - Congo'),
                   ('Bachiller - Costa Rica', 'Bachiller - Costa Rica'),
                   ('Licenciado - Costa Rica', 'Licenciado - Costa Rica'),
                   ('Maestría - Costa Rica', 'Maestría - Costa Rica'),
                   ('Graduat - Democratic Republic of Congo (DRC)', 'Graduat - Democratic Republic of Congo (DRC)'),
                   ('Licence - Democratic Republic of Congo (DRC)', 'Licence - Democratic Republic of Congo (DRC)'),
                   ('Diplôme d’Etudes Approfondies - Democratic Republic of Congo (DRC)', 'Diplôme d’Etudes Approfondies - Democratic Republic of Congo (DRC)'),
                   ('Título de Licenciado - Ecuador', 'Título de Licenciado - Ecuador'),
                   ('Título de Magíster - Ecuador', 'Título de Magíster - Ecuador'),
                   ('Bachelor degree (from a Higher Institute) - Egypt', 'Bachelor degree (from a Higher Institute) - Egypt'),
                   ('Bachelor degree (from a public or private University) - Egypt', 'Bachelor degree (from a public or private University) - Egypt'),
                   ('Masters degree - Egypt', 'Masters degree - Egypt'),
                   ('Bachelor degree - Ethiopia', 'Bachelor degree - Ethiopia'),
                   ('Masters degree - Ethiopia', 'Masters degree - Ethiopia'),
                   ('Bachelor degree - Eritrea', 'Bachelor degree - Eritrea'),
                   ('Licence - France', 'Licence - France'),
                   ('Diplôme d’Études Approfondies - France', 'Diplôme d’Études Approfondies - France'),
                   ('Licence - Gabon', 'Licence -  Gabon'),
                   ('Master - Gabon', 'Master - Gabon'),
                   ('Bachelor degree - Ghana', 'Bachelor degree - Ghana'),
                   ('Masters degree - Ghana', 'Masters degree - Ghana'),
                   ('Bachelor degree - Germany', 'Bachelor degree - Germany'),
                   ('Master - Germany', 'Master - Germany'),
                   ('Licence - Guinea', 'Licence - Guinea'),
                   ('Master - Guinea', 'Master - Guinea'),
                   ('Bachelor degree (from University of Guyana) - Guyana', 'Bachelor degree (from University of Guyana) - Guyana'),
                   ('Masters degree (from University of Guyana) - Guyana', 'Masters degree (from University of Guyana) - Guyana'),
                   ('Bachelor degree (Ordinary/Pass) - India', 'Bachelor degree (Ordinary/Pass) - India'),
                   ('Bachelor degree (Honours / Special / in a professional subject) - India', 'Bachelor degree (Honours / Special / in a professional subject) - India'),
                   ('Masters degree - India', 'Masters degree - India'),
                   ('Bachelor degree (Licence/Karshenasi) - Iran', 'Bachelor degree (Licence/Karshenasi) - Iran'),
                   ('Masters degree (Karshenasi Ershad) - Iran', 'Masters degree (Karshenasi Ershad) - Iran'),
                   ('Ordinary Bachelor Degree - Ireland', 'Ordinary Bachelor Degree - Ireland'),
                   ('Honours Bachelor Degree - Ireland', 'Honours Bachelor Degree - Ireland'),
                   ('Masters degree - Ireland', 'Masters degree - Ireland'),
                   ('Bachelore degree - Israel', 'Bachelore degree - Israel'),
                   ('Masters degree - Israel', 'Masters degree - Israel'),
                   ('Laurea - Italy', 'Laurea - Italy'),
                   ('Laurea Magistrale - Italy', 'Laurea Magistrale - Italy'),
                   ('Licence - Ivory Coast', 'Licence - Ivory Coast'),
                   ('Maîtrise - Ivory Coast', 'Maîtrise - Ivory Coast'),
                   ('Diplôme d’Études Approfondies - Ivory Coast', 'Diplôme d’Études Approfondies - Ivory Coast'),
                   ('Doctorat de Specialité de Troisiéme Cycle - Ivory Coast', 'Doctorat de Specialité de Troisiéme Cycle - Ivory Coast'),
                   ('Bachelor degree - Kenya', 'Bachelor degree - Kenya'),
                   ('Master of Philosophy/Masters degree - Kenya', 'Master of Philosophy/Masters degree - Kenya'),
                   ('Bachelor degree part 2 (further 2 years of study) - Lesotho', 'Bachelor degree part 2 (further 2 years of study) - Lesotho'),
                   ('Masters degree - Lesotho', 'Masters degree - Lesotho'),
                   ('Doctorate - Lesotho', 'Doctorate - Lesotho'),
                   ('Bachelor degree - Liberia', 'Bachelor degree - Liberia'),
                   ('Masters degree - Liberia', 'Masters deegree - Liberia'),
                   ('Licence - Madagascar', 'Licence - Madagascar'),
                   ('Maîtrise - Madagascar', 'Maîtrise - Madagascar'),
                   ('Diplôme d’Études Approfondies - Madagascar', 'Diplôme d’Études Approfondies - Madagascar'),
                   ('Bachelor degree - Malawi', 'Bachelor degree - Malawi'),
                   ('Masters’s degree (from Mzuzu University/ University of Malawi) - Malawi', 'Masters’s degree (from Mzuzu University/ University of Malawi) - Malawi'),
                   ('Master - Mali', 'Master - Mali'),
                   ('Diplôme d’Etudes Approfondies - Mali', 'Diplôme d’Etudes Approfondies - Mali'),
                   ('Bachelor degree - Mauritius', 'Bachelor degree - Mauritius'),
                   ('Masters degree - Mauritius', 'Masters degree - Mauritius'),
                   ('Titulo de Licenciado - Mexico', 'Titulo de Licenciado - Mexico'),
                   ('Grado Académico de Maestría - Mexico', 'Grado Académico de Maestría - Mexico'),
                   ('Licence - Morocco', 'Licence - Morocco'),
                   ('Master - Morocco', 'Master - Morocco'),
                   ('Grau de Licenciado/a - Mozambique', 'Grau de Licenciado/a - Mozambique'),
                   ('Grau de Mestre - Mozambique', 'Grau de Mestre - Mozambique'),
                   ('Bachelor degree - Namibia', 'Bachelor degree - Namibia'),
                   ('Masters degree - Namibia', 'Masters degree - Namibia'),
                   ('Bachelor degree - New Zealand', 'Bachelor degree - New Zealand'),
                   ('Bachelor (Honours) degree - New Zealand', 'Bachelor (Honours) degree - New Zealand'),
                   ('Masters degree - New Zealand', 'Masters degree - New Zealand'),
                   ('Bachelor degree with Honours - Nigeria', 'Bachelor degree with Honours - Nigeria'),
                   ('Masters degree - Nigeria', 'Masters degree - Nigeria'),
                   ('Bachelor of degree - Pakistan', 'Bachelor of degree - Pakistan'),
                   ('Masters degree (following a two or three - year Bachelor degree) - Pakistan', 'Masters degree (following a two or three - year Bachelor degree) - Pakistan'),
                   ('Master’s degree (following a four - year Bachelor degree) - Pakistan', 'Master’s degree (following a four - year Bachelor degree) - Pakistan'),
                   ('Grado de Académico Bachiller - Peru', 'Grado de Académico Bachiller - Peru'),
                   ('Titulo de Licenciado - Peru', 'Titulo de Licenciado - Peru'),
                   ('Titulo de Maestría - Peru', 'Titulo de Maestría - Peru'),
                   ('Licenciado - Portugal', 'Licenciado - Portugal'),
                   ('Masters degree - Portugal', 'Masters degree - Portugal'),
                   ('Diplomă de Licenţă - Romania', 'Diplomă de Licenţă - Romania'),
                   ('Diplomă de Master - Romania', 'Diplomă de Master - Romania'),
                   ('Bachelor Degree - Russian Federation', 'Bachelor Degree - Russian Federation'),
                   ('Masters degree - Russian Federation', 'Masters degree - Russian Federation'),
                   ('Baccalauréat - Rwanda', 'Baccalauréat - Rwanda'),
                   ('Licence - Rwanda', 'Licence - Rwanda'),
                   ('Ordinary Bachelor degree - Rwanda', 'Ordinary Bachelor degree - Rwanda'),
                   ('Bachelor (Honours) degree - Rwanda', 'Bachelor (Honours) degree - Rwanda'),
                   ('Masters degree - Rwanda', 'Masters degree - Rwanda'),
                   ('Bachelor degree - Sierra Leone', 'Bachelor degree - Sierra Leone'),
                   ('Bachelor degree (Honours) - Sierra Leone', 'Bachelor degree (Honours) - Sierra Leone'),
                   ('Masters degree - Sierra Leone', 'Masters degree - Sierra Leone'),
                   ('Titulo de Grade en [subject area] - Spain', 'Titulo de Grade en [subject area] - Spain'),
                   ('Titulo de Máster - Spain', 'Titulo de Máster - Spain'),
                   ('Bachelor of Science in Computer Science - South Africa', 'Bachelor of Science in Computer Science - South Africa'),
                   ('Honours in Computer Science -  South Africa','Honours in Computer Science -  South Africa'),
                   ('Masters in Computer Science - South Africa', 'Masters in Computer Science - South Africa'),
                   ('Masters in Information Technology - South Africa','Masters in Information Technology - South Africa'),
                   ('Bachelor of Business Science specialising in CS - South Africa', 'Bachelor of Business Science specialising in CS - South Africa'),
                   ('Bachelor of Business Science specialising in IS - South Africa', 'Bachelor of Business Science specialising in IS - South Africa'),
                   ('Bachelor of Commerce specialising in IS - South Africa', 'Bachelor of Commerce specialising in IS - South Africa'),
                   ('Bachelor of Commerce specialising in IS & CS - South Africa', 'Bachelor of Commerce specialising in IS & CS - South Africa'),
                   ('Honours in Information Systems - South Africa', 'Honours in Information Systems - South Africa'),
                   ('Honours in Management Information Systems - South Africa', 'Honours in Management Information Systems - South Africa'),
                   ('Postgraduate Diploma in Management in Information Systems - South Africa','Postgraduate Diploma in Management in Information Systems - South Africa'),
                   ('Masters of Commerce in Information Systems - South Africa', 'Masters of Commerce in Information Systems - South Africa'),
                   ('Bachelor Degree - Sudan', 'Bachelor Degree - Sudan'),
                   ('Master degree - Sudan', 'Master degree - Sudan'),
                   ('Bachelor degree (awarded on completion of part 2) - Swaziland', 'Bachelor degree (awarded on completion of part 2) - Swaziland'),
                   ('Masters degree - Swaziland', 'Masters degree - Swaziland'),
                   ('Bachelor degree - Tanzania', 'Bachelor degree - Tanzania'),
                   ('Masters degree - Tanzania', 'Masters degree - Tanzania'),
                   ('Licence - Tunisia', 'Licence - Tunisia'),
                   ('Master Professionnel - Tunisia', 'Master Professionnel - Tunisia'),
                   ('Bachelor degree - Uganda', 'Bachelor degree - Uganda'),
                   ('Masters degree - Uganda', 'Masters degree - Uganda'),
                   ('Bachelor degree - United States of America', 'Bachelor degree - United States of America'),
                   ('Masters degree - United States of America', 'Masters degree - United States of America'),
                   ('Bachelor degree - Zambia', 'Bachelor degree - Zambia'),
                   ('Postgraduate Diploma - Zambia', 'Postgraduate Diploma - Zambia'),
                   ('Masters degree - Zambia', 'Masters degree - Zambia'),
                   ('Bachelor degree (General) - Zimbabwe', 'Bachelor degree (General) - Zimbabwe'),
                   ('Bachelor degree (Honours) - Zimbabwe', 'Bachelor degree (Honours) - Zimbabwe'),
                   ('Masters degree - Zimbabwe', 'Masters degree - Zimbabwe'),
                   ('Other', 'Other'),
)

POST_DEGREES = (
    ('Honors in Computer Science (full-time)', 'HNs in CS'),
    ('Masters in Information Technology', 'MIT'),
    ('Masters by Coursework and Dissertation', 'MSc by C+D'),
    ('Masters by Dissertation', 'MSc by D'),
    ('PhD in Computer Science', 'PhD in CS'),
    ('Honours in Information System (full-time)', 'Hns in IS'),
    ('Honours in Management Information Systems (part-time)', 'HNs in Manage. IS'),
    ('Postgraduate Diploma in Management in Information Systems (part-time)', 'Postgrad Diploma in Manage. IS'),
    ('Master of Commerce in Information Systems', 'MSc in Commerce in IS'),
    ('PhD in Information Systems', 'PhD in IS')
)
STATUS = (
    ('Application in review', 'Applied'),
    ('Application is successful', 'Accepted'),
    ('Application is unsuccessful', 'Denied'),
    ('Application has been withdrawn', 'Withdrawn')
)

CITIZENSHIP = (
    ('South African citizen', 'SA citizen'),
    ('South African permanent resident', 'SA permanent resident'),
    ('International applicant', 'International')
)

RACE = (
    ('Coloured', 'Coloured'),
    ('Black', 'Black'),
    ('White', 'White'),
    ('Indian', 'Indian')
)

BINARY = (
    ('YES', 'Yes'),
    ('NO', 'No')
)

MATH_EXPERIENCE_OPTIONS = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
)

fs = FileSystemStorage(location='/media')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # cascade: if a user is deleted then delete profile, however if profile is deleted, user remains
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=10, null=True)
    student_number = models.CharField(max_length=10, null=True)
    email_address = models.CharField(max_length=30, null=True)  # citizenship = models.CharField()
    citizenship = models.CharField(max_length=250, choices=CITIZENSHIP, null=True)
    country_of_origin = models.CharField(max_length=250, choices=COUNTRY, blank=True, null=True)
    race = models.CharField(max_length=250, choices=RACE, blank=True, null=True)
    city_of_residence = models.CharField(max_length=30, null=True)
    country_of_residence = models.CharField(max_length=30, choices=COUNTRY, null=True)  # drop down? # prevDegree = models.CharField()
    country_of_previous_institute = models.CharField(max_length=200, choices=COUNTRY, null=True)
    Other_country = models.CharField(max_length=200, blank=True, null=True)
    previous_degree = models.CharField(max_length=200, choices=PREVIOUS_DEGREE, null=True)
    Other_degree = models.CharField(max_length=200, blank=True, null=True)
    nqf_equivalent = models.CharField(max_length=100, null=True)
    minimum_year_of_degree = models.IntegerField(null=True)
    previous_university = models.CharField(max_length=50, null=True)
    degree = models.CharField(max_length=250, choices=POST_DEGREES, null=True)
    years_of_IT_experience = models.IntegerField(blank=True, null=True)
    math_level = models.CharField(max_length=250, choices=MATH_EXPERIENCE_OPTIONS, blank=True, null=True)
    math_average = models.CharField(max_length=50, blank=True, null=True)
    thesis_completed_previously = models.CharField(max_length=10, choices=BINARY,blank=True, null=True)
    thesis_description = models.CharField(max_length=400, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    evaluator = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS, blank=True, null=True)
    upload = models.FileField(upload_to='documents', null=True)


    def get_absolute_url(self):
        return reverse('student_home', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
