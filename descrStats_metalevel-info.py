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
    
    # read in data files, calculate age and keep datestamp for later
    df_A = pd.read_csv(fileA)
    df_A['ids'] = df_A['ID'].map(lambda x: str(x)[0:5])
    ageA = pd.Series(pd.to_datetime(df_A['datestamp'], format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_A['GBT'], format='%Y-%m-%d %H:%M:%S'))
    df_A['Age day 1'] = ageA.dt.days / 365
    df_A['datestamp_A'] = df_A['datestamp']
    
    df_B = pd.read_csv(fileB)
    df_B['ids'] = df_B['ID'].map(lambda x: str(x)[0:5])
    ageB = pd.Series(pd.to_datetime(df_B['datestamp'], format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_B['GBT'], format='%Y-%m-%d %H:%M:%S'))
    df_B['Age day 2'] = ageB.dt.days / 365
    df_B['datestamp_B'] = df_B['datestamp']
    
    df_C_active = pd.read_csv(fileC_act)
    df_C_inactive = pd.read_csv(fileC_inact)
    df_C_corrected = pd.read_csv(fileC_corrected)
    df_C = pd.concat([df_C_active, df_C_inactive, df_C_corrected])
    df_C['ids'] = df_C['ID'].map(lambda x: str(x)[0:5])
    ageC = pd.Series(pd.to_datetime(df_C['datestamp'], format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_C['GBT'], format='%Y-%m-%d %H:%M:%S'))
    df_C['Age day 3'] = ageC.dt.days / 365
    df_C['datestamp_C'] = df_C['datestamp']
    
    df_F = pd.read_csv(fileF)
    df_F['ids'] = df_F['ID'].map(lambda x: str(x)[0:5])
    ageF = pd.Series(pd.to_datetime(df_F['datestamp'], format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_F['GBT'], format='%m-%d-%Y'))
    df_F['Age day 5a'] = ageF.dt.days / 365
    df_F['datestamp_F'] = df_F['datestamp']
    
    df_G = pd.read_csv(fileG)
    df_G['ids'] = df_G['ID'].map(lambda x: str(x)[0:5])
    ageG = pd.Series(pd.to_datetime(df_G['datestamp'], format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_G['GBT'], format='%m-%d-%Y'))
    df_G['Age day 5b'] = ageG.dt.days / 365
    df_G['datestamp_G'] = df_G['datestamp']
    
    df_hannes = pd.read_csv(fileHannes)#, parse_dates=['test day'])
    df_hannes = df_hannes[df_hannes['done'] == '1']
    df_hannes['ids'] = df_hannes['DB_ID'].map(lambda x: str(x)[0:5])
    df_hannes = pd.merge(df_hannes, df_A[['ids', 'GBT']], on=['ids'], how='left')
    agehannes = pd.Series(pd.to_datetime(df_hannes['test day'], format='%d.%m.%Y') - pd.to_datetime(df_hannes['GBT'], format='%m-%d-%Y'))
    df_hannes['Age day 4'] = agehannes.dt.days / 365
    df_hannes['datestamp_hannes'] = df_hannes['test day']
    
    df_cogntests = pd.read_csv(fileCognTests, converters={'done':str}) # parse_dates=['test day'])
    df_cogntests = df_cogntests[df_cogntests['done'] == '1']
    df_cogntests['ids'] = df_cogntests['DB_ID'].map(lambda x: str(x)[0:5])
    df_cogntests = pd.merge(df_cogntests, df_A[['ids', 'GBT']], on=['ids'], how='left')
    agecogntests = pd.Series(pd.to_datetime(df_cogntests['test day'], format='%d.%m.%Y') - pd.to_datetime(df_cogntests['GBT'], format='%m-%d-%Y'))
    df_cogntests['Age day 6'] = agecogntests.dt.days / 365
    df_cogntests['datestamp_CognTests'] = df_cogntests['test day']
    
    df_lemon = pd.read_csv(fileLemon)
    df_lemon['ids'] = df_lemon['ids'].map(lambda x: str(x)[0:5])
    df_lemon = pd.merge(df_lemon, df_A[['ids', 'GBT']], on=['ids'], how='left')
    age_lemon = pd.Series(pd.to_datetime(df_lemon['lemon1'], format='%d.%m.%y') - pd.to_datetime(df_lemon['GBT'], format='%m-%d-%Y'))
    df_lemon['Age LEMON'] = age_lemon.dt.days / 365

    # merge surveys
    df_meta = pd.merge(df_A[['ids', 'GSH', 'Age day 1', 'datestamp_A']], df_B[['ids', 'GSH', 'Age day 2', 'datestamp_B']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_C[['ids', 'GSH', 'Age day 3', 'datestamp_C']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_F[['ids', 'GSH', 'Age day 5a', 'datestamp_F']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_G[['ids', 'GSH', 'Age day 5b', 'datestamp_G']], on=['ids', 'GSH'], how='outer')
    df_meta = pd.merge(df_meta, df_hannes[['ids', 'Age day 4', 'datestamp_hannes']], on=['ids'], how='outer')
    df_meta = pd.merge(df_meta, df_cogntests[['ids', 'Age day 6', 'datestamp_CognTests']], on=['ids'], how='outer')
    df_meta = pd.merge(df_meta, df_lemon[['ids', 'Age LEMON', 'lemon1', 'lemon2']], on=['ids'], how='left')
    df_meta.rename(columns={'GSH': 'gender'}, inplace=True)
    
    # calculate time interval between scanning and other surveys
    diffA = pd.Series(pd.to_datetime(df_meta['datestamp_A'], format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_meta['datestamp_C'], format='%Y-%m-%d %H:%M:%S'))
    df_meta['Day 1'] = diffA.dt.days
    
    diffB = pd.Series(pd.to_datetime(df_meta['datestamp_B'], format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_meta['datestamp_C'], format='%Y-%m-%d %H:%M:%S'))
    df_meta['Day 2'] = diffB.dt.days
    
    diffC = pd.Series(pd.to_datetime(df_meta['datestamp_C'], format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_meta['datestamp_C'], format='%Y-%m-%d %H:%M:%S'))
    df_meta['Day 3'] = diffC.dt.days
    
    diffF = pd.Series(pd.to_datetime(df_meta['datestamp_F'], format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_meta['datestamp_C'], format='%Y-%m-%d %H:%M:%S'))
    df_meta['Day 5a'] = diffF.dt.days
    
    diffG = pd.Series(pd.to_datetime(df_meta['datestamp_G'], format='%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_meta['datestamp_C'], format='%Y-%m-%d %H:%M:%S'))
    df_meta['Day 5b'] = diffG.dt.days
    
    diff_hannes = pd.Series(pd.to_datetime(df_meta['datestamp_hannes'], format='%d.%m.%Y') - pd.to_datetime(df_meta['datestamp_C'], format='%Y-%m-%d %H:%M:%S'))
    df_meta['Day 4'] = diff_hannes.dt.days
    
    diff_cogntests = pd.Series(pd.to_datetime(df_meta['datestamp_CognTests'], format='%d.%m.%Y') - pd.to_datetime(df_meta['datestamp_C'], format='%Y-%m-%d %H:%M:%S'))
    df_meta['Day 6'] = diff_cogntests.dt.days
    
    diff_lemon_1 = pd.Series(pd.to_datetime(df_meta['lemon1'], format='%d.%m.%y') - pd.to_datetime(df_meta['datestamp_C'], format='%Y-%m-%d %H:%M:%S'))
    df_meta['Day LEMON 1'] = diff_lemon_1.dt.days
    
    diff_lemon_2 = pd.Series(pd.to_datetime(df_meta['lemon2'], format='%d.%m.%y') - pd.to_datetime(df_meta['datestamp_C'], format='%Y-%m-%d %H:%M:%S'))
    df_meta['Day LEMON 2'] = diff_lemon_2.dt.days
     
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
    
    # drug info & cogn task order
    df_drug = pd.read_csv(filePhysio,converters={'DB-ID':str})
    df_drug['ids'] = df_drug['DB-ID'].map(lambda x: str(x)[0:5])
    df_meta = pd.merge(df_meta, df_drug[['ids', 'drug test', 'task order (1=CCPT-ETS, 2=ETS-CCPT)']], on='ids', how='left') 
    
    
    drops  = df_meta[(df_meta['Age day 1'].isnull())
                   & (df_meta['Age day 2'].isnull())
                   & (df_meta['Age day 3'].isnull())
                   & (df_meta['Age day 4'].isnull())
                   & (df_meta['Age day 5a'].isnull())
                   & (df_meta['Age day 5b'].isnull())
                   & (df_meta['Age day 6'].isnull())].index
    
    df_meta = df_meta.drop(df_meta.index[drops])
    
    # meta info dataframe
    cols_export = ['ids', 'gender', 'Age day 1', 'Age day 2', 'Age day 3', 'Age day 4',
                   'Age day 5a', 'Age day 5b', 'Age day 6', 'Age LEMON', 
                   'Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5a', 'Day 5b', 'Day 6', 'Day LEMON 1', 'Day LEMON 2', 
                   'education', 'SKID (0=none, 1=indications, 2=diagnosis)', 'SKID diagnoses', 
                   'drug test', 'task order (1=CCPT-ETS, 2=ETS-CCPT)']
    
    df_meta[cols_export].to_csv('%s/meta_level_info.csv' % out_dir, decimal='.', index=False)   
    return df_meta[cols_export]



def run_demographics(df):
    
    print '\n#### overall cohort, at time of scanning ####\n'        
    print 'N = ' + str(len(df))
    print 'N female = ' + str(len(df[df['gender']==1]))
    print 'N male = ' + str(len(df[df['gender']==2]))
    sns.countplot(df['gender'])
    plt.show()
    print 'age distribution - female:'
    sns.distplot(df['Age day 3'][df['gender'] == 1].dropna())
    plt.show()
    print 'age distribution - male:'
    sns.distplot(df['Age day 3'][df['gender'] == 2].dropna())
    plt.show()
    print '\n\n'
    
    for survey in ['Age day 1', 'Age day 2', 'Age day 3', 'Age day 4', 'Age day 5a', 'Age day 5b', 'Age day 6', 'Age LEMON']:
    
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
    for survey in ['1', '2', '4', '5a', '5b', '6', 'LEMON 1', 'LEMON 2']:
        print '\n\nSurvey %s' % survey
        print 'number of days between scanning and survey'
        print '\n\tmean: ' + str(df['Day %s' % survey].dropna().abs().mean())
        print '\tmedian: ' + str(df['Day %s' % survey].dropna().abs().median())
        print '\tstand. dev.: ' + str(df['Day %s' % survey].dropna().abs().std())
        sns.distplot(df['Day %s' % survey].dropna(), bins=15, kde=False)
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
     