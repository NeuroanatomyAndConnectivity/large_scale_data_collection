# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:27:22 2015

@author: oligschlager
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def run_metainfo(fileA, fileB, fileC_act, fileC_inact, fileC_corrected, fileF, fileG, fileEdu, out_dir):
    
    # read in data files, calculate age and keep datestamp for later
    df_A = pd.read_csv(survA_f)
    df_A['ids'] = df_A['ID'].map(lambda x: str(x)[0:5])
    ageA = pd.Series(pd.to_datetime(df_A['datestamp']) - pd.to_datetime(df_A['GBT']))
    df_A['age_A'] = ageA.dt.days / 365
    df_A['datestamp_A'] = df_A['datestamp']
    
    df_B = pd.read_csv(survB_f)
    df_B['ids'] = df_B['ID'].map(lambda x: str(x)[0:5])
    ageB = pd.Series(pd.to_datetime(df_B['datestamp']) - pd.to_datetime(df_B['GBT']))
    df_B['age_B'] = ageB.dt.days / 365
    df_B['datestamp_B'] = df_B['datestamp']
    
    df_C_active = pd.read_csv(survC_active_f)
    df_C_inactive = pd.read_csv(survC_inactive_f)
    df_C_corrected = pd.read_csv(survC_corrected_f)
    df_C = pd.concat([df_C_active, df_C_inactive, df_C_corrected])
    df_C['ids'] = df_C['ID'].map(lambda x: str(x)[0:5])
    ageC = pd.Series(pd.to_datetime(df_C['datestamp']) - pd.to_datetime(df_C['GBT']))
    df_C['age_C'] = ageC.dt.days / 365
    df_C['datestamp_C'] = df_C['datestamp']
    
    df_F = pd.read_csv(survF_f)
    df_F['ids'] = df_F['ID'].map(lambda x: str(x)[0:5])
    ageF = pd.Series(pd.to_datetime(df_F['datestamp']) - pd.to_datetime(df_F['GBT']))
    df_F['age_F'] = ageF.dt.days / 365
    df_F['datestamp_F'] = df_F['datestamp']
    
    df_G = pd.read_csv(survG_f)
    df_G['ids'] = df_G['ID'].map(lambda x: str(x)[0:5])
    ageG = pd.Series(pd.to_datetime(df_G['datestamp']) - pd.to_datetime(df_G['GBT']))
    df_G['age_G'] = ageG.dt.days / 365
    df_G['datestamp_G'] = df_G['datestamp']
    
    # merge surveys
    df_meta = pd.merge(df_A[['ids', 'GSH', 'age_A', 'datestamp_A']], df_B[['ids', 'GSH', 'age_B', 'datestamp_B']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_C[['ids', 'GSH', 'age_C', 'datestamp_C']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_F[['ids', 'GSH', 'age_F', 'datestamp_F']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_G[['ids', 'GSH', 'age_G', 'datestamp_G']], on=['ids', 'GSH'], how='outer')
    df_meta.rename(columns={'GSH': 'gender'}, inplace=True)
    
    # calculate time interval between scanning and other surveys
    diffA = pd.Series(pd.to_datetime(df_meta['datestamp_A']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_diff_A'] = diffA.dt.days
    
    diffB = pd.Series(pd.to_datetime(df_meta['datestamp_B']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_diff_B'] = diffB.dt.days
    
    diffC = pd.Series(pd.to_datetime(df_meta['datestamp_C']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_diff_C'] = diffC.dt.days
    
    diffF = pd.Series(pd.to_datetime(df_meta['datestamp_F']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_diff_F'] = diffF.dt.days
    
    diffG = pd.Series(pd.to_datetime(df_meta['datestamp_G']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_diff_G'] = diffG.dt.days
    
    # add info on education
    df_edu = pd.read_csv(edu_f, converters={'ids':str})
    df_meta = pd.merge(df_meta, df_edu, on='ids', how='left')
    
    # meta info dataframe
    cols_export = ['ids', 'gender', 'age_A', 'age_B', 'age_C', 'age_F', 'age_G',
                   'day_diff_A', 'day_diff_B', 'day_diff_C', 'day_diff_F', 'day_diff_G', 'education']
    
    df_meta[cols_export].to_csv('%s/meta_level_info.csv' % out_dir)   
    return df_meta[cols_export]




def run_demographics(df):
    
    print '\n#### overall cohort, at time of scanning ####\n'        
    print 'N = ' + str(len(df))
    print 'N female = ' + str(len(df[df['gender']==1]))
    print 'N male = ' + str(len(df[df['gender']==2]))
    sns.countplot(df['gender'])
    plt.show()
    print 'age distribution - female:'
    sns.distplot(df['age_C'][df['gender'] == 1].dropna())
    plt.show()
    print 'age distribution - male:'
    sns.distplot(df['age_C'][df['gender'] == 2].dropna())
    plt.show()
    
    
    for survey in ['A', 'B', 'C', 'F', 'G']:
    
        print '\n\n#### young cohort, Survey %s ####\n' % survey  
        print 'N = ' + str(len(df[df['age_%s' % survey]<=40]))
        print 'N female = ' + str(len(df[(df['age_%s' % survey]<=40) & (df['gender']==1)]))
        print 'N male = ' + str(len(df[(df['age_%s' % survey]<=40) & (df['gender']==2)]))
        sns.countplot(df[df['age_%s' % survey]<=40]['gender'])
        plt.show()
        print 'age distribution - female:'
        sns.distplot(df['age_%s' % survey][(df['age_%s' % survey]<=40) & (df['gender'] == 1)].dropna(), bins=15)
        plt.show()
        print 'age distribution - male:'
        sns.distplot(df['age_%s' % survey][(df['age_%s' % survey]<=40) & (df['gender'] == 2)].dropna(), bins=15)
        plt.show()
        


def run_studycourse(df):
    for survey in ['A', 'B', 'F', 'G']:
        print '\n\nSurvey %s' % survey
        print 'number of days between scanning and survey'
        print '\n\tmean: ' + str(df['day_diff_%s' % survey].dropna().abs().mean())
        print '\tmedian: ' + str(df['day_diff_%s' % survey].dropna().abs().median())
        print '\tstand. dev.: ' + str(df['day_diff_%s' % survey].dropna().abs().std())
        sns.distplot(df['day_diff_%s' % survey].dropna(), bins=15, kde=False)
        plt.show()