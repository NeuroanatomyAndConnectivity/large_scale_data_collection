# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:27:22 2015

@author: oligschlager
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def run_metainfo(fileA, fileB, fileC_act, fileC_inact, fileC_corrected, fileF, fileG, fileHannes, fileCognTests, fileEdu, fileSKID, out_dir):
    
    # read in data files, calculate age and keep datestamp for later
    df_A = pd.read_csv(fileA)
    df_A['ids'] = df_A['ID'].map(lambda x: str(x)[0:5])
    ageA = pd.Series(pd.to_datetime(df_A['datestamp']) - pd.to_datetime(df_A['GBT']))
    df_A['age_A'] = ageA.dt.days / 365
    df_A['datestamp_A'] = df_A['datestamp']
    
    df_B = pd.read_csv(fileB)
    df_B['ids'] = df_B['ID'].map(lambda x: str(x)[0:5])
    ageB = pd.Series(pd.to_datetime(df_B['datestamp']) - pd.to_datetime(df_B['GBT']))
    df_B['age_B'] = ageB.dt.days / 365
    df_B['datestamp_B'] = df_B['datestamp']
    
    df_C_active = pd.read_csv(fileC_act)
    df_C_inactive = pd.read_csv(fileC_inact)
    df_C_corrected = pd.read_csv(fileC_corrected)
    df_C = pd.concat([df_C_active, df_C_inactive, df_C_corrected])
    df_C['ids'] = df_C['ID'].map(lambda x: str(x)[0:5])
    ageC = pd.Series(pd.to_datetime(df_C['datestamp']) - pd.to_datetime(df_C['GBT']))
    df_C['age_C'] = ageC.dt.days / 365
    df_C['datestamp_C'] = df_C['datestamp']
    
    df_F = pd.read_csv(fileF)
    df_F['ids'] = df_F['ID'].map(lambda x: str(x)[0:5])
    ageF = pd.Series(pd.to_datetime(df_F['datestamp']) - pd.to_datetime(df_F['GBT']))
    df_F['age_F'] = ageF.dt.days / 365
    df_F['datestamp_F'] = df_F['datestamp']
    
    df_G = pd.read_csv(fileG)
    df_G['ids'] = df_G['ID'].map(lambda x: str(x)[0:5])
    ageG = pd.Series(pd.to_datetime(df_G['datestamp']) - pd.to_datetime(df_G['GBT']))
    df_G['age_G'] = ageG.dt.days / 365
    df_G['datestamp_G'] = df_G['datestamp']
    
    df_hannes = pd.read_csv(fileHannes, parse_dates=['test day'])
    df_hannes = df_hannes[df_hannes['done'] == '1']
    df_hannes['ids'] = df_hannes['DB_ID'].map(lambda x: str(x)[0:5])
    df_hannes = pd.merge(df_hannes, df_A[['ids', 'GBT']], on=['ids'], how='left')
    agehannes = pd.Series(pd.to_datetime(df_hannes['test day']) - pd.to_datetime(df_hannes['GBT']))
    df_hannes['age_Hannes'] = agehannes.dt.days / 365
    df_hannes['datestamp_hannes'] = df_hannes['test day']
    
    df_cogntests = pd.read_csv(fileCognTests, parse_dates=['test day'], converters={'done':str})
    df_cogntests = df_cogntests[df_cogntests['done'] == '1']
    df_cogntests['ids'] = df_cogntests['DB_ID'].map(lambda x: str(x)[0:5])
    df_cogntests = pd.merge(df_cogntests, df_A[['ids', 'GBT']], on=['ids'], how='left')
    agecogntests = pd.Series(pd.to_datetime(df_cogntests['test day']) - pd.to_datetime(df_cogntests['GBT']))
    df_cogntests['age_CognTests'] = agecogntests.dt.days / 365
    df_cogntests['datestamp_CognTests'] = df_cogntests['test day']
    

    # merge surveys
    df_meta = pd.merge(df_A[['ids', 'GSH', 'age_A', 'datestamp_A']], df_B[['ids', 'GSH', 'age_B', 'datestamp_B']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_C[['ids', 'GSH', 'age_C', 'datestamp_C']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_F[['ids', 'GSH', 'age_F', 'datestamp_F']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_G[['ids', 'GSH', 'age_G', 'datestamp_G']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_hannes[['ids', 'age_Hannes', 'datestamp_hannes']], on=['ids'], how='outer')
    df_meta = pd.merge(df_meta, df_cogntests[['ids', 'age_CognTests', 'datestamp_CognTests']], on=['ids'], how='outer')
    df_meta.rename(columns={'GSH': 'gender'}, inplace=True)
    
    # calculate time interval between scanning and other surveys
    diffA = pd.Series(pd.to_datetime(df_meta['datestamp_A']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_ref_A'] = diffA.dt.days
    
    diffB = pd.Series(pd.to_datetime(df_meta['datestamp_B']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_ref_B'] = diffB.dt.days
    
    diffC = pd.Series(pd.to_datetime(df_meta['datestamp_C']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_ref_C'] = diffC.dt.days
    
    diffF = pd.Series(pd.to_datetime(df_meta['datestamp_F']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_ref_F'] = diffF.dt.days
    
    diffG = pd.Series(pd.to_datetime(df_meta['datestamp_G']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_ref_G'] = diffG.dt.days
    
    diff_hannes = pd.Series(pd.to_datetime(df_meta['datestamp_hannes']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_ref_Hannes'] = diff_hannes.dt.days
    
    diff_cogntests = pd.Series(pd.to_datetime(df_meta['datestamp_CognTests']) - pd.to_datetime(df_meta['datestamp_C']))
    df_meta['day_ref_CognTests'] = diff_cogntests.dt.days
    
    
    # add info on education
    df_edu = pd.read_csv(fileEdu, converters={'ids':str})
    df_meta = pd.merge(df_meta, df_edu, on='ids', how='left')
    
    # add SKID and drug info
    df_skid = pd.read_csv(fileSKID, skiprows=[0],converters={'DB_ID':str})
    df_skid['ids'] = df_skid['DB_ID'].map(lambda x: str(x)[0:5])
    df_meta = pd.merge(df_meta, df_skid[['ids', 'SKID_Diagnoses', 'Drug_Test (nothing=negative)']], on='ids', how='left')    
        
    # meta info dataframe
    cols_export = ['ids', 'gender', 'age_A', 'age_B', 'age_C', 'age_F', 'age_G', 'age_Hannes', 'age_CognTests',
                   'day_ref_A', 'day_ref_B', 'day_ref_C', 'day_ref_F', 'day_ref_G', 'day_ref_Hannes', 
                   'day_ref_CognTests', 'education', 'SKID_Diagnoses', 'Drug_Test (nothing=negative)']
    
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
    print '\n\n'
    
    for survey in ['A', 'B', 'C', 'F', 'G', 'Hannes', 'CognTests']:
    
        print '\n\n\n#### young cohort, %s ####\n' % survey  
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
    for survey in ['A', 'B', 'F', 'G', 'Hannes', 'CognTests']:
        print '\n\nSurvey %s' % survey
        print 'number of days between scanning and survey'
        print '\n\tmean: ' + str(df['day_ref_%s' % survey].dropna().abs().mean())
        print '\tmedian: ' + str(df['day_ref_%s' % survey].dropna().abs().median())
        print '\tstand. dev.: ' + str(df['day_ref_%s' % survey].dropna().abs().std())
        sns.distplot(df['day_ref_%s' % survey].dropna(), bins=15, kde=False)
        plt.show()