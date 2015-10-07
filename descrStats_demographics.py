# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:27:22 2015

@author: oligschlager
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_demographics(f):
    df = pd.read_csv(f, skiprows=1,usecols=['DB_ID', 'Age', 'Gender', 'Day 3'])
    df = df[df['Day 3']=='y']
    
    for idx in range(len(df)):
        if df['Gender'].iloc[idx] == 'M':
            df['Gender'].iloc[idx] = 'm'
        if df['Gender'].iloc[idx] == 'F':
            df['Gender'].iloc[idx] = 'f'
    
    print '\n#### overall cohort ####\n'        
    print 'N = ' + str(len(df))
    print 'N female = ' + str(len(df[df['Gender']=='f']))
    print 'N male = ' + str(len(df[df['Gender']=='m']))
    sns.countplot(df['Gender'])
    plt.show()
    print 'age distribution - female:'
    sns.distplot(df['Age'][df['Gender'] == 'f'])
    plt.show()
    print 'age distribution - male:'
    sns.distplot(df['Age'][df['Gender'] == 'm'])
    plt.show()
    
    print '\n\n#### young cohort ####\n'  
    print 'N = ' + str(len(df[df['Age']<=40]))
    print 'N female = ' + str(len(df[(df['Age']<=40) & (df['Gender']=='f')]))
    print 'N male = ' + str(len(df[(df['Age']<=40) & (df['Gender']=='m')]))
    sns.countplot(df[df['Age']<=40]['Gender'])
    plt.show()
    print 'age distribution - female:'
    sns.distplot(df['Age'][(df['Age']<=40) & (df['Gender'] == 'f')])
    plt.show()
    print 'age distribution - male:'
    sns.distplot(df['Age'][(df['Age']<=40) & (df['Gender'] == 'm')])
    plt.show()