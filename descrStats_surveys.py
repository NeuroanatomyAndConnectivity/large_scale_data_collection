# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:35:28 2015

@author: oligschlager
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


##############################################################################
########################## self control scale ################################
##############################################################################

def run_SelfCtrl(df, out_dir=None):
    #items to be recoded                                
    items_recoded = ['SCSaBASEQ[SCS2r]',
                     'SCSaBASEQ[SCS3r]',
                     'SCSaBASEQ[SCS4r]',
                     'SCSaBASEQ[SCS5r]',
                     'SCSaBASEQ[SCS6r]',
                     'SCSbBASEQ[SCS7r]',
                     'SCSbBASEQ[SCS8r]',
                     'SCSbBASEQ[SCS9r]',
                     'SCSbBASEQ[SCS10r]',
                     'SCSbBASEQ[SCS11r]' ]    
                             
    #recode items                 
    recoder = {1: 5, 2: 4, 4: 2, 5: 1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   

    #Calculate total score as the sum of Item 1-13.
    
    cols = ['SCSaBASEQ[SCS1]',
            'SCSaBASEQ[SCS2r]',
            'SCSaBASEQ[SCS3r]',
            'SCSaBASEQ[SCS4r]',
            'SCSaBASEQ[SCS5r]',
            'SCSaBASEQ[SCS6r]',
            'SCSbBASEQ[SCS7r]',
            'SCSbBASEQ[SCS8r]',
            'SCSbBASEQ[SCS9r]',
            'SCSbBASEQ[SCS10r]',
            'SCSbBASEQ[SCS11r]',
            'SCSbBASEQ[SCS12]',
            'SCSbBASEQ[SCS13]']    
    
    df['SelfCtrl_sum'] = df[cols].sum(axis=1)
                      
    print "Questionnaire measures self control (total score is calculated as the sum of the 13 items)\n"   
    print df["SelfCtrl_sum"].describe() 
    sns.distplot(df["SelfCtrl_sum"].dropna(), kde = True)
    
    if out_dir:
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ["SelfCtrl_sum"]        
        df[cols_export].to_csv('%s/SCS.csv' % out_dir, index=False)
        
    


##############################################################################                      
################ Internet Addiction test #####################################
##############################################################################
#note: Item 3 not included due to differerent scale format

def run_IAT(df, out_dir=None):
                              
    #Calculate total score as the sum of Item 1-19.
    
    cols = ['IATaBASEQ[IAT1]',
            'IATaBASEQ[IAT2]',
            'IATcBASEQ[IAT4]',
            'IATcBASEQ[IAT5]',
            'IATcBASEQ[IAT6]',
            'IATcBASEQ[IAT7]',
            'IATcBASEQ[IAT8]',
            'IATcBASEQ[IAT9]',
            'IATcBASEQ[IAT10]',
            'IATcBASEQ[IAT11]',
            'IATcBASEQ[IAT12]',
            'IATcBASEQ[IAT13]',
            'IATcBASEQ[IAT14]',
            'IATdBASEQ[IAT15]',
            'IATdBASEQ[IAT16]',
            'IATdBASEQ[IAT17]',
            'IATdBASEQ[IAT18]',
            'IATdBASEQ[IAT19]',
            'IATdBASEQ[IAT20]']    
    df['IAT_sum'] = df[cols].sum(axis=1)
    
    print "Questionnaire measures internet addiction (total score is calculated as the sum of the 19 items; Item 3 not incl (different format)\n"   
    print df["IAT_sum"].describe()
    sns.distplot(df["IAT_sum"].dropna(), kde = True)
    
    if out_dir:
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ["IAT_sum"]        
        df[cols_export].to_csv('%s/IAT.csv' % out_dir, index=False)



##############################################################################
########################### Arten innerer Sprache ############################
#################### varieties of inner speech (VIS) #########################
##############################################################################

def run_VIS(df, out_dir=None):
    #items to be recoded                                
    items_recoded = ['AISaBASEQ[AIS7]',
                     'AISbBASEQ[AIS15]']  
    #recode items                 
    recoder = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   
           
    #Calculate subscales (Dialogic, Condensed, Otherpeople, Evaluative/Motivat.) - sumscores
    #dialogic inner speech    

    print "Questionnaire measures 4 facets of inner speech: dialogic, condensed, other, evaluative"

                       
    df['VIS_dialog_sum'] = df[['AISaBASEQ[AIS2]',
                           'AISaBASEQ[AIS6]',
                           'AISaBASEQ[AIS10]',
                           'AISbBASEQ[AIS13]']].sum(axis=1)   
                           
    print '\n### dialogic inner speech ###' 
    print df['VIS_dialog_sum'].describe()
     
    #condensed inner speech
    df['VIS_condensed_sum'] = df[['AISaBASEQ[AIS1]',
                              'AISaBASEQ[AIS7]',
                              'AISaBASEQ[AIS8]',
                              'AISbBASEQ[AIS14]', 
                              'AISbBASEQ[AIS15]']].sum(axis=1)
    
    print '\n### condensed inner speech ###'                     
    print df['VIS_condensed_sum'].describe()

    #other people in inner speech
    df['VIS_other_sum'] = df[['AISaBASEQ[AIS3]',
                          'AISaBASEQ[AIS4]',
                          'AISaBASEQ[AIS5]',
                          'AISbBASEQ[AIS12]', 
                          'AISbBASEQ[AIS16]']].sum(axis=1)
                          
    print '\n### others in inner speech ###'                      
    print df['VIS_other_sum'].describe()
    
    
    #evaluative/motivational inner speech
    df['VIS_eval_sum'] = df[['AISaBASEQ[AIS9]',
                         'AISbBASEQ[AIS11]',
                         'AISbBASEQ[AIS17]',
                         'AISbBASEQ[AIS18]']].sum(axis=1)  
     
    print '\n### evaluative inner speech ###'               
    print df['VIS_eval_sum'].describe()

                    
    #create histograms of subscales
    plt.figure(figsize =(16,12))
    
    plt.subplot(221)
    sns.distplot(df['VIS_dialog_sum'].dropna(), kde = True)
    
    plt.subplot(222)
    sns.distplot(df['VIS_condensed_sum'].dropna(), kde = True)
    
    plt.subplot(223)
    sns.distplot(df['VIS_other_sum'].dropna(), kde = True)
    
    plt.subplot(224)
    sns.distplot(df['VIS_eval_sum'].dropna(), kde = True) 
    
    if out_dir:
        
        cols = ['AISaBASEQ[AIS1]', 'AISaBASEQ[AIS2]', 'AISaBASEQ[AIS3]', 'AISaBASEQ[AIS4]',
                'AISaBASEQ[AIS5]', 'AISaBASEQ[AIS6]', 'AISaBASEQ[AIS7]', 'AISaBASEQ[AIS8]',
                'AISaBASEQ[AIS9]', 'AISaBASEQ[AIS10]', 'AISbBASEQ[AIS11]', 'AISbBASEQ[AIS12]',
                'AISbBASEQ[AIS13]', 'AISbBASEQ[AIS14]', 'AISbBASEQ[AIS15]', 'AISbBASEQ[AIS16]',
                'AISbBASEQ[AIS17]', 'AISbBASEQ[AIS18]']
                
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['VIS_dialog_sum', 
        'VIS_condensed_sum', 'VIS_other_sum', 'VIS_eval_sum']        
        df[cols_export].to_csv('%s/VIS.csv' % out_dir, index=False)



##############################################################################
############# Spontaneous and Deliberate Mind Wandering ######################
##############################################################################

def run_MW_SD(df, out_dir=None):
    df['Mean_MW_delib_mean'] = np.round(df[["MWBASEQ[MWD1]",
                                       "MWBASEQ[MWD2]",
                                       "MWBASEQ[MWD3]",
                                       "MWBASEQ[MWD4]"]].mean(axis=1),3)
    df['Mean_MW_spont_mean'] = np.round(df[["MWBASEQ[MWS1]",
                                       "MWBASEQ[MWS2]",
                                       "MWBASEQ[MWS3]",
                                       "MWBASEQ[MWS4]"]].mean(axis=1),3)
    
    
    print "Questionnaire measures spont/delib MW (subscores are calculated by averaging)"   
    print '\n### MW deliberate ###'
    print df['Mean_MW_delib_mean'].describe() 
    print '\n### MW spontaneous ###'
    print df['Mean_MW_spont_mean'].describe()
    
    
   #create histos
    plt.figure(figsize =(16,12))
    
    plt.subplot(221)
    sns.distplot(df['Mean_MW_delib_mean'].dropna(), kde = True)
    
    plt.subplot(222)
    sns.distplot(df['Mean_MW_spont_mean'].dropna() , kde = True)

    if out_dir:
        
        cols = ["MWBASEQ[MWD1]", "MWBASEQ[MWD2]", "MWBASEQ[MWD3]", "MWBASEQ[MWD4]",
                "MWBASEQ[MWS1]", "MWBASEQ[MWS2]", "MWBASEQ[MWS3]", "MWBASEQ[MWS4]"]
        
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['Mean_MW_delib_mean', 'Mean_MW_spont_mean']          
        df[cols_export].to_csv('%s/MW_SD.csv' % out_dir, index=False)



##############################################################################
############################# short dark triad  ##############################
##############################################################################

def run_SDT(df, out_dir=None):
    #items to be recoded                                
    items_recoded = ['SDTnBASEQ[SDTN2r]',
                     'SDTnBASEQ[SDTN6r]',
                     'SDTnBASEQ[SDTN8r]',
                     'SDTpBASEQ[SDTP2r]',
                     'SDTpBASEQ[SDTP7r]']             
                                                      
    #recode items                 
    recoder = {1: 5, 2: 4, 4: 2, 5: 1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   

    #Calculate total score as the sum of Item 1-9 for Machiavellism.
    print 'Questionnaire measures dark triad (Machiavellism, Narcissism, Psychopathy). Scores are sumscores'

    df['Mach_sum'] = df[['SDTmBASEQ[SDTM1]',
                     'SDTmBASEQ[SDTM2]',
                     'SDTmBASEQ[SDTM3]',
                     'SDTmBASEQ[SDTM4]',
                     'SDTmBASEQ[SDTM5]',
                     'SDTmBASEQ[SDTM6]',
                     'SDTmBASEQ[SDTM7]',
                     'SDTmBASEQ[SDTM8]',
                     'SDTmBASEQ[SDTM9]']].sum(axis=1)
        
    print '\n### Machiavellism ###'
    print df['Mach_sum'].describe()
    
    #Calculate total score as the sum of Item 1-9 for Narcissism.               
    df['Narc_sum'] = df[['SDTnBASEQ[SDTN1]',
                      'SDTnBASEQ[SDTN2r]',
                      'SDTnBASEQ[SDTN3]',
                      'SDTnBASEQ[SDTN4]',
                      'SDTnBASEQ[SDTN5]',
                      'SDTnBASEQ[SDTN6r]',
                      'SDTnBASEQ[SDTN7]',
                      'SDTnBASEQ[SDTN8r]',
                      'SDTnBASEQ[SDTN9]']].sum(axis=1)
                      
    print '\n### Narcissism ###'
    print df['Narc_sum'].describe()
        
   #Calculate total score as the sum of Item 1-9 for Psychopathy.                      
    df['Psycho_sum'] = df[['SDTpBASEQ[SDTP1]',
                       'SDTpBASEQ[SDTP2r]',
                       'SDTpBASEQ[SDTP3]',
                       'SDTpBASEQ[SDTP4]',
                       'SDTpBASEQ[SDTP5]',
                       'SDTpBASEQ[SDTP6]',
                       'SDTpBASEQ[SDTP7r]',
                       'SDTpBASEQ[SDTP8]',
                       'SDTpBASEQ[SDTP9]']].sum(axis=1)
                       
    print '\n### Psychopathy ###'
    print df['Psycho_sum'].describe()
    
    
    #create histo
    plt.figure(figsize =(16,12))
    
    plt.subplot(241)
    sns.distplot(df['Mach_sum'].dropna(), kde = True)
  
    plt.subplot(242)
    sns.distplot(df['Narc_sum'].dropna(), kde = True) 
  
    plt.subplot(243)
    sns.distplot(df['Psycho_sum'].dropna(), kde = True)
    
    if out_dir:
        
        cols = ['SDTmBASEQ[SDTM1]', 'SDTmBASEQ[SDTM2]', 'SDTmBASEQ[SDTM3]', 'SDTmBASEQ[SDTM4]',
                'SDTmBASEQ[SDTM5]', 'SDTmBASEQ[SDTM6]', 'SDTmBASEQ[SDTM7]', 'SDTmBASEQ[SDTM8]',
                'SDTmBASEQ[SDTM9]','SDTnBASEQ[SDTN1]', 'SDTnBASEQ[SDTN2r]', 'SDTnBASEQ[SDTN3]',
                'SDTnBASEQ[SDTN4]', 'SDTnBASEQ[SDTN5]', 'SDTnBASEQ[SDTN6r]', 'SDTnBASEQ[SDTN7]',
                'SDTnBASEQ[SDTN8r]', 'SDTnBASEQ[SDTN9]', 'SDTpBASEQ[SDTP1]', 'SDTpBASEQ[SDTP2r]',
                'SDTpBASEQ[SDTP3]', 'SDTpBASEQ[SDTP4]', 'SDTpBASEQ[SDTP5]', 'SDTpBASEQ[SDTP6]',
                'SDTpBASEQ[SDTP7r]', 'SDTpBASEQ[SDTP8]', 'SDTpBASEQ[SDTP9]']
        
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['Mach_sum', 'Narc_sum', 'Psycho_sum']          
        df[cols_export].to_csv('%s/SDT.csv' % out_dir, index=False)



##############################################################################
################################ SES #########################################
##############################################################################

# social desirability

def run_SES(df, out_dir=None):
    #items to be recoded     

    print 'Questionnaire measure social des. as the sum of 17 items\n'

                           
    items_recoded = ['SESaBASEQ[SES1r]',
                     'SESaBASEQ[SES4r]',
                     'SESaBASEQ[SES6r]',
                     'SESaBASEQ[SES7r]',
                     'SESbBASEQ[SES11r]',
                     'SESbBASEQ[SES15r]',
                     'SESbBASEQ[SES17r]']    
                             
    #recode items                 
    recoder = {1: 2 , 2: 1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   

    cols = ['SESaBASEQ[SES1r]',
            'SESaBASEQ[SES2]',
            'SESaBASEQ[SES3]',
            'SESaBASEQ[SES4r]',
            'SESaBASEQ[SES5]',
            'SESaBASEQ[SES6r]',
            'SESaBASEQ[SES7r]',
            'SESaBASEQ[SES8]',
            'SESaBASEQ[SES9]',
            'SESaBASEQ[SES10]',
            'SESbBASEQ[SES11r]',
            'SESbBASEQ[SES12]',
            'SESbBASEQ[SES13]',
            'SESbBASEQ[SES14]',
            'SESbBASEQ[SES15r]',
            'SESbBASEQ[SES16]',
            'SESbBASEQ[SES17r]']     

    #Calculate total score as the sum of Item 1-17.
    df['SES_sum'] = df[cols].sum(axis=1)
                    
    print df['SES_sum'].describe()
                   
    #create histo
    sns.distplot(df['SES_sum'].dropna(), kde = True)              
    
    if out_dir:
        
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['SES_sum']          
        df[cols_export].to_csv('%s/SES.csv' % out_dir, index=False)
  


##############################################################################            
##################### UPPSP - impulsivity ####################################
##############################################################################

def run_UPPSP(df, out_dir=None):
    
    print 'Questionnaire measures facets of impuls.: NegUrg, LoPremed, LoPersev, SS, PosUrg (scores are averaged)\n'    
    
    #items that need to be recoded
    items_recoded = ['UPPSaBASEQ[UPP2r]','UPPSaBASEQ[UPP3r]','UPPSaBASEQ[UPP5r]',
                     'UPPSaBASEQ[UPP7r]','UPPSaBASEQ[UPP8r]','UPPSaBASEQ[UPP9r]',
                     'UPPSaBASEQ[UPP10r]','UPPSbBASEQ[UPP12r]','UPPSbBASEQ[UPP13r]',
                     'UPPSbBASEQ[UPP15r]','UPPSbBASEQ[UPP17r]','UPPSbBASEQ[UPP18r]',
                     'UPPSbBASEQ[UPP20r]','UPPScBASEQ[UPP22r]','UPPScBASEQ[UPP23r]',
                     'UPPScBASEQ[UPP25r]','UPPScBASEQ[UPP26r]','UPPScBASEQ[UPP29r]',
                     'UPPScBASEQ[UPP30r]','UPPSdBASEQ[UPP31r]','UPPSdBASEQ[UPP34r]',
                     'UPPSdBASEQ[UPP35r]','UPPSdBASEQ[UPP36r]','UPPSdBASEQ[UPP39r]',
                     'UPPSdBASEQ[UPP40r]','UPPSeBASEQ[UPP41r]','UPPSeBASEQ[UPP44r]',
                     'UPPSeBASEQ[UPP45r]','UPPSeBASEQ[UPP46r]','UPPSeBASEQ[UPP47r]',
                     'UPPSeBASEQ[UPP49]','UPPSeBASEQ[UPP50r]','UPPSfBASEQ[UPP51r]',
                     'UPPSfBASEQ[UPP52r]','UPPSfBASEQ[UPP54]','UPPSfBASEQ[UPP56r]',
                     'UPPSfBASEQ[UPP57r]','UPPSfBASEQ[UPP58r]','UPPSfBASEQ[UPP59r]']
    #recode items                 
    recoder = {1: 4, 2: 3, 3: 2, 4: 1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)
    #calculate subscales (averages)
    #Negative Urgency
    df['Mean_NegUrg'] = np.round(df[['UPPSaBASEQ[UPP2r]',
                                     'UPPSaBASEQ[UPP7r]',
                                     'UPPSbBASEQ[UPP12r]',
                                     'UPPSbBASEQ[UPP17r]',
                                     'UPPScBASEQ[UPP22r]',
                                     'UPPScBASEQ[UPP29r]',
                                     'UPPSdBASEQ[UPP34r]',
                                     'UPPSdBASEQ[UPP39r]',  
                                     'UPPSeBASEQ[UPP44r]',
                                     'UPPSeBASEQ[UPP50r]',
                                     'UPPSfBASEQ[UPP53r]',
                                     'UPPSfBASEQ[UPP58r]']].mean(axis=1),3)                                     
    print '\n### Negative Urgency ###'                                 
    print df['Mean_NegUrg'].describe()
                          
    #lack of premeditation                              
    df['Mean_Premed'] = np.round(df[['UPPSaBASEQ[UPP1]',
                                     'UPPSaBASEQ[UPP6]',
                                     'UPPSbBASEQ[UPP11]',
                                     'UPPSbBASEQ[UPP16]',
                                     'UPPScBASEQ[UPP21]',
                                     'UPPScBASEQ[UPP28]',
                                     'UPPSdBASEQ[UPP33]',
                                     'UPPSdBASEQ[UPP38]',
                                     'UPPSeBASEQ[UPP43]',
                                     'UPPSeBASEQ[UPP48]',
                                     'UPPSfBASEQ[UPP55r]']].mean(axis=1),3)                                     
    print '\n### Lack of Premed ###'
    print df['Mean_Premed'].describe()    
                                                        
    #lack of perseverance
    df['Mean_Persev'] = np.round(df[['UPPSaBASEQ[UPP4]',
                                     'UPPSaBASEQ[UPP9r]',
                                     'UPPSbBASEQ[UPP14]',
                                     'UPPSbBASEQ[UPP19]',
                                     'UPPScBASEQ[UPP24]',
                                     'UPPScBASEQ[UPP27]',
                                     'UPPSdBASEQ[UPP32]',
                                     'UPPSdBASEQ[UPP37]',
                                     'UPPSeBASEQ[UPP42]',
                                     'UPPSeBASEQ[UPP47r]']].mean(axis=1),3)                                     
    print '\n### Lack of Persev ###'
    print df['Mean_Persev'].describe()                                                                  
              
    #sensation seeking
    df['Mean_SS'] = np.round(df[['UPPSaBASEQ[UPP3r]',
                                 'UPPSaBASEQ[UPP8r]',
                                 'UPPSbBASEQ[UPP13r]',
                                 'UPPSbBASEQ[UPP18r]',
                                 'UPPScBASEQ[UPP23r]',
                                 'UPPScBASEQ[UPP26r]',
                                 'UPPSdBASEQ[UPP31r]',
                                 'UPPSdBASEQ[UPP36r]',
                                 'UPPSeBASEQ[UPP41r]',
                                 'UPPSeBASEQ[UPP46r]',
                                 'UPPSfBASEQ[UPP51r]',
                                 'UPPSfBASEQ[UPP56r]']].mean(axis=1),3)                                 
    print '\n### SS ###'                              
    print df['Mean_SS'].describe()
                       
    #Positive Urgency
    df['Mean_PosUrg'] = np.round(df[['UPPSaBASEQ[UPP5r]',
                                     'UPPSaBASEQ[UPP10r]',
                                     'UPPSbBASEQ[UPP15r]',
                                     'UPPSbBASEQ[UPP20r]',
                                     'UPPScBASEQ[UPP25r]',
                                     'UPPScBASEQ[UPP30r]',
                                     'UPPSdBASEQ[UPP35r]',
                                     'UPPSdBASEQ[UPP40r]',
                                     'UPPSeBASEQ[UPP45r]',
                                     'UPPSeBASEQ[UPP49]',
                                     'UPPSfBASEQ[UPP52r]',
                                     'UPPSfBASEQ[UPP54]',
                                     'UPPSfBASEQ[UPP57r]',
                                     'UPPSfBASEQ[UPP59r]']].mean(axis=1),3)
        
    print '\n### Positive Urgency ###'                              
    print df['Mean_PosUrg'].describe()
   
                                     

    #create histograms of subscales
    plt.figure(figsize =(16,12))
    
    plt.subplot(231)
    sns.distplot(df['Mean_NegUrg'].dropna(), kde = True) 
    
    plt.subplot(232)
    sns.distplot(df['Mean_Premed'].dropna(), kde = True) 
    
    plt.subplot(233)
    sns.distplot(df['Mean_Persev'].dropna(), kde = True) 
   
    plt.subplot(234)
    sns.distplot(df['Mean_SS'].dropna(), kde = True) 
    
    plt.subplot(235)
    sns.distplot(df['Mean_PosUrg'].dropna(), kde = True)   
            
    if out_dir:
   
        
        cols = ['UPPSaBASEQ[UPP1]', 'UPPSaBASEQ[UPP2r]', 'UPPSaBASEQ[UPP3r]', 'UPPSaBASEQ[UPP4]',
                'UPPSaBASEQ[UPP5r]', 'UPPSaBASEQ[UPP6]', 'UPPSaBASEQ[UPP7r]', 'UPPSaBASEQ[UPP8r]',
                'UPPSaBASEQ[UPP9r]', 'UPPSaBASEQ[UPP10r]', 'UPPSbBASEQ[UPP11]', 'UPPSbBASEQ[UPP12r]',
                'UPPSbBASEQ[UPP13r]', 'UPPSbBASEQ[UPP14]', 'UPPSbBASEQ[UPP15r]', 'UPPSbBASEQ[UPP16]',
                'UPPSbBASEQ[UPP17r]', 'UPPSbBASEQ[UPP18r]', 'UPPSbBASEQ[UPP19]', 'UPPSbBASEQ[UPP20r]',
                'UPPScBASEQ[UPP21]', 'UPPScBASEQ[UPP22r]', 'UPPScBASEQ[UPP23r]', 'UPPScBASEQ[UPP24]',
                'UPPScBASEQ[UPP25r]', 'UPPScBASEQ[UPP26r]', 'UPPScBASEQ[UPP27]', 'UPPScBASEQ[UPP28]',
                'UPPScBASEQ[UPP29r]', 'UPPScBASEQ[UPP30r]', 'UPPSdBASEQ[UPP31r]', 'UPPSdBASEQ[UPP32]',
                'UPPSdBASEQ[UPP33]', 'UPPSdBASEQ[UPP34r]', 'UPPSdBASEQ[UPP35r]', 'UPPSdBASEQ[UPP36r]',
                'UPPSdBASEQ[UPP37]', 'UPPSdBASEQ[UPP38]', 'UPPSdBASEQ[UPP39r]', 'UPPSdBASEQ[UPP40r]',
                'UPPSeBASEQ[UPP41r]', 'UPPSeBASEQ[UPP42]', 'UPPSeBASEQ[UPP43]', 'UPPSeBASEQ[UPP44r]',
                'UPPSeBASEQ[UPP45r]', 'UPPSeBASEQ[UPP46r]', 'UPPSeBASEQ[UPP47r]', 'UPPSeBASEQ[UPP48]',
                'UPPSeBASEQ[UPP49]', 'UPPSeBASEQ[UPP50r]', 'UPPSfBASEQ[UPP51r]', 'UPPSfBASEQ[UPP52r]',
                'UPPSfBASEQ[UPP53r]', 'UPPSfBASEQ[UPP54]', 'UPPSfBASEQ[UPP55r]', 'UPPSfBASEQ[UPP56r]',
                'UPPSfBASEQ[UPP57r]', 'UPPSfBASEQ[UPP58r]','UPPSfBASEQ[UPP59r]']        
        
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['Mean_NegUrg', 'Mean_Premed', 'Mean_Persev', 'Mean_SS','Mean_PosUrg']          
        df[cols_export].to_csv('%s/SES.csv' % out_dir, index=False)
  


##############################################################################
############################## TPS-D #########################################
################ Tuckmann Procrastination Scale (TPS_D)#######################
##############################################################################

def run_TPS(df, out_dir=None):
    #items to be recoded    

    print 'Questionnaire measures procrastination as the sum of 16 items\n'
                            
    items_recoded = ['TPSBASEQ[TPS7]',
                     'TPSBASEQ[TPS12]',
                     'TPSBASEQ[TPS14]',
                     'TPSBASEQ[TPS16]']    
                             
    #recode items                 
    recoder = {1: 5, 2: 4, 4: 2, 5: 1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   

    #Calculate total score as the sum of Item 1-16.
    cols = ['TPSBASEQ[TPS1]',
            'TPSBASEQ[TPS2]',
            'TPSBASEQ[TPS3]',
            'TPSBASEQ[TPS4]',
            'TPSBASEQ[TPS5]',
            'TPSBASEQ[TPS6]',
            'TPSBASEQ[TPS7]',
            'TPSBASEQ[TPS8]',
            'TPSBASEQ[TPS9]',
            'TPSBASEQ[TPS10]',
            'TPSBASEQ[TPS11]',
            'TPSBASEQ[TPS12]',
            'TPSBASEQ[TPS13]',
            'TPSBASEQ[TPS14]',
            'TPSBASEQ[TPS15]',
            'TPSBASEQ[TPS16]']
    
    df['TPS_D_sum'] = df[cols].sum(axis=1)
                      
    print df['TPS_D_sum'].describe()
    sns.distplot(df['TPS_D_sum'].dropna(), kde = True)                  

    if out_dir:
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['TPS_D_sum']          
        df[cols_export].to_csv('%s/TPS.csv' % out_dir, index=False)
        


##############################################################################
############################ ASR 18-59 #######################################
##############################################################################

def run_ASR(data, out_dir=None):
    ######################## adaptive functioning #################################
    print 'The Adult Self-Report (ASR; part of the Achenbach System of Empirically Based Assessment)\n' 
    print 'Adaptive Functioning Scales: \nFriends; Spouse/Partner; Family; Job; Education, Personal Strengths\n'
    print 'Substance Use Scales: \nTobacco, Alcohol, Drugs, mean substance use\n'     
    print 'Syndrome Scales (123 items on a 3-point scale):'
    print 'Anxious/Depressed; Withdrawn; Somatic Complaints (together form the Internalizing scale)' 
    print 'Aggressive Behavior; Rule-breaking Behavior, and Intrusive (form the Externalzing scale)'
    print 'Thought Problems; Attention Problems' 
   
    print '\n\n', '##### Adaptive Functioning #####'
    
    ##### friends #####     
    data['ASR_summary_adaptiveFunctioning_friends_sum' ] = data[['ASRIABASEQ[ASRIA]',
                                                                 'ASRIBBASEQ[ASRIB]',
                                                                 'ASRICBASEQ[ASRIC]',
                                                                 'ASRIDBASEQ[ASRID]']].sum(axis=1)
    
    
    ##### spouse / partner #####
    recoded = ['ASRII3BASEQ[ASRIIBr]', 'ASRII3BASEQ[ASRIIEr]', 'ASRII3BASEQ[ASRIIFr]', 'ASRII3BASEQ[ASRIIHr]']
    for item in recoded:
        data[item] = -data[item]
    data['ASR_summary_adaptiveFunctioning_spouse_sum'] = data[['ASRII3BASEQ[ASRIIA]', 
                                                              'ASRII3BASEQ[ASRIIBr]',
                                                              'ASRII3BASEQ[ASRIIC]',
                                                              'ASRII3BASEQ[ASRIID]',
                                                              'ASRII3BASEQ[ASRIIEr]',
                                                              'ASRII3BASEQ[ASRIIFr]',
                                                              'ASRII3BASEQ[ASRIIG]',
                                                              'ASRII3BASEQ[ASRIIHr]']].sum(axis=1)
    
    ##### family #####
    # also in literature: 'ASR_summary_adaptiveFunctioning_family_mean'
    items = ['ASRIIIABASEQ[ASRIIIA]', 'ASRIIIBBASEQ[ASRIIIB]', 'ASRIIICBASEQ[ASRIIIC]',
            'ASRIIIDBASEQ[ASRIIID]', 'ASRIIIEbBASEQ[ASRIIIE1]', 'ASRIIIEbBASEQ[ASRIIIE2]',
            'ASRIIIEbBASEQ[ASRIIIE3]', 'ASRIIIEbBASEQ[ASRIIIE4]', 'ASRIIIFBASEQ[ASRIIIF]']
    data['ASR_summary_adaptiveFunctioning_family_sum'] = pd.Series('NaN', index=data.index)
    for sub in range(len(data)):
        score = 0
        for i in items:
            try:
                if int(data[i].iloc[[sub]]) in [0,1,2,3]:
                    score += 1
            except:
                pass
        data['ASR_summary_adaptiveFunctioning_family_sum'].iloc[[sub]] = float(score)
    
    
    ##### job #####
    #satisfied_job = data['ASRIVbBASEQ[ASRIVE]'] is not scored
    recoded = ['ASRIVbBASEQ[ASRIVBr]', 'ASRIVbBASEQ[ASRIVDr]', 'ASRIVbBASEQ[ASRIVFr]',
               'ASRIVbBASEQ[ASRIVGr]', 'ASRIVbBASEQ[ASRIVHr]', 'ASRIVbBASEQ[ASRIVIr]']
    for item in recoded:
        data[item] = -data[item]
    data['ASR_summary_adaptiveFunctioning_job_sum'] = data[['ASRIVbBASEQ[ASRIVA]',
                                                            'ASRIVbBASEQ[ASRIVBr]',
                                                            'ASRIVbBASEQ[ASRIVC]',
                                                            'ASRIVbBASEQ[ASRIVDr]',
                                                            'ASRIVbBASEQ[ASRIVFr]',
                                                            'ASRIVbBASEQ[ASRIVGr]',
                                                            'ASRIVbBASEQ[ASRIVHr]',
                                                            'ASRIVbBASEQ[ASRIVIr]']].sum(axis=1)
    
    ##### education #####
    # careful with older ages
    # though we're using raw total scores, it's important to notice that normed scores only available for ages 18-29
    recoded = ['ASRVcBASEQ[ASRVCr]', 'ASRVcBASEQ[ASRVEr]']
    for item in recoded:
        data[item] = -data[item]
    data['ASR_summary_adaptiveFunctioning_education_sum'] = data[['ASRVcBASEQ[ASRVA]',
                                                                  'ASRVcBASEQ[ASRVB]',
                                                                  'ASRVcBASEQ[ASRVCr]',
                                                                  'ASRVcBASEQ[ASRVD]',
                                                                  'ASRVcBASEQ[ASRVEr]']].sum(axis=1)
    
    
    scales = ['ASR_summary_adaptiveFunctioning_friends_sum',
              'ASR_summary_adaptiveFunctioning_spouse_sum', 
              'ASR_summary_adaptiveFunctioning_family_sum',
              'ASR_summary_adaptiveFunctioning_job_sum',
              'ASR_summary_adaptiveFunctioning_education_sum']
    
        
   
    for scale in scales:
        print '\n'
        print data[scale].describe()
        sns.countplot(data[scale].dropna(), order=range(int(data[scale].min()),int(data[scale].max())))
        plt.xlabel(scale, fontsize=14)
        plt.show()
        
        
        
    
    ######################## substance use #################################
    
    print '\n\n\n', '##### Substance Use #####'
    
    data['ASR_scale_substanceUse_tabaco_perday'] = data['ASRQ124']
    data['ASR_scale_substanceUse_alcohol_daysdrunk'] = data['ASRQ125']
    data['ASR_scale_substanceUse_drugs_daysused'] = data['ASRQ126']
    
    substance_scales = ['ASR_scale_substanceUse_tabaco_perday', 
                        'ASR_scale_substanceUse_alcohol_daysdrunk', 
                        'ASR_scale_substanceUse_drugs_daysused']
    
    for scale in substance_scales:
        print '\n'
        print data[scale].describe() 
        sns.countplot(data[scale].dropna(), order=range(int(data[scale].min()),int(data[scale].max())))
        plt.xlabel(scale, fontsize=14)
        plt.show()
    
    
    ######################### items #############################################
    Q1 = data['ASRQ1BASEQ[ASRQ1]']
    Q2 = data['ASRQ1BASEQ[ASRQ2]']
    Q3 = data['ASRQ1BASEQ[ASRQ3]']
    Q4 = data['ASRQ1BASEQ[ASRQ4]']
    Q5 = data['ASRQ1BASEQ[ASRQ5]']
    Q6 = data['ASRQ1BASEQ[ASRQ6]']
    Q7 = data['ASRQ7BASEQ[ASRQ7]']
    Q8 = data['ASRQ7BASEQ[ASRQ8]']
    Q9 = data['ASRQ7BASEQ[ASRQ9]']
    Q10 = data['ASRQ10BASEQ[ASRQ10]']
    Q11 = data['ASRQ10BASEQ[ASRQ11]']
    Q12 = data['ASRQ10BASEQ[ASRQ12]']
    Q13 = data['ASRQ10BASEQ[ASRQ13]']
    Q14 = data['ASRQ10BASEQ[ASRQ14]']
    Q15 = data['ASRQ10BASEQ[ASRQ15]']
    Q16 = data['ASRQ10BASEQ[ASRQ16]']
    Q17 = data['ASRQ10BASEQ[ASRQ17]']
    Q18 = data['ASRQ10BASEQ[ASRQ18]']
    Q19 = data['ASRQ10BASEQ[ASRQ19]']
    Q20 = data['ASRQ10BASEQ[ASRQ20]']
    Q21 = data['ASRQ21BASEQ[ASRQ21]']
    Q22 = data['ASRQ21BASEQ[ASRQ22]']
    Q23 = data['ASRQ21BASEQ[ASRQ23]']
    Q24 = data['ASRQ21BASEQ[ASRQ24]']
    Q25 = data['ASRQ21BASEQ[ASRQ25]']
    Q26 = data['ASRQ21BASEQ[ASRQ26]']
    Q27 = data['ASRQ21BASEQ[ASRQ27]']
    Q28 = data['ASRQ21BASEQ[ASRQ28]']
    Q29 = data['ASRQ21BASEQ[ASRQ29]']
    Q30 = data['ASRQ30BASEQ[ASRQ30]']
    Q31 = data['ASRQ30BASEQ[ASRQ31]']
    Q32 = data['ASRQ30BASEQ[ASRQ32]']
    Q33 = data['ASRQ30BASEQ[ASRQ33]']
    Q34 = data['ASRQ30BASEQ[ASRQ34]']
    Q35 = data['ASRQ30BASEQ[ASRQ35]']
    Q36 = data['ASRQ30BASEQ[ASRQ36]']
    Q37 = data['ASRQ30BASEQ[ASRQ37]']
    Q38 = data['ASRQ30BASEQ[ASRQ38]']
    Q39 = data['ASRQ30BASEQ[ASRQ39]']
    Q40 = data['ASRQ30BASEQ[ASRQ40]']
    Q41 = data['ASRQ41BASEQ[ASRQ41]']
    Q42 = data['ASRQ41BASEQ[ASRQ42]']
    Q43 = data['ASRQ41BASEQ[ASRQ43]']
    Q44 = data['ASRQ41BASEQ[ASRQ44]']
    Q45 = data['ASRQ41BASEQ[ASRQ45]']
    Q46 = data['ASRQ41BASEQ[ASRQ46]']
    Q47 = data['ASRQ41BASEQ[ASRQ47]']
    Q48 = data['ASRQ41BASEQ[ASRQ48]']
    Q49 = data['ASRQ41BASEQ[ASRQ49]']
    Q50 = data['ASRQ41BASEQ[ASRQ50]']
    Q51 = data['ASRQ51BASEQ[ASRQ51]']
    Q52 = data['ASRQ51BASEQ[ASRQ52]']
    Q53 = data['ASRQ51BASEQ[ASRQ53]']
    Q54 = data['ASRQ51BASEQ[ASRQ54]']
    Q55 = data['ASRQ51BASEQ[ASRQ55]']
    Q56a = data['ASRQ56BASEQ[ASRVIII561]']
    Q56b = data['ASRQ56BASEQ[ASRVIII562]']
    Q56c = data['ASRQ56BASEQ[ASRVIII563]']
    Q56d = data['ASRQ56BASEQ[ASRVIII564]']
    Q56e = data['ASRQ56BASEQ[ASRVIII565]']
    Q56f = data['ASRQ56BASEQ[ASRVIII566]']
    Q56g = data['ASRQ56BASEQ[ASRVIII567]']
    Q57 = data['ASRQ57BASEQ[ASRQ57]']
    Q58 = data['ASRQ57BASEQ[ASRQ58]']
    Q59 = data['ASRQ57BASEQ[ASRQ59]']
    Q60 = data['ASRQ57BASEQ[ASRQ60]']
    Q61 = data['ASRQ61BASEQ[ASRQ61]']
    Q62 = data['ASRQ61BASEQ[ASRQ62]']
    Q63 = data['ASRQ61BASEQ[ASRQ63]']
    Q64 = data['ASRQ61BASEQ[ASRQ64]']
    Q65 = data['ASRQ61BASEQ[ASRQ65]']
    Q66 = data['ASRQ61BASEQ[ASRQ66]']
    Q67 = data['ASRQ61BASEQ[ASRQ67]']
    Q68 = data['ASRQ61BASEQ[ASRQ68]']
    Q69 = data['ASRQ61BASEQ[ASRQ69]']
    Q70 = data['ASRQ61BASEQ[ASRQ70]']
    Q71 = data['ASRQ71BASEQ[ASRQ71]']
    Q72 = data['ASRQ71BASEQ[ASRQ72]']
    Q73 = data['ASRQ71BASEQ[ASRQ73]']
    Q74 = data['ASRQ71BASEQ[ASRQ74]']
    Q75 = data['ASRQ71BASEQ[ASRQ75]']
    Q76 = data['ASRQ71BASEQ[ASRQ76]']
    Q77 = data['ASRQ71BASEQ[ASRQ77]']
    Q78 = data['ASRQ71BASEQ[ASRQ78]']
    Q79 = data['ASRQ71BASEQ[ASRQ79]']
    Q80 = data['ASRQ71BASEQ[ASRQ80]']
    Q81 = data['ASRQ81BASEQ[ASRQ81]']
    Q82 = data['ASRQ81BASEQ[ASRQ82]']
    Q83 = data['ASRQ81BASEQ[ASRQ83]']
    Q84 = data['ASRQ81BASEQ[ASRQ84]']
    Q85 = data['ASRQ81BASEQ[ASRQ85]']
    Q86 = data['ASRQ81BASEQ[ASRQ86]']
    Q87 = data['ASRQ81BASEQ[ASRQ87]']
    Q88 = data['ASRQ81BASEQ[ASRQ88]']
    Q89 = data['ASRQ81BASEQ[ASRQ89]']
    Q90 = data['ASRQ81BASEQ[ASRQ90]']
    Q91 = data['ASRQ91BASEQ[ASRQ91]']
    Q92 = data['ASRQ91BASEQ[ASRQ92]']
    Q93 = data['ASRQ91BASEQ[ASRQ93]']
    Q94 = data['ASRQ91BASEQ[ASRQ94]']
    Q95 = data['ASRQ91BASEQ[ASRQ95]']
    Q96 = data['ASRQ91BASEQ[ASRQ96]']
    Q97 = data['ASRQ91BASEQ[ASRQ97]']
    Q98 = data['ASRQ91BASEQ[ASRQ98]']
    Q99 = data['ASRQ91BASEQ[ASRQ99]']
    Q100 = data['ASRQ91BASEQ[ASRQ100]']
    Q101 = data['ASRQ101BASEQ[ASRQ101]']
    Q102 = data['ASRQ101BASEQ[ASRQ102]']
    Q103 = data['ASRQ101BASEQ[ASRQ103]']
    Q104 = data['ASRQ101BASEQ[ASRQ104]']
    Q105 = data['ASRQ101BASEQ[ASRQ105]']
    Q106 = data['ASRQ101BASEQ[ASRQ106]']
    Q107 = data['ASRQ101BASEQ[ASRQ107]']
    Q108 = data['ASRQ101BASEQ[ASRQ108]']
    Q109 = data['ASRQ101BASEQ[ASRQ109]']
    Q110 = data['ASRQ101BASEQ[ASRQ110]']
    Q111 = data['ASRQ111BASEQ[ASRQ111]']
    Q112 = data['ASRQ111BASEQ[ASRQ112]']
    Q113 = data['ASRQ111BASEQ[ASRQ113]']
    Q114 = data['ASRQ111BASEQ[ASRQ114]']
    Q115 = data['ASRQ111BASEQ[ASRQ115]']
    Q116 = data['ASRQ111BASEQ[ASRQ116]']
    Q117 = data['ASRQ111BASEQ[ASRQ117]']
    Q118 = data['ASRQ111BASEQ[ASRQ118]']
    Q119 = data['ASRQ111BASEQ[ASRQ119]']
    Q120 = data['ASRQ111BASEQ[ASRQ120]']
    Q121 = data['ASRQ121BASEQ[ASRQ121]']
    Q122 = data['ASRQ121BASEQ[ASRQ122]']
    Q123 = data['ASRQ121BASEQ[ASRQ123]']
    
    
    ######################## critical items #################################
    
    print '\n\n\n', '##### Critical Items #####'
    data['ASR_summary_criticalItems_sum'] = Q6 + Q8 + Q9 + Q10 + Q14 + Q16 + Q18 + Q21 + Q40 + Q55 + Q57 + Q66 + Q70 + Q84 + Q90 + Q91 + Q92 + Q97 + Q103
    print '\n\n', 'ASR_summary_criticalItems_sum', '\n'
    print data['ASR_summary_criticalItems_sum'].describe()
    sns.countplot(data['ASR_summary_criticalItems_sum'].dropna(), order=range(int(data['ASR_summary_criticalItems_sum'].min()),int(data['ASR_summary_criticalItems_sum'].max())))
    plt.show()
    
    
    ######################## syndrome profiles #################################
    
    print '\n\n\n', '##### Syndrome Profiles #####'
    
    data['ASR_summary_syndromeProfiles_anxiousdepressed_sum'] = Q12 + Q13 + Q14 + Q22 + Q31 + Q33 + Q34 + Q35 + Q45 + Q47 + Q50 + Q52 + Q71 + Q91 + Q103 + Q107 + Q112 + Q113 
    data['ASR_summary_syndromeProfiles_withdrawn_sum'] = Q25 + Q30 + Q42 + Q48 + Q60 + Q65 + Q67 + Q69 + Q111
    data['ASR_summary_syndromeProfiles_somaticComplaints_sum'] = Q51 + Q54 + Q56a + Q56b + Q56c + Q56d + Q56e + Q56f + Q56g + Q100
    data['ASR_summary_syndromeProfiles_thoughtProblems_sum'] = Q9 + Q18 + Q36 + Q40 + Q46 + Q63 + Q66 + Q70 + Q84 + Q85 
    data['ASR_summary_syndromeProfiles_attentionProblems_sum'] = Q1 + Q8 + Q11 + Q17 + Q53 + Q59 + Q61 + Q64 + Q78 + Q101 + Q102 + Q105 + Q108 + Q119 + Q121
    data['ASR_summary_syndromeProfiles_aggressiveBehavior_sum'] = Q3 + Q5 + Q16 + Q28 + Q37 + Q55 + Q57 + Q68 + Q81 + Q86 + Q87 + Q95 + Q97 + Q116 + Q118
    data['ASR_summary_syndromeProfiles_rulebreakingBehavior_sum'] = Q6 + Q20 + Q23 + Q26 + Q39 + Q41 + Q43 + Q76 + Q82 + Q90 + Q92 + Q114 + Q117 + Q122 
    data['ASR_summary_syndromeProfiles_intrusive_sum'] = Q7 + Q19 + Q74 + Q93 + Q94 + Q104
    
    data['ASR_summary_syndromeProfiles_internalizing_sum'] = data[['ASR_summary_syndromeProfiles_anxiousdepressed_sum',
                                                                   'ASR_summary_syndromeProfiles_withdrawn_sum', 
                                                                   'ASR_summary_syndromeProfiles_somaticComplaints_sum']].sum(axis=1)
    
    data['ASR_summary_syndromeProfiles_externalizing_sum'] = data[['ASR_summary_syndromeProfiles_aggressiveBehavior_sum',
                                                                   'ASR_summary_syndromeProfiles_rulebreakingBehavior_sum',
                                                                   'ASR_summary_syndromeProfiles_intrusive_sum']].sum(axis=1)
    
    
    syndrome_scales = ['ASR_summary_syndromeProfiles_anxiousdepressed_sum', 
                       'ASR_summary_syndromeProfiles_withdrawn_sum', 
                       'ASR_summary_syndromeProfiles_somaticComplaints_sum',
                       'ASR_summary_syndromeProfiles_thoughtProblems_sum', 
                       'ASR_summary_syndromeProfiles_attentionProblems_sum', 
                       'ASR_summary_syndromeProfiles_aggressiveBehavior_sum', 
                       'ASR_summary_syndromeProfiles_rulebreakingBehavior_sum', 
                       'ASR_summary_syndromeProfiles_intrusive_sum', 
                       'ASR_summary_syndromeProfiles_internalizing_sum', 
                       'ASR_summary_syndromeProfiles_externalizing_sum']
    
    for scale in syndrome_scales:
        print '\n\n', scale, '\n'
        print data[scale].describe()  
        sns.countplot(data[scale].dropna(), order=range(int(data[scale].min()),int(data[scale].max())))
        plt.xlabel(scale, fontsize=14)
        plt.show()
    
    print '\n\n'
    sns.lmplot(x='ASR_summary_syndromeProfiles_externalizing_sum', y='ASR_summary_syndromeProfiles_internalizing_sum', data=data)


    if out_dir:

        cols = ['ASRIABASEQ[ASRIA]','ASRIBBASEQ[ASRIB]','ASRICBASEQ[ASRIC]','ASRIDBASEQ[ASRID]','ASRII1','ASRII1[comment]','ASRII2','ASRII3BASEQ[ASRIIA]',
                'ASRII3BASEQ[ASRIIBr]','ASRII3BASEQ[ASRIIC]','ASRII3BASEQ[ASRIID]','ASRII3BASEQ[ASRIIEr]','ASRII3BASEQ[ASRIIFr]','ASRII3BASEQ[ASRIIG]',
                'ASRII3BASEQ[ASRIIHr]','ASRIIIABASEQ[ASRIIIA]','ASRIIIBBASEQ[ASRIIIB]','ASRIIICBASEQ[ASRIIIC]','ASRIIIDBASEQ[ASRIIID]','ASRIIIEaBASEQ[ASRIIIE]',
                'ASRIIIEbBASEQ[ASRIIIE1]','ASRIIIEbBASEQ[ASRIIIE2]','ASRIIIEbBASEQ[ASRIIIE3]','ASRIIIEbBASEQ[ASRIIIE4]','ASRIIIFBASEQ[ASRIIIF]','ASRIVaBASEQ[ASRIV]',
                'ASRIVbBASEQ[ASRIVA]','ASRIVbBASEQ[ASRIVBr]','ASRIVbBASEQ[ASRIVC]','ASRIVbBASEQ[ASRIVDr]','ASRIVbBASEQ[ASRIVE]','ASRIVbBASEQ[ASRIVFr]',
                'ASRIVbBASEQ[ASRIVGr]', 'ASRIVbBASEQ[ASRIVHr]','ASRIVbBASEQ[ASRIVIr]','ASRVa','ASRVa[comment]','ASRVbBASEQ[ASRV1]','ASRVbBASEQ[ASRV1comment]',
                'ASRVbBASEQ[ASRV3]','ASRVbBASEQ[ASRV3comment]','ASRVbBASEQ[ASRV4]','ASRVbBASEQ[ASRV4comment]','ASRVcBASEQ[ASRVA]','ASRVcBASEQ[ASRVB]',
                'ASRVcBASEQ[ASRVCr]','ASRVcBASEQ[ASRVD]','ASRVcBASEQ[ASRVEr]','ASRVI','ASRVI[comment]','ASRVII','ASRVII[comment]','ASRVIII','ASRQ1BASEQ[ASRQ1]',
                'ASRQ1BASEQ[ASRQ2]','ASRQ1BASEQ[ASRQ3]','ASRQ1BASEQ[ASRQ4]','ASRQ1BASEQ[ASRQ5]','ASRQ1BASEQ[ASRQ6]','ASRQ6Freitext','ASRQ7BASEQ[ASRQ7]','ASRQ7BASEQ[ASRQ8]',
                'ASRQ7BASEQ[ASRQ9]','ASRQ9Freitext','ASRQ10BASEQ[ASRQ10]','ASRQ10BASEQ[ASRQ11]','ASRQ10BASEQ[ASRQ12]','ASRQ10BASEQ[ASRQ13]','ASRQ10BASEQ[ASRQ14]',
                'ASRQ10BASEQ[ASRQ15]','ASRQ10BASEQ[ASRQ16]','ASRQ10BASEQ[ASRQ17]','ASRQ10BASEQ[ASRQ18]','ASRQ10BASEQ[ASRQ19]','ASRQ10BASEQ[ASRQ20]','ASRQ21BASEQ[ASRQ21]',
                'ASRQ21BASEQ[ASRQ22]','ASRQ21BASEQ[ASRQ23]','ASRQ21BASEQ[ASRQ24]','ASRQ21BASEQ[ASRQ25]','ASRQ21BASEQ[ASRQ26]','ASRQ21BASEQ[ASRQ27]','ASRQ21BASEQ[ASRQ28]',
                'ASRQ21BASEQ[ASRQ29]','ASRQ29Freitext','ASRQ30BASEQ[ASRQ30]','ASRQ30BASEQ[ASRQ31]','ASRQ30BASEQ[ASRQ32]','ASRQ30BASEQ[ASRQ33]','ASRQ30BASEQ[ASRQ34]',
                'ASRQ30BASEQ[ASRQ35]','ASRQ30BASEQ[ASRQ36]','ASRQ30BASEQ[ASRQ37]','ASRQ30BASEQ[ASRQ38]','ASRQ30BASEQ[ASRQ39]','ASRQ30BASEQ[ASRQ40]','ASRQ40Freitext',
                'ASRQ41BASEQ[ASRQ41]','ASRQ41BASEQ[ASRQ42]','ASRQ41BASEQ[ASRQ43]','ASRQ41BASEQ[ASRQ44]','ASRQ41BASEQ[ASRQ45]','ASRQ41BASEQ[ASRQ46]','ASRQ41BASEQ[ASRQ47]',
                'ASRQ41BASEQ[ASRQ48]','ASRQ41BASEQ[ASRQ49]','ASRQ41BASEQ[ASRQ50]','ASRQ46Freitext','ASRQ51BASEQ[ASRQ51]','ASRQ51BASEQ[ASRQ52]','ASRQ51BASEQ[ASRQ53]',
                'ASRQ51BASEQ[ASRQ54]','ASRQ51BASEQ[ASRQ55]','ASRQ56BASEQ[ASRVIII561]','ASRQ56BASEQ[ASRVIII562]','ASRQ56BASEQ[ASRVIII563]','ASRQ56BASEQ[ASRVIII564]',
                'ASRQ56BASEQ[ASRVIII565]','ASRQ56BASEQ[ASRVIII566]','ASRQ56BASEQ[ASRVIII567]','ASRQ56Freitext','ASRQ57BASEQ[ASRQ57]','ASRQ57BASEQ[ASRQ58]',
                'ASRQ57BASEQ[ASRQ59]', 'ASRQ57BASEQ[ASRQ60]','ASRQ58Freitext','ASRQ61BASEQ[ASRQ61]','ASRQ61BASEQ[ASRQ62]','ASRQ61BASEQ[ASRQ63]','ASRQ61BASEQ[ASRQ64]',
                'ASRQ61BASEQ[ASRQ65]','ASRQ61BASEQ[ASRQ66]','ASRQ61BASEQ[ASRQ67]','ASRQ61BASEQ[ASRQ68]','ASRQ61BASEQ[ASRQ69]','ASRQ61BASEQ[ASRQ70]','ASRQ66','ASRQ70',
                'ASRQ71BASEQ[ASRQ71]','ASRQ71BASEQ[ASRQ72]','ASRQ71BASEQ[ASRQ73]','ASRQ71BASEQ[ASRQ74]','ASRQ71BASEQ[ASRQ75]','ASRQ71BASEQ[ASRQ76]','ASRQ71BASEQ[ASRQ77]',
                'ASRQ71BASEQ[ASRQ78]','ASRQ71BASEQ[ASRQ79]','ASRQ71BASEQ[ASRQ80]','ASRQ77Freitext','ASQQ79Freitext','ASRQ81BASEQ[ASRQ81]','ASRQ81BASEQ[ASRQ82]','ASRQ81BASEQ[ASRQ83]',
                'ASRQ81BASEQ[ASRQ84]','ASRQ81BASEQ[ASRQ85]','ASRQ81BASEQ[ASRQ86]','ASRQ81BASEQ[ASRQ87]','ASRQ81BASEQ[ASRQ88]','ASRQ81BASEQ[ASRQ89]','ASRQ81BASEQ[ASRQ90]',
                'ASRQ84Freitext','ASRQ85Freitext','ASRQ91BASEQ[ASRQ91]','ASRQ91BASEQ[ASRQ92]','ASRQ91BASEQ[ASRQ93]','ASRQ91BASEQ[ASRQ94]','ASRQ91BASEQ[ASRQ95]',
                'ASRQ91BASEQ[ASRQ96]','ASRQ91BASEQ[ASRQ97]','ASRQ91BASEQ[ASRQ98]','ASRQ91BASEQ[ASRQ99]','ASRQ91BASEQ[ASRQ100]','ASR92Freitext','ASR100Freitext',
                'ASRQ101BASEQ[ASRQ101]','ASRQ101BASEQ[ASRQ102]','ASRQ101BASEQ[ASRQ103]','ASRQ101BASEQ[ASRQ104]','ASRQ101BASEQ[ASRQ105]','ASRQ101BASEQ[ASRQ106]',
                'ASRQ101BASEQ[ASRQ107]','ASRQ101BASEQ[ASRQ108]','ASRQ101BASEQ[ASRQ109]','ASRQ101BASEQ[ASRQ110]','ASRQ111BASEQ[ASRQ111]','ASRQ111BASEQ[ASRQ112]',
                'ASRQ111BASEQ[ASRQ113]','ASRQ111BASEQ[ASRQ114]','ASRQ111BASEQ[ASRQ115]','ASRQ111BASEQ[ASRQ116]','ASRQ111BASEQ[ASRQ117]','ASRQ111BASEQ[ASRQ118]',
                'ASRQ111BASEQ[ASRQ119]','ASRQ111BASEQ[ASRQ120]','ASRQ121BASEQ[ASRQ121]','ASRQ121BASEQ[ASRQ122]','ASRQ121BASEQ[ASRQ123]','ASRQ124','ASRQ125','ASRQ126']

        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['ASR_summary_adaptiveFunctioning_friends_sum','ASR_summary_adaptiveFunctioning_spouse_sum',
                                                    'ASR_summary_adaptiveFunctioning_family_sum', 'ASR_summary_adaptiveFunctioning_family_sum',
                                                    'ASR_summary_adaptiveFunctioning_job_sum', 'ASR_summary_adaptiveFunctioning_education_sum',
                                                    'ASR_scale_substanceUse_tabaco_perday','ASR_scale_substanceUse_alcohol_daysdrunk', 
                                                    'ASR_scale_substanceUse_drugs_daysused','ASR_summary_criticalItems_sum', 
                                                    'ASR_summary_syndromeProfiles_anxiousdepressed_sum', 
                                                    'ASR_summary_syndromeProfiles_withdrawn_sum', 
                                                    'ASR_summary_syndromeProfiles_somaticComplaints_sum',
                                                    'ASR_summary_syndromeProfiles_thoughtProblems_sum', 
                                                    'ASR_summary_syndromeProfiles_attentionProblems_sum', 
                                                    'ASR_summary_syndromeProfiles_aggressiveBehavior_sum', 
                                                    'ASR_summary_syndromeProfiles_rulebreakingBehavior_sum', 
                                                    'ASR_summary_syndromeProfiles_intrusive_sum', 
                                                    'ASR_summary_syndromeProfiles_internalizing_sum', 
                                                    'ASR_summary_syndromeProfiles_externalizing_sum']          
        df[cols_export].to_csv('%s/ASR.csv' % out_dir, index=False)



##############################################################################
########################## Self-Esteem Scale ################################# 
##############################################################################

def run_SelfEst(df, out_dir=None):
    
    
    print "Questionnaire measure self-esteem as the mean of 8 items\n"    
    
    #items to be recoded
    items_recoded = ['SEBASEQ[SE5r]',
                     'SEBASEQ[SE6r]',
                     'SEBASEQ[SE7r]',
                     'SEBASEQ[SE8r]'] 
    
    recoder = {1: 5, 2: 4, 4: 2, 5: 1}     
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64) 
    
    #scale aggregation
    cols = ['SEBASEQ[SE1]',
            'SEBASEQ[SE2]',
            'SEBASEQ[SE3]',
            'SEBASEQ[SE4]',
            'SEBASEQ[SE5r]', 
            'SEBASEQ[SE6r]',
            'SEBASEQ[SE7r]',
            'SEBASEQ[SE8r]']
    
    df['Mean_SelfEst'] = np.round(df[cols].mean(axis=1),3) 
                                      
    print df['Mean_SelfEst'].describe()
    sns.distplot(df['Mean_SelfEst'].dropna(), kde = True)                                  

    if out_dir:
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['Mean_SelfEst']          
        df[cols_export].to_csv('%s/SelfEst.csv' % out_dir, index=False)



##############################################################################
####################### Epsworth Sleepiness Scale ############################
##############################################################################

def run_ESS(data, out_dir=None):

    print 'Questionnaire measures general level of sleepiness as the sum of 8 Items\n'
    
    cols = ['ESSBASEQ[ESS1]', 'ESSBASEQ[ESS2]', 'ESSBASEQ[ESS3]', 'ESSBASEQ[ESS4]',
            'ESSBASEQ[ESS5]', 'ESSBASEQ[ESS6]', 'ESSBASEQ[ESS7]', 'ESSBASEQ[ESS8]']    
    
    data['ESS_summary_sum'] = data[cols].sum(axis=1)
    
                                
    print data['ESS_summary_sum'].describe()
    sns.countplot(data['ESS_summary_sum'].dropna(), order=range(int(data['ESS_summary_sum'].min()),int(data['ESS_summary_sum'].max())))
    plt.show()
    
    if out_dir:
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['ESS_summary_sum']          
        df[cols_export].to_csv('%s/ESS.csv' % out_dir, index=False)
    


##############################################################################
############################## BDI ###########################################
##############################################################################

def run_BDI(data, out_dir=None):

    cols_BDI = ['BDIABASEQ[BDIA0]','BDIABASEQ[BDIA1]','BDIABASEQ[BDIA2]','BDIABASEQ[BDIA3]','BDIBBASEQ[BDIB0]','BDIBBASEQ[BDIB1]','BDIBBASEQ[BDIB2]','BDIBBASEQ[BDIB3]',
                'BDICBASEQ[BDIC0]','BDICBASEQ[BDIC1]','BDICBASEQ[BDIC2]','BDICBASEQ[BDIC3]','BDIDBASEQ[BDID0]','BDIDBASEQ[BDID1]','BDIDBASEQ[BDID2]','BDIDBASEQ[BDID3]',
                'BDIEBASEQ[BDIE0]','BDIEBASEQ[BDIE1]','BDIEBASEQ[BDIE2]','BDIEBASEQ[BDIE3]','BDIFBASEQ[BDIF0]','BDIFBASEQ[BDIF1]','BDIFBASEQ[BDIF2]','BDIFBASEQ[BDIF3]',
                'BDIGBASEQ[BDIG0]','BDIGBASEQ[BDIG1]','BDIGBASEQ[BDIG2]','BDIGBASEQ[BDIG3]','BDIHBASEQ[BDIH0]','BDIHBASEQ[BDIH1]','BDIHBASEQ[BDIH2]','BDIHBASEQ[BDIH3]',
                'BDIIBASEQ[BDII0]','BDIIBASEQ[BDII1]','BDIIBASEQ[BDII2]','BDIIBASEQ[BDII3]','BDIJBASEQ[BDIJ0]','BDIJBASEQ[BDIJ1]','BDIJBASEQ[BDIJ2]','BDIJBASEQ[BDIJ3]',
                'BDIKBASEQ[BDIK0]','BDIKBASEQ[BDIK1]','BDIKBASEQ[BDIK2]','BDIKBASEQ[BDIK3]','BDILBASEQ[BDIL0]','BDILBASEQ[BDIL1]','BDILBASEQ[BDIL2]','BDILBASEQ[BDIL3]',
                'BDIMBASEQ[BDIM0]','BDIMBASEQ[BDIM1]','BDIMBASEQ[BDIM2]','BDIMBASEQ[BDIM3]','BDINBASEQ[BDIN0]','BDINBASEQ[BDIN1]','BDINBASEQ[BDIN2]','BDINBASEQ[BDIN3]',
                'BDIOBASEQ[BDIO0]','BDIOBASEQ[BDIO1]','BDIOBASEQ[BDIO2]','BDIOBASEQ[BDIO3]','BDIPBASEQ[BDIP0]','BDIPBASEQ[BDIP1]','BDIPBASEQ[BDIP2]','BDIPBASEQ[BDIP3]',
                'BDIQBASEQ[BDIQ0]','BDIQBASEQ[BDIQ1]','BDIQBASEQ[BDIQ2]','BDIQBASEQ[BDIQ3]','BDIRBASEQ[BDIR0]','BDIRBASEQ[BDIR1]','BDIRBASEQ[BDIR2]','BDIRBASEQ[BDIR3]',
                'BDISBASEQ[BDIS0]','BDISBASEQ[BDIS1]','BDISBASEQ[BDIS2]','BDISBASEQ[BDIS3]','BDIS4','BDITBASEQ[BDIT0]','BDITBASEQ[BDIT1]','BDITBASEQ[BDIT2]',
                'BDITBASEQ[BDIT3]','BDIUBASEQ[BDIU0]','BDIUBASEQ[BDIU1]','BDIUBASEQ[BDIU2]','BDIUBASEQ[BDIU3]']
    
    # recode items
    zero = ['BDIABASEQ[BDIA0]', 'BDIBBASEQ[BDIB0]', 'BDICBASEQ[BDIC0]',
            'BDIDBASEQ[BDID0]', 'BDIEBASEQ[BDIE0]', 'BDIFBASEQ[BDIF0]',
            'BDIGBASEQ[BDIG0]', 'BDIHBASEQ[BDIH0]', 'BDIIBASEQ[BDII0]', 
            'BDIJBASEQ[BDIJ0]', 'BDIKBASEQ[BDIK0]', 'BDILBASEQ[BDIL0]', 
            'BDIMBASEQ[BDIM0]', 'BDINBASEQ[BDIN0]', 'BDIOBASEQ[BDIO0]',
            'BDIPBASEQ[BDIP0]', 'BDIQBASEQ[BDIQ0]', 'BDIRBASEQ[BDIR0]',
            'BDISBASEQ[BDIS0]', 'BDITBASEQ[BDIT0]', 'BDIUBASEQ[BDIU0]']
    for item in zero:
        data[item].replace(to_replace='Y', value=0, inplace=True)
        data[item].replace(to_replace='NaN', value=0, inplace=True)
            
    one = ['BDIABASEQ[BDIA1]', 'BDIBBASEQ[BDIB1]', 'BDICBASEQ[BDIC1]',
           'BDIDBASEQ[BDID1]', 'BDIEBASEQ[BDIE1]', 'BDIFBASEQ[BDIF1]',
           'BDIGBASEQ[BDIG1]', 'BDIHBASEQ[BDIH1]', 'BDIIBASEQ[BDII1]', 
           'BDIJBASEQ[BDIJ1]', 'BDIKBASEQ[BDIK1]', 'BDILBASEQ[BDIL1]',
           'BDIMBASEQ[BDIM1]', 'BDINBASEQ[BDIN1]', 'BDIOBASEQ[BDIO1]',
           'BDIPBASEQ[BDIP1]', 'BDIQBASEQ[BDIQ1]', 'BDIRBASEQ[BDIR1]',
           'BDISBASEQ[BDIS1]', 'BDITBASEQ[BDIT1]', 'BDIUBASEQ[BDIU1]']
    for item in one:
        data[item].replace(to_replace='Y', value=1, inplace=True)
        data[item].replace(to_replace='NaN', value=0, inplace=True)
            
    two = ['BDIABASEQ[BDIA2]', 'BDIBBASEQ[BDIB2]', 'BDICBASEQ[BDIC2]',
           'BDIDBASEQ[BDID2]', 'BDIEBASEQ[BDIE2]', 'BDIFBASEQ[BDIF2]',
           'BDIGBASEQ[BDIG2]', 'BDIHBASEQ[BDIH2]', 'BDIIBASEQ[BDII2]', 
           'BDIJBASEQ[BDIJ2]', 'BDIKBASEQ[BDIK2]', 'BDILBASEQ[BDIL2]', 
           'BDIMBASEQ[BDIM2]', 'BDINBASEQ[BDIN2]', 'BDIOBASEQ[BDIO2]',
           'BDIPBASEQ[BDIP2]', 'BDIQBASEQ[BDIQ2]', 'BDIRBASEQ[BDIR2]',
           'BDISBASEQ[BDIS2]', 'BDITBASEQ[BDIT2]', 'BDIUBASEQ[BDIU2]']
    for item in two:
        data[item].replace(to_replace='Y', value=2, inplace=True)
        data[item].replace(to_replace='NaN', value=0, inplace=True)
            
    three = ['BDIABASEQ[BDIA3]', 'BDIBBASEQ[BDIB3]', 'BDICBASEQ[BDIC3]',
             'BDIDBASEQ[BDID3]', 'BDIEBASEQ[BDIE3]', 'BDIFBASEQ[BDIF3]', 
             'BDIGBASEQ[BDIG3]', 'BDIHBASEQ[BDIH3]', 'BDIIBASEQ[BDII3]', 
             'BDIJBASEQ[BDIJ3]', 'BDIKBASEQ[BDIK3]', 'BDILBASEQ[BDIL3]',
             'BDIMBASEQ[BDIM3]', 'BDINBASEQ[BDIN3]', 'BDIOBASEQ[BDIO3]',
             'BDIPBASEQ[BDIP3]', 'BDIQBASEQ[BDIQ3]', 'BDIRBASEQ[BDIR3]',
             'BDISBASEQ[BDIS3]', 'BDITBASEQ[BDIT3]', 'BDIUBASEQ[BDIU3]']
    for item in three:
        data[item].replace(to_replace='Y', value=3, inplace=True)
        data[item].replace(to_replace='NaN', value=0, inplace=True)         
             
    # output
    data['BDI_summary_sum'] = data[cols_BDI].sum(axis=1)                
    print 'For the general population, a score of 21 or over represents depression\n'   
    print data['BDI_summary_sum'].describe()
    sns.countplot(data['BDI_summary_sum'].dropna(), order=range(int(data['BDI_summary_sum'].min()),int(data['BDI_summary_sum'].max())))
    plt.show()
    
    if out_dir:
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols_BDI + ['BDI_summary_sum']          
        df[cols_export].to_csv('%s/BDI.csv' % out_dir, index=False)
    


##############################################################################
############################## HADS ##########################################
##############################################################################

def run_HADS(data, out_dir=None):
    # rescaled by 1- and reversed coding for items tense, frightened, worry, restless, panic, cheerful, slowed, appearance
    
    # anxiety / HADS-A
    tense = data['HADS1BASEQ[HADS1]'].subtract(1).multiply(-1).add(3)
    frightened = data['HADS3BASEQ[HADS3]'].subtract(1).multiply(-1).add(3)
    worry = data['HADS5BASEQ[HADS5]'].subtract(1).multiply(-1).add(3)
    relaxed = data['HADS7BASEQ[HADS7]'].subtract(1)
    butterflies = data['HADS9BASEQ[HADS9]'].subtract(1)
    restless = data['HADS11BASEQ[HADS11]'].subtract(1).multiply(-1).add(3)
    panic = data['HADS13BASEQ[HADS13]'].subtract(1).multiply(-1).add(3)
    anxiety = [tense, frightened, worry, relaxed, butterflies, restless, panic]
    
    # depression / HADS-D
    enjoy = data['HADS2BASEQ[HADS2]'].subtract(1)
    laugh = data['HADS4BASEQ[HADS4]'].subtract(1)
    cheerful = data['HADS6BASEQ[HADS6]'].subtract(1).multiply(-1).add(3)
    slowed = data['HADS8BASEQ[HADS8]'].subtract(1).multiply(-1).add(3)
    appearance = data['HADS10BASEQ[HADS10]'].subtract(1).multiply(-1).add(3)
    lookforward = data['HADS12BASEQ[HADS12]'].subtract(1)
    entertain = data['HADS14BASEQ[HADS14]'].subtract(1)
    depression = [enjoy, laugh, cheerful, slowed, appearance, lookforward, entertain]
    
    print 'rough interpretation: \n0-7 normal range, 8-10 suggestive presence of mood disorder, >11 probable presence of mood disorder \n'
    
    #### anxiety ####
    print 'HADS-A - anxiety\n'
    data['HADS_summary_HADS-A_sum'] = tense + frightened + worry + relaxed + butterflies + restless + panic
    print data['HADS_summary_HADS-A_sum'].describe()
    sns.countplot(data['HADS_summary_HADS-A_sum'].dropna(), order=range(int(data['HADS_summary_HADS-A_sum'].min()),int(data['HADS_summary_HADS-A_sum'].max())))
    plt.show()
     
    
    #### depression ####
    print '\n\nHADS-D - depression\n'
    data['HADS_summary_HADS-D_sum'] = enjoy + laugh + cheerful + slowed + appearance + lookforward + entertain
    print data['HADS_summary_HADS-D_sum'].describe()
    sns.countplot(data['HADS_summary_HADS-D_sum'].dropna(), order=range(int(data['HADS_summary_HADS-D_sum'].min()),int(data['HADS_summary_HADS-D_sum'].max())))
    plt.show()
    
    if out_dir:
        cols = ['HADS1BASEQ[HADS1]','HADS2BASEQ[HADS2]','HADS3BASEQ[HADS3]','HADS4BASEQ[HADS4]','HADS5BASEQ[HADS5]',
                'HADS6BASEQ[HADS6]','HADS7BASEQ[HADS7]','HADS8BASEQ[HADS8]','HADS9BASEQ[HADS9]','HADS10BASEQ[HADS10]',
                'HADS11BASEQ[HADS11]','HADS12BASEQ[HADS12]','HADS13BASEQ[HADS13]','HADS14BASEQ[HADS14]']
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['HADS_summary_HADS-A_sum', 'HADS_summary_HADS-D_sum']          
        df[cols_export].to_csv('%s/HADS.csv' % out_dir, index=False)



##############################################################################
##################### Boredom Proness Scale ##################################
##############################################################################

def run_BPS(df, out_dir=None):

    print "Questionnaire measures boredom proneness as the sum of 28 items\n"
    
    #items to be recoded                                
    items_recoded = ['BPSaBASEQ[BPS1]',
                     'BPSaBASEQ[BPS7]',
                     'BPSaBASEQ[BPS8]',
                     'BPSbBASEQ[BPS11]',
                     'BPSbBASEQ[BPS11]',
                     'BPSbBASEQ[BPS13]',
                     'BPSbBASEQ[BPS15]',
                     'BPSbBASEQ[BPS18]',
                     'BPScBASEQ[BPS22]',
                     'BPScBASEQ[BPS23]',
                     'BPScBASEQ[BPS24]']
                         
                             
    #recode items                 
    recoder = {1: 7 , 2: 6, 3: 5, 5: 3, 6: 2, 7: 1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   

    #Calculate total score as the sum of Item 1-28.
    cols = ['BPSaBASEQ[BPS1]','BPSaBASEQ[BPS2]','BPSaBASEQ[BPS3]',
            'BPSaBASEQ[BPS4]','BPSaBASEQ[BPS5]','BPSaBASEQ[BPS6]',
            'BPSaBASEQ[BPS7]','BPSaBASEQ[BPS8]','BPSaBASEQ[BPS9]',
            'BPSaBASEQ[BPS10]','BPSbBASEQ[BPS11]','BPSbBASEQ[BPS12]',
            'BPSbBASEQ[BPS13]','BPSbBASEQ[BPS14]','BPSbBASEQ[BPS15]',
            'BPSbBASEQ[BPS16]','BPSbBASEQ[BPS17]','BPSbBASEQ[BPS18]',
            'BPSbBASEQ[BPS19]','BPSbBASEQ[BPS20]','BPSbBASEQ[BPS21]',
            'BPScBASEQ[BPS22]','BPScBASEQ[BPS23]','BPScBASEQ[BPS24]',
            'BPScBASEQ[BPS25]','BPScBASEQ[BPS26]','BPScBASEQ[BPS27]',
            'BPScBASEQ[BPS28]']
    
    df['BPS_sum'] = df[cols].sum(axis=1)
                    
    print df['BPS_sum'].describe() 
    sns.distplot(df['BPS_sum'].dropna(), kde = True)                
    
    if out_dir:
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['BPS_sum']          
        df[cols_export].to_csv('%s/BPS.csv' % out_dir, index=False)



##############################################################################
################# Derryberry Attention Control Scale #########################
##############################################################################

def run_DAC(df, out_dir=None):
    #items to be recoded                                
    items_recoded = ['DACaBASEQ[DAC1]',
                    'DACaBASEQ[DAC2]',
                    'DACaBASEQ[DAC3]',
                    'DACaBASEQ[DAC6]',
                    'DACaBASEQ[DAC7]',
                    'DACbBASEQ[DAC8]',
                    'DACbBASEQ[DAC11]',
                    'DACbBASEQ[DAC12]',     
                    'DACbBASEQ[DAC15]',
                    'DACcBASEQ[DAC16]',
                    'DACcBASEQ[DAC20]']
    
    #recode items                 
    recoder = {1: 4 , 2: 3, 3: 2, 4: 1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   

    #Calculate total score as the sum of Item 1-20.
    cols = ['DACaBASEQ[DAC1]','DACaBASEQ[DAC2]','DACaBASEQ[DAC3]',
            'DACaBASEQ[DAC4]','DACaBASEQ[DAC5]','DACaBASEQ[DAC6]',
            'DACaBASEQ[DAC7]','DACbBASEQ[DAC8]','DACbBASEQ[DAC9]',
            'DACbBASEQ[DAC10]','DACbBASEQ[DAC11]','DACbBASEQ[DAC12]',
            'DACbBASEQ[DAC13]','DACbBASEQ[DAC14]','DACbBASEQ[DAC15]',
            'DACcBASEQ[DAC16]','DACcBASEQ[DAC17]','DACcBASEQ[DAC18]',
            'DACcBASEQ[DAC19]','DACcBASEQ[DAC20]']     
    
    df['DAC_sum'] = df[cols].sum(axis=1)
    print df['DAC_sum'].describe()   
    sns.distplot(df['DAC_sum'].dropna(), kde = True)
    
    if out_dir:
        age = pd.Series(pd.to_datetime(df['submitdate']) - pd.to_datetime(df['GBT']))
        df['age'] = age.dt.days / 365
        df['ID'] = df['ID'].map(lambda x: str(x)[0:5])
        cols_export = ['ID', 'GSH', 'age'] + cols + ['DAC_sum']          
        df[cols_export].to_csv('%s/DAC.csv' % out_dir, index=False)
  


##############################################################################
############################## NEO-PI-R ######################################
##############################################################################

def run_NEOPIR():
    
    print 'measure of the Five Factor Model and uses these five dimensions to evaluate adult personality' 
    print '– emotional, interpersonal, experiential, attitudinal, and motivational styles –' 
    print '181 items using a 5-point scale'
    
    df = pd.read_pickle('/scr/liberia1/data/lsd/behavioral/NEO/Neo_complete.pkl')
        
    #recode reversed items
    items_recoded = ['61','1','121','181','36','96','156','11','71','46','106','166','21'
                     ,'81','231','141','56','116','176','206','236','32','92','7','67','127',
                     '187','42','102','162','222','17','77','137','52','112','27',
                     '87','147','207','33','93','153','183','213','8','68','128','43','103',
                     '163','18','78','138','198','228','53','113','173', '28', '88', '148', '208',
                     '238' ,'4' ,'64','124','39','99','159','189','219',
                     '14','74','134','49','109','169','199','229','24','84','144','234',
                     '59','119','35','95','155','10','70','130','190','220','45','105','20',
                     '80','140','55','115','175','205','30','90','150']
                 
                  
                     
    recoder = {0: 4, 1: 3, 3: 1, 4: 0}    
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)  
    
    # calculate subscales as means for all 30 facets

    #Neuroticism
    df['NEO_N'] = df[['1','31','61','91','121','151','181','211',
                       '6','36','66','96','126','156','186','216',
                       '11','41','71','101','131','161','191','221',
                       '16','46','76','106','136','166','196','226',
                       '21','51','81','111','141','171','201','231',
                       '26','56','86','116','146','176','206','236']].mean(axis=1)
                       
    print '\n','### NEO Neuroticism ###'                   
    print df['NEO_N'].describe()                    
            
    #N1 anxiety
    df['NEO_N1_anx'] = df[['1','31','61','91','121','151','181','211']].mean(axis=1)
    #N2 angry hostility
    df['NEO_N2_host'] = df[['6','36','66','96','126','156','186','216']].mean(axis=1)
    #N3 Depression
    df['NEO_N3_depr'] = df[['11','41','71','101','131','161','191','221']].mean(axis=1)
    #N4 Self Consciousness
    df['NEO_N4_selfcon'] = df[['16','46','76','106','136','166','196','226']].mean(axis=1)
    #N5 Impulsiveness
    df['NEO_N5_imp'] = df[['21','51','81','111','141','171','201','231']].mean(axis=1)
    #N6 Vulnerability
    df['NEO_N6_vuln'] = df[['26','56','86','116','146','176','206','236']].mean(axis=1)
    
    
    
    
    #Extraversion
    
    df['NEO_E'] = df[['2','32','62','92','122','152','182','212',
                      '7','37','67','97','127','157','187','217',
                      '12','42','72','102','132','162','192','222',
                      '17','47','77','107','137','167','197','227',
                      '22','52','82','112','142','172','202','232',
                      '27','57','87','117','147','177','207','237']].mean(axis=1)
     
    print '\n','### NEO Extraversion ###'                   
    print df['NEO_E'].describe()  

       
    #E1 warmth
    df['NEO_E1_warm'] = df[['2','32','62','92','122','152','182','212']].mean(axis=1)
    #E2 Gregariousness
    df['NEO_E2_greg'] = df[['7','37','67','97','127','157','187','217']].mean(axis=1)
    #N3 Assertiveness
    df['NEO_E3_ass'] = df[['12','42','72','102','132','162','192','222']].mean(axis=1)
    #N4 Activity
    df['NEO_E4_act'] = df[['17','47','77','107','137','167','197','227']].mean(axis=1)
    #N5 Excitement Seeking
    df['NEO_E5_excseek'] = df[['22','52','82','112','142','172','202','232']].mean(axis=1)
    #N6 Positive Emotions
    df['NEO_E6_PosEmo'] = df[['27','57','87','117','147','177','207','237']].mean(axis=1)

    
    #Openness
    #item 83 missing
    
    df['NEO_O'] = df[['3','33','63','93','123','153','183','213',
                      '8','38','68','98','128','158','188','218',
                      '13','43','73','103','133','163','193','223',
                      '18','48','78','108','138','168','198','228',
                      '23','53','113','143','173','203','233',
                      '28','58','88','118','148','178','208','238']].mean(axis=1)
    
    print '\n','### NEO Openness (item 83 missing) ###'                   
    print df['NEO_O'].describe()     
    
    
    #O1 fantasy
    df['NEO_O1_fan'] = df[['3','33','63','93','123','153','183','213']].mean(axis=1)
    #O2 aesthetics
    df['NEO_O2_aest'] = df[['8','38','68','98','128','158','188','218']].mean(axis=1)
    #O3 feelings
    df['NEO_O3_feel'] = df[['13','43','73','103','133','163','193','223']].mean(axis=1)
    #04 actions
    df['NEO_O4_act'] = df[['18','48','78','108','138','168','198','228']].mean(axis=1)
    #05 ideas
    #item 83 missing
    df['NEO_O5_idea'] = df[['23','53','113','143','173','203','233']].mean(axis=1)
    #06 values
    df['NEO_O6_value'] = df[['28','58','88','118','148','178','208','238']].mean(axis=1)
    
    #Agreeableness
    
    df['NEO_A'] = df[['4','34','64','94','124','154','184','214',
                      '9','39','69','99','129','159','189','219',
                      '14','44','74','104','134','164','194','224',
                      '19','49','79','109','139','169','199','229',
                      '24','54','84','114','144','174','204','234',
                      '29','59','89','119','149','179','209','239']].mean(axis=1)
    
    print '\n','### NEO Agreeableness ###'                   
    print df['NEO_A'].describe()        
    
    
    
    #A1 trust
    df['NEO_A1_trust'] = df[['4','34','64','94','124','154','184','214']].mean(axis=1)
    #A2 straightforwardedness
    df['NEO_A2_sf'] = df[['9','39','69','99','129','159','189','219']].mean(axis=1)
    #A3 altruism
    df['NEO_A3_altr'] = df[['14','44','74','104','134','164','194','224']].mean(axis=1)
    #A4 compliance
    df['NEO_A4_compl'] = df[['19','49','79','109','139','169','199','229']].mean(axis=1)
    #A5 modesty
    df['NEO_A5_modes'] = df[['24','54','84','114','144','174','204','234']].mean(axis=1)
    #A6 tender_mindedness
    df['NEO_A6_tenmind'] = df[['29','59','89','119','149','179','209','239']].mean(axis=1)
    
    #Conscientiousness
    
    df['NEO_C'] = df[['5','35','65','95','125','155','185','215',
                             '10','40','70','100','130','160','190','220',
                             '15','45','75','105','135','165','195','225',
                             '20','50','80','110','140','170','200','230',
                             '25','55','85','115','145','175','205','235',
                             '30','60','90','120','150','180','210','240']].mean(axis=1)
    
    
    print '\n','### NEO Conscientiousnesss ###'                   
    print df['NEO_C'].describe()     
    
    
    #C1 compentence 
    df['NEO_C1_comp'] = df[['5','35','65','95','125','155','185','215']].mean(axis=1)
    #C2 order
    df['NEO_C2_order'] = df[['10','40','70','100','130','160','190','220']].mean(axis=1)
    #C3 dutifulness
    df['NEO_C3_dutif'] = df[['15','45','75','105','135','165','195','225']].mean(axis=1)
    #C4 achievement striving 
    df['NEO_C4_achstr'] = df[['20','50','80','110','140','170','200','230']].mean(axis=1)
    #C5 self discipline
    df['NEO_C5_selfdis'] = df[['25','55','85','115','145','175','205','235']].mean(axis=1)
    #C6 deliberation
    df['NEO_C6_deli'] = df[['30','60','90','120','150','180','210','240']].mean(axis=1)
  
    #create histograms of subscales
    plt.figure(figsize =(16,12))
    
    plt.subplot(231)
    sns.distplot(df["NEO_N"].dropna(), kde = True)
    plt.xlabel('NEO_N', fontsize = 14)
    
    plt.subplot(232)
    sns.distplot(df['NEO_E'].dropna(), kde = True)
    plt.xlabel('NEO_E', fontsize = 14)
   
    plt.subplot(233)
    sns.distplot(df['NEO_O'].dropna(), kde = True)
    plt.xlabel('NEO_O', fontsize = 14)
    
    
    plt.subplot(234)
    sns.distplot(df['NEO_A'].dropna(), kde = True)
    plt.xlabel('NEO_A', fontsize = 14)
    
    
    plt.subplot(235)
    sns.distplot(df['NEO_C'].dropna(), kde = True)
    plt.xlabel('NEO_C', fontsize = 14)
    plt.show()
    clf()
    
  
    
    
    plt.figure(figsize =(20,35))
    
    plt.subplot(841)
    sns.distplot(df['NEO_N1_anx'].dropna(), kde = True)
    plt.xlabel('NEO_N1_anx', fontsize = 14)
    
    plt.subplot(842)
    sns.distplot(df['NEO_N2_host'].dropna(), kde = True)
    plt.xlabel('NEO_N2_host', fontsize = 14)
    
    plt.subplot(843)
    sns.distplot(df['NEO_N3_depr'].dropna(), kde = True)
    plt.xlabel('NEO_N3_depr', fontsize = 14)
    
    plt.subplot(8,4,4)
    sns.distplot(df['NEO_N4_selfcon'].dropna(), kde = True)
    plt.xlabel('NEO_N4_selfcon', fontsize = 14)
    
    plt.subplot(8,4,5)
    sns.distplot(df['NEO_N5_imp'].dropna(), kde = True)
    plt.xlabel('NEO_N5_imp', fontsize = 14)
    
    plt.subplot(8,4,6)
    sns.distplot(df['NEO_N6_vuln'].dropna(), kde = True)
    plt.xlabel('NEO_N6_vuln', fontsize = 14)
    
    plt.subplot(8,4,7)
    sns.distplot(df['NEO_E1_warm'].dropna(), kde = True)
    plt.xlabel('NEO_E1_warm', fontsize = 14)
    
    plt.subplot(8,4,8)
    sns.distplot(df['NEO_E2_greg'].dropna(), kde = True)
    plt.xlabel('NEO_E2_greg', fontsize = 14)
    
    plt.subplot(8,4,9)
    sns.distplot(df['NEO_E3_ass'].dropna(), kde = True)
    plt.xlabel('NEO_E3_ass', fontsize = 14)
    
    plt.subplot(8,4,10)
    sns.distplot(df['NEO_E4_act'].dropna(), kde = True)
    plt.xlabel('NEO_E4_act', fontsize = 14)
    
    plt.subplot(8,4,11)
    sns.distplot(df['NEO_E5_excseek'].dropna(), kde = True)
    plt.xlabel('NEO_E5_excseek', fontsize = 14)
    
    plt.subplot(8,4,12)
    sns.distplot(df['NEO_E6_PosEmo'].dropna(), kde = True)
    plt.xlabel('NEO_E6_PosEmo', fontsize = 14)
    
    plt.subplot(8,4,13)
    sns.distplot(df['NEO_O1_fan'].dropna(), kde = True)
    plt.xlabel('NEO_O1_fan', fontsize = 14)
    
    plt.subplot(8,4,14)
    sns.distplot(df['NEO_O2_aest'].dropna(), kde = True)
    plt.xlabel('NEO_O2_aest', fontsize = 14)
    
    plt.subplot(8,4,15)
    sns.distplot(df['NEO_O3_feel'].dropna(), kde = True)
    plt.xlabel('NEO_O3_feel', fontsize = 14)
    
    plt.subplot(8,4,16)
    sns.distplot(df['NEO_O4_act'].dropna(), kde = True)
    plt.xlabel('NEO_O4_act', fontsize = 14)
    
    plt.subplot(8,4,17)
    sns.distplot(df['NEO_O5_idea'].dropna(), kde = True)
    plt.xlabel('NEO_O5_idea', fontsize = 14)
           
    plt.subplot(8,4,18)
    sns.distplot(df['NEO_O6_value'].dropna(), kde = True)
    plt.xlabel('NEO_O6_value', fontsize = 14)
    
    plt.subplot(8,4,19)
    sns.distplot(df['NEO_A1_trust'].dropna(), kde = True)
    plt.xlabel('NEO_A1_trust', fontsize = 14)
    
    plt.subplot(8,4,20)
    sns.distplot(df['NEO_A2_sf'].dropna(), kde = True)
    plt.xlabel('NEO_A2_sf', fontsize = 14)
    
    plt.subplot(8,4,21)
    sns.distplot(df['NEO_A3_altr'].dropna(), kde = True)
    plt.xlabel('NEO_A3_altr', fontsize = 14)
    
    plt.subplot(8,4,22)
    sns.distplot(df['NEO_A4_compl'].dropna(), kde = True)
    plt.xlabel('NEO_A4_compl', fontsize = 14)
    
    plt.subplot(8,4,23)
    sns.distplot(df['NEO_A5_modes'].dropna(), kde = True)
    plt.xlabel('NEO_A5_modes', fontsize = 14)
          
    plt.subplot(8,4,24)
    sns.distplot(df['NEO_A6_tenmind'].dropna(), kde = True)
    plt.xlabel('NEO_A6_tenmind', fontsize = 14)
    
    plt.subplot(8,4,25)
    sns.distplot(df['NEO_C1_comp'].dropna(), kde = True)
    plt.xlabel('NEO_C1_comp', fontsize = 14)
          
    plt.subplot(8,4,26)
    sns.distplot(df['NEO_C2_order'].dropna(), kde = True)
    plt.xlabel('NEO_C2_order', fontsize = 14)
    
    plt.subplot(8,4,27)
    sns.distplot(df['NEO_C3_dutif'].dropna(), kde = True)
    plt.xlabel('NEO_C3_dutif', fontsize = 14)
    
    plt.subplot(8,4,28)
    sns.distplot(df['NEO_C4_achstr'].dropna(), kde = True)
    plt.xlabel('NEO_C4_achstr', fontsize = 14)
    
    plt.subplot(8,4,29)
    sns.distplot(df['NEO_C5_selfdis'].dropna(), kde = True)
    plt.xlabel('NEO_C5_selfdis', fontsize = 14)
          
    plt.subplot(8,4,30)
    sns.distplot(df['NEO_C6_deli'].dropna(), kde = True)
    plt.xlabel('NEO_C6_deli', fontsize = 14)



##############################################################################
############# PSSI - Persönlichkeitsstil- und Störungsinventar################
##############################################################################

def run_PSSI(df, out_dir=None):
    cols_PSSI = ['PSSaBASEQ[PSS1]','PSSaBASEQ[PSS2]','PSSaBASEQ[PSS3]','PSSaBASEQ[PSS4]','PSSaBASEQ[PSS5]','PSSaBASEQ[PSS6]','PSSaBASEQ[PSS7]','PSSaBASEQ[PSS8]','PSSaBASEQ[PSS9]',
             'PSSaBASEQ[PSS10]','PSSbBASEQ[PSS11]','PSSbBASEQ[PSS12]','PSSbBASEQ[PSS13]','PSSbBASEQ[PSS14]','PSSbBASEQ[PSS15r]','PSSbBASEQ[PSS16]','PSSbBASEQ[PSS17]',
             'PSSbBASEQ[PSS18]','PSSbBASEQ[PSS19]','PSSbBASEQ[PSS20]','PSScBASEQ[PSS21]','PSScBASEQ[PSS22]','PSScBASEQ[PSS23]','PSScBASEQ[PSS24]','PSScBASEQ[PSS25]',
             'PSScBASEQ[PSS26]','PSScBASEQ[PSS27]','PSScBASEQ[PSS28]','PSScBASEQ[PSS29]','PSScBASEQ[PSS30]','PSSdBASEQ[PSS31]','PSSdBASEQ[PSS32]','PSSdBASEQ[PSS33]',
             'PSSdBASEQ[PSS34]','PSSdBASEQ[PSS35]','PSSdBASEQ[PSS36]','PSSdBASEQ[PSS37]','PSSdBASEQ[PSS38]','PSSdBASEQ[PSS39r]','PSSdBASEQ[PSS40]','PSSeBASEQ[PSS41]',
             'PSSeBASEQ[PSS42]','PSSeBASEQ[PSS43r]','PSSeBASEQ[PSS44r]','PSSeBASEQ[PSS45]','PSSeBASEQ[PSS46]','PSSeBASEQ[PSS47]','PSSeBASEQ[PSS48]','PSSeBASEQ[PSS49r]',
             'PSSeBASEQ[PSS50]','PSSfBASEQ[PSS51]','PSSfBASEQ[PSS52]','PSSfBASEQ[PSS53]','PSSfBASEQ[PSS54]','PSSfBASEQ[PSS55]','PSSfBASEQ[PSS56]','PSSfBASEQ[PSS57]',
             'PSSfBASEQ[PSS58]','PSSfBASEQ[PSS59]','PSSfBASEQ[PSS60]','PSSgBASEQ[PSS61]','PSSgBASEQ[PSS62]','PSSgBASEQ[PSS63]','PSSgBASEQ[PSS64]','PSSgBASEQ[PSS65]',
             'PSSgBASEQ[PSS66]','PSSgBASEQ[PSS67r]','PSSgBASEQ[PSS68]','PSSgBASEQ[PSS69]','PSSgBASEQ[PSS70]','PSShBASEQ[PSS71r]','PSShBASEQ[PSS72r]','PSShBASEQ[PSS73]',
             'PSShBASEQ[PSS74]','PSShBASEQ[PSS75]','PSShBASEQ[PSS76]','PSShBASEQ[PSS77]','PSShBASEQ[PSS78]','PSShBASEQ[PSS79]','PSShBASEQ[PSS80]','PSSiBASEQ[PSS81]',
             'PSSiBASEQ[PSS82]','PSSiBASEQ[PSS83]','PSSiBASEQ[PSS84]','PSSiBASEQ[PSS85]','PSSiBASEQ[PSS86r]','PSSiBASEQ[PSS87]','PSSiBASEQ[PSS88]','PSSiBASEQ[PSS89]',
             'PSSiBASEQ[PSS90]','PSSjBASEQ[PSS91r]','PSSjBASEQ[PSS92]','PSSjBASEQ[PSS93]','PSSjBASEQ[PSS94]','PSSjBASEQ[PSS95]','PSSjBASEQ[PSS96]','PSSjBASEQ[PSS97]',
             'PSSjBASEQ[PSS98]','PSSjBASEQ[PSS99r]','PSSjBASEQ[PSS100]','PSSkBASEQ[PSS101]','PSSkBASEQ[PSS102]','PSSkBASEQ[PSS103]','PSSkBASEQ[PSS104r]','PSSkBASEQ[PSS105r]',
             'PSSkBASEQ[PSS106]','PSSkBASEQ[PSS107]','PSSkBASEQ[PSS108]','PSSkBASEQ[PSS109r]','PSSkBASEQ[PSS110]','PSSlBASEQ[PSS111]','PSSlBASEQ[PSS112]','PSSlBASEQ[PSS113]',
             'PSSlBASEQ[PSS114]','PSSlBASEQ[PSS115]','PSSlBASEQ[PSS116]','PSSlBASEQ[PSS117]','PSSlBASEQ[PSS118]','PSSlBASEQ[PSS119]','PSSlBASEQ[PSS120]','PSSmBASEQ[PSS121]',
             'PSSmBASEQ[PSS122]','PSSmBASEQ[PSS123]','PSSmBASEQ[PSS124]','PSSmBASEQ[PSS125]','PSSmBASEQ[PSS126]','PSSmBASEQ[PSS127]','PSSmBASEQ[PSS128]','PSSmBASEQ[PSS129]',
             'PSSmBASEQ[PSS130]','PSSnBASEQ[PSS131]','PSSnBASEQ[PSS132]','PSSnBASEQ[PSS133]','PSSnBASEQ[PSS134]','PSSnBASEQ[PSS135]','PSSnBASEQ[PSS136]','PSSnBASEQ[PSS137r]',
             'PSSnBASEQ[PSS138]','PSSnBASEQ[PSS139]','PSSnBASEQ[PSS140]']
    #recode all items to original format (limesurvey: 1234, original = 0123)
    recoder = {1: 0, 2: 1, 3: 2, 4: 3 }
    for i in cols_PSSI:
        df[i] = df[i].map(recoder).astype(float64) 
        
    #recode reversed items
    items_recoded = ['PSSbBASEQ[PSS15r]',
                     'PSSeBASEQ[PSS43r]',
                     'PSShBASEQ[PSS71r]',
                     'PSSjBASEQ[PSS99r]',
                     'PSSeBASEQ[PSS44r]', 
                     'PSShBASEQ[PSS72r]',
                     'PSSiBASEQ[PSS86r]',
                     'PSSkBASEQ[PSS104r]',
                     'PSSeBASEQ[PSS49r]',
                     'PSSjBASEQ[PSS91r]', 
                     'PSSkBASEQ[PSS105r]',
                     'PSSdBASEQ[PSS39r]',
                     'PSSgBASEQ[PSS67r]',
                     'PSSkBASEQ[PSS109r]',
                     'PSSnBASEQ[PSS137r]']    
                     
    recoder = {0: 3, 1: 2, 2: 1, 3: 0}     
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)  
    
    # calculate subscales as sumscores   
    
    #PN = eigenwillig_paranoid     
    df['PSSI_PN'] = df[['PSSaBASEQ[PSS1]',
                        'PSSbBASEQ[PSS15r]',
                        'PSScBASEQ[PSS29]',
                        'PSSeBASEQ[PSS43r]', 
                        'PSSfBASEQ[PSS57]',
                        'PSShBASEQ[PSS71r]',
                        'PSSiBASEQ[PSS85]',
                        'PSSjBASEQ[PSS99r]',
                        'PSSlBASEQ[PSS113]',
                        'PSSmBASEQ[PSS127]']].sum(axis=1)
                        
    print '\n', '### PSSI_PN: eigenwillig paranoid ###'
    print df['PSSI_PN'].describe()                    
    
    #SZ = zurückhaltend-schizoid                    
    df['PSSI_SZ'] = df[['PSSaBASEQ[PSS2]',
                        'PSSbBASEQ[PSS16]',
                        'PSScBASEQ[PSS30]',
                        'PSSeBASEQ[PSS44r]', 
                        'PSSfBASEQ[PSS58]',
                        'PSShBASEQ[PSS72r]',
                        'PSSiBASEQ[PSS86r]',
                        'PSSjBASEQ[PSS100]',
                        'PSSlBASEQ[PSS114]', 
                        'PSSmBASEQ[PSS128]']].sum(axis=1)
    
    
    print '\n','### PSSI_SZ: zurückhaltend-schizoid ###'
    print df['PSSI_SZ'].describe()                     
    
    
    
    #ST = ahnungsvoll-schizotypisch
                        
    df['PSSI_ST'] = df[['PSSaBASEQ[PSS3]',
                        'PSSbBASEQ[PSS17]',
                        'PSSdBASEQ[PSS31]',
                        'PSSeBASEQ[PSS45]',
                        'PSSfBASEQ[PSS59]',
                        'PSShBASEQ[PSS73]',
                        'PSSiBASEQ[PSS87]',
                        'PSSkBASEQ[PSS101]',
                        'PSSlBASEQ[PSS115]', 
                        'PSSmBASEQ[PSS129]']].sum(axis=1)     
    
    
    print '\n', '### PSSI_ST ahnungsvoll-schizotypisch ###'
    print df['PSSI_ST'].describe()                         
                        
    #BL = spontan-borderline
    df['PSSI_BL'] = df[['PSSaBASEQ[PSS4]',
                        'PSSbBASEQ[PSS18]',
                        'PSSdBASEQ[PSS32]',
                        'PSSeBASEQ[PSS46]', 
                        'PSSfBASEQ[PSS60]',
                        'PSShBASEQ[PSS74]',
                        'PSSiBASEQ[PSS88]',
                        'PSSkBASEQ[PSS102]',
                        'PSSlBASEQ[PSS116]', 
                        'PSSmBASEQ[PSS130]']].sum(axis=1) 
    
    print '\n','### PSSI_BL spontan-borderline ###'
    print df['PSSI_BL'].describe()                         
                                                
    #HI = liebenswürdig-hisrtionisch
    df['PSSI_HI'] = df[['PSSaBASEQ[PSS5]',
                        'PSSbBASEQ[PSS19]',
                        'PSSdBASEQ[PSS33]',
                        'PSSeBASEQ[PSS47]', 
                        'PSSgBASEQ[PSS61]',
                        'PSShBASEQ[PSS75]',
                        'PSSiBASEQ[PSS89]',
                        'PSSkBASEQ[PSS103]',
                        'PSSlBASEQ[PSS117]', 
                        'PSSnBASEQ[PSS131]']].sum(axis=1)
    
    print '\n','### PSSI_HI liebenswürdig-histrionisch ###'
    print df['PSSI_HI'].describe()                         
                                      
    # NA = ehrgeizig_narzisstisch                   
    df['PSSI_NA'] = df[['PSSaBASEQ[PSS6]',
                        'PSSbBASEQ[PSS20]',
                        'PSSdBASEQ[PSS34]',
                        'PSSeBASEQ[PSS48]', 
                        'PSSgBASEQ[PSS62]',
                        'PSShBASEQ[PSS76]',
                        'PSSiBASEQ[PSS90]',
                        'PSSkBASEQ[PSS104r]',
                        'PSSlBASEQ[PSS118]', 
                        'PSSnBASEQ[PSS132]']].sum(axis=1)  
    
    print '\n','### PSSI_NA ehrgeizig_narzisstisch  ###'
    print df['PSSI_NA'].describe()                         
                                      
    #SU = selbstkritisch-selbstunsicher                    
    df['PSSI_SU'] = df[['PSSaBASEQ[PSS7]',
                        'PSScBASEQ[PSS21]',
                        'PSSdBASEQ[PSS35]',
                        'PSSeBASEQ[PSS49r]', 
                        'PSSgBASEQ[PSS63]',
                        'PSShBASEQ[PSS77]',
                        'PSSjBASEQ[PSS91r]',
                        'PSSkBASEQ[PSS105r]',
                        'PSSlBASEQ[PSS119]', 
                        'PSSnBASEQ[PSS133]']].sum(axis=1)
    
    print '\n','### PSSI_SU selbstkritisch-selbstunsicher ###'
    print df['PSSI_SU'].describe()                         
                                  
    # AB = loyal-abhängig  
    df['PSSI_AB'] = df[['PSSaBASEQ[PSS8]',
                        'PSScBASEQ[PSS22]',
                        'PSSdBASEQ[PSS36]',
                        'PSSeBASEQ[PSS50]', 
                        'PSSgBASEQ[PSS64]',
                        'PSShBASEQ[PSS78]',
                        'PSSjBASEQ[PSS92]',
                        'PSSkBASEQ[PSS106]',
                        'PSSlBASEQ[PSS120]', 
                        'PSSnBASEQ[PSS134]']].sum(axis=1)    
    
    print '\n','### PSSI_AB loyal-abhängig  ###'
    print df['PSSI_AB'].describe()                         
                             
    # ZW = sorgfältig - zwanghaft
    df['PSSI_ZW'] = df[['PSSaBASEQ[PSS9]',
                        'PSScBASEQ[PSS23]',
                        'PSSdBASEQ[PSS37]',
                        'PSSfBASEQ[PSS51]', 
                        'PSSgBASEQ[PSS65]',
                        'PSShBASEQ[PSS79]',
                        'PSSjBASEQ[PSS93]',
                        'PSSkBASEQ[PSS107]',
                        'PSSmBASEQ[PSS121]', 
                        'PSSnBASEQ[PSS135]']].sum(axis=1)   
    
    print '\n','### PSSI_ZW sorgfältig - zwanghaft  ###'
    print df['PSSI_ZW'].describe()                         
                                 
    #NT = kritisch-negativistisch    
    df['PSSI_NT'] = df[['PSSaBASEQ[PSS10]',
                        'PSScBASEQ[PSS24]',
                        'PSSdBASEQ[PSS38]',
                        'PSSfBASEQ[PSS52]', 
                        'PSSgBASEQ[PSS66]',
                        'PSShBASEQ[PSS80]',
                        'PSSjBASEQ[PSS94]',
                        'PSSkBASEQ[PSS108]',
                        'PSSmBASEQ[PSS122]', 
                        'PSSnBASEQ[PSS136]']].sum(axis=1)
    
    print '\n','### PSSI_NT kritisch-negativistisch   ###'
    print df['PSSI_NT'].describe()                         
                                                
    # DP = still depressiv
    df['PSSI_DP'] = df[['PSSbBASEQ[PSS11]',
                        'PSScBASEQ[PSS25]',
                        'PSSdBASEQ[PSS39r]',
                        'PSSfBASEQ[PSS53]', 
                        'PSSgBASEQ[PSS67r]', 
                        'PSSiBASEQ[PSS81]',
                        'PSSjBASEQ[PSS95]',
                        'PSSkBASEQ[PSS109r]',
                        'PSSmBASEQ[PSS123]', 
                        'PSSnBASEQ[PSS137r]']].sum(axis=1)
    
    print '\n','### PSSI_DP still depressiv ###'
    print df['PSSI_DP'].describe()                         
                           
    #SL = hilfsbereit-selbstlos
    df['PSSI_SL'] = df[['PSSbBASEQ[PSS12]',
                        'PSScBASEQ[PSS26]',
                        'PSSdBASEQ[PSS40]',
                        'PSSfBASEQ[PSS54]', 
                        'PSSgBASEQ[PSS68]', 
                        'PSSiBASEQ[PSS82]', 
                        'PSSjBASEQ[PSS96]',
                        'PSSkBASEQ[PSS110]',
                        'PSSmBASEQ[PSS124]', 
                        'PSSnBASEQ[PSS138]']].sum(axis=1)
    
    print '\n','### PSSI_SL hilfsbereit-selbstlos ###'
    print df['PSSI_SL'].describe()                         
                             
    #RH = optimistisch-rhapsodisch
    df['PSSI_RH'] = df[['PSSbBASEQ[PSS13]',
                        'PSScBASEQ[PSS27]',
                        'PSSeBASEQ[PSS41]',
                        'PSSfBASEQ[PSS55]', 
                        'PSSgBASEQ[PSS69]',
                        'PSSiBASEQ[PSS83]',
                        'PSSjBASEQ[PSS97]',
                        'PSSlBASEQ[PSS111]',
                        'PSSmBASEQ[PSS125]', 
                        'PSSnBASEQ[PSS139]']].sum(axis=1)
    

    print '\n', '### PSSI_RH optimistisch-rhapsodisch ###'
    print df['PSSI_RH'].describe()                         
                       
    #AS = selbstbehauptend-antisozial
    df['PSSI_AS'] = df[['PSSbBASEQ[PSS14]',
                        'PSScBASEQ[PSS28]',
                        'PSSeBASEQ[PSS42]',
                        'PSSfBASEQ[PSS56]', 
                        'PSSgBASEQ[PSS70]',
                        'PSSiBASEQ[PSS84]',
                        'PSSjBASEQ[PSS98]',
                        'PSSlBASEQ[PSS112]',
                        'PSSmBASEQ[PSS126]', 
                        'PSSnBASEQ[PSS140]']].sum(axis=1)
    
    print '\n','### PSSI_AS selbstbehauptend-antisozial ###'
    print df['PSSI_AS'].describe()                         
       
    #create histograms of subscales
    plt.figure(figsize =(16,12))
    
    plt.subplot(441)
    sns.distplot(df["PSSI_PN"].dropna(), kde = True)
    plt.xlabel('PSSI_PN', fontsize = 12)
    
    plt.subplot(442)
    sns.distplot(df['PSSI_SZ'].dropna(), kde = True)
    plt.xlabel('PSSI_SZ', fontsize = 12)
    
    plt.subplot(443)
    sns.distplot(df['PSSI_ST'].dropna(), kde = True)
    plt.xlabel('PSSI_ST', fontsize = 12)
    
    plt.subplot(444)
    sns.distplot(df['PSSI_BL'].dropna(), kde = True)
    plt.xlabel('PSSI_BL', fontsize = 12)
    
    plt.subplot(445)
    sns.distplot(df['PSSI_HI'].dropna(), kde = True)
    plt.xlabel('PSSI_HI', fontsize = 12)
    
    plt.subplot(446)
    sns.distplot(df['PSSI_NA'].dropna(), kde = True)
    plt.xlabel('PSSI_NA', fontsize = 12)
    
    plt.subplot(447)
    sns.distplot(df['PSSI_SU'].dropna(), kde = True)
    plt.xlabel('PSSI_SU', fontsize = 12)
    
    plt.subplot(448)
    sns.distplot(df['PSSI_AB'].dropna(), kde = True)
    plt.xlabel('PSSI_AB', fontsize = 12)
    
    plt.subplot(449)
    sns.distplot(df['PSSI_ZW'].dropna(), kde = True)
    plt.xlabel('PSSI_ZW', fontsize = 12)
    
    plt.subplot(4,4,10)
    sns.distplot(df['PSSI_NT'].dropna(), kde = True)
    plt.xlabel('PSSI_NT', fontsize = 12)
    
    plt.subplot(4,4,11)
    sns.distplot(df['PSSI_DP'].dropna(), kde = True)
    plt.xlabel('PSSI_DP', fontsize = 12)
    
    plt.subplot(4,4,12)
    sns.distplot(df['PSSI_SL'].dropna(), kde = True)
    plt.xlabel('PSSI_SL', fontsize = 12)
    
    plt.subplot(4,4,13)
    sns.distplot(df['PSSI_RH'].dropna(), kde = True)
    plt.xlabel('PSSI_RH', fontsize = 12)
    
    plt.subplot(4,4,14)
    sns.distplot(df['PSSI_AS'].dropna(), kde = True)
    plt.xlabel('PSSI_AS', fontsize = 12)



##############################################################################
################################## MMI #######################################
##############################################################################

def run_MMI(df, out_dir=None):
#items to be recoded                                
    items_recoded= ['MMIadBASEQ[MMI41]' ,'MMIadBASEQ[MMI42]' ,'MMIadBASEQ[MMI43]' ,'MMIadBASEQ[MMI44]' ,'MMIadBASEQ[MMI45]' ,'MMIadBASEQ[MMI46]' ,
                   'MMIadBASEQ[MMI47]' ,'MMIadBASEQ[MMI48]' ,'MMIadBASEQ[MMI49]' ,'MMIadBASEQ[MMI410]' ,'MMIadBASEQ[MMI411]' ,'MMIadBASEQ[MMI412]' ,
                   'MMIahBASEQ[MMI81]' ,'MMIahBASEQ[MMI82]' ,'MMIahBASEQ[MMI83]' ,'MMIahBASEQ[MMI84]' ,'MMIahBASEQ[MMI85]' ,'MMIahBASEQ[MMI86]' ,
                   'MMIahBASEQ[MMI87]' ,'MMIahBASEQ[MMI88]' ,'MMIahBASEQ[MMI89]' ,'MMIahBASEQ[MMI810]' ,'MMIahBASEQ[MMI811]' ,'MMIahBASEQ[MMI812]' ,
                   'MMIalBASEQ[MMI121]' ,'MMIalBASEQ[MMI122]' ,'MMIalBASEQ[MMI123]' ,'MMIalBASEQ[MMI124]' ,'MMIalBASEQ[MMI125]' , 'MMIalBASEQ[MMI126]' ,
                   'MMIalBASEQ[MMI127]' ,'MMIalBASEQ[MMI128]' ,'MMIalBASEQ[MMI129]' ,'MMIalBASEQ[MMI1210]' ,'MMIalBASEQ[MMI1211]' ,'MMIalBASEQ[MMI1212]' ,
                   'MMIapBASEQ[MMI161]' ,'MMIapBASEQ[MMI162]' ,'MMIapBASEQ[MMI163]' ,'MMIapBASEQ[MMI164]' ,'MMIapBASEQ[MMI165]' ,'MMIapBASEQ[MMI166]' ,
                   'MMIapBASEQ[MMI167]' ,'MMIapBASEQ[MMI168]' ,'MMIapBASEQ[MMI169]' ,'MMIapBASEQ[MMI1610]' ,'MMIapBASEQ[MMI1611]' ,'MMIapBASEQ[MMI1612]' ,
                   'MMIatBASEQ[MMI201]' ,'MMIatBASEQ[MMI202]' ,'MMIatBASEQ[MMI203]' ,'MMIatBASEQ[MMI204]' ,'MMIatBASEQ[MMI205]' ,'MMIatBASEQ[MMI206]' ,
                   'MMIatBASEQ[MMI207]' ,'MMIatBASEQ[MMI208]' ,'MMIatBASEQ[MMI209]' ,'MMIatBASEQ[MMI2010]' ,'MMIatBASEQ[MMI2011]' ,'MMIatBASEQ[MMI2012]' ,
                   'MMIaxBASEQ[MMI241]' ,'MMIaxBASEQ[MMI242]' ,'MMIaxBASEQ[MMI243]' ,'MMIaxBASEQ[MMI244]' ,'MMIaxBASEQ[MMI245]' ,'MMIaxBASEQ[MMI246]' ,
                   'MMIaxBASEQ[MMI247]' ,'MMIaxBASEQ[MMI248]' ,'MMIaxBASEQ[MMI249]' ,'MMIaxBASEQ[MMI2410]' ,'MMIaxBASEQ[MMI2411]' ,'MMIaxBASEQ[MMI2412]' ,
                   'MMIbbBASEQ[MMI281]' ,'MMIbbBASEQ[MMI282]' ,'MMIbbBASEQ[MMI283]' ,'MMIbbBASEQ[MMI284]' ,'MMIbbBASEQ[MMI285]' ,'MMIbbBASEQ[MMI286]' ,
                   'MMIbbBASEQ[MMI287]' ,'MMIbbBASEQ[MMI288]' ,'MMIbbBASEQ[MMI289]' ,'MMIbbBASEQ[MMI2810]' ,'MMIbbBASEQ[MMI2811]' ,'MMIbbBASEQ[MMI2812]' ,
                   'MMIbfBASEQ[MMI321]' ,'MMIbfBASEQ[MMI322]' ,'MMIbfBASEQ[MMI323]' ,'MMIbfBASEQ[MMI324]' ,'MMIbfBASEQ[MMI325]' ,'MMIbfBASEQ[MMI326]' ,
                   'MMIbfBASEQ[MMI327]' ,'MMIbfBASEQ[MMI328]' ,'MMIbfBASEQ[MMI329]' ,'MMIbfBASEQ[MMI3210]' ,'MMIbfBASEQ[MMI3211]' ,'MMIbfBASEQ[MMI3212]' ,
                   'MMIbkBASEQ[MMI371]','MMIbkBASEQ[MMI372]' ,'MMIbkBASEQ[MMI373]' ,'MMIbkBASEQ[MMI374]' ,'MMIbkBASEQ[MMI375]' ,'MMIbkBASEQ[MMI376]' ,
                   'MMIbkBASEQ[MMI377]' ,'MMIbkBASEQ[MMI378]' ,'MMIbkBASEQ[MMI379]' ,'MMIbkBASEQ[MMI3710]' ,'MMIbkBASEQ[MMI3711]' ,'MMIbkBASEQ[MMI3712]' ,
                   'MMIboBASEQ[MMI411]' ,'MMIboBASEQ[MMI412]' ,'MMIboBASEQ[MMI413]' ,'MMIboBASEQ[MMI414]' ,'MMIboBASEQ[MMI415]' ,'MMIboBASEQ[MMI416]' ,
                   'MMIboBASEQ[MMI417]' ,'MMIboBASEQ[MMI418]' ,'MMIboBASEQ[MMI419]' ,'MMIboBASEQ[MMI4110]' ,'MMIboBASEQ[MMI4111]' ,'MMIboBASEQ[MMI4112]' ,
                   'MMIbsBASEQ[MMI451]' ,'MMIbsBASEQ[MMI452]' ,'MMIbsBASEQ[MMI453]' ,'MMIbsBASEQ[MMI454]' ,'MMIbsBASEQ[MMI455]' ,'MMIbsBASEQ[MMI456]' ,
                   'MMIbsBASEQ[MMI457]' ,'MMIbsBASEQ[MMI458]' ,'MMIbsBASEQ[MMI459]' ,'MMIbsBASEQ[MMI4510]' ,'MMIbsBASEQ[MMI4511]' ,'MMIbsBASEQ[MMI4512]' ,
                   'MMIbwBASEQ[MMI491]' ,'MMIbwBASEQ[MMI492]' ,'MMIbwBASEQ[MMI493]' ,'MMIbwBASEQ[MMI494]' ,'MMIbwBASEQ[MMI495]' ,'MMIbwBASEQ[MMI496]' ,
                   'MMIbwBASEQ[MMI497]' ,'MMIbwBASEQ[MMI498]'] 
    
    #recode items                 
    recoder = {5 : 'NaN', 4 : 1, 3: 0.66, 2: 0.33, 1: 0}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   
    
    #Calculate total score as the sum for media types
    df['MMI1'] = df[['MMIadBASEQ[MMI41]',
                     'MMIadBASEQ[MMI42]',
                     'MMIadBASEQ[MMI43]',
                     'MMIadBASEQ[MMI44]',
                     'MMIadBASEQ[MMI45]',
                     'MMIadBASEQ[MMI46]',
                     'MMIadBASEQ[MMI47]',
                     'MMIadBASEQ[MMI48]',
                     'MMIadBASEQ[MMI49]',
                     'MMIadBASEQ[MMI410]',
                     'MMIadBASEQ[MMI411]',
                     'MMIadBASEQ[MMI412]']].sum(axis=1)

    
    df['MMI2'] = df[['MMIahBASEQ[MMI81]' ,
                     'MMIahBASEQ[MMI82]' ,
                     'MMIahBASEQ[MMI83]' ,
                     'MMIahBASEQ[MMI84]' ,
                     'MMIahBASEQ[MMI85]' ,
                     'MMIahBASEQ[MMI86]' ,
                     'MMIahBASEQ[MMI87]' ,
                     'MMIahBASEQ[MMI88]' ,
                     'MMIahBASEQ[MMI89]' ,
                     'MMIahBASEQ[MMI810]' ,
                     'MMIahBASEQ[MMI811]' ,
                     'MMIahBASEQ[MMI812]']].sum(axis=1)
    
    df['MMI3'] = df[['MMIalBASEQ[MMI121]',
                     'MMIalBASEQ[MMI122]',
                     'MMIalBASEQ[MMI123]',
                     'MMIalBASEQ[MMI124]',
                     'MMIalBASEQ[MMI125]',
                     'MMIalBASEQ[MMI126]',
                     'MMIalBASEQ[MMI127]',
                     'MMIalBASEQ[MMI128]',
                     'MMIalBASEQ[MMI129]',
                     'MMIalBASEQ[MMI1210]',
                     'MMIalBASEQ[MMI1211]',
                     'MMIalBASEQ[MMI1212]']].sum(axis=1)
    
    df['MMI4'] = df[['MMIapBASEQ[MMI161]',
                     'MMIapBASEQ[MMI162]',
                     'MMIapBASEQ[MMI163]',
                     'MMIapBASEQ[MMI164]',
                     'MMIapBASEQ[MMI165]',
                     'MMIapBASEQ[MMI166]',
                     'MMIapBASEQ[MMI167]',
                     'MMIapBASEQ[MMI168]',
                     'MMIapBASEQ[MMI169]',
                     'MMIapBASEQ[MMI1610]',
                     'MMIapBASEQ[MMI1611]',
                     'MMIapBASEQ[MMI1612]']].sum(axis=1)
    
    df['MMI5'] = df[['MMIatBASEQ[MMI201]',
                     'MMIatBASEQ[MMI202]',
                     'MMIatBASEQ[MMI203]',
                     'MMIatBASEQ[MMI204]',
                     'MMIatBASEQ[MMI205]',
                     'MMIatBASEQ[MMI206]',
                     'MMIatBASEQ[MMI207]',
                     'MMIatBASEQ[MMI208]',
                     'MMIatBASEQ[MMI209]',
                     'MMIatBASEQ[MMI2010]',
                     'MMIatBASEQ[MMI2011]',
                     'MMIatBASEQ[MMI2012]']].sum(axis=1)
    
    df['MMI6'] = df[['MMIaxBASEQ[MMI241]',
                     'MMIaxBASEQ[MMI242]',
                     'MMIaxBASEQ[MMI243]',
                     'MMIaxBASEQ[MMI244]',
                     'MMIaxBASEQ[MMI245]',
                     'MMIaxBASEQ[MMI246]',
                     'MMIaxBASEQ[MMI247]',
                     'MMIaxBASEQ[MMI248]',
                     'MMIaxBASEQ[MMI249]',
                     'MMIaxBASEQ[MMI2410]',
                     'MMIaxBASEQ[MMI2411]',
                     'MMIaxBASEQ[MMI2412]']].sum(axis=1)
    
    df['MMI7'] = df[['MMIbbBASEQ[MMI281]',
                     'MMIbbBASEQ[MMI282]',
                     'MMIbbBASEQ[MMI283]',
                     'MMIbbBASEQ[MMI284]',
                     'MMIbbBASEQ[MMI285]',
                     'MMIbbBASEQ[MMI286]',
                     'MMIbbBASEQ[MMI287]',
                     'MMIbbBASEQ[MMI288]',
                     'MMIbbBASEQ[MMI289]',
                     'MMIbbBASEQ[MMI2810]',
                     'MMIbbBASEQ[MMI2811]',
                     'MMIbbBASEQ[MMI2812]']].sum(axis=1)
    
    df['MMI8'] = df[['MMIbfBASEQ[MMI321]',
                     'MMIbfBASEQ[MMI322]',
                     'MMIbfBASEQ[MMI323]',
                     'MMIbfBASEQ[MMI324]',
                     'MMIbfBASEQ[MMI325]',
                     'MMIbfBASEQ[MMI326]',
                     'MMIbfBASEQ[MMI327]',
                     'MMIbfBASEQ[MMI328]',
                     'MMIbfBASEQ[MMI329]',
                     'MMIbfBASEQ[MMI3210]',
                     'MMIbfBASEQ[MMI3211]',
                     'MMIbfBASEQ[MMI3212]']].sum(axis=1)
    
    df['MMI9'] = df[['MMIbkBASEQ[MMI371]',
                     'MMIbkBASEQ[MMI372]',
                     'MMIbkBASEQ[MMI373]',
                     'MMIbkBASEQ[MMI374]',
                     'MMIbkBASEQ[MMI375]',
                     'MMIbkBASEQ[MMI376]',
                     'MMIbkBASEQ[MMI377]',
                     'MMIbkBASEQ[MMI378]',
                     'MMIbkBASEQ[MMI379]',
                     'MMIbkBASEQ[MMI3710]',
                     'MMIbkBASEQ[MMI3711]',
                     'MMIbkBASEQ[MMI3712]']].sum(axis=1)
    
    df['MMI10'] = df[['MMIboBASEQ[MMI411]',
                     'MMIboBASEQ[MMI412]',
                     'MMIboBASEQ[MMI413]',
                     'MMIboBASEQ[MMI414]',
                     'MMIboBASEQ[MMI415]',
                     'MMIboBASEQ[MMI416]',
                     'MMIboBASEQ[MMI417]',
                     'MMIboBASEQ[MMI418]',
                     'MMIboBASEQ[MMI419]',
                     'MMIboBASEQ[MMI4110]',
                     'MMIboBASEQ[MMI4111]',
                     'MMIboBASEQ[MMI4112]']].sum(axis=1)
    
    df['MMI11'] = df[['MMIbsBASEQ[MMI451]',
                     'MMIbsBASEQ[MMI452]',
                     'MMIbsBASEQ[MMI453]',
                     'MMIbsBASEQ[MMI454]',
                     'MMIbsBASEQ[MMI455]',
                     'MMIbsBASEQ[MMI456]',
                     'MMIbsBASEQ[MMI457]',
                     'MMIbsBASEQ[MMI458]',
                     'MMIbsBASEQ[MMI459]',
                     'MMIbsBASEQ[MMI4510]',
                     'MMIbsBASEQ[MMI4511]',
                     'MMIbsBASEQ[MMI4512]']].sum(axis=1)
    
    df['MMI12'] = df[['MMIbwBASEQ[MMI491]',
                     'MMIbwBASEQ[MMI492]',
                     'MMIbwBASEQ[MMI493]',
                     'MMIbwBASEQ[MMI494]',
                     'MMIbwBASEQ[MMI495]',
                     'MMIbwBASEQ[MMI496]',
                     'MMIbwBASEQ[MMI497]',
                     'MMIbwBASEQ[MMI498]',
                     'MMIbwBASEQ[MMI499]',
                     'MMIbwBASEQ[MMI4910]',
                     'MMIbwBASEQ[MMI4911]',
                     'MMIbwBASEQ[MMI4912]']].sum(axis=1)
    
    df['TotalHours'] = df[['MMIaa','MMIae', 'MMIai', 'MMIam', 'MMIaq', 'MMIau', 'MMIay', 'MMIbc',
                           'MMIbg', 'MMIbl', 'MMIbp', 'MMIbt']].sum(axis=1)
    
    #mediatypes weighted by hours of primary medium divided by hours spent with all media
    
    df['MMI1xhours‎dividedbytotalhours'] = df['MMI1']*df['MMIaa']/df['TotalHours']
    df['MMI2xhours‎dividedbytotalhours'] = df['MMI2']*df['MMIae']/df['TotalHours']
    df['MMI3xhours‎dividedbytotalhours'] = df['MMI3']*df['MMIai']/df['TotalHours']
    df['MMI4xhours‎dividedbytotalhours'] = df['MMI4']*df['MMIam']/df['TotalHours']
    df['MMI5xhours‎dividedbytotalhours'] = df['MMI5']*df['MMIaq']/df['TotalHours']
    df['MMI6xhours‎dividedbytotalhours'] = df['MMI6']*df['MMIau']/df['TotalHours']
    df['MMI7xhours‎dividedbytotalhours'] = df['MMI7']*df['MMIay']/df['TotalHours']
    df['MMI8xhours‎dividedbytotalhours'] = df['MMI8']*df['MMIbc']/df['TotalHours']
    df['MMI9xhours‎dividedbytotalhours'] = df['MMI9']*df['MMIbg']/df['TotalHours']
    df['MMI10xhours‎dividedbytotalhours'] = df['MMI10']*df['MMIbl']/df['TotalHours']
    df['MMI11xhours‎dividedbytotalhours'] = df['MMI11']*df['MMIbp']/df['TotalHours']
    df['MMI12xhours‎dividedbytotalhours'] = df['MMI12']*df['MMIbt']/df['TotalHours']
    
    #Index by summing the weighted scales
    
    df['MMI'] = df[['MMI1xhours‎dividedbytotalhours',
                    'MMI2xhours‎dividedbytotalhours',
                    'MMI3xhours‎dividedbytotalhours',
                    'MMI4xhours‎dividedbytotalhours',
                    'MMI5xhours‎dividedbytotalhours',
                    'MMI6xhours‎dividedbytotalhours',
                    'MMI7xhours‎dividedbytotalhours', 
                    'MMI8xhours‎dividedbytotalhours',
                    'MMI9xhours‎dividedbytotalhours',
                    'MMI10xhours‎dividedbytotalhours',
                    'MMI11xhours‎dividedbytotalhours',
                    'MMI12xhours‎dividedbytotalhours']].sum(axis=1)
    
    print "Questionnaire measures the amount of media used at the same time"
    print df["MMI"].describe()
       
    sns.distplot(df["MMI"].dropna(), kde = True)



##############################################################################
############################## BIS/BAS #######################################
##############################################################################

def run_BISBAS(df, out_dir=None):
    #items to be recoded                                
    items_recoded = ['BISBAS02[SQ001]',
                     'BISBAS22[SQ001]']    
                             
    #recode items                 
    recoder = {1: 4, 2: 3, 3: 2, 4: 1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   

    #Calculate total score as the sum of Item 1-22.
    df['BIS'] = df[['BISBAS02[SQ001]', 'BISBAS08[SQ001]', 'BISBAS13[SQ001]', 'BISBAS16[SQ001]', 
                       'BISBAS19[SQ001]', 'BISBAS22[SQ001]', 'BISBAS24[SQ001]']].sum(axis=1)
    
    
    df['BAS'] = df[['BISBAS03[SQ001]', 'BISBAS09[SQ001]', 'BISBAS12[SQ001]', 'BISBAS21[SQ001]',
                       'BISBAS05[SQ001]', 'BISBAS10[SQ001]', 'BISBAS15[SQ001]', 'BISBAS20[SQ001]',
                       'BISBAS04[SQ001]', 'BISBAS07[SQ001]', 'BISBAS14[SQ001]', 'BISBAS18[SQ001]', 
                       'BISBAS23[SQ001]']].sum(axis=1)
                       
    print '\n', '### BIS ###'  
    print df['BIS'].describe()     

    print '\n', '### BAS ###'  
    print df['BAS'].describe()                 

 
    plt.figure(figsize =(16,6))
    
    plt.subplot(121)
    sns.distplot(df["BIS"].dropna(), kde = True)
    plt.xlabel('BIS', fontsize = 14)
    
    plt.subplot(122)
    sns.distplot(df["BAS"].dropna(), kde = True)
    plt.xlabel('BAS', fontsize = 14)
 

  
##############################################################################
################################# STAI #######################################
##############################################################################

def run_STAI(df, out_dir=None):

    cols_STAI = ['STAI01[STAI01]','STAI01[STAI02]','STAI01[STAI03]','STAI01[STAI04]','STAI01[STAI05]','STAI01[STAI06]','STAI01[STAI07]','STAI01[STAI08]',
                 'STAI01[STAI09]','STAI01[STAI10]','STAI11[STAI11]','STAI11[STAI12]','STAI11[STAI13]','STAI11[STAI14]','STAI11[STAI15]','STAI11[STAI16]',
                 'STAI11[STAI17]','STAI11[STAI18]','STAI11[STAI19]','STAI11[STAI20]']
    
    items_recoded = ['STAI01[STAI01]', 'STAI01[STAI06]', 'STAI01[STAI07]', 'STAI01[STAI10]', 
                     'STAI11[STAI13]', 'STAI11[STAI16]', 'STAI11[STAI19]']
                    
    recoder = {1: 4, 2: 3, 3: 2, 4: 1 }
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   
    
    df['STAI_A-Trait_summary_sum'] = df[cols_STAI].sum(axis=1)
    
    print df['STAI_A-Trait_summary_sum'].describe()  
    plt.figure
    sns.distplot(df['STAI_A-Trait_summary_sum'].dropna(), kde = True)
    plt.show()
    clf()
    


##############################################################################    
############################### STAXI ########################################
##############################################################################

def run_STAXI(df, out_dir=None):

              
    cols_trait2 = ['STAXI11[STAXI11]','STAXI11[STAXI12]','STAXI11[STAXI13]','STAXI11[STAXI14]','STAXI11[STAXI15]',
                  'STAXI11[STAXI16]','STAXI11[STAXI17]','STAXI11[STAXI18]','STAXI11[STAXI19]','STAXI11[STAXI20]']
    cols_trait3_inward = ['STAXI21[STAXI22]', 'STAXI21[STAXI24]','STAXI21[STAXI25]', 'STAXI21[STAXI28]',
                          'STAXI21[STAXI30]', 'STAXI34[STAXI41]','STAXI34[STAXI42]', 'STAXI34[STAXI44]']
    cols_trait3_outward = ['STAXI21[STAXI26]','STAXI21[STAXI27]', 'STAXI21[STAXI31]', 'STAXI34[STAXI35]', 
                           'STAXI34[STAXI37]','STAXI34[STAXI38]','STAXI34[STAXI39]', 'STAXI34[STAXI43]']
    cols_trait3_control = ['STAXI21[STAXI21]', 'STAXI21[STAXI23]', 'STAXI21[STAXI29]', 'STAXI21[STAXI32]',
                           'STAXI21[STAXI33]','STAXI34[STAXI34]', 'STAXI34[STAXI36]', 'STAXI34[STAXI40]']
    
    df["anger_trait"] = df[cols_trait2].sum(axis=1)
    df["anger_inward"] = df[cols_trait3_inward].sum(axis=1)
    df["anger_outward"] = df[cols_trait3_outward].sum(axis=1)
    df["anger_control"] = df[cols_trait3_control].sum(axis=1)
    
    
    print '\n', '### anger_trait ###'
    print df["anger_trait"].describe()
    
    print '\n', '### anger_inward ###'
    print df["anger_inward"].describe()   
    
    print '\n', '### anger_outward ###'
    print df["anger_outward"].describe()      
    
    print '\n', '### anger_control ###'
    print df["anger_control"].describe()      
    
    plt.figure(figsize =(16,12))
    
    plt.subplot(221)
    sns.distplot(df["anger_trait"].dropna(), kde = True)
    plt.xlabel('anger - trait', fontsize = 14)
    
    plt.subplot(222)
    sns.distplot(df["anger_inward"].dropna(), kde = True)
    plt.xlabel('inward-directed anger', fontsize = 14)

    plt.subplot(223)
    sns.distplot(df["anger_outward"].dropna(), kde = True)
    plt.xlabel('outward-directed anger', fontsize = 14)
    
    plt.subplot(224)
    sns.distplot(df["anger_control"].dropna(), kde = True)
    plt.xlabel('anger control', fontsize = 14)
