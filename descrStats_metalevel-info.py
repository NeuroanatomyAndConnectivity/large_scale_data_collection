# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:27:22 2015

@author: oligschlager
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def run_metainfo(fileA, fileB, fileC_act, fileC_inact, fileC_corrected, fileF, fileG, 
                 fileHannes, fileCognTests, fileEdu, fileSKID, filePhysio, fileLemon, out_dir):
    
    # read in data files,  keep datestamp for later, merge all
    
    df_A = pd.read_csv(fileA)
    df_A['ids'] = df_A['ID'].map(lambda x: str(x)[0:5])
    df_A['datestamp_A'] = pd.to_datetime(df_A['datestamp'], format='%Y-%m-%d %H:%M:%S')
    df_A['GBT'] = pd.to_datetime(df_A['GBT'], format='%Y-%m-%d %H:%M:%S')
    
    df_B = pd.read_csv(fileB)
    df_B['ids'] = df_B['ID'].map(lambda x: str(x)[0:5])    
    df_B['datestamp_B'] = pd.to_datetime(df_B['datestamp'], format='%Y-%m-%d %H:%M:%S')
    df_meta = pd.merge(df_A[['ids', 'GSH', 'GBT', 'datestamp_A']], df_B[['ids', 'GSH', 'datestamp_B']], on=['ids', 'GSH'], how='outer')
    del df_A, df_B
    
    df_C_active = pd.read_csv(fileC_act)
    df_C_inactive = pd.read_csv(fileC_inact)
    df_C_corrected = pd.read_csv(fileC_corrected)
    df_C = pd.concat([df_C_active, df_C_inactive, df_C_corrected])
    df_C['ids'] = df_C['ID'].map(lambda x: str(x)[0:5])
    df_C['datestamp_C'] = pd.to_datetime(df_C['datestamp'], format='%Y-%m-%d %H:%M:%S')
    df_meta = pd.merge(df_meta, df_C[['ids', 'GSH', 'datestamp_C']], on=['ids', 'GSH'], how='outer')
    del df_C
    
    df_F = pd.read_csv(fileF)
    df_F['ids'] = df_F['ID'].map(lambda x: str(x)[0:5])
    df_F['datestamp_F'] = pd.to_datetime(df_F['datestamp'], format='%Y-%m-%d %H:%M:%S')
    df_meta = pd.merge(df_meta, df_F[['ids', 'GSH', 'datestamp_F']], on=['ids', 'GSH'], how='outer')
    del df_F
    
    df_G = pd.read_csv(fileG)
    df_G['ids'] = df_G['ID'].map(lambda x: str(x)[0:5])
    df_G['datestamp_G'] = pd.to_datetime(df_G['datestamp'], format='%Y-%m-%d %H:%M:%S')
    df_meta = pd.merge(df_meta, df_G[['ids', 'GSH', 'datestamp_G']], on=['ids', 'GSH'], how='outer')
    del df_G
    
    df_hannes = pd.read_csv(fileHannes, parse_dates=['test day'])
    df_hannes = df_hannes[df_hannes['done'] == '1']
    df_hannes['ids'] = df_hannes['DB_ID'].map(lambda x: str(x)[0:5])
    df_hannes['datestamp_hannes'] = pd.to_datetime(df_hannes['test day'], format='%d.%m.%Y')
    df_meta = pd.merge(df_meta, df_hannes[['ids', 'datestamp_hannes']], on=['ids'], how='left')
    del df_hannes
    
    df_cogntests = pd.read_csv(fileCognTests, converters={'done':str}, parse_dates=['test day'])
    df_cogntests = df_cogntests[df_cogntests['done'] == '1']
    df_cogntests['ids'] = df_cogntests['DB_ID'].map(lambda x: str(x)[0:5])
    df_cogntests['datestamp_CognTests'] = pd.to_datetime(df_cogntests['test day'], format='%d.%m.%Y')
    df_meta = pd.merge(df_meta, df_cogntests[['ids', 'datestamp_CognTests']], on=['ids'], how='left')
    del df_cogntests
    
    df_lemon = pd.read_csv(fileLemon, parse_dates=['lemon1'], dayfirst=True)
    df_lemon['ids'] = df_lemon['ids'].map(lambda x: str(x)[0:5])    
    df_lemon['datestamp_lemon1'] = df_lemon['lemon1']
    df_meta = pd.merge(df_meta, df_lemon[['ids', 'datestamp_lemon1']], on=['ids'], how='left')
    
    df_lemon = pd.read_csv(fileLemon, parse_dates=['lemon2'], dayfirst=True)
    df_lemon['ids'] = df_lemon['ids'].map(lambda x: str(x)[0:5])
    df_lemon['datestamp_lemon2'] = df_lemon['lemon2']
    df_meta = pd.merge(df_meta, df_lemon[['ids', 'datestamp_lemon2']], on=['ids'], how='left')
    
    df_lemon = pd.read_csv(fileLemon, parse_dates=['lemon3'], dayfirst=True)
    df_lemon['ids'] = df_lemon['ids'].map(lambda x: str(x)[0:5])
    df_lemon['datestamp_lemon3'] = df_lemon['lemon3']
    df_meta = pd.merge(df_meta, df_lemon[['ids', 'datestamp_lemon3']], on=['ids'], how='left')
    del df_lemon
    
    df_meta.rename(columns={'GSH': 'gender'}, inplace=True)
    
    # calculate age 
    df_meta['age day 1'] = pd.Series(df_meta['datestamp_A'] - df_meta['GBT']).dt.days / 365
    df_meta['age day 2'] = pd.Series(df_meta['datestamp_B'] - df_meta['GBT']).dt.days / 365
    df_meta['age day 3'] = pd.Series(df_meta['datestamp_C'] - df_meta['GBT']).dt.days / 365
    df_meta['age day 5a'] = pd.Series(df_meta['datestamp_F'] - df_meta['GBT']).dt.days / 365
    df_meta['age day 5b'] = pd.Series(df_meta['datestamp_G'] - df_meta['GBT']).dt.days / 365
    df_meta['age day 4'] = pd.Series(df_meta['datestamp_hannes'] - df_meta['GBT']).dt.days / 365
    df_meta['age day 6'] = pd.Series(df_meta['datestamp_CognTests'] - df_meta['GBT']).dt.days / 365
    df_meta['age LEMON'] = pd.Series(df_meta['datestamp_lemon1'] - df_meta['GBT']).dt.days / 365
    
    
    # calculate time interval between scanning and other surveys
    df_meta['day 1'] = pd.Series(df_meta['datestamp_A'] - df_meta['datestamp_C']).dt.days
    df_meta['day 2'] = pd.Series(df_meta['datestamp_B'] - df_meta['datestamp_C']).dt.days
    df_meta['day 3'] = pd.Series(df_meta['datestamp_C'] - df_meta['datestamp_C']).dt.days
    df_meta['day 5a'] = pd.Series(df_meta['datestamp_F'] - df_meta['datestamp_C']).dt.days
    df_meta['day 5b'] = pd.Series(df_meta['datestamp_G'] - df_meta['datestamp_C']).dt.days
    df_meta['day 4'] = pd.Series(df_meta['datestamp_hannes'] - df_meta['datestamp_C']).dt.days
    df_meta['day 6'] = pd.Series(df_meta['datestamp_CognTests'] - df_meta['datestamp_C']).dt.days
    df_meta['day LEMON 1'] = pd.Series(df_meta['datestamp_lemon1'] - df_meta['datestamp_C']).dt.days
    df_meta['day LEMON 2'] = pd.Series(df_meta['datestamp_lemon2'] - df_meta['datestamp_C']).dt.days
    df_meta['day LEMON 3'] = pd.Series(df_meta['datestamp_lemon3'] - df_meta['datestamp_C']).dt.days
    
    
    # add info on education
    df_edu = pd.read_csv(fileEdu, converters={'ids':str})
    entries = ['Keinen Schulabschluss',
               'Ohne Hauptschulabschluss/Volksschulabschluss',
               'Hauptschulabschluss/Volksschulabschluss',
               'Realschulabschluss/Mittlere Reife',
               'Abschluss einer Sonderschule/Förderschule',
               'Abschluss der Polytechnischen Oberschule, 10. Klasse vor 1965: 8. Klasse.',
               'Fachhochschulreife, Abschluss Fachoberschule',
               'Allgemeine oder fachgebundene Hochschulreife/Abitur Gymnasium bzw. EOS, auch EOS mit Lehre.',
               'Sonstiges']
    for n,entry in enumerate(entries):
        df_edu['education'][df_edu['education'] == entry] = n+1
    df_meta = pd.merge(df_meta, df_edu, on='ids', how='left')
    
    # add SKID
    df_skid = pd.read_csv(fileSKID, skiprows=[0],converters={'DB_ID':str})
    df_skid['ids'] = df_skid['DB_ID'].map(lambda x: str(x)[0:5])
    df_meta = pd.merge(df_meta, df_skid[['ids', 'SKID (0=none, 1=indications, 2=diagnosis)', 'SKID diagnoses']], on='ids', how='left')
    df_meta.rename(columns={'SKID (0=none, 1=indications, 2=diagnosis)': 'SKID key', 'SKID diagnoses':'SKID description'}, inplace=True)
    
    # drug info & cogn task order
    df_drug = pd.read_csv(filePhysio,converters={'DB-ID':str})
    df_drug['ids'] = df_drug['DB-ID'].map(lambda x: str(x)[0:5])
    df_meta = pd.merge(df_meta, df_drug[['ids', 'drug test', 'task order (1=CCPT-ETS, 2=ETS-CCPT)']], on='ids', how='left')
    df_meta.rename(columns={'task order (1=CCPT-ETS, 2=ETS-CCPT)': 'task order'}, inplace=True)
    
    
    drops  = df_meta[(df_meta['age day 1'].isnull())
                   & (df_meta['age day 2'].isnull())
                   & (df_meta['age day 3'].isnull())
                   & (df_meta['age day 4'].isnull())
                   & (df_meta['age day 5a'].isnull())
                   & (df_meta['age day 5b'].isnull())
                   & (df_meta['age day 6'].isnull())].index
    
    df_meta = df_meta.drop(df_meta.index[drops])
    
    # meta info dataframe
    cols_export = ['ids', 'gender', 'age day 1', 'age day 2', 'age day 3', 'age day 4',
                   'age day 5a', 'age day 5b', 'age day 6', 'age LEMON', 
                   'day 1', 'day 2', 'day 3', 'day 4', 'day 5a', 'day 5b', 'day 6', 
                   'day LEMON 1', 'day LEMON 2', 'day LEMON 3',
                   'education', 'SKID key', 'SKID description', 'drug test', 'task order']
    
    df_meta[cols_export].to_csv('%s/meta_info.csv' % out_dir, decimal='.', index=False)   
    return df_meta[cols_export]



