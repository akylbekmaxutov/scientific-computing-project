import streamlit as st
import numpy as np
from PIL import Image

# ================================================================================

# Images
image_data = Image.open("images/data.png")
image_prep_data = Image.open("images/prep-data.png")
image_education_data = Image.open("images/education-data.png")
image_lunch_data = Image.open("images/lunch-data.png")

image_race = Image.open("images/race-ethnicity-plot.png")
image_gender = Image.open("images/gender-plot.png")
image_lunch = Image.open("images/lunch-plot.png")
image_preparation = Image.open("images/preparation-plot.png")
image_education = Image.open("images/education.png")

image_grades = Image.open("images/grade-distribution.png")
image_total = Image.open("images/total-grade.png")

# ================================================================================

# Numpy files
option_gender = np.load('np_files/gender.npy', allow_pickle=True)
option_race = np.load('np_files/race.npy', allow_pickle=True)
option_education = np.load('np_files/education.npy', allow_pickle=True)
option_lunch = np.load('np_files/lunch.npy', allow_pickle=True)
option_preparation = np.load('np_files/test_prep.npy', allow_pickle=True)

coefs = np.load('np_files/coefs.npy')

# ================================================================================

# Page Title
st.title("Students Performance Prediction on the Exam")

# ================================================================================

# Header
st.header("Introduction:")
intro_txt = '''
During the university application process, applicants are required to complete 
a survey as part of the application form. This survey typically encompasses 
a wide range of questions related to the applicant's economic, sociological, 
and ethnic background. Such information is valuable for admission departments 
to gain insight into the diverse characteristics of the applicants.

-------------------------------------------------------------------------------

For instance, at Nazarbayev University, students applying to Bachelor programs 
or the Foundation program are presented with a variety of questions. 
These questions may cover aspects such as:

1. Gender
2. Ethnicity
3. Educational background of parents

In response to the current trend where many students utilize external services 
during their preparation period, the application form may also include queries 
to understand the extent to which these external courses contribute to the 
applicant's readiness. This additional information aids in comprehending the 
effectiveness and impact of external resources on the applicants' preparedness 
for university studies.
'''
st.text(intro_txt)

# ================================================================================

# Presentation parts
st.header("Objectives:")
st.subheader("Project-wise:")
project_goals = '''
1. Understanding the Influence of Parental Education on Children's Grades
2. Exploring the Impact of Utilizing External Services on Applicant's Academic 
Performance
3. Considering Whether Having a Meal Before an Exam is Beneficial for Applicants
'''
st.text(project_goals)
st.subheader("Personal:")
personal_goals = '''
1. Achieving an End-to-End Data Science Project
2. Harnessing the Power of Streamlit Apps to Present Analysis Results in a 
User-Friendly Manner
3. Implementing a Test-Driven Approach by Designing Tests
4. Enhancing Proficiency in Version Control Systems for Systematic Project 
Development
'''
st.text(personal_goals)

# ================================================================================

# Software presentation 
st.header("Softwares:")
st.subheader('Python')
softwares = '''
1. Numpy => Numerical Calculations
2. Pandas => Data Analysis
3. Matplotlib => Visualizations
4. Seaborn => Visualizations
5. Sci-kit Learn => Machine Learning Models
6. Streamlit => User Interface
7. Git and GitHub => Version Control
'''
st.text(softwares)

# ================================================================================

# Data presentation
st.header("Model Formulation")
st.subheader('Data Analysis')
st.image(image_data, caption="Table 1. Given Data", use_column_width=True)

st.text('Sociological Data')
st.image(image_race, caption='Figure 1. Race', use_column_width=True)
st.image(image_gender, caption='Figure 2. Gender', use_column_width=True)

st.text('Score Distribution')
st.image(image_grades, caption="Figure 3. Score Distribution", use_column_width=True)
st.image(image_total, caption="Figure 4. Total Score Distribution", use_column_width=True)

st.text('Data related to the Parental Education')
st.image(image_education, caption='Figure 5. Parental Education', use_column_width=True)
st.image(image_education_data, caption='Table 2. Parental Education', use_column_width=True)

st.text('Data related to the Applicants Preparation')
st.image(image_preparation, caption='Figure 6. Test Preparation', use_column_width=True)
st.image(image_prep_data, caption='Table 3. Test Preparation', use_column_width=True)

st.text('LUNCH')
st.image(image_lunch, caption='Figure 7. Did you have Lunch before Exam?', use_column_width=True)
st.image(image_lunch_data, caption='Table 4. Did you have Lunch before Exam?', use_column_width=True)

# ================================================================================

# ML model
st.subheader('Machine Learning Model')
st.text('Linear Regression')
units = '''
x1 - Gender of an Applicant
x2 - Race of an Applicant
x3 - the Parental Education of an Applicant
x4 - Did an Applicant have a lunch before the exam?
x5 - Did an Applicant attend courses to prepare?
'''
st.text(units)

st.text('Equation to Calculate the Math Score:')
st.text(f'''
Math Score = {round(coefs[0][0], 3)} * x1 + {round(coefs[0][1], 3)} * x2 {round(coefs[0][2], 3)} * x3 + {round(coefs[0][3], 3)} * x4 {round(coefs[0][4], 3)} * x5 + {round(coefs[0][5], 3)}
Root Mean Squared Error = 13.284
R^2 = 0.232

Writing Score = {round(coefs[1][0], 3)} * x1 + {round(coefs[1][1], 3)} * x2 {round(coefs[1][2], 3)} * x3 + {round(coefs[1][3], 3)} * x4 {round(coefs[1][4], 3)} * x5 + {round(coefs[1][5], 3)}
Root Mean Squared Error = 12.727
R^2 = 0.255

Reading Score = {round(coefs[2][0], 3)} * x1 + {round(coefs[2][1], 3)} * x2 {round(coefs[2][2], 3)} * x3 + {round(coefs[2][3], 3)} * x4 {round(coefs[2][4], 3)} * x5 + {round(coefs[2][5], 3)}
Root Mean Squared Error = 13.203
R^2 = 0.171
''')

# ================================================================================

# User Input
st.subheader("Let's test: ")

inputs = []
user_input_gender = int(st.number_input('Enter your gender'))
gender_txt = '''
Options are:
1. female => 1
2. male => 2
'''
st.text(gender_txt)
inputs.append(user_input_gender)

user_input_race = int(st.number_input('Enter your ethnicity'))
race_txt = '''
Options are:
1. Group A => 1
2. Group B => 2
3. Group C => 3
4. Group D => 4
5. Group E => 5
'''
st.text(race_txt)
inputs.append(user_input_race)

user_input_education = int(st.number_input('Enter the education level of your parents'))
education_txt = '''
Options are:
1. Associate's Degree => 1
2. Bachelor's Degree => 2
3. High School => 3
4. Master's Degree => 4
5. Some College => 5
6. Some High School => 6
'''
st.text(education_txt)
inputs.append(user_input_education)

user_input_lunch = int(st.number_input('Did you have a lunch before the exam?'))
lunch_txt = '''
Options are:
1. No or Partially (free/reduced) => 1
2. Yes (standard lunch) => 2
'''
st.text(lunch_txt)
inputs.append(user_input_lunch)

user_input_preparation = int(st.number_input('Did you attend preparation courses?'))
preparation_txt = '''
Options are:
1. Yes (completed) => 1
2. No (none) => 2
'''
st.text(preparation_txt)
inputs.append(user_input_preparation)

st.subheader('Testing results')

def tests(inputs):
    test_results = np.zeros(5)
    # Input Tests
    # test 1
    if (inputs[0]-1 in list(option_gender)):
        st.write("<font color='green'>Test 1 --- Passed</font>", unsafe_allow_html=True)
        st.text('Gender of the user is in the correct range')
        test_results[0] = 0
    else:
        st.write("<font color='red'>Test 1 --- Failed</font>", unsafe_allow_html=True)
        st.text('Gender of the user is not in the correct range')
        test_results[0] = 1

    # test 2
    if (inputs[1]-1 in list(option_race)):
        st.write("<font color='green'>Test 2 --- Passed</font>", unsafe_allow_html=True)
        st.text('Ethnicity of the user is in the correct range')
        test_results[1] = 0
    else:
        st.write("<font color='red'>Test 2 --- Failed</font>", unsafe_allow_html=True)
        st.text('Ethnicity of the user is not in the correct range')
        test_results[1] = 1

    # test 3
    if (inputs[2]-1 in list(option_education)):
        st.write("<font color='green'>Test 3 --- Passed</font>", unsafe_allow_html=True)
        st.text('Education of Parents of the user is in the correct range')
        test_results[2] = 0
    else:
        st.write("<font color='red'>Test 3 --- Failed</font>", unsafe_allow_html=True)
        st.text('Education of Parents of the user is not in the correct range')
        test_results[2] = 1

    # test 4
    if (inputs[3]-1 in list(option_lunch)):
        st.write("<font color='green'>Test 4 --- Passed</font>", unsafe_allow_html=True)
        st.text('Question did user have a lunch is in the correct range')
        test_results[3] = 0
    else:
        st.write("<font color='red'>Test 4 --- Failed</font>", unsafe_allow_html=True)
        st.text('Question did user have a lunch is not in the correct range')
        test_results[3] = 1

    # test 5
    if (inputs[4]-1 in list(option_preparation)):
        st.write("<font color='green'>Test 5 --- Passed</font>", unsafe_allow_html=True)
        st.text('Preparation of the user is in the correct range')
        test_results[4] = 0
    else:
        st.write("<font color='red'>Test 5 --- Failed</font>", unsafe_allow_html=True)
        st.text('Preparation of the user a lunch is not in the correct range')
        test_results[4] = 0

    return test_results

if (0 not in inputs):
    results = tests(inputs)
else:
    st.text('You have not entered all information!')
user_input = np.ones(6)

