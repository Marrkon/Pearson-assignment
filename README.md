# Pearson-assignment

Task for Junior Data Engineer position in Pearson company

## Table of contents
* [Intro](#intro)
* [Requirements](#requirements)
* [Setup](#setup)
* [Usage](#usage)
* [Additional info](#additional info)


## Intro

All the tasks are executable from the terminal (see Usage section), placed in separate .py files. Alternatively they are solved in jupyter notebook ***ETL.ipynb***

## Requirements

pandas==0.25.3  
numpy==1.17.3

## Setup

To instal above requrements, navigate to the main folder of the repository, and run below command:

```python

pip3 install -r requirements.txt

```

## Usage

Return test.csv, test_level.csv, class_csv
```python
python3 task1.py
```
Return filtered test.csv
```python
python3 task2.py
```
Return test_utilization
```python
python3 task3.py
```
Return test_average_scores
```python
python3 task4.py
```
Prepare test_utilization.csv and test_average_scores.csv
```python
python3 task5.py
```

## Additional info

- _avg_class_test_overall_score_ in ***test_average_scores.csv*** has been rounded to 2 decimal places
- some of the classes has empty _avg_class_test_overall_score_ despite they are authorized and have SCORING_SCORED status. They have just empty _overall_score_ column on every relevant test.
- some of the classes have no relevant tests and can be deleted from ***classes.csv***
- in ***test_average_scores.csv*** _test_created_at_ is the earliest date when test appeared. _Test_authorized_at_ is the oldest date of authorization.