def run_demographics(df):
    
    print '\n#### overall cohort, at time of scanning ####\n'        
    print 'N = ' + str(len(df))
    print 'N female = ' + str(len(df[df['gender']==1]))
    print 'N male = ' + str(len(df[df['gender']==2]))
    sns.countplot(df['gender'])
    plt.show()
    print 'age distribution - female:'
    sns.distplot(df['age day 3'][df['gender'] == 1].dropna())
    plt.show()
    print 'age distribution - male:'
    sns.distplot(df['age day 3'][df['gender'] == 2].dropna())
    plt.show()
    print '\n\n'
    
    for survey in ['age day 1', 'age day 2', 'age day 3', 'age day 4', 'age day 5a', 'age day 5b', 'age day 6', 'age LEMON']:
    
        print '\n\n\n#### young cohort, %s ####\n' % survey  
        print 'N = ' + str(len(df[df[survey]<=40]))
        print 'N female = ' + str(len(df[(df[survey]<=40) & (df['gender']==1)]))
        print 'N male = ' + str(len(df[(df[survey]<=40) & (df['gender']==2)]))
        sns.countplot(df[df[survey]<=40]['gender'])
        plt.show()
        print 'age distribution - female:'
        sns.distplot(df[survey][(df[survey]<=40) & (df['gender'] == 1)].dropna(), bins=15)
        plt.show()
        print 'age distribution - male:'
        sns.distplot(df[survey][(df[survey]<=40) & (df['gender'] == 2)].dropna(), bins=15)
        plt.show()
        


def run_studycourse(df):
    for survey in ['1', '2', '4', '5a', '5b', '6', 'LEMON 1']:
        print '\n\nSurvey %s' % survey
        print 'number of days between scanning and survey'
        print '\n\tmean: ' + str(df['day %s' % survey].dropna().abs().mean())
        print '\tmedian: ' + str(df['day %s' % survey].dropna().abs().median())
        print '\tstand. dev.: ' + str(df['day %s' % survey].dropna().abs().std())
        sns.distplot(df['day %s' % survey].dropna(), bins=15, kde=False)
        plt.show()
        
        

def run_physio(filePhysio, out_dir):
    
    df = pd.read_csv(filePhysio, converters={'DB-ID':str})
    df['ids'] = df['DB-ID'].map(lambda x: str(x)[0:5])
    
    cols_export = ['ids', 'systolic blood pressure', 'diastolic blood pressure', 
                   'pulse', 'arm length']    
    df[cols_export].to_csv('%s/physio.csv' % out_dir, decimal='.', index=False)
    
    
    for col in cols_export[1:]:
        
        print '\n%s' % col
        sns.distplot(df[col].dropna())
        plt.show()
        
    return df
     