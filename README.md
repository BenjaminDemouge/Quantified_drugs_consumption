# Quantified drug consumption
⚠️ This Readme is a short summary of our project and does not reflect the whole process. To get more details about our approach, please refer to the following documents:
- Our complete Notebook: [Quantified_drug_consumption_notebook.ipynb](https://github.com/flaviendeseure/Quantified_drug_consumption/blob/main/Quantified_drug_consumption_notebook.ipynb)
- The html version of the notebook: [Quantified_drug_consumption_notebook.html](https://github.com/flaviendeseure/Quantified_drug_consumption/blob/main/Quantified_drug_consumption_notebook.html)
- Our powerpoint presentation: [[PPT]Quantified_drug_consumption_flavien_deseure--charron_benjamin_demouge](https://github.com/flaviendeseure/Quantified_drug_consumption/blob/main/[PPT]Quantified_drug_consumption_flavien_deseure--charron_benjamin_demouge.pdf)

## Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Notebook](#notebook)
  - [Website & API](#website-&-api)
    - [Website](#website)
    - [API](#api)
- [Data Vizualisation](#data-vizualisation)
  - [Features](#features)
  - [Targets](#targets)
- [Preprocessing](#preprocessing)
  - [Features](#features)
  - [Targets](#targets)
- [Modeling](#modeling)
- [Selected models](#selected-models)
- [Conclusion](#conclusion)
- [Authors](#authors)
   
  
## About
The objective of this project is to carry out a Data Science project from an imposed dataset. We get the following database: [Drug Consumption Quantified](https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29) from UCI Machine Learning repository.  
  
It is derived from an online survey conducted between 2011 and 2012 among 1885 respondents aged 18 years and older from English-speaking countries.
It collects demographic informations, three personality tests:
- NEO-FFI-R: The Big Five personality test measures the five personality factors that psychologists have determined are core to our personality makeup.
  - Nscore:	Neuroticism - How sensitive a person is to stress and negative emotional triggers.
  - Escore: Extraversion - How much a person is energized by the outside world.	
  - Oscore: Openness - How open a person is to new ideas and experiences.	
  - Ascore: Agreeableness - How much a person puts others' interests and needs ahead of their own.	
  - Cscore: Conscientiousness - How goal-directed, persistent, and organized a person is.	
- BIS11: assess the personality/behavioral construct of impulsiveness 	
- ImpSS: assess various personality characteristics and behaviors related to impulsivity and sensation seeking
   
and 19 central nervous system psychoactive drugs with the following possibilities:
|Never Used | Used over a Decade Ago | Used in Last Decade | Used in Last Year | Used in Last Month | Used in Last Week | Used in Last Day |
|-----------|------------------------|---------------------|-------------------|--------------------|-------------------|------------------|
   
The authors of the survey showed that there is a relationship between risk of addiction to drugs and personnality attributes.    
 
<p align="center">
  <img src="/src/relationships_drugs_personaliy.jpg">
</p>  

From this dataset, we choose to address the following problematic:  
<h3 align="center"><strong>How can we model the risk of addiction to a drug based on personality and demographic data?</strong></h3>  
    
</br>
     
We choose the following drugs with the following classes to answer the problematic:
- For Alcohol, Cannabis, Nicotine, Amphet, Benzos, Coke, Ecstasy, Legalh, LSD, Mushrooms  
   
| Not addicted | Addicted |  
|--------------|----------|  
  
- For Amyl, Crack, Heroin, Ketamine, Meth, VSA  
  
| Never Used | Used |   
|------------|------|  
  
- For Caff  
  
| Not daily addicted | Daily addicted |  
|--------------------|----------------|  
  
</br>
  
This repository contains:  
- Drug Consumption Quantified dataset (if the weblink stop working)
- Requirements file
- Python Notebook (ipynb and html)
- Python Web application Django and API which predicts the addiction to the drugs.
- An example of api used
- PowerPoint Presentation of the project
- Final trained models for each drugs   
  

## Getting Started
### Prerequisites
1. Clone the repository
```bash
git clone https://github.com/flaviendeseure/Quantified_drug_consumption.git
```
2. Install python libraries 
```bash
pip install -r requirements.txt
```

### Notebook
Simply launch the notebook on jupyter!

### Website & API
1. Get to the api directory
```bash
cd PATH_TO_API/api 
```
2. Launch the server
```bash
python manage.py runserver
```
#### Website   
Simply browse on the website  
![](/src/demo_site_web.gif)  
  
#### API  
**Parameters**  
  
|**Feature**| **Format**|  
|:-:|:-:|   
| age | int >= 18 |  
| gender | {"Man", "Woman"} |  
| education | {"Left school before 16 years", "Left school at 16 years", "Left school at 17 years", "Left school at 18 years", "Some college or university, no certificate or degree", "Professional certificate/ diploma", "University degree", "Master's degree","Doctoral degree"} |  
| country | {"Australia", Canada", "New Zealand", "Other", "Republic of Ireland", "UK", "USA"} |  
| ethnicity | {"Asian", Black", "Mixed-Black/Asian", "Mixed-White/Asian", "Mixed-White/Black", "Other", "White"}|  
| nscore | 12 <= int <= 60 |  
| escore | 16 <= int <= 59 |  
| oscore | 24 <= int <= 60 |  
| ascore | 12 <= int <= 60 |  
| cscore | 17 <= int <= 57 |  
| impulsivity | 1 <= int <= 10 |  
| SS | 1 <= int <= 11 |  
  
**Results**
|**Result**| **Description**|  
|:-:|:-:|   
| Addicted | Used last month |  
| Not addicted | Never used in the last month |  
| Used | Used |  
| Never used | Never used |  
| Daily addicted | Used yesterday |  
| Not daily addicted | Not used yesterday |  
  
You can use this python file example (example_api.py)
```python
import requests

age = 18
gender = "Man"
education = "Left school before 16 years"
country = "Australia"
ethnicity = "Asian"
nscore = 12
escore = 16
oscore = 24
ascore = 12
cscore = 17
impulsivity = 1
SS = 1

parameters = [age, gender, education, country, ethnicity, nscore, escore, oscore, ascore, cscore, impulsivity, SS]
parameter_names = ["age", "gender", "education", "country", "ethnicity", "nscore", "escore", "oscore", "ascore", "cscore", "impulsivity", "SS"]

url = 'http://127.0.0.1:8000/api/score/?'

for n, p in zip(parameter_names, parameters):
    url += f"{n}={p}"
    if n != SS:
        url += "&"

r = requests.get(url)

print(r.status_code)
if r.status_code == 200:
    for name, result in r.json().items():
        print(f"{name}: {result}")
else:
    print(r.text)
```

## Data Vizualisation
### Features
The following graph describes the repartition of the number of drugs used per responders. We can clearly identify two groups of people:
- people who have tried less than 6 drugs (47.53%)
- people who have tried more than 7 drugs (52.47%)
![](/src/repartition_nb_drugs.png)  

### Targets
The following graph describes the repartition for each drug of each classes. As expected, we have an imbalanced repartition of data for each class given that for most drugs, majority of people didn't consume drugs.   
![](/src/repartition_class_drugs.png)   

## Preprocessing
### Features
1. **Feature selection**  
Drop feature that will not be used for modelling: ID   
  
2. **Feature encoding**  
Encoding have already been performed on the original dataset, so we just changed the encoding for country and ethnicity (one hot) because there are not ordinal variables.
  
### Targets
1. **Target selection**  
Drop drug that will not be used for modelling: Choc (performances too low due to the popularity of this drug) and Semer(fictif)  
  
2. **Target encoding**  
- First we keep the 7 classes
- Then we group the classes into binary classes

## Modeling
**Metrics**
- Accuracy
- Balanced accuracy
- Confusion matrix  
  
**Technics used (imbalanced data)**
- Weighting
- Sampling: SMOTE
  
**Phases**  
- Initial classes  
We keep the original classes and see what we get.
  - Original models and data
  - Weighting features
  - Sampling features  
  
- New classes  
We create our own classes to obtain better results.
  - Original models and data
  - Weighting features
  - Sampling features  
  
- Tuning hyperparameters  

Finally we obtained the following evaluation balanced accuracy scores:  
![](/src/best_scores.png)  

## Selected models
| Drug      | Model               |   
|-----------|---------------------|  
| Alcohol   | Logistic Regression |  
| Amphet    | Logistic Regression |  
| Amyl      | Logistic Regression |  
| Benzos    | Logistic Regression |  
| Caff      | Logistic Regression |  
| Cannabis  | Logistic Regression |  
| Coke      | SVC                 |  
| Crack     | Logistic Regression |  
| Esctasy   | SVC                 |  
| Heroin    | SVC                 |  
| Ketamine  | SVC                 |  
| Legalh    | SVC                 |  
| LSD       | SVC                 |  
| Meth      | Logistic Regression |  
| Mushrooms | BernoulliNB         |  
| Nicotine  | BernoulliNB         |  
| VSA       | Logistic Regression |  

## Conclusion
Finally the best method to overcome the imbalanced classes in targets was weighting. Thus, we have achieved a mean of 71.24% of balanced accuracy.  
To conclude majors difficulties we encounter were: 
- Lack of data
- Imbalanced classes for the target
- Preprocessed features
- Biased dataset: 
  - young population
  - most people comes from UK
   
## Authors
- [Flavien Deseure--Charron](https://github.com/flaviendeseure)
- [Benjamin Demouge](https://github.com/benjamindemouge)
