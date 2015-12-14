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
#################### Abbreviated Math Anxiety Scale ##########################
##############################################################################

def run_AMAS(df, out_dir=None):
 

    #Calculate total score as the sum of Item 1-9.
    
    cols = ['AMAS[1]',
            'AMAS[2]',
            'AMAS[3]',
            'AMAS[4]',
            'AMAS[5]',
            'AMAS[6]',
            'AMAS[7]',
            'AMAS[8]',
            'AMAS[9]']    
    
    df['AMAS_sum'] = df[cols].sum(axis=1)
                      
    print "Questionnaire measures math anxiety (total score is calculated as the sum of the 9 items)\n"   
    print df["AMAS_sum"].describe() 
    sns.distplot(df["AMAS_sum"].dropna(), kde = True)
    
    if out_dir:
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['AMAS_sum']
        df[cols_export].to_csv('%s/quest_AMAS_9.csv' % out_dir, index=False)        
    


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
    recoder = {1:5, 2:4, 3:3, 4:2, 5:1 }
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
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['SelfCtrl_sum']
        df[cols_export].to_csv('%s/quest_SCS_13.csv' % out_dir, index=False)
        
    

##############################################################################                      
################ Internet Addiction test #####################################
##############################################################################
#note: Item 3 not included due to differerent scale format

def run_IAT(df, out_dir=None):
                              
    #Calculate total score as the sum of Item 1-19.
    
    cols = ['IATaBASEQ[IAT1]',
            'IATaBASEQ[IAT2]',
            'IATbBASEQ[IAT3]',
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
                             
    #recode items                 
    recoder = {1:1, 2:2, 3:3, 4:4, 5:5, 6:0}
    for i in cols:
        df[i] = df[i].map(recoder).astype(float64)              
                        
                
    df['IAT_sum'] = df[cols].sum(axis=1)
    
    print "Questionnaire measures internet addiction (total score is calculated as the sum of the 19 items; Item 3 not incl (different format)\n"   
    print df["IAT_sum"].describe()
    sns.distplot(df["IAT_sum"].dropna(), kde = True)
    
    if out_dir:
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ["IAT_sum"]
        df[cols_export].to_csv('%s/quest_IAT_20.csv' % out_dir, index=False)



##############################################################################
########################### Arten innerer Sprache ############################
#################### varieties of inner speech (VIS) #########################
##############################################################################

def run_VIS(df, out_dir=None):
    #items to be recoded                                
    items_recoded = ['AISaBASEQ[AIS7]',
                     'AISbBASEQ[AIS15]']  
    #recode items                 
    recoder = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
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
            
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['VIS_dialog_sum', 'VIS_condensed_sum', 'VIS_other_sum', 'VIS_eval_sum'] 
        df[cols_export].to_csv('%s/quest_VISQ_18.csv' % out_dir, index=False)



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
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['Mean_MW_delib_mean', 'Mean_MW_spont_mean']
        df[cols_export].to_csv('%s/quest_S-D-MW_8.csv' % out_dir, index=False)



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
    recoder = {1:5, 2:4, 3:3, 4:2, 5:1 }
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
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['Mach_sum', 'Narc_sum', 'Psycho_sum']    
        df[cols_export].to_csv('%s/quest_SD3_27.csv' % out_dir, index=False)



##############################################################################
################################ SDS #########################################
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
    recoder = {1:1, 2:0}
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
    df['SDS_sum'] = df[cols].sum(axis=1)
                    
    print df['SDS_sum'].describe()
                   
    #create histo
    sns.distplot(df['SDS_sum'].dropna(), kde = True)              
    
    if out_dir:
    
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['SDS_sum']      
        df[cols_export].to_csv('%s/quest_SDS_17.csv' % out_dir, index=False)
  


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
    recoder = {1:4, 2:3, 3:2, 4:1}
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
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['Mean_NegUrg', 'Mean_Premed', 'Mean_Persev', 'Mean_SS','Mean_PosUrg']       
        df[cols_export].to_csv('%s/quest_UPPS-P_59.csv' % out_dir, index=False)
  


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
    recoder = {1:5, 2:4, 3:3, 4:2, 5:1 }
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
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['TPS_D_sum']        
        df[cols_export].to_csv('%s/quest_TPS_16.csv' % out_dir, index=False)
  


##############################################################################
############################ ASR 18-59 #######################################
##############################################################################

def run_ASR(df, out_dir=None):
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
    df['ASR_summary_adaptiveFunctioning_friends_sum' ] = df[['ASRIABASEQ[ASRIA]',
                                                                 'ASRIBBASEQ[ASRIB]',
                                                                 'ASRICBASEQ[ASRIC]',
                                                                 'ASRIDBASEQ[ASRID]']].sum(axis=1)
    
    
    ##### spouse / partner #####
    recoded = ['ASRII3BASEQ[ASRIIBr]', 'ASRII3BASEQ[ASRIIEr]', 'ASRII3BASEQ[ASRIIFr]', 'ASRII3BASEQ[ASRIIHr]']
    for item in recoded:
        df[item] = -df[item]
    df['ASR_summary_adaptiveFunctioning_spouse_sum'] = df[['ASRII3BASEQ[ASRIIA]', 
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
    df['ASR_summary_adaptiveFunctioning_family_sum'] = pd.Series('NaN', index=df.index)
    for sub in range(len(df)):
        score = 0
        for i in items:
            try:
                if int(df[i].iloc[[sub]]) in [0,1,2,3]:
                    score += 1
            except:
                pass
        df['ASR_summary_adaptiveFunctioning_family_sum'].iloc[[sub]] = float(score)
    
    
    ##### job #####
    #satisfied_job = df['ASRIVbBASEQ[ASRIVE]'] is not scored
    recoded = ['ASRIVbBASEQ[ASRIVBr]', 'ASRIVbBASEQ[ASRIVDr]', 'ASRIVbBASEQ[ASRIVFr]',
               'ASRIVbBASEQ[ASRIVGr]', 'ASRIVbBASEQ[ASRIVHr]', 'ASRIVbBASEQ[ASRIVIr]']
    for item in recoded:
        df[item] = -df[item]
    df['ASR_summary_adaptiveFunctioning_job_sum'] = df[['ASRIVbBASEQ[ASRIVA]',
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
        df[item] = -df[item]
    df['ASR_summary_adaptiveFunctioning_education_sum'] = df[['ASRVcBASEQ[ASRVA]',
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
        print df[scale].describe()
        sns.countplot(df[scale].dropna(), order=range(int(df[scale].min()),int(df[scale].max())))
        plt.xlabel(scale, fontsize=14)
        plt.show()
        
        
        
    
    ######################## substance use #################################
    
    print '\n\n\n', '##### Substance Use #####'
    
    df['ASR_scale_substanceUse_tabaco_perday'] = df['ASRQ124']
    df['ASR_scale_substanceUse_alcohol_daysdrunk'] = df['ASRQ125']
    df['ASR_scale_substanceUse_drugs_daysused'] = df['ASRQ126']
    
    substance_scales = ['ASR_scale_substanceUse_tabaco_perday', 
                        'ASR_scale_substanceUse_alcohol_daysdrunk', 
                        'ASR_scale_substanceUse_drugs_daysused']
    
    for scale in substance_scales:
        print '\n'
        print df[scale].describe() 
        sns.countplot(df[scale].dropna(), order=range(int(df[scale].min()),int(df[scale].max())))
        plt.xlabel(scale, fontsize=14)
        plt.show()
    
    
    ######################### items #############################################
    Q1 = df['ASRQ1BASEQ[ASRQ1]']
    Q2 = df['ASRQ1BASEQ[ASRQ2]']
    Q3 = df['ASRQ1BASEQ[ASRQ3]']
    Q4 = df['ASRQ1BASEQ[ASRQ4]']
    Q5 = df['ASRQ1BASEQ[ASRQ5]']
    Q6 = df['ASRQ1BASEQ[ASRQ6]']
    Q7 = df['ASRQ7BASEQ[ASRQ7]']
    Q8 = df['ASRQ7BASEQ[ASRQ8]']
    Q9 = df['ASRQ7BASEQ[ASRQ9]']
    Q10 = df['ASRQ10BASEQ[ASRQ10]']
    Q11 = df['ASRQ10BASEQ[ASRQ11]']
    Q12 = df['ASRQ10BASEQ[ASRQ12]']
    Q13 = df['ASRQ10BASEQ[ASRQ13]']
    Q14 = df['ASRQ10BASEQ[ASRQ14]']
    Q15 = df['ASRQ10BASEQ[ASRQ15]']
    Q16 = df['ASRQ10BASEQ[ASRQ16]']
    Q17 = df['ASRQ10BASEQ[ASRQ17]']
    Q18 = df['ASRQ10BASEQ[ASRQ18]']
    Q19 = df['ASRQ10BASEQ[ASRQ19]']
    Q20 = df['ASRQ10BASEQ[ASRQ20]']
    Q21 = df['ASRQ21BASEQ[ASRQ21]']
    Q22 = df['ASRQ21BASEQ[ASRQ22]']
    Q23 = df['ASRQ21BASEQ[ASRQ23]']
    Q24 = df['ASRQ21BASEQ[ASRQ24]']
    Q25 = df['ASRQ21BASEQ[ASRQ25]']
    Q26 = df['ASRQ21BASEQ[ASRQ26]']
    Q27 = df['ASRQ21BASEQ[ASRQ27]']
    Q28 = df['ASRQ21BASEQ[ASRQ28]']
    Q29 = df['ASRQ21BASEQ[ASRQ29]']
    Q30 = df['ASRQ30BASEQ[ASRQ30]']
    Q31 = df['ASRQ30BASEQ[ASRQ31]']
    Q32 = df['ASRQ30BASEQ[ASRQ32]']
    Q33 = df['ASRQ30BASEQ[ASRQ33]']
    Q34 = df['ASRQ30BASEQ[ASRQ34]']
    Q35 = df['ASRQ30BASEQ[ASRQ35]']
    Q36 = df['ASRQ30BASEQ[ASRQ36]']
    Q37 = df['ASRQ30BASEQ[ASRQ37]']
    Q38 = df['ASRQ30BASEQ[ASRQ38]']
    Q39 = df['ASRQ30BASEQ[ASRQ39]']
    Q40 = df['ASRQ30BASEQ[ASRQ40]']
    Q41 = df['ASRQ41BASEQ[ASRQ41]']
    Q42 = df['ASRQ41BASEQ[ASRQ42]']
    Q43 = df['ASRQ41BASEQ[ASRQ43]']
    Q44 = df['ASRQ41BASEQ[ASRQ44]']
    Q45 = df['ASRQ41BASEQ[ASRQ45]']
    Q46 = df['ASRQ41BASEQ[ASRQ46]']
    Q47 = df['ASRQ41BASEQ[ASRQ47]']
    Q48 = df['ASRQ41BASEQ[ASRQ48]']
    Q49 = df['ASRQ41BASEQ[ASRQ49]']
    Q50 = df['ASRQ41BASEQ[ASRQ50]']
    Q51 = df['ASRQ51BASEQ[ASRQ51]']
    Q52 = df['ASRQ51BASEQ[ASRQ52]']
    Q53 = df['ASRQ51BASEQ[ASRQ53]']
    Q54 = df['ASRQ51BASEQ[ASRQ54]']
    Q55 = df['ASRQ51BASEQ[ASRQ55]']
    Q56a = df['ASRQ56BASEQ[ASRVIII561]']
    Q56b = df['ASRQ56BASEQ[ASRVIII562]']
    Q56c = df['ASRQ56BASEQ[ASRVIII563]']
    Q56d = df['ASRQ56BASEQ[ASRVIII564]']
    Q56e = df['ASRQ56BASEQ[ASRVIII565]']
    Q56f = df['ASRQ56BASEQ[ASRVIII566]']
    Q56g = df['ASRQ56BASEQ[ASRVIII567]']
    Q57 = df['ASRQ57BASEQ[ASRQ57]']
    Q58 = df['ASRQ57BASEQ[ASRQ58]']
    Q59 = df['ASRQ57BASEQ[ASRQ59]']
    Q60 = df['ASRQ57BASEQ[ASRQ60]']
    Q61 = df['ASRQ61BASEQ[ASRQ61]']
    Q62 = df['ASRQ61BASEQ[ASRQ62]']
    Q63 = df['ASRQ61BASEQ[ASRQ63]']
    Q64 = df['ASRQ61BASEQ[ASRQ64]']
    Q65 = df['ASRQ61BASEQ[ASRQ65]']
    Q66 = df['ASRQ61BASEQ[ASRQ66]']
    Q67 = df['ASRQ61BASEQ[ASRQ67]']
    Q68 = df['ASRQ61BASEQ[ASRQ68]']
    Q69 = df['ASRQ61BASEQ[ASRQ69]']
    Q70 = df['ASRQ61BASEQ[ASRQ70]']
    Q71 = df['ASRQ71BASEQ[ASRQ71]']
    Q72 = df['ASRQ71BASEQ[ASRQ72]']
    Q73 = df['ASRQ71BASEQ[ASRQ73]']
    Q74 = df['ASRQ71BASEQ[ASRQ74]']
    Q75 = df['ASRQ71BASEQ[ASRQ75]']
    Q76 = df['ASRQ71BASEQ[ASRQ76]']
    Q77 = df['ASRQ71BASEQ[ASRQ77]']
    Q78 = df['ASRQ71BASEQ[ASRQ78]']
    Q79 = df['ASRQ71BASEQ[ASRQ79]']
    Q80 = df['ASRQ71BASEQ[ASRQ80]']
    Q81 = df['ASRQ81BASEQ[ASRQ81]']
    Q82 = df['ASRQ81BASEQ[ASRQ82]']
    Q83 = df['ASRQ81BASEQ[ASRQ83]']
    Q84 = df['ASRQ81BASEQ[ASRQ84]']
    Q85 = df['ASRQ81BASEQ[ASRQ85]']
    Q86 = df['ASRQ81BASEQ[ASRQ86]']
    Q87 = df['ASRQ81BASEQ[ASRQ87]']
    Q88 = df['ASRQ81BASEQ[ASRQ88]']
    Q89 = df['ASRQ81BASEQ[ASRQ89]']
    Q90 = df['ASRQ81BASEQ[ASRQ90]']
    Q91 = df['ASRQ91BASEQ[ASRQ91]']
    Q92 = df['ASRQ91BASEQ[ASRQ92]']
    Q93 = df['ASRQ91BASEQ[ASRQ93]']
    Q94 = df['ASRQ91BASEQ[ASRQ94]']
    Q95 = df['ASRQ91BASEQ[ASRQ95]']
    Q96 = df['ASRQ91BASEQ[ASRQ96]']
    Q97 = df['ASRQ91BASEQ[ASRQ97]']
    Q98 = df['ASRQ91BASEQ[ASRQ98]']
    Q99 = df['ASRQ91BASEQ[ASRQ99]']
    Q100 = df['ASRQ91BASEQ[ASRQ100]']
    Q101 = df['ASRQ101BASEQ[ASRQ101]']
    Q102 = df['ASRQ101BASEQ[ASRQ102]']
    Q103 = df['ASRQ101BASEQ[ASRQ103]']
    Q104 = df['ASRQ101BASEQ[ASRQ104]']
    Q105 = df['ASRQ101BASEQ[ASRQ105]']
    Q106 = df['ASRQ101BASEQ[ASRQ106]']
    Q107 = df['ASRQ101BASEQ[ASRQ107]']
    Q108 = df['ASRQ101BASEQ[ASRQ108]']
    Q109 = df['ASRQ101BASEQ[ASRQ109]']
    Q110 = df['ASRQ101BASEQ[ASRQ110]']
    Q111 = df['ASRQ111BASEQ[ASRQ111]']
    Q112 = df['ASRQ111BASEQ[ASRQ112]']
    Q113 = df['ASRQ111BASEQ[ASRQ113]']
    Q114 = df['ASRQ111BASEQ[ASRQ114]']
    Q115 = df['ASRQ111BASEQ[ASRQ115]']
    Q116 = df['ASRQ111BASEQ[ASRQ116]']
    Q117 = df['ASRQ111BASEQ[ASRQ117]']
    Q118 = df['ASRQ111BASEQ[ASRQ118]']
    Q119 = df['ASRQ111BASEQ[ASRQ119]']
    Q120 = df['ASRQ111BASEQ[ASRQ120]']
    Q121 = df['ASRQ121BASEQ[ASRQ121]']
    Q122 = df['ASRQ121BASEQ[ASRQ122]']
    Q123 = df['ASRQ121BASEQ[ASRQ123]']
    
    
    ######################## critical items #################################
    
    print '\n\n\n', '##### Critical Items #####'
    df['ASR_summary_criticalItems_sum'] = Q6 + Q8 + Q9 + Q10 + Q14 + Q16 + Q18 + Q21 + Q40 + Q55 + Q57 + Q66 + Q70 + Q84 + Q90 + Q91 + Q92 + Q97 + Q103
    print '\n\n', 'ASR_summary_criticalItems_sum', '\n'
    print df['ASR_summary_criticalItems_sum'].describe()
    sns.countplot(df['ASR_summary_criticalItems_sum'].dropna(), order=range(int(df['ASR_summary_criticalItems_sum'].min()),int(df['ASR_summary_criticalItems_sum'].max())))
    plt.show()
    
    
    ######################## syndrome profiles #################################
    
    print '\n\n\n', '##### Syndrome Profiles #####'
    
    df['ASR_summary_syndromeProfiles_anxiousdepressed_sum'] = Q12 + Q13 + Q14 + Q22 + Q31 + Q33 + Q34 + Q35 + Q45 + Q47 + Q50 + Q52 + Q71 + Q91 + Q103 + Q107 + Q112 + Q113 
    df['ASR_summary_syndromeProfiles_withdrawn_sum'] = Q25 + Q30 + Q42 + Q48 + Q60 + Q65 + Q67 + Q69 + Q111
    df['ASR_summary_syndromeProfiles_somaticComplaints_sum'] = Q51 + Q54 + Q56a + Q56b + Q56c + Q56d + Q56e + Q56f + Q56g + Q100
    df['ASR_summary_syndromeProfiles_thoughtProblems_sum'] = Q9 + Q18 + Q36 + Q40 + Q46 + Q63 + Q66 + Q70 + Q84 + Q85 
    df['ASR_summary_syndromeProfiles_attentionProblems_sum'] = Q1 + Q8 + Q11 + Q17 + Q53 + Q59 + Q61 + Q64 + Q78 + Q101 + Q102 + Q105 + Q108 + Q119 + Q121
    df['ASR_summary_syndromeProfiles_aggressiveBehavior_sum'] = Q3 + Q5 + Q16 + Q28 + Q37 + Q55 + Q57 + Q68 + Q81 + Q86 + Q87 + Q95 + Q97 + Q116 + Q118
    df['ASR_summary_syndromeProfiles_rulebreakingBehavior_sum'] = Q6 + Q20 + Q23 + Q26 + Q39 + Q41 + Q43 + Q76 + Q82 + Q90 + Q92 + Q114 + Q117 + Q122 
    df['ASR_summary_syndromeProfiles_intrusive_sum'] = Q7 + Q19 + Q74 + Q93 + Q94 + Q104
    
    df['ASR_summary_syndromeProfiles_internalizing_sum'] = df[['ASR_summary_syndromeProfiles_anxiousdepressed_sum',
                                                                   'ASR_summary_syndromeProfiles_withdrawn_sum', 
                                                                   'ASR_summary_syndromeProfiles_somaticComplaints_sum']].sum(axis=1)
    
    df['ASR_summary_syndromeProfiles_externalizing_sum'] = df[['ASR_summary_syndromeProfiles_aggressiveBehavior_sum',
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
        print df[scale].describe()  
        sns.countplot(df[scale].dropna(), order=range(int(df[scale].min()),int(df[scale].max())))
        plt.xlabel(scale, fontsize=14)
        plt.show()


    if out_dir:
        
        d = {'ASQQ79Freitext': '79.comment',
             'ASR100Freitext': '100.comment',
             'ASR92Freitext': '92.comment',
             'ASRIABASEQ[ASRIA]': 'I.A',
             'ASRIBBASEQ[ASRIB]': 'I.B',
             'ASRICBASEQ[ASRIC]': 'I.C',
             'ASRIDBASEQ[ASRID]': 'I.D',
             'ASRII1': 'II.1',
             'ASRII1[comment]': 'II.1.comment',
             'ASRII2': 'II.2',
             'ASRII3BASEQ[ASRIIA]': 'II.A',
             'ASRII3BASEQ[ASRIIBr]': 'II.B',
             'ASRII3BASEQ[ASRIIC]': 'II.C',
             'ASRII3BASEQ[ASRIID]': 'II.D',
             'ASRII3BASEQ[ASRIIEr]': 'II.E',
             'ASRII3BASEQ[ASRIIFr]': 'II.F',
             'ASRII3BASEQ[ASRIIG]': 'II.G',
             'ASRII3BASEQ[ASRIIHr]': 'II.H',
             'ASRIIIABASEQ[ASRIIIA]': 'III.A',
             'ASRIIIBBASEQ[ASRIIIB]': 'III.B',
             'ASRIIICBASEQ[ASRIIIC]': 'III.C',
             'ASRIIIDBASEQ[ASRIIID]': 'III.D',
             'ASRIIIEaBASEQ[ASRIIIE]': 'III.E',
             'ASRIIIEbBASEQ[ASRIIIE1]': 'III.E.1',
             'ASRIIIEbBASEQ[ASRIIIE2]': 'III.E.2',
             'ASRIIIEbBASEQ[ASRIIIE3]': 'III.E.3',
             'ASRIIIEbBASEQ[ASRIIIE4]': 'III.E.4',
             'ASRIIIFBASEQ[ASRIIIF]': 'III.F',
             'ASRIVaBASEQ[ASRIV]': 'IV.1comment',
             'ASRIVbBASEQ[ASRIVA]': 'IV.A',
             'ASRIVbBASEQ[ASRIVBr]': 'IV.B',
             'ASRIVbBASEQ[ASRIVC]': 'IV.C',
             'ASRIVbBASEQ[ASRIVDr]': 'IV.D',
             'ASRIVbBASEQ[ASRIVE]': 'IV.E',
             'ASRIVbBASEQ[ASRIVFr]': 'IV.F',
             'ASRIVbBASEQ[ASRIVGr]': 'IV.G',
             'ASRIVbBASEQ[ASRIVHr]': 'IV.H',
             'ASRIVbBASEQ[ASRIVIr]': 'IV.I',
             'ASRQ101BASEQ[ASRQ101]': '101',
             'ASRQ101BASEQ[ASRQ102]': '102',
             'ASRQ101BASEQ[ASRQ103]': '103',
             'ASRQ101BASEQ[ASRQ104]': '104',
             'ASRQ101BASEQ[ASRQ105]': '105',
             'ASRQ101BASEQ[ASRQ106]': '106',
             'ASRQ101BASEQ[ASRQ107]': '107',
             'ASRQ101BASEQ[ASRQ108]': '108',
             'ASRQ101BASEQ[ASRQ109]': '109',
             'ASRQ101BASEQ[ASRQ110]': '110',
             'ASRQ10BASEQ[ASRQ10]': '10',
             'ASRQ10BASEQ[ASRQ11]': '11',
             'ASRQ10BASEQ[ASRQ12]': '12',
             'ASRQ10BASEQ[ASRQ13]': '13',
             'ASRQ10BASEQ[ASRQ14]': '14',
             'ASRQ10BASEQ[ASRQ15]': '15',
             'ASRQ10BASEQ[ASRQ16]': '16',
             'ASRQ10BASEQ[ASRQ17]': '17',
             'ASRQ10BASEQ[ASRQ18]': '18',
             'ASRQ10BASEQ[ASRQ19]': '19',
             'ASRQ10BASEQ[ASRQ20]': '20',
             'ASRQ111BASEQ[ASRQ111]': '111',
             'ASRQ111BASEQ[ASRQ112]': '112',
             'ASRQ111BASEQ[ASRQ113]': '113',
             'ASRQ111BASEQ[ASRQ114]': '114',
             'ASRQ111BASEQ[ASRQ115]': '115',
             'ASRQ111BASEQ[ASRQ116]': '116',
             'ASRQ111BASEQ[ASRQ117]': '117',
             'ASRQ111BASEQ[ASRQ118]': '118',
             'ASRQ111BASEQ[ASRQ119]': '119',
             'ASRQ111BASEQ[ASRQ120]': '120',
             'ASRQ121BASEQ[ASRQ121]': '121',
             'ASRQ121BASEQ[ASRQ122]': '122',
             'ASRQ121BASEQ[ASRQ123]': '123',
             'ASRQ124': '124',
             'ASRQ125': '125',
             'ASRQ126': '126',
             'ASRQ1BASEQ[ASRQ1]': '1',
             'ASRQ1BASEQ[ASRQ2]': '2',
             'ASRQ1BASEQ[ASRQ3]': '3',
             'ASRQ1BASEQ[ASRQ4]': '4',
             'ASRQ1BASEQ[ASRQ5]': '5',
             'ASRQ1BASEQ[ASRQ6]': '6',
             'ASRQ21BASEQ[ASRQ21]': '21',
             'ASRQ21BASEQ[ASRQ22]': '22',
             'ASRQ21BASEQ[ASRQ23]': '23',
             'ASRQ21BASEQ[ASRQ24]': '24',
             'ASRQ21BASEQ[ASRQ25]': '25',
             'ASRQ21BASEQ[ASRQ26]': '26',
             'ASRQ21BASEQ[ASRQ27]': '27',
             'ASRQ21BASEQ[ASRQ28]': '28',
             'ASRQ21BASEQ[ASRQ29]': '29',
             'ASRQ29Freitext': '29.comment',
             'ASRQ30BASEQ[ASRQ30]': '30',
             'ASRQ30BASEQ[ASRQ31]': '31',
             'ASRQ30BASEQ[ASRQ32]': '32',
             'ASRQ30BASEQ[ASRQ33]': '33',
             'ASRQ30BASEQ[ASRQ34]': '34',
             'ASRQ30BASEQ[ASRQ35]': '35',
             'ASRQ30BASEQ[ASRQ36]': '36',
             'ASRQ30BASEQ[ASRQ37]': '37',
             'ASRQ30BASEQ[ASRQ38]': '38',
             'ASRQ30BASEQ[ASRQ39]': '39',
             'ASRQ30BASEQ[ASRQ40]': '40',
             'ASRQ40Freitext': '40.comment',
             'ASRQ41BASEQ[ASRQ41]': '41',
             'ASRQ41BASEQ[ASRQ42]': '42',
             'ASRQ41BASEQ[ASRQ43]': '43',
             'ASRQ41BASEQ[ASRQ44]': '44',
             'ASRQ41BASEQ[ASRQ45]': '45',
             'ASRQ41BASEQ[ASRQ46]': '46',
             'ASRQ41BASEQ[ASRQ47]': '47',
             'ASRQ41BASEQ[ASRQ48]': '48',
             'ASRQ41BASEQ[ASRQ49]': '49',
             'ASRQ41BASEQ[ASRQ50]': '50',
             'ASRQ46Freitext': '46.comment',
             'ASRQ51BASEQ[ASRQ51]': '51',
             'ASRQ51BASEQ[ASRQ52]': '52',
             'ASRQ51BASEQ[ASRQ53]': '53',
             'ASRQ51BASEQ[ASRQ54]': '54',
             'ASRQ51BASEQ[ASRQ55]': '55',
             'ASRQ56BASEQ[ASRVIII561]': '56.a',
             'ASRQ56BASEQ[ASRVIII562]': '56.b',
             'ASRQ56BASEQ[ASRVIII563]': '56.c',
             'ASRQ56BASEQ[ASRVIII564]': '56.d',
             'ASRQ56BASEQ[ASRVIII565]': '56.e',
             'ASRQ56BASEQ[ASRVIII566]': '56.f',
             'ASRQ56BASEQ[ASRVIII567]': '56.g',
             'ASRQ56Freitext': '56.d.comment',
             'ASRQ57BASEQ[ASRQ57]': '57',
             'ASRQ57BASEQ[ASRQ58]': '58',
             'ASRQ57BASEQ[ASRQ59]': '59',
             'ASRQ57BASEQ[ASRQ60]': '60',
             'ASRQ58Freitext': '58.comment',
             'ASRQ61BASEQ[ASRQ61]': '61',
             'ASRQ61BASEQ[ASRQ62]': '62',
             'ASRQ61BASEQ[ASRQ63]': '63',
             'ASRQ61BASEQ[ASRQ64]': '64',
             'ASRQ61BASEQ[ASRQ65]': '65',
             'ASRQ61BASEQ[ASRQ66]': '66',
             'ASRQ61BASEQ[ASRQ67]': '67',
             'ASRQ61BASEQ[ASRQ68]': '68',
             'ASRQ61BASEQ[ASRQ69]': '69',
             'ASRQ61BASEQ[ASRQ70]': '70',
             'ASRQ66': '66.comment',
             'ASRQ6Freitext': '6.comment',
             'ASRQ70': '70.comment',
             'ASRQ71BASEQ[ASRQ71]': '71',
             'ASRQ71BASEQ[ASRQ72]': '72',
             'ASRQ71BASEQ[ASRQ73]': '73',
             'ASRQ71BASEQ[ASRQ74]': '74',
             'ASRQ71BASEQ[ASRQ75]': '75',
             'ASRQ71BASEQ[ASRQ76]': '76',
             'ASRQ71BASEQ[ASRQ77]': '77',
             'ASRQ71BASEQ[ASRQ78]': '78',
             'ASRQ71BASEQ[ASRQ79]': '79',
             'ASRQ71BASEQ[ASRQ80]': '80',
             'ASRQ77Freitext': '77.comment',
             'ASRQ7BASEQ[ASRQ7]': '7',
             'ASRQ7BASEQ[ASRQ8]': '8',
             'ASRQ7BASEQ[ASRQ9]': '9',
             'ASRQ81BASEQ[ASRQ81]': '81',
             'ASRQ81BASEQ[ASRQ82]': '82',
             'ASRQ81BASEQ[ASRQ83]': '83',
             'ASRQ81BASEQ[ASRQ84]': '84',
             'ASRQ81BASEQ[ASRQ85]': '85',
             'ASRQ81BASEQ[ASRQ86]': '86',
             'ASRQ81BASEQ[ASRQ87]': '87',
             'ASRQ81BASEQ[ASRQ88]': '88',
             'ASRQ81BASEQ[ASRQ89]': '89',
             'ASRQ81BASEQ[ASRQ90]': '90',
             'ASRQ84Freitext': '84.comment',
             'ASRQ85Freitext': '85.comment',
             'ASRQ91BASEQ[ASRQ100]': '100',
             'ASRQ91BASEQ[ASRQ91]': '91',
             'ASRQ91BASEQ[ASRQ92]': '92',
             'ASRQ91BASEQ[ASRQ93]': '93',
             'ASRQ91BASEQ[ASRQ94]': '94',
             'ASRQ91BASEQ[ASRQ95]': '95',
             'ASRQ91BASEQ[ASRQ96]': '96',
             'ASRQ91BASEQ[ASRQ97]': '97',
             'ASRQ91BASEQ[ASRQ98]': '98',
             'ASRQ91BASEQ[ASRQ99]': '99',
             'ASRQ9Freitext': '9.comment',
             'ASRVI': 'VI.',
             'ASRVII': 'VII.',
             'ASRVIII': 'VIII.',
             'ASRVII[comment]': 'VII.comment',
             'ASRVI[comment]': 'VI.comment',
             'ASRVa': 'V.1',
             'ASRVa[comment]': 'V.1.comment',
             'ASRVbBASEQ[ASRV1]': 'V.2',
             'ASRVbBASEQ[ASRV1comment]': 'V.2.comment',
             'ASRVbBASEQ[ASRV3]': 'V.3',
             'ASRVbBASEQ[ASRV3comment]': 'V.3.comment',
             'ASRVbBASEQ[ASRV4]': 'V.4',
             'ASRVbBASEQ[ASRV4comment]': 'V.4.comment',
             'ASRVcBASEQ[ASRVA]': 'V.A',
             'ASRVcBASEQ[ASRVB]': 'V.B',
             'ASRVcBASEQ[ASRVCr]': 'V.C',
             'ASRVcBASEQ[ASRVD]': 'V.D',
             'ASRVcBASEQ[ASRVEr]': 'V.E'}
        
        item_order = ['I.A','I.B','I.C','I.D','II.1','II.1.comment','II.2','II.A',
                      'II.B','II.C','II.D','II.E','II.F','II.G','II.H','III.A','III.B',
                      'III.C','III.D','III.E','III.E.1','III.E.2','III.E.3','III.E.4',
                      'III.F','IV.1comment','IV.A','IV.B','IV.C','IV.D','IV.E','IV.F',
                      'IV.G','IV.H','IV.I','V.1','V.1.comment','V.2','V.2.comment',
                      'V.3','V.3.comment','V.4','V.4.comment','V.A','V.B','V.C','V.D',
                      'V.E','VI.','VI.comment','VII.','VII.comment','VIII.','1','2','3',
                      '4','5','6','6.comment','7','8','9','9.comment','10','11','12',
                      '13','14','15','16','17','18','19','20','21','22','23','24','25',
                      '26','27','28','29','29.comment','30','31','32','33','34','35',
                      '36','37','38','39','40','40.comment','41','42','43','44','45',
                      '46','47','48','49','50','46.comment','51','52','53','54','55',
                      '56.a','56.b','56.c','56.d','56.e','56.f','56.g','56.d.comment',
                      '57','58','59','60','58.comment','61','62','63','64','65','66',
                      '67','68','69','70','66.comment','70.comment','71','72','73','74',
                      '75','76','77','78','79','80','77.comment','79.comment','81','82',
                      '83','84','85','86','87','88','89','90','84.comment','85.comment',
                      '91','92','93','94','95','96','97','98','99','100','92.comment',
                      '100.comment','101','102','103','104','105','106','107','108',
                      '109','110','111','112','113','114','115','116','117','118','119',
                      '120','121','122','123','124','125','126']
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=d, inplace=True)
        cols_export = ['ids'] + item_order + ['ASR_summary_adaptiveFunctioning_friends_sum','ASR_summary_adaptiveFunctioning_spouse_sum',
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
        df[cols_export].to_csv('%s/quest_ASR-18-59.csv' % out_dir, index=False)
  


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
    
    recoder = {1:5, 2:4, 3:3, 4:2, 5:1}     
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
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['Mean_SelfEst']          
        df[cols_export].to_csv('%s/quest_SE_8.csv' % out_dir, index=False)
  


##############################################################################
####### Involuntary Musical Imagery Scale (Earworm Scale) ####################
##############################################################################

def run_IMIS(df, out_dir=None):

    ### Additional questions about the frequency of episodes, the length of the music loop in one's head ( Sec Length) 
    ### and the length of INMI episode (Epi Length)

    print 'Involuntary Musical Imagery Scale (IMIS) \n\n'
    print 'An Involuntary Musical Imagery (INMI) episode is the \n experience of a repetition of a short music loop in one s head, \n unbidden to the mind and without conscious control\n INMI are also called Earworms. \n'

    print 'Frequency of INMI episodes'
    print df["EWSaBASEQ[AQ_1]"].describe()
    print '\n'


    print 'All subsequent reported scores are for participants who reported experiencing INMI'
    print ' (answer to the frequency question different from "never" = 1) \n\n' 
    
    print 'Section length (length of music loop experienced as INMI)'
    print df["EWSdBASEQ[AQ2]"].describe()
    print '\n'

    print 'Episode length'
    print df["EWSeBASEQ[AQ3]"].describe()
    print '\n'

   
    plt.figure
    plt.subplot(131)   
    sns.countplot(df["EWSaBASEQ[AQ_1]"].dropna(), order=range(int(df["EWSaBASEQ[AQ_1]"].min()),int(df["EWSaBASEQ[AQ_1]"].max())))   
    plt.xlabel("Freq", fontsize = 14)                        
    

    plt.subplot(132)
    sns.countplot(df["EWSdBASEQ[AQ2]"].dropna(), order=range(int(df["EWSdBASEQ[AQ2]"].min()),int(df["EWSdBASEQ[AQ2]"].max())))
    plt.xlabel("Sec length", fontsize = 14)    

    plt.subplot(133)
    sns.countplot(df["EWSeBASEQ[AQ3]"].dropna(), order=range(int(df["EWSeBASEQ[AQ3]"].min()),int(df["EWSeBASEQ[AQ3]"].max())))
    plt.xlabel("Epi Length", fontsize = 14)
    plt.show()

    #Calculate factors
    df['IMIS_NegVal_sum'] = df[['EWSbBASEQ[NV1]','EWSbBASEQ[NV2]','EWSbBASEQ[NV3]','EWSbBASEQ[NV4]','EWSbBASEQ[NV5]','EWSbBASEQ[NV6]','EWSbBASEQ[NV7]']].sum(axis=1)
    df['IMIS_Help_sum'] = df[['EWScBASEQ[H1]','EWScBASEQ[H2]']].sum(axis=1)
    df['IMIS_Movement_sum'] = df[['EWScBASEQ[M1]','EWScBASEQ[M2]','EWScBASEQ[M3]']].sum(axis=1)
    df['IMIS_PersRef_sum'] = df[['EWScBASEQ[PR1]','EWScBASEQ[PR2]','EWScBASEQ[PR3]']].sum(axis=1)

    print 'Negative Valence'
    print df["IMIS_NegVal_sum"].describe()
    print '\n\n'

    print 'Help'
    print df["IMIS_Help_sum"].describe()
    print '\n'

    print 'Movement'
    print df["IMIS_Movement_sum"].describe()
    print '\n'

    print 'Personal Reflections'
    print df["IMIS_PersRef_sum"].describe()
    print '\n'


    plt.figure
    plt.subplot(121)   
    sns.distplot(df["IMIS_NegVal_sum"].dropna(), kde = True)
    plt.xlabel("Negative Valence", fontsize = 14)                        
    
    plt.subplot(122)
    sns.distplot(df["IMIS_Help_sum"].dropna(), kde = True)
    plt.xlabel("Help", fontsize = 14)    
    plt.show()

    plt.figure
    plt.subplot(121)
    sns.distplot(df["IMIS_Movement_sum"].dropna(), kde = True)
    plt.xlabel("Movement ", fontsize = 14)
        
    plt.subplot(122)
    sns.distplot(df["IMIS_PersRef_sum"].dropna(), kde = True)
    plt.xlabel("Pers Refl ", fontsize = 14)
    plt.show()


    if out_dir:
        cols = ['EWSaBASEQ[AQ_1]','EWSbBASEQ[NV1]','EWSbBASEQ[NV2]','EWSbBASEQ[NV3]','EWSbBASEQ[NV4]','EWSbBASEQ[NV5]',
                'EWSbBASEQ[NV6]','EWSbBASEQ[NV7]','EWScBASEQ[M1]','EWScBASEQ[M2]','EWScBASEQ[M3]','EWScBASEQ[PR1]',
                'EWScBASEQ[PR2]','EWScBASEQ[PR3]','EWScBASEQ[H1]','EWScBASEQ[H2]','EWSdBASEQ[AQ2]','EWSeBASEQ[AQ3]']
                
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ["IMIS_NegVal_sum", "IMIS_Help_sum", "IMIS_Movement_sum", "IMIS_PersRef_sum"]          
        df[cols_export].to_csv('%s/quest_IMIS_18.csv' % out_dir, index=False)
  


##############################################################################
####### Goldsmiths Musical Sophistication Index (Gold-MSI) ###################
##############################################################################
  
def run_GoldMSI(df, out_dir=None):
    #items to be recoded
    items_recoded = ['MUSaBASEQ[MUS_21]',
                     'MUSdBASEQ[MUS_14]',
                     'MUSdBASEQ[MUS_27]'] 
    recoder = {1:7, 2:6, 3:5, 4:4, 5:3, 6:2, 7:1} 
     
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64) 

    df['GoldMSI_Active_sum'] = df[['MUSaBASEQ[MUS_21]','MUSaBASEQ[MUS_1]','MUSaBASEQ[MUS_15]','MUSaBASEQ[MUS_24]','MUSaBASEQ[MUS_28]','MUSaBASEQ[MUS_3]','MUSaBASEQ[MUS_8]','MUSbBASEQ[MUS_34]','MUScBASEQ[MUS_38]']].sum(axis=1)

    df['GoldMSI_Training_sum'] = df[['MUSdBASEQ[MUS_14]','MUSdBASEQ[MUS_27]','MUSeBASEQ[MUS_32]','MUSfBASEQ[MUS_33]','MUSgBASEQ[MUS_35]','MUShBASEQ[MUS_36]','MUSiBASEQ[MUS_37]']].sum(axis=1)
    
    print 'Goldsmiths Musical Sophistication Index (Gold-MSI) \n\n'
    
    print "Active Engagement in Musical Activities:\n"
    print df['GoldMSI_Active_sum'].describe()
    print "\n"

    print "Musical Training:\n"
    print df['GoldMSI_Training_sum'].describe()
    print "\n"

    plt.figure
    plt.subplot(121)
    sns.distplot(df["GoldMSI_Active_sum"].dropna(), kde = True)
    plt.xlabel("Active Engagement ", fontsize = 14)
        
    plt.subplot(122)
    sns.distplot(df["GoldMSI_Training_sum"].dropna(), kde = True)
    plt.xlabel("Training ", fontsize = 14)
    plt.show()
    
    if out_dir:
        cols = ['MUSaBASEQ[MUS_1]','MUSaBASEQ[MUS_3]','MUSaBASEQ[MUS_8]','MUSaBASEQ[MUS_15]','MUSaBASEQ[MUS_21]','MUSaBASEQ[MUS_24]',
                'MUSaBASEQ[MUS_28]','MUSbBASEQ[MUS_34]','MUScBASEQ[MUS_38]','MUSdBASEQ[MUS_14]','MUSdBASEQ[MUS_27]','MUSeBASEQ[MUS_32]',
                'MUSfBASEQ[MUS_33]','MUSgBASEQ[MUS_35]','MUShBASEQ[MUS_36]','MUSiBASEQ[MUS_37]']
               
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ["GoldMSI_Active_sum", 'GoldMSI_Training_sum']          
        df[cols_export].to_csv('%s/quest_Gold-MSI_16.csv' % out_dir, index=False)
  


##############################################################################
####################### Epsworth Sleepiness Scale ############################
##############################################################################

def run_ESS(df, out_dir=None):

    print 'Questionnaire measures general level of sleepiness as the sum of 8 Items\n'
    
    cols = ['ESSBASEQ[ESS1]', 'ESSBASEQ[ESS2]', 'ESSBASEQ[ESS3]', 'ESSBASEQ[ESS4]',
            'ESSBASEQ[ESS5]', 'ESSBASEQ[ESS6]', 'ESSBASEQ[ESS7]', 'ESSBASEQ[ESS8]']    
    
    df['ESS_summary_sum'] = df[cols].sum(axis=1)
    
                                
    print df['ESS_summary_sum'].describe()
    sns.countplot(df['ESS_summary_sum'].dropna(), order=range(int(df['ESS_summary_sum'].min()),int(df['ESS_summary_sum'].max())))
    plt.show()
    
    if out_dir:
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['ESS_summary_sum']      
        df[cols_export].to_csv('%s/quest_ESS_8.csv' % out_dir, index=False)
  
    

##############################################################################
############################## BDI ###########################################
##############################################################################

def run_BDI(df, out_dir=None):
    
    # recode items
    zero = ['BDIABASEQ[BDIA0]', 'BDIBBASEQ[BDIB0]', 'BDICBASEQ[BDIC0]',
            'BDIDBASEQ[BDID0]', 'BDIEBASEQ[BDIE0]', 'BDIFBASEQ[BDIF0]',
            'BDIGBASEQ[BDIG0]', 'BDIHBASEQ[BDIH0]', 'BDIIBASEQ[BDII0]', 
            'BDIJBASEQ[BDIJ0]', 'BDIKBASEQ[BDIK0]', 'BDILBASEQ[BDIL0]', 
            'BDIMBASEQ[BDIM0]', 'BDINBASEQ[BDIN0]', 'BDIOBASEQ[BDIO0]',
            'BDIPBASEQ[BDIP0]', 'BDIQBASEQ[BDIQ0]', 'BDIRBASEQ[BDIR0]',
            'BDISBASEQ[BDIS0]', 'BDITBASEQ[BDIT0]', 'BDIUBASEQ[BDIU0]']
    for item in zero:
        df[item].replace(to_replace=1, value=0, inplace=True)
        df[item].replace(to_replace='NaN', value=0, inplace=True)
            
    one = ['BDIABASEQ[BDIA1]', 'BDIBBASEQ[BDIB1]', 'BDICBASEQ[BDIC1]',
           'BDIDBASEQ[BDID1]', 'BDIEBASEQ[BDIE1]', 'BDIFBASEQ[BDIF1]',
           'BDIGBASEQ[BDIG1]', 'BDIHBASEQ[BDIH1]', 'BDIIBASEQ[BDII1]', 
           'BDIJBASEQ[BDIJ1]', 'BDIKBASEQ[BDIK1]', 'BDILBASEQ[BDIL1]',
           'BDIMBASEQ[BDIM1]', 'BDINBASEQ[BDIN1]', 'BDIOBASEQ[BDIO1]',
           'BDIPBASEQ[BDIP1]', 'BDIQBASEQ[BDIQ1]', 'BDIRBASEQ[BDIR1]',
           'BDISBASEQ[BDIS1]', 'BDITBASEQ[BDIT1]', 'BDIUBASEQ[BDIU1]']
    for item in one:
        df[item].replace(to_replace=1, value=1, inplace=True)
        df[item].replace(to_replace='NaN', value=0, inplace=True)
            
    two = ['BDIABASEQ[BDIA2]', 'BDIBBASEQ[BDIB2]', 'BDICBASEQ[BDIC2]',
           'BDIDBASEQ[BDID2]', 'BDIEBASEQ[BDIE2]', 'BDIFBASEQ[BDIF2]',
           'BDIGBASEQ[BDIG2]', 'BDIHBASEQ[BDIH2]', 'BDIIBASEQ[BDII2]', 
           'BDIJBASEQ[BDIJ2]', 'BDIKBASEQ[BDIK2]', 'BDILBASEQ[BDIL2]', 
           'BDIMBASEQ[BDIM2]', 'BDINBASEQ[BDIN2]', 'BDIOBASEQ[BDIO2]',
           'BDIPBASEQ[BDIP2]', 'BDIQBASEQ[BDIQ2]', 'BDIRBASEQ[BDIR2]',
           'BDISBASEQ[BDIS2]', 'BDITBASEQ[BDIT2]', 'BDIUBASEQ[BDIU2]']
    for item in two:
        df[item].replace(to_replace=1, value=2, inplace=True)
        df[item].replace(to_replace='NaN', value=0, inplace=True)
            
    three = ['BDIABASEQ[BDIA3]', 'BDIBBASEQ[BDIB3]', 'BDICBASEQ[BDIC3]',
             'BDIDBASEQ[BDID3]', 'BDIEBASEQ[BDIE3]', 'BDIFBASEQ[BDIF3]', 
             'BDIGBASEQ[BDIG3]', 'BDIHBASEQ[BDIH3]', 'BDIIBASEQ[BDII3]', 
             'BDIJBASEQ[BDIJ3]', 'BDIKBASEQ[BDIK3]', 'BDILBASEQ[BDIL3]',
             'BDIMBASEQ[BDIM3]', 'BDINBASEQ[BDIN3]', 'BDIOBASEQ[BDIO3]',
             'BDIPBASEQ[BDIP3]', 'BDIQBASEQ[BDIQ3]', 'BDIRBASEQ[BDIR3]',
             'BDISBASEQ[BDIS3]', 'BDITBASEQ[BDIT3]', 'BDIUBASEQ[BDIU3]']
    for item in three:
        df[item].replace(to_replace=1, value=3, inplace=True)
        df[item].replace(to_replace='NaN', value=0, inplace=True)         
    
    df['1'] = df[['BDIABASEQ[BDIA0]', 'BDIABASEQ[BDIA1]', 'BDIABASEQ[BDIA2]', 'BDIABASEQ[BDIA3]']].sum(axis=1)
    df['2'] = df[['BDIBBASEQ[BDIB0]', 'BDIBBASEQ[BDIB1]', 'BDIBBASEQ[BDIB2]', 'BDIBBASEQ[BDIB3]']].sum(axis=1)
    df['3'] = df[['BDICBASEQ[BDIC0]', 'BDICBASEQ[BDIC1]', 'BDICBASEQ[BDIC2]', 'BDICBASEQ[BDIC3]']].sum(axis=1)
    df['4'] = df[['BDIDBASEQ[BDID0]', 'BDIDBASEQ[BDID1]', 'BDIDBASEQ[BDID2]', 'BDIDBASEQ[BDID3]']].sum(axis=1)
    df['5'] = df[['BDIEBASEQ[BDIE0]', 'BDIEBASEQ[BDIE1]', 'BDIEBASEQ[BDIE2]', 'BDIEBASEQ[BDIE3]']].sum(axis=1)
    df['6'] = df[['BDIFBASEQ[BDIF0]', 'BDIFBASEQ[BDIF1]', 'BDIFBASEQ[BDIF2]', 'BDIFBASEQ[BDIF3]']].sum(axis=1)
    df['7'] = df[['BDIGBASEQ[BDIG0]', 'BDIGBASEQ[BDIG1]', 'BDIGBASEQ[BDIG2]', 'BDIGBASEQ[BDIG3]']].sum(axis=1)
    df['8'] = df[['BDIHBASEQ[BDIH0]', 'BDIHBASEQ[BDIH1]', 'BDIHBASEQ[BDIH2]', 'BDIHBASEQ[BDIH3]']].sum(axis=1)
    df['9'] = df[['BDIIBASEQ[BDII0]', 'BDIIBASEQ[BDII1]', 'BDIIBASEQ[BDII2]', 'BDIIBASEQ[BDII3]']].sum(axis=1)
    df['10'] = df[['BDIJBASEQ[BDIJ0]', 'BDIJBASEQ[BDIJ1]', 'BDIJBASEQ[BDIJ2]', 'BDIJBASEQ[BDIJ3]']].sum(axis=1)
    df['11'] = df[['BDIKBASEQ[BDIK0]', 'BDIKBASEQ[BDIK1]', 'BDIKBASEQ[BDIK2]', 'BDIKBASEQ[BDIK3]']].sum(axis=1)
    df['12'] = df[['BDILBASEQ[BDIL0]', 'BDILBASEQ[BDIL1]', 'BDILBASEQ[BDIL2]', 'BDILBASEQ[BDIL3]']].sum(axis=1)
    df['13'] = df[['BDIMBASEQ[BDIM0]', 'BDIMBASEQ[BDIM1]', 'BDIMBASEQ[BDIM2]', 'BDIMBASEQ[BDIM3]']].sum(axis=1)
    df['14'] = df[['BDINBASEQ[BDIN0]', 'BDINBASEQ[BDIN1]', 'BDINBASEQ[BDIN2]', 'BDINBASEQ[BDIN3]']].sum(axis=1)
    df['15'] = df[['BDIOBASEQ[BDIO0]', 'BDIOBASEQ[BDIO1]', 'BDIOBASEQ[BDIO2]', 'BDIOBASEQ[BDIO3]']].sum(axis=1)
    df['16'] = df[['BDIPBASEQ[BDIP0]', 'BDIPBASEQ[BDIP1]', 'BDIPBASEQ[BDIP2]', 'BDIPBASEQ[BDIP3]']].sum(axis=1)
    df['17'] = df[['BDIQBASEQ[BDIQ0]', 'BDIQBASEQ[BDIQ1]', 'BDIQBASEQ[BDIQ2]', 'BDIQBASEQ[BDIQ3]']].sum(axis=1)
    df['18'] = df[['BDIRBASEQ[BDIR0]', 'BDIRBASEQ[BDIR1]', 'BDIRBASEQ[BDIR2]', 'BDIRBASEQ[BDIR3]']].sum(axis=1)
    df['19'] = df[['BDISBASEQ[BDIS0]', 'BDISBASEQ[BDIS1]', 'BDISBASEQ[BDIS2]', 'BDISBASEQ[BDIS3]']].sum(axis=1)
    df['20'] = df[['BDIS4']]
    df['21'] = df[['BDITBASEQ[BDIT0]', 'BDITBASEQ[BDIT1]', 'BDITBASEQ[BDIT2]', 'BDITBASEQ[BDIT3]']].sum(axis=1) 
    df['22'] = df[['BDIUBASEQ[BDIU0]', 'BDIUBASEQ[BDIU1]', 'BDIUBASEQ[BDIU2]', 'BDIUBASEQ[BDIU3]']].sum(axis=1)
                         
    # output
    df['BDI_summary_sum'] = df[[str(x+1) for x in range(22)]].sum(axis=1)                
    print 'For the general population, a score of 21 or over represents depression\n'   
    print df['BDI_summary_sum'].describe()
    sns.countplot(df['BDI_summary_sum'].dropna(), order=range(int(df['BDI_summary_sum'].min()),int(df['BDI_summary_sum'].max())))
    plt.show()
    
    if out_dir:  
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        cols_export = ['ids'] + [str(x+1) for x in range(22)] + ['BDI_summary_sum']              
        df[cols_export].to_csv('%s/quest_BDI_22.csv' % out_dir, index=False)
  


##############################################################################
############################## HADS ##########################################
##############################################################################

def run_HADS(df, out_dir=None):
    
    # anxiety / HADS-A
    df['tense'] = df['HADS1BASEQ[HADS1]'].subtract(1).multiply(-1).add(3)
    df['frightened'] = df['HADS3BASEQ[HADS3]'].subtract(1).multiply(-1).add(3)
    df['worry'] = df['HADS5BASEQ[HADS5]'].subtract(1).multiply(-1).add(3)
    df['relaxed'] = df['HADS7BASEQ[HADS7]'].subtract(1)
    df['butterflies'] = df['HADS9BASEQ[HADS9]'].subtract(1)
    df['restless'] = df['HADS11BASEQ[HADS11]'].subtract(1).multiply(-1).add(3)
    df['panic'] = df['HADS13BASEQ[HADS13]'].subtract(1).multiply(-1).add(3)
    df['HADS-A_summary_sum'] = df[['tense', 'frightened', 'worry', 'relaxed', 'butterflies', 'restless', 'panic']].sum(axis=1)   
    
    # depression / HADS-D
    df['enjoy'] = df['HADS2BASEQ[HADS2]'].subtract(1)
    df['laugh'] = df['HADS4BASEQ[HADS4]'].subtract(1)
    df['cheerful'] = df['HADS6BASEQ[HADS6]'].subtract(1).multiply(-1).add(3)
    df['slowed'] = df['HADS8BASEQ[HADS8]'].subtract(1).multiply(-1).add(3)
    df['appearance'] = df['HADS10BASEQ[HADS10]'].subtract(1).multiply(-1).add(3)
    df['lookforward'] = df['HADS12BASEQ[HADS12]'].subtract(1)
    df['entertain'] = df['HADS14BASEQ[HADS14]'].subtract(1)
    df['HADS-D_summary_sum'] = df[['enjoy', 'laugh', 'cheerful', 'slowed', 'appearance', 'lookforward', 'entertain']].sum(axis=1)
    
    
    print 'rough interpretation: \n0-7 normal range, 8-10 suggestive presence of mood disorder, >11 probable presence of mood disorder \n'
    
    #### anxiety ####
    print 'HADS-A - anxiety\n'
    print df['HADS-A_summary_sum'].describe()
    sns.countplot(df['HADS-A_summary_sum'].dropna(), order=range(int(df['HADS-A_summary_sum'].min()),int(df['HADS-A_summary_sum'].max())))
    plt.show()
     
    
    #### depression ####
    print '\n\nHADS-D - depression\n'
    print df['HADS-D_summary_sum'].describe()
    sns.countplot(df['HADS-D_summary_sum'].dropna(), order=range(int(df['HADS-D_summary_sum'].min()),int(df['HADS-D_summary_sum'].max())))
    plt.show()
    
    if out_dir:
        cols = ['tense','enjoy','frightened','laugh','worry','cheerful','relaxed','slowed',
                'butterflies','appearance','restless','lookforward','panic','entertain']
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['HADS-A_summary_sum', 'HADS-D_summary_sum']               
        df[cols_export].to_csv('%s/quest_HADS_14.csv' % out_dir, index=False)



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
                     'BPSbBASEQ[BPS13]',
                     'BPSbBASEQ[BPS15]',
                     'BPSbBASEQ[BPS18]',
                     'BPScBASEQ[BPS22]',
                     'BPScBASEQ[BPS23]',
                     'BPScBASEQ[BPS24]']
                         
                             
    #recode items                 
    recoder = {1:7 , 2:6, 3:5, 4:4, 5:3, 6:2, 7:1 }
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
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['BPS_sum']                 
        df[cols_export].to_csv('%s/quest_BP_28' % out_dir, index=False)
  


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
                    'DACcBASEQ[DAC18]',
                    'DACcBASEQ[DAC20]']
    
    #recode items                 
    recoder = {1:4 , 2:3, 3:2, 4:1}
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
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['DAC_sum']                  
        df[cols_export].to_csv('%s/quest_ACS_20.csv' % out_dir, index=False)
  
  

##############################################################################
############################## NEO-PI-R ######################################
##############################################################################

def run_NEOPIR(pir_f, ffi_lsd_f, out_dir=None):
    
    
#####  create combined dataframe ####    
    

    cols_neo_pir = ['ID', 'NEOaBASEQ[NEO2]','NEOaBASEQ[NEO3]','NEOaBASEQ[NEO5]','NEOaBASEQ[NEO7r]','NEOaBASEQ[NEO8r]','NEOaBASEQ[NEO9]','NEOaBASEQ[NEO10r]','NEOaBASEQ[NEO12]',
                'NEOaBASEQ[NEO13]','NEOaBASEQ[NEO16]','NEObBASEQ[NEO17r]','NEObBASEQ[NEO18r]','NEObBASEQ[NEO20r]','NEObBASEQ[NEO21r]','NEObBASEQ[NEO22]','NEObBASEQ[NEO24r]',
                'NEObBASEQ[NEO27r]','NEObBASEQ[NEO29]','NEObBASEQ[NEO30r]','NEObBASEQ[NEO31]','NEOcBASEQ[NEO32r]','NEOcBASEQ[NEO33r]','NEOcBASEQ[NEO34]','NEOcBASEQ[NEO35r]',
                'NEOcBASEQ[NEO36r]','NEOcBASEQ[NEO38]','NEOcBASEQ[NEO42r]','NEOcBASEQ[NEO43r]','NEOcBASEQ[NEO47]','NEOcBASEQ[NEO48]','NEOdBASEQ[NEO49r]','NEOdBASEQ[NEO51]',
                'NEOdBASEQ[NEO52r]','NEOdBASEQ[NEO54]','NEOdBASEQ[NEO56r]','NEOdBASEQ[NEO57]','NEOdBASEQ[NEO58]','NEOdBASEQ[NEO60]','NEOdBASEQ[NEO62]','NEOdBASEQ[NEO63]',
                'NEOeBASEQ[NEO65]','NEOeBASEQ[NEO66]','NEOeBASEQ[NEO68r]','NEOeBASEQ[NEO69]','NEOeBASEQ[NEO70r]','NEOeBASEQ[NEO71r]','NEOeBASEQ[NEO72]','NEOeBASEQ[NEO73]',
                'NEOeBASEQ[NEO75]','NEOeBASEQ[NEO77r]','NEOfBASEQ[NEO78r]','NEOfBASEQ[NEO79]','NEOfBASEQ[NEO80r]','NEOfBASEQ[NEO81r]','NEOfBASEQ[NEO82]','NEOfBASEQ[NEO84r]',
                'NEOfBASEQ[NEO89]','NEOfBASEQ[NEO90r]','NEOfBASEQ[NEO92r]','NEOfBASEQ[NEO94]','NEOgBASEQ[NEO95r]','NEOgBASEQ[NEO96r]','NEOgBASEQ[NEO97]','NEOgBASEQ[NEO99r]',
                'NEOgBASEQ[NEO100]','NEOgBASEQ[NEO101]','NEOgBASEQ[NEO102r]','NEOgBASEQ[NEO103r]','NEOgBASEQ[NEO105r]','NEOgBASEQ[NEO106r]','NEOhBASEQ[NEO111]','NEOhBASEQ[NEO112r]',
                'NEOhBASEQ[NEO113r]','NEOhBASEQ[NEO114]','NEOhBASEQ[NEO115r]','NEOhBASEQ[NEO116r]','NEOhBASEQ[NEO117]','NEOhBASEQ[NEO118]','NEOhBASEQ[NEO119r]','NEOhBASEQ[NEO120]',
                'NEOiBASEQ[NEO121r]','NEOiBASEQ[NEO123]','NEOiBASEQ[NEO124r]','NEOiBASEQ[NEO125]','NEOiBASEQ[NEO126]','NEOiBASEQ[NEO127r]','NEOiBASEQ[NEO129]','NEOiBASEQ[NEO131]',
                'NEOiBASEQ[NEO132]','NEOiBASEQ[NEO133]','NEOjBASEQ[NEO134r]','NEOjBASEQ[NEO137r]','NEOjBASEQ[NEO138r]','NEOjBASEQ[NEO139]','NEOjBASEQ[NEO140r]','NEOjBASEQ[NEO141r]',
                'NEOjBASEQ[NEO143]','NEOjBASEQ[NEO144r]','NEOjBASEQ[NEO145]','NEOjBASEQ[NEO146]','NEOkBASEQ[NEO148r]','NEOkBASEQ[NEO149]','NEOkBASEQ[NEO150r]','NEOkBASEQ[NEO151]',
                'NEOkBASEQ[NEO152]','NEOkBASEQ[NEO153r]','NEOkBASEQ[NEO154]','NEOkBASEQ[NEO155r]','NEOkBASEQ[NEO156r]','NEOkBASEQ[NEO157]','NEOlBASEQ[NEO158]','NEOlBASEQ[NEO159r]',
                'NEOlBASEQ[NEO160]','NEOlBASEQ[NEO161]','NEOlBASEQ[NEO165]','NEOlBASEQ[NEO166r]','NEOlBASEQ[NEO167]','NEOlBASEQ[NEO168]','NEOlBASEQ[NEO169r]','NEOlBASEQ[NEO170]',
                'NEOmBASEQ[NEO171]','NEOmBASEQ[NEO172]','NEOmBASEQ[NEO174]','NEOmBASEQ[NEO175r]','NEOmBASEQ[NEO176r]','NEOmBASEQ[NEO178]','NEOmBASEQ[NEO179]','NEOmBASEQ[NEO180]',
                'NEOmBASEQ[NEO181r]','NEOmBASEQ[NEO182]','NEOnBASEQ[NEO183r]','NEOnBASEQ[NEO184]','NEOnBASEQ[NEO185]','NEOnBASEQ[NEO186]','NEOnBASEQ[NEO187r]','NEOnBASEQ[NEO189r]',
                'NEOnBASEQ[NEO190r]','NEOnBASEQ[NEO191]','NEOnBASEQ[NEO192]','NEOnBASEQ[NEO193]','NEOoBASEQ[NEO194]','NEOoBASEQ[NEO195]','NEOoBASEQ[NEO196]','NEOoBASEQ[NEO198r]',
                'NEOoBASEQ[NEO199r]','NEOoBASEQ[NEO201]','NEOoBASEQ[NEO202]','NEOoBASEQ[NEO204]','NEOoBASEQ[NEO205r]','NEOoBASEQ[NEO206r]','NEOpBASEQ[NEO207r]','NEOpBASEQ[NEO208r]',
                'NEOpBASEQ[NEO209]','NEOpBASEQ[NEO210]','NEOpBASEQ[NEO211]','NEOpBASEQ[NEO212]','NEOpBASEQ[NEO213r]','NEOpBASEQ[NEO214]','NEOpBASEQ[NEO215]','NEOpBASEQ[NEO216]',
                'NEOqBASEQ[NEO217]','NEOqBASEQ[NEO218]','NEOqBASEQ[NEO219r]','NEOqBASEQ[NEO220r]','NEOqBASEQ[NEO222r]','NEOqBASEQ[NEO223]','NEOqBASEQ[NEO224]','NEOqBASEQ[NEO225]',
                'NEOqBASEQ[NEO226]','NEOqBASEQ[NEO228r]','NEOrBASEQ[NEO230]','NEOrBASEQ[NEO231r]','NEOrBASEQ[NEO232]','NEOrBASEQ[NEO233]','NEOrBASEQ[NEO234r]','NEOrBASEQ[NEO235]',
                'NEOrBASEQ[NEO236r]','NEOrBASEQ[NEO238r]','NEOrBASEQ[NEO239]','NEOrBASEQ[NEO240]','NEOrBASEQ[NEO241]']
    
    cols_NEOFFI = ['ID', 'NEOFFI01[NEOFFI01]','NEOFFI01[NEOFFI02]','NEOFFI01[NEOFFI03]','NEOFFI01[NEOFFI04]','NEOFFI01[NEOFFI05]','NEOFFI01[NEOFFI06]','NEOFFI01[NEOFFI07]',
                   'NEOFFI01[NEOFFI08]','NEOFFI01[NEOFFI09]','NEOFFI01[NEOFFI10]','NEOFFI01[NEOFFI11]','NEOFFI01[NEOFFI12]','NEOFFI13[NEOFFI13]','NEOFFI13[NEOFFI14]',
                   'NEOFFI13[NEOFFI15]','NEOFFI13[NEOFFI16]','NEOFFI13[NEOFFI17]','NEOFFI13[NEOFFI18]','NEOFFI13[NEOFFI19]','NEOFFI13[NEOFFI20]','NEOFFI13[NEOFFI21]',
                   'NEOFFI13[NEOFFI22]','NEOFFI13[NEOFFI23]','NEOFFI13[NEOFFI24]','NEOFFI25[NEOFFI25]','NEOFFI25[NEOFFI26]','NEOFFI25[NEOFFI27]','NEOFFI25[NEOFFI28]',
                   'NEOFFI25[NEOFFI29]','NEOFFI25[NEOFFI30]','NEOFFI25[NEOFFI31]','NEOFFI25[NEOFFI32]','NEOFFI25[NEOFFI33]','NEOFFI25[NEOFFI34]','NEOFFI25[NEOFFI35]',
                   'NEOFFI25[NEOFFI36]','NEOFFI37[NEOFFI37]','NEOFFI37[NEOFFI38]','NEOFFI37[NEOFFI39]','NEOFFI37[NEOFFI40]','NEOFFI37[NEOFFI41]','NEOFFI37[NEOFFI42]',
                   'NEOFFI37[NEOFFI43]','NEOFFI37[NEOFFI44]','NEOFFI37[NEOFFI45]','NEOFFI37[NEOFFI46]','NEOFFI37[NEOFFI47]','NEOFFI37[NEOFFI48]','NEOFFI49[NEOFFI49]',
                   'NEOFFI49[NEOFFI50]','NEOFFI49[NEOFFI51]','NEOFFI49[NEOFFI52]','NEOFFI49[NEOFFI53]','NEOFFI49[NEOFFI54]','NEOFFI49[NEOFFI55]','NEOFFI49[NEOFFI56]',
                   'NEOFFI49[NEOFFI57]','NEOFFI49[NEOFFI58]','NEOFFI49[NEOFFI59]','NEOFFI49[NEOFFI60]']
     
    
    ##### Neo PI R lemon & lsd #### 
    
    df_pir = pd.read_csv(pir_f, sep = ",")[cols_neo_pir]
    # prep df
    df_pir['ID'].replace('LSD2', '25729', inplace = True)
    df_pir['ID'] = df_pir['ID'].map(lambda x: str(x)[0:5])
    
    # recode item names from complicated to item numbers
    new_items = []
    for item in df_pir.columns.values[1:]:
        item = item[13:]
        item = item[:-1]
        if item[-1] == 'r':
            item = item[:-1]
        new_items.append(item)
    dictionary1 = dict(zip(df_pir.columns.values[1:], new_items))
    df_pir.rename(columns=dictionary1, inplace=True)
    df_pir.dropna(inplace=True)
    
    
    
    ##### NEO FFI lsd #####
    
    df_ffi_lsd = pd.read_csv(ffi_lsd_f, sep = ",", converters={'ID':str})[cols_NEOFFI]
    
    # recode item names from complicated to 1-60
    new_items = []
    for item in df_ffi_lsd.columns.values[1:]:
        item = item[15:]
        item = item[:-1]
        item = int(item)
        item = str(item)
        new_items.append(item)
    dictionary2 = dict(zip(df_ffi_lsd.columns.values[1:], new_items))
    df_ffi_lsd.rename(columns=dictionary2, inplace=True)
    
    # recode ffi item numbers into pir item numbers
    ffi2pir = pd.read_excel('/scr/liberia1/data/lsd/behavioral/NEO/NEO KEY.xlsx', converters={0:str, 1:str})
    dictionary3 = dict(zip(ffi2pir['Neo FFI'],ffi2pir['NEO PI R']))
    df_ffi_lsd.rename(columns=dictionary3, inplace=True)
    df_ffi_lsd.dropna(inplace=True)
    
    
    
    ##### NEO FFI lemon #####
    
    # read in lemon ffi
    df_ffi_lemon = pd.read_csv('/scr/liberia1/data/lsd/behavioral/NEO/NEO-FFI_60.csv').ix[:, 0:61]
    # recode ffi item numbers into pir item numbers
    df_ffi_lemon.rename(columns=dictionary3, inplace=True)
    # change lemon ID to db ID
    df_ffi_lemon.rename(columns={'ID':'Lemon_ID'}, inplace=True)
    df_ffi_lemon.dropna(inplace=True)
    IDentifier = pd.read_excel('/scr/liberia1/data/lsd/behavioral/NEO/LEMONidentifier.xlsx', 
                               sheetname='Overview', converters={1:str}).ix[:193, :2]
    for n in range(len(IDentifier)):
        try:
            IDentifier['DB_ID'][n] = str(IDentifier['DB_ID'][n])[:5]
        except:
            pass
    IDentifier.dropna(inplace=True)
    for n in range(len(IDentifier)):
        if (IDentifier['Lemon_ID'][n][0] != 'L') & (len(IDentifier['Lemon_ID'][n]) == 1):
            IDentifier['Lemon_ID'][n] = 'LEMON00' + IDentifier['Lemon_ID'][n]
        if (IDentifier['Lemon_ID'][n][0] != 'L') & (len(IDentifier['Lemon_ID'][n]) == 2):
            IDentifier['Lemon_ID'][n] = 'LEMON0' + IDentifier['Lemon_ID'][n]
        if (IDentifier['Lemon_ID'][n][0] != 'L') & (len(IDentifier['Lemon_ID'][n]) == 3):
            IDentifier['Lemon_ID'][n] = 'LEMON' + IDentifier['Lemon_ID'][n]
    IDentifier.rename(columns={'DB_ID':'ID'}, inplace=True)
    df_ffi_lemon = pd.merge(df_ffi_lemon, IDentifier, on='Lemon_ID', how='left')
    df_ffi_lemon.drop('Lemon_ID', axis=1, inplace=True)
    
    
    ##### merge everything #####
    
    # combine FFI of lemon and lsd
    df_ffi = pd.concat([df_ffi_lemon, df_ffi_lsd])
    # merge FFI with PI R
    df_neo = pd.merge(df_pir, df_ffi, on='ID', how='inner')
    df_neo.rename(columns={'70_x':'70_pir', '70_y':'70'}, inplace=True)
    col_ordered = ['ID']+[str(x+1) for x in range(241) if x != 82]
    df =  df_neo[col_ordered].copy()
    

#### compute scales ####    

    print 'measure of the Five Factor Model and uses these five dimensions to evaluate adult personality' 
    print '– emotional, interpersonal, experiential, attitudinal, and motivational styles –' 
    print '241 items using a 5-point scale'
    
        
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
                 
                  
                     
    recoder = {0:4, 1:3, 2:2, 3:1, 4:0}    
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

    if out_dir:
        df.to_csv('%s/quest_NEO-PI-R_241.csv' % out_dir, index=False)
  
  

##############################################################################
############# PSSI - Persönlichkeitsstil- und Störungsinventar################
##############################################################################

def run_PSSI(df, out_dir=None):
    cols = ['PSSaBASEQ[PSS1]','PSSaBASEQ[PSS2]','PSSaBASEQ[PSS3]','PSSaBASEQ[PSS4]','PSSaBASEQ[PSS5]','PSSaBASEQ[PSS6]','PSSaBASEQ[PSS7]','PSSaBASEQ[PSS8]','PSSaBASEQ[PSS9]',
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
    recoder = {1:0, 2:1, 3:2, 4:3 }
    for i in cols:
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
                     
    recoder = {0:3, 1:2, 2:1, 3:0}     
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

    if out_dir:
        
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ["PSSI_PN", 'PSSI_SZ', 'PSSI_ST', 'PSSI_BL', 
                                                                    'PSSI_HI', 'PSSI_NA', 'PSSI_SU', 'PSSI_AB', 
                                                                    'PSSI_ZW', 'PSSI_NT', 'PSSI_DP', 'PSSI_SL', 
                                                                    'PSSI_RH', 'PSSI_AS']                 
        df[cols_export].to_csv('%s/quest_PSSI_140.csv' % out_dir, index=False)
  

##############################################################################
################################## MMI #######################################
##############################################################################

def run_MMI(df, out_dir=None):
#items to be recoded                                
    cols= ['MMIadBASEQ[MMI41]' ,'MMIadBASEQ[MMI42]' ,'MMIadBASEQ[MMI43]' ,'MMIadBASEQ[MMI44]' ,'MMIadBASEQ[MMI45]' ,'MMIadBASEQ[MMI46]' ,
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
    recoder = {5 :'NaN', 4 :1, 3:0.66, 2:0.33, 1:0}
    for i in cols:
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
    
    if out_dir:
        
        d = {'MMIaa': '1.1.',
             'MMIab': '1.2.',
             'MMIacBASEQ[MMI31]': '1.3.A',
             'MMIacBASEQ[MMI32]': '1.3.B',
             'MMIacBASEQ[MMI33]': '1.3.C',
             'MMIacBASEQ[MMI34]': '1.3.D',
             'MMIacBASEQ[MMI35]': '1.3.E',
             'MMIadBASEQ[MMI410]': '1.4.J',
             'MMIadBASEQ[MMI411]': '1.4.K',
             'MMIadBASEQ[MMI412]': '1.4.L',
             'MMIadBASEQ[MMI41]': '1.4.A',
             'MMIadBASEQ[MMI42]': '1.4.B',
             'MMIadBASEQ[MMI43]': '1.4.C',
             'MMIadBASEQ[MMI44]': '1.4.D',
             'MMIadBASEQ[MMI45]': '1.4.E',
             'MMIadBASEQ[MMI46]': '1.4.F',
             'MMIadBASEQ[MMI47]': '1.4.G',
             'MMIadBASEQ[MMI48]': '1.4.H',
             'MMIadBASEQ[MMI49]': '1.4.I',
             'MMIae': '2.1.',
             'MMIaf': '2.2.',
             'MMIagBASEQ[MMI71]': '2.3.A',
             'MMIagBASEQ[MMI72]': '2.3.B',
             'MMIagBASEQ[MMI73]': '2.3.C',
             'MMIagBASEQ[MMI74]': '2.3.D',
             'MMIagBASEQ[MMI75]': '2.3.E',
             'MMIahBASEQ[MMI810]': '2.4.J',
             'MMIahBASEQ[MMI811]': '2.4.K',
             'MMIahBASEQ[MMI812]': '2.4.L',
             'MMIahBASEQ[MMI81]': '2.4.A',
             'MMIahBASEQ[MMI82]': '2.4.B',
             'MMIahBASEQ[MMI83]': '2.4.C',
             'MMIahBASEQ[MMI84]': '2.4.D',
             'MMIahBASEQ[MMI85]': '2.4.E',
             'MMIahBASEQ[MMI86]': '2.4.F',
             'MMIahBASEQ[MMI87]': '2.4.G',
             'MMIahBASEQ[MMI88]': '2.4.H',
             'MMIahBASEQ[MMI89]': '2.4.I',
             'MMIai': '3.1.',
             'MMIaj': '3.2.',
             'MMIakBASEQ[MMI111]': '3.3.A',
             'MMIakBASEQ[MMI112]': '3.3.B',
             'MMIakBASEQ[MMI113]': '3.3.C',
             'MMIakBASEQ[MMI114]': '3.3.D',
             'MMIakBASEQ[MMI115]': '3.3.E',
             'MMIalBASEQ[MMI1210]': '3.4.J',
             'MMIalBASEQ[MMI1211]': '3.4.K',
             'MMIalBASEQ[MMI1212]': '3.4.L',
             'MMIalBASEQ[MMI121]': '3.4.A',
             'MMIalBASEQ[MMI122]': '3.4.B',
             'MMIalBASEQ[MMI123]': '3.4.C',
             'MMIalBASEQ[MMI124]': '3.4.D',
             'MMIalBASEQ[MMI125]': '3.4.E',
             'MMIalBASEQ[MMI126]': '3.4.F',
             'MMIalBASEQ[MMI127]': '3.4.G',
             'MMIalBASEQ[MMI128]': '3.4.H',
             'MMIalBASEQ[MMI129]': '3.4.I',
             'MMIam': '4.1.',
             'MMIan': '4.2.',
             'MMIaoBASEQ[MMI151]': '4.3.A',
             'MMIaoBASEQ[MMI152]': '4.3.B',
             'MMIaoBASEQ[MMI153]': '4.3.C',
             'MMIaoBASEQ[MMI154]': '4.3.D',
             'MMIaoBASEQ[MMI155]': '4.3.E',
             'MMIapBASEQ[MMI1610]': '4.4.J',
             'MMIapBASEQ[MMI1611]': '4.4.K',
             'MMIapBASEQ[MMI1612]': '4.4.L',
             'MMIapBASEQ[MMI161]': '4.4.A',
             'MMIapBASEQ[MMI162]': '4.4.B',
             'MMIapBASEQ[MMI163]': '4.4.C',
             'MMIapBASEQ[MMI164]': '4.4.D',
             'MMIapBASEQ[MMI165]': '4.4.E',
             'MMIapBASEQ[MMI166]': '4.4.F',
             'MMIapBASEQ[MMI167]': '4.4.G',
             'MMIapBASEQ[MMI168]': '4.4.H',
             'MMIapBASEQ[MMI169]': '4.4.I',
             'MMIaq': '5.1.',
             'MMIar': '5.2.',
             'MMIasBASEQ[MMI191]': '5.3.A',
             'MMIasBASEQ[MMI192]': '5.3.B',
             'MMIasBASEQ[MMI193]': '5.3.C',
             'MMIasBASEQ[MMI194]': '5.3.D',
             'MMIasBASEQ[MMI195]': '5.3.E',
             'MMIatBASEQ[MMI2010]': '5.4.J',
             'MMIatBASEQ[MMI2011]': '5.4.K',
             'MMIatBASEQ[MMI2012]': '5.4.L',
             'MMIatBASEQ[MMI201]': '5.4.A',
             'MMIatBASEQ[MMI202]': '5.4.B',
             'MMIatBASEQ[MMI203]': '5.4.C',
             'MMIatBASEQ[MMI204]': '5.4.D',
             'MMIatBASEQ[MMI205]': '5.4.E',
             'MMIatBASEQ[MMI206]': '5.4.F',
             'MMIatBASEQ[MMI207]': '5.4.G',
             'MMIatBASEQ[MMI208]': '5.4.H',
             'MMIatBASEQ[MMI209]': '5.4.I',
             'MMIau': '6.1.',
             'MMIav': '6.2.',
             'MMIawBASEQ[MMI232]': '6.3.B',
             'MMIawBASEQ[MMI233]': '6.3.C',
             'MMIawBASEQ[MMI234]': '6.3.D',
             'MMIawBASEQ[MMI235]': '6.3.E',
             'MMIawBASEQ[MMI23]': '6.3.A',
             'MMIaxBASEQ[MMI2410]': '6.4.J',
             'MMIaxBASEQ[MMI2411]': '6.4.K',
             'MMIaxBASEQ[MMI2412]': '6.4.L',
             'MMIaxBASEQ[MMI241]': '6.4.A',
             'MMIaxBASEQ[MMI242]': '6.4.B',
             'MMIaxBASEQ[MMI243]': '6.4.C',
             'MMIaxBASEQ[MMI244]': '6.4.D',
             'MMIaxBASEQ[MMI245]': '6.4.E',
             'MMIaxBASEQ[MMI246]': '6.4.F',
             'MMIaxBASEQ[MMI247]': '6.4.G',
             'MMIaxBASEQ[MMI248]': '6.4.H',
             'MMIaxBASEQ[MMI249]': '6.4.I',
             'MMIay': '7.1.',
             'MMIaz': '7.2.',
             'MMIbaBASEQ[MMI271]': '7.3.A',
             'MMIbaBASEQ[MMI272]': '7.3.B',
             'MMIbaBASEQ[MMI273]': '7.3.C',
             'MMIbaBASEQ[MMI274]': '7.3.D',
             'MMIbaBASEQ[MMI275]': '7.3.E',
             'MMIbbBASEQ[MMI2810]': '7.4.J',
             'MMIbbBASEQ[MMI2811]': '7.4.K',
             'MMIbbBASEQ[MMI2812]': '7.4.L',
             'MMIbbBASEQ[MMI281]': '7.4.A',
             'MMIbbBASEQ[MMI282]': '7.4.B',
             'MMIbbBASEQ[MMI283]': '7.4.C',
             'MMIbbBASEQ[MMI284]': '7.4.D',
             'MMIbbBASEQ[MMI285]': '7.4.E',
             'MMIbbBASEQ[MMI286]': '7.4.F',
             'MMIbbBASEQ[MMI287]': '7.4.G',
             'MMIbbBASEQ[MMI288]': '7.4.H',
             'MMIbbBASEQ[MMI289]': '7.4.I',
             'MMIbc': '8.1.',
             'MMIbd': '8.2.',
             'MMIbeBASEQ[MMI311]': '8.3.A',
             'MMIbeBASEQ[MMI312]': '8.3.B',
             'MMIbeBASEQ[MMI313]': '8.3.C',
             'MMIbeBASEQ[MMI314]': '8.3.D',
             'MMIbeBASEQ[MMI315]': '8.3.E',
             'MMIbfBASEQ[MMI3210]': '8.4.J',
             'MMIbfBASEQ[MMI3211]': '8.4.K',
             'MMIbfBASEQ[MMI3212]': '8.4.L',
             'MMIbfBASEQ[MMI321]': '8.4.A',
             'MMIbfBASEQ[MMI322]': '8.4.B',
             'MMIbfBASEQ[MMI323]': '8.4.C',
             'MMIbfBASEQ[MMI324]': '8.4.D',
             'MMIbfBASEQ[MMI325]': '8.4.E',
             'MMIbfBASEQ[MMI326]': '8.4.F',
             'MMIbfBASEQ[MMI327]': '8.4.G',
             'MMIbfBASEQ[MMI328]': '8.4.H',
             'MMIbfBASEQ[MMI329]': '8.4.I',
             'MMIbg': '9.1.',
             'MMIbh': '9.2.',
             'MMIbh[comment]': '9.3.',
             'MMIbi': '9.4.',
             'MMIbjBASEQ[MMI361]': '9.5.A',
             'MMIbjBASEQ[MMI362]': '9.5.B',
             'MMIbjBASEQ[MMI363]': '9.5.C',
             'MMIbjBASEQ[MMI364]': '9.5.D',
             'MMIbjBASEQ[MMI365]': '9.5.E',
             'MMIbkBASEQ[MMI3710]': '9.6.J',
             'MMIbkBASEQ[MMI3711]': '9.6.K',
             'MMIbkBASEQ[MMI3712]': '9.6.L',
             'MMIbkBASEQ[MMI371]': '9.6.A',
             'MMIbkBASEQ[MMI372]': '9.6.B',
             'MMIbkBASEQ[MMI373]': '9.6.C',
             'MMIbkBASEQ[MMI374]': '9.6.D',
             'MMIbkBASEQ[MMI375]': '9.6.E',
             'MMIbkBASEQ[MMI376]': '9.6.F',
             'MMIbkBASEQ[MMI377]': '9.6.G',
             'MMIbkBASEQ[MMI378]': '9.6.H',
             'MMIbkBASEQ[MMI379]': '9.6.I',
             'MMIbl': '10.1.',
             'MMIbm': '10.2.',
             'MMIbnBASEQ[MMI402]': '10.3.B',
             'MMIbnBASEQ[MMI403]': '10.3.C',
             'MMIbnBASEQ[MMI404]': '10.3.D',
             'MMIbnBASEQ[MMI405]': '10.3.E',
             'MMIbnBASEQ[MMI40]': '10.3.A',
             'MMIboBASEQ[MMI4110]': '10.4.J',
             'MMIboBASEQ[MMI4111]': '10.4.K',
             'MMIboBASEQ[MMI4112]': '10.4.L',
             'MMIboBASEQ[MMI411]': '10.4.A',
             'MMIboBASEQ[MMI412]': '10.4.B',
             'MMIboBASEQ[MMI413]': '10.4.C',
             'MMIboBASEQ[MMI414]': '10.4.D',
             'MMIboBASEQ[MMI415]': '10.4.E',
             'MMIboBASEQ[MMI416]': '10.4.F',
             'MMIboBASEQ[MMI417]': '10.4.G',
             'MMIboBASEQ[MMI418]': '10.4.H',
             'MMIboBASEQ[MMI419]': '10.4.I',
             'MMIbp': '11.1.',
             'MMIbq': '11.2.',
             'MMIbrBASEQ[MMI441]': '11.3.A',
             'MMIbrBASEQ[MMI442]': '11.3.B',
             'MMIbrBASEQ[MMI443]': '11.3.C',
             'MMIbrBASEQ[MMI444]': '11.3.D',
             'MMIbrBASEQ[MMI445]': '11.3.E',
             'MMIbsBASEQ[MMI4510]': '11.4.J',
             'MMIbsBASEQ[MMI4511]': '11.4.K',
             'MMIbsBASEQ[MMI4512]': '11.4.L',
             'MMIbsBASEQ[MMI451]': '11.4.A',
             'MMIbsBASEQ[MMI452]': '11.4.B',
             'MMIbsBASEQ[MMI453]': '11.4.C',
             'MMIbsBASEQ[MMI454]': '11.4.D',
             'MMIbsBASEQ[MMI455]': '11.4.E',
             'MMIbsBASEQ[MMI456]': '11.4.F',
             'MMIbsBASEQ[MMI457]': '11.4.G',
             'MMIbsBASEQ[MMI458]': '11.4.H',
             'MMIbsBASEQ[MMI459]': '11.4.I',
             'MMIbt': '12.1.',
             'MMIbu': '12.2.',
             'MMIbvBASEQ[MMI481]': '12.3.A',
             'MMIbvBASEQ[MMI482]': '12.3.B',
             'MMIbvBASEQ[MMI483]': '12.3.C',
             'MMIbvBASEQ[MMI484]': '12.3.D',
             'MMIbvBASEQ[MMI485]': '12.3.E',
             'MMIbwBASEQ[MMI4910]': '12.4.J',
             'MMIbwBASEQ[MMI4911]': '12.4.K',
             'MMIbwBASEQ[MMI4912]': '12.4.L',
             'MMIbwBASEQ[MMI491]': '12.4.A',
             'MMIbwBASEQ[MMI492]': '12.4.B',
             'MMIbwBASEQ[MMI493]': '12.4.C',
             'MMIbwBASEQ[MMI494]': '12.4.D',
             'MMIbwBASEQ[MMI495]': '12.4.E',
             'MMIbwBASEQ[MMI496]': '12.4.F',
             'MMIbwBASEQ[MMI497]': '12.4.G',
             'MMIbwBASEQ[MMI498]': '12.4.H',
             'MMIbwBASEQ[MMI499]': '12.4.I'}


        item_order = ['1.1.', '1.2.', '1.3.A', '1.3.B', '1.3.C', '1.3.D', '1.3.E',
              '1.4.J', '1.4.K', '1.4.L','1.4.A', '1.4.B', '1.4.C', 
              '1.4.D', '1.4.E', '1.4.F', '1.4.G', '1.4.H', '1.4.I',
              '2.1.','2.2.', '2.3.A', '2.3.B', '2.3.C', '2.3.D', '2.3.E',
              '2.4.J', '2.4.K', '2.4.L', '2.4.A', '2.4.B', '2.4.C',
              '2.4.D', '2.4.E', '2.4.F', '2.4.G', '2.4.H', '2.4.I', 
              '3.1.', '3.2.', '3.3.A', '3.3.B', '3.3.C', '3.3.D', '3.3.E',
              '3.4.J', '3.4.K', '3.4.L', '3.4.A', '3.4.B', '3.4.C', 
              '3.4.D', '3.4.E', '3.4.F', '3.4.G', '3.4.H', '3.4.I',
              '4.1.', '4.2.', '4.3.A', '4.3.B', '4.3.C', '4.3.D', '4.3.E',
              '4.4.J', '4.4.K', '4.4.L', '4.4.A', '4.4.B', '4.4.C',
              '4.4.D', '4.4.E', '4.4.F', '4.4.G', '4.4.H', '4.4.I',
              '5.1.', '5.2.', '5.3.A', '5.3.B', '5.3.C', '5.3.D', '5.3.E',
              '5.4.J', '5.4.K', '5.4.L', '5.4.A', '5.4.B', '5.4.C',
              '5.4.D', '5.4.E', '5.4.F', '5.4.G', '5.4.H', '5.4.I',
              '6.1.', '6.2.', '6.3.B', '6.3.C', '6.3.D', '6.3.E', '6.3.A',
              '6.4.J', '6.4.K', '6.4.L', '6.4.A', '6.4.B', '6.4.C', 
              '6.4.D', '6.4.E', '6.4.F', '6.4.G', '6.4.H', '6.4.I',
              '7.1.', '7.2.', '7.3.A', '7.3.B', '7.3.C', '7.3.D', '7.3.E',
              '7.4.J', '7.4.K', '7.4.L', '7.4.A', '7.4.B', '7.4.C',
              '7.4.D', '7.4.E', '7.4.F', '7.4.G', '7.4.H', '7.4.I',
              '8.1.', '8.2.', '8.3.A', '8.3.B', '8.3.C', '8.3.D', '8.3.E',
              '8.4.J', '8.4.K', '8.4.L', '8.4.A', '8.4.B', '8.4.C', 
              '8.4.D', '8.4.E', '8.4.F', '8.4.G', '8.4.H', '8.4.I',
              '9.1.', '9.2.', '9.3.', '9.4.', '9.5.A', '9.5.B', '9.5.C', '9.5.D', '9.5.E',
              '9.6.J', '9.6.K', '9.6.L', '9.6.A', '9.6.B', '9.6.C',
              '9.6.D', '9.6.E', '9.6.F', '9.6.G', '9.6.H', '9.6.I',
              '10.1.', '10.2.', '10.3.B', '10.3.C', '10.3.D', '10.3.E', '10.3.A',
              '10.4.J', '10.4.K', '10.4.L', '10.4.A', '10.4.B', '10.4.C',
              '10.4.D', '10.4.E', '10.4.F', '10.4.G', '10.4.H', '10.4.I',
              '11.1.', '11.2.', '11.3.A', '11.3.B', '11.3.C', '11.3.D', '11.3.E',
              '11.4.J', '11.4.K', '11.4.L', '11.4.A', '11.4.B', '11.4.C', 
              '11.4.D', '11.4.E', '11.4.F', '11.4.G', '11.4.H', '11.4.I',
              '12.1.', '12.2.', '12.3.A', '12.3.B', '12.3.C', '12.3.D', '12.3.E',
              '12.4.J', '12.4.K', '12.4.L', '12.4.A', '12.4.B', '12.4.C',
              '12.4.D', '12.4.E', '12.4.F', '12.4.G', '12.4.H', '12.4.I']
              
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=d, inplace=True)
        cols_export = ['ids'] + item_order + ['MMI']                  
        df[cols_export].to_csv('%s/quest_MMI_12x4.csv' % out_dir, index=False)
  
  

##############################################################################
############################## BIS/BAS #######################################
##############################################################################

def run_BISBAS(df, out_dir=None):
    #items to be recoded                                
    items_recoded = ['BISBAS02[SQ001]',
                     'BISBAS22[SQ001]']    
                             
    #recode items                 
    recoder = {1:4, 2:3, 3:2, 4:1}
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
 

    if out_dir:
        cols = ['BISBAS01[SQ001]','BISBAS02[SQ001]','BISBAS03[SQ001]','BISBAS04[SQ001]','BISBAS05[SQ001]','BISBAS06[SQ001]','BISBAS07[SQ001]','BISBAS08[SQ001]',
               'BISBAS09[SQ001]','BISBAS10[SQ001]','BISBAS11[SQ001]','BISBAS12[SQ001]','BISBAS13[SQ001]','BISBAS14[SQ001]','BISBAS15[SQ001]','BISBAS16[SQ001]',
               'BISBAS17[SQ001]','BISBAS18[SQ001]','BISBAS19[SQ001]','BISBAS20[SQ001]','BISBAS21[SQ001]','BISBAS22[SQ001]','BISBAS23[SQ001]','BISBAS24[SQ001]']
     
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['BIS', 'BAS']                  
        df[cols_export].to_csv('%s/quest_BISBAS_24.csv' % out_dir, index=False)
      
    
      
##############################################################################
################################# STAI #######################################
##############################################################################

def run_STAI(df, out_dir=None):

    cols = ['STAI01[STAI01]','STAI01[STAI02]','STAI01[STAI03]','STAI01[STAI04]','STAI01[STAI05]','STAI01[STAI06]','STAI01[STAI07]','STAI01[STAI08]',
                 'STAI01[STAI09]','STAI01[STAI10]','STAI11[STAI11]','STAI11[STAI12]','STAI11[STAI13]','STAI11[STAI14]','STAI11[STAI15]','STAI11[STAI16]',
                 'STAI11[STAI17]','STAI11[STAI18]','STAI11[STAI19]','STAI11[STAI20]']
    
    items_recoded = ['STAI01[STAI01]', 'STAI01[STAI06]', 'STAI01[STAI07]', 'STAI01[STAI10]', 
                     'STAI11[STAI13]', 'STAI11[STAI16]', 'STAI11[STAI19]']
                    
    recoder = {1:4, 2:3, 3:2, 4:1}
    for i in items_recoded:
        df[i] = df[i].map(recoder).astype(float64)   
    
    df['STAI_A-Trait_summary_sum'] = df[cols].sum(axis=1)
    
    print df['STAI_A-Trait_summary_sum'].describe()  
    plt.figure
    sns.distplot(df['STAI_A-Trait_summary_sum'].dropna(), kde = True)
    plt.show()
    
    if out_dir:
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ['STAI_A-Trait_summary_sum']                  
        df[cols_export].to_csv('%s/quest_STAI-G-X2_20.csv' % out_dir, index=False)
      


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

    if out_dir:
        
        cols = ['STAXI01[STAXI01]','STAXI01[STAXI02]','STAXI01[STAXI03]','STAXI01[STAXI04]','STAXI01[STAXI05]','STAXI01[STAXI06]','STAXI01[STAXI07]',
              'STAXI01[STAXI08]','STAXI01[STAXI09]','STAXI01[STAXI10]','STAXI11[STAXI11]','STAXI11[STAXI12]','STAXI11[STAXI13]','STAXI11[STAXI14]','STAXI11[STAXI15]',
              'STAXI11[STAXI16]','STAXI11[STAXI17]','STAXI11[STAXI18]','STAXI11[STAXI19]','STAXI11[STAXI20]','STAXI21[STAXI21]','STAXI21[STAXI22]','STAXI21[STAXI23]',
              'STAXI21[STAXI24]','STAXI21[STAXI25]','STAXI21[STAXI26]','STAXI21[STAXI27]','STAXI21[STAXI28]','STAXI21[STAXI29]','STAXI21[STAXI30]','STAXI21[STAXI31]',
              'STAXI21[STAXI32]','STAXI21[STAXI33]','STAXI34[STAXI34]','STAXI34[STAXI35]','STAXI34[STAXI36]','STAXI34[STAXI37]','STAXI34[STAXI38]','STAXI34[STAXI39]',
              'STAXI34[STAXI40]','STAXI34[STAXI41]','STAXI34[STAXI42]','STAXI34[STAXI43]','STAXI34[STAXI44]']

        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] + ["anger_trait", "anger_inward", "anger_outward", "anger_control"]            
        df[cols_export].to_csv('%s/quest_STAXI_44.csv' % out_dir, index=False)
      


##############################################################################
#################### Gender Identitiy Questionnaire ##########################
##############################################################################

def run_GIQ(df, out_dir=None):
    
    if out_dir:
        
        d = {'MGQ11BASEQ[MGQ11]': '11',
             'MGQ11BASEQ[MGQ12]': '12',
             'MGQ11BASEQ[MGQ13]': '13',
             'MGQ11BASEQ[MGQ14]': '14',
             'MGQ11BASEQ[MGQ15]': '15',
             'MGQ11BASEQ[MGQ16]': '16',
             'MGQ11BASEQ[MGQ17]': '17',
             'MGQ11BASEQ[MGQ18]': '18',
             'MGQ11BASEQ[MGQ19]': '19',
             'MGQ1BASEQ[MGQ1]': '1',
             'MGQ1BASEQ[MGQ2]': '2',
             'MGQ20BASEQ[MGQ20]': '20',
             'MGQ21BASEQ[MGQ21]': '21',
             'MGQ22BASEQ[MGQ22]': '22',
             'MGQ22BASEQ[MGQ23]': '23',
             'MGQ24BASEQ[MGQ24]': '24',
             'MGQ25BASEQ[MGQ25]': '25',
             'MGQ25BASEQ[MGQ26]': '26',
             'MGQ27BASEQ[MGQ27]': '27',
             'MGQ27BASEQ[MGQ28]': '28',
             'MGQ29BASEQ[MGQ29]': '29',
             'MGQ29BASEQ[MGQ30]': '30',
             'MGQ31BASEQ[MGQ31]': '31',
             'MGQ31BASEQ[MGQ32]': '32',
             'MGQ33': '33',
             'MGQ33[other]': '33.B',
             'MGQ34': '34',
             'MGQ34[comment]': '34.B',
             'MGQ35': '34.C',
             'MGQ36': '34.D',
             'MGQ37': '35',
             'MGQ37[comment]': '35.B',
             'MGQ38': '36',
             'MGQ39': '37',
             'MGQ3BASEQ[MGQ10]': '10',
             'MGQ3BASEQ[MGQ3]': '3',
             'MGQ3BASEQ[MGQ4]': '4',
             'MGQ3BASEQ[MGQ5]': '5',
             'MGQ3BASEQ[MGQ6]': '6',
             'MGQ3BASEQ[MGQ7]': '7',
             'MGQ3BASEQ[MGQ8]': '8',
             'MGQ3BASEQ[MGQ9]': '9',
             'MGQ40': '38',
             'MGQ41': '39',
             'MGQ42': '40',
             'MGQ43BASEQ[MGQ431]': '41.A',
             'MGQ43BASEQ[MGQ432]': '41.B',
             'MGQ43BASEQ[MGQ433]': '41.C',
             'MGQ43BASEQ[MGQ434]': '41.D',
             'MGQ43BASEQ[MGQ435]': '41.E',
             'MGQ43BASEQ[MGQ436]': '41.F',
             'MGQ43BASEQ[MGQ437]': '41.G',
             'MGQ43BASEQ[MGQ438]': '41.H',
             'MGQ43BASEQ[MGQ439]': '41.I',
             'MGQ43BASEQ[other]': '41.J',
             'MGQ44BASEQ[MGQ44]': '42',
             'MGQ44BASEQ[MGQ45]': '43',
             'MGQ46': '44',
             'MGQ46[other]': '44.B',
             'MGQ47': '45',
             'MGQ48': '46',
             'MGQ48[other]': '46.B',
             'MGQ49BASEQ[MGQ49a]': '47.A',
             'MGQ49BASEQ[MGQ49b]': '47.B',
             'MGQ49BASEQ[MGQ49c]': '47.C',
             'MGQ49BASEQ[MGQ49d]': '47.D',
             'MGQ49BASEQ[MGQ49e]': '47.E',
             'MGQ49BASEQ[MGQ49f]': '47.F',
             'MGQ49BASEQ[MGQ49g]': '47.G',
             'MGQ49BASEQ[MGQ49h]': '47.H',
             'MGQ49BASEQ[MGQ49i]': '47.I',
             'MGQ49BASEQ[MGQ49j]': '47.J',
             'MGQ49BASEQ[MGQ49k]': '47.K',
             'MGQ49BASEQ[MGQ49l]': '47.L',
             'MGQ49BASEQ[other]': '47.M',
             'MGQ50BASEQ[MGQ50]': '48',
             'MGQ50BASEQ[MGQ51]': '49',
             'MGQ52BASEQ[MGQ52]': '50',
             'MGQ52BASEQ[MGQ53]': '51',
             'MGQ52BASEQ[MGQ54]': '52',
             'MGQ52BASEQ[MGQ55]': '53',
             'MGQ52BASEQ[MGQ56]': '54',
             'MGQ52BASEQ[MGQ57]': '55',
             'MGQ52BASEQ[MGQ58]': '56',
             'MGQ52BASEQ[MGQ59]': '57',
             'MGQ52BASEQ[MGQ60]': '58',
             'MGQ52BASEQ[MGQ61]': '59',
             'MGQ62BASEQ[MGQ62]': '60',
             'MGQ62BASEQ[MGQ63]': '61',
             'MGQ62BASEQ[MGQ64]': '62',
             'MGQ62BASEQ[MGQ65]': '63',
             'MGQ62BASEQ[MGQ66]': '64',
             'MGQ62BASEQ[MGQ67]': '65',
             'MGQ62BASEQ[MGQ68]': '66',
             'MGQ62BASEQ[MGQ69]': '67',
             'MGQ62BASEQ[MGQ70]': '68',
             'MGQ62BASEQ[MGQ71]': '69',
             'MGQ62BASEQ[MGQ72]': '70',
             'MGQ73BASEQ[MGQ73]': '71',
             'MGQ73BASEQ[MGQ74]': '72',
             'MGQ73BASEQ[MGQ75]': '73',
             'MGQ73BASEQ[MGQ76]': '74',
             'MGQ73BASEQ[MGQ77]': '75',
             'MGQ73BASEQ[MGQ78]': '76',
             'MGQ73BASEQ[MGQ79]': '77',
             'MGQ73BASEQ[MGQ80]': '78',
             'MGQ73BASEQ[MGQ81]': '79',
             'MGQ73BASEQ[MGQ82]': '80',
             'MGQ73BASEQ[MGQ83]': '81',
             'MGQ84BASEQ[MGQ84]': '82',
             'MGQ85BASEQ[MGQ85]': '83',
             'MGQ85BASEQ[MGQ86]': '84',
             'MGQ85BASEQ[MGQ87]': '85',
             'MGQ88BASEQ[MGQ88]': '86',
             'MGQ89BASEQ[MGQ89]': '87',
             'MGQ89BASEQ[MGQ90]': '88',
             'MGQ89BASEQ[MGQ91]': '89',
             'MGQ89BASEQ[MGQ92]': '90',
             'MGQ89BASEQ[MGQ93]': '91',
             'MGQ89BASEQ[MGQ94]': '92',
             'MGQ89BASEQ[MGQ95]': '93',
             'MGQ96BASEQ[MGQ100]': '98',
             'MGQ96BASEQ[MGQ101]': '99',
             'MGQ96BASEQ[MGQ102]': '100',
             'MGQ96BASEQ[MGQ96]': '94',
             'MGQ96BASEQ[MGQ97]': '95',
             'MGQ96BASEQ[MGQ98]': '96',
             'MGQ96BASEQ[MGQ99]': '97'}
             
        item_order = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14',
                      '15','16','17','18','19','20','21','22','23','24','25','26',
                      '27','28','29','30','31','32','33','33.B','34','34.B','34.C',
                      '34.D','35','35.B','36','37','38','39','40','41.A','41.B',
                      '41.C','41.D','41.E','41.F','41.G','41.H','41.I','41.J','42',
                      '43','44','44.B','45','46','46.B','47.A','47.B','47.C','47.D',
                      '47.E','47.F','47.G','47.H','47.I','47.J','47.K','47.L','47.M',
                      '48','49','50','51','52','53','54','55','56','57','58','59',
                      '60','61','62','63','64','65','66','67','68','69','70','71',
                      '72','73','74','75','76','77','78','79','80','81','82','83',
                      '84','85','86','87','88','89','90','91','92','93','94','95',
                      '96','97','98','99','100']
    
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=d, inplace=True)
        cols_export = ['ids'] + item_order 
        df[cols_export].to_csv('%s/quest_MGIQ_100.csv' % out_dir, index=False)  



##############################################################################
############################## Type D Scale-14 ###############################
##############################################################################

def run_DS14(df, out_dir=None):
    
    cols = ['DS14BASEQ[1]', 'DS14BASEQ[2]', 'DS14BASEQ[3]', 'DS14BASEQ[4]',
            'DS14BASEQ[5]', 'DS14BASEQ[6]', 'DS14BASEQ[7]', 'DS14BASEQ[8]',
            'DS14BASEQ[9]', 'DS14BASEQ[10]', 'DS14BASEQ[11]', 'DS14BASEQ[12]',
            'DS14BASEQ[13]', 'DS14BASEQ[14]']
        
    if out_dir:
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] 
        df[cols_export].to_csv('%s/quest_DS_14.csv' % out_dir, index=False)  



##############################################################################
#################### childhood trauma questionnaire ##########################
##############################################################################

def run_CTQ(df, out_dir=None):
    
    cols = ['ChildTraum1BASE[1]', 'ChildTraum1BASE[2]', 'ChildTraum1BASE[3]',
           'ChildTraum1BASE[4]', 'ChildTraum1BASE[5]', 'ChildTraum1BASE[6]',
           'ChildTraum1BASE[7]', 'ChildTraum1BASE[8]', 'ChildTraum1BASE[9]',
           'ChildTraum2BASE[10]', 'ChildTraum2BASE[11]', 'ChildTraum2BASE[12]',
           'ChildTraum2BASE[13]', 'ChildTraum2BASE[14]', 'ChildTraum2BASE[15]',
           'ChildTraum2BASE[16]', 'ChildTraum2BASE[17]', 'ChildTraum2BASE[18]',
           'ChildTraum3BASE[19]', 'ChildTraum3BASE[20]', 'ChildTraum3BASE[21]',
           'ChildTraum3BASE[22]', 'ChildTraum3BASE[23]', 'ChildTraum3BASE[24]',
           'ChildTraum3BASE[25]', 'ChildTraum3BASE[26]', 'ChildTraum3BASE[27]',
           'ChildTraum3BASE[28]']
        
    if out_dir:
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] 
        df[cols_export].to_csv('%s/quest_CTQ_28.csv' % out_dir, index=False)
        
        

##############################################################################
######################## LIMIT - NYC-Q post scan #############################
##############################################################################
        
def run_NYCQ_postscan(df, out_dir=None):
    
    cols = ['Q01', 'Q02', 'Q03', 'Q04', 'Q05', 'Q06', 'Q07', 'Q08', 
            'Q09', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16',
            'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22', 'Q23', 'Q24', 
            'Q25', 'Q26', 'Q27', 'Q28', 'Q29', 'Q30', 'Q31']
        
    if out_dir:
        df['ids'] = df['DB-ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] 
        df[cols_export].to_csv('%s/quest_NYC-Q_31_postscan.csv' % out_dir, index=False)
        
        
        
##############################################################################
######################## LIMIT - NYC-Q  in Survey C ##########################
##############################################################################
        
def run_NYCQ_posttasks(df, out_dir=None):
    
    cols = ['LMTaBASEQ[LMT1]', 'LMTaBASEQ[LMT2]', 'LMTaBASEQ[LMT3]',
           'LMTaBASEQ[LMT4]', 'LMTaBASEQ[LMT5]', 'LMTaBASEQ[LMT6]',
           'LMTaBASEQ[LMT7]', 'LMTaBASEQ[LMT8]', 'LMTaBASEQ[LMT9]',
           'LMTaBASEQ[LMT10]', 'LMTbBASEQ[LMT11]', 'LMTbBASEQ[LMT12]',
           'LMTbBASEQ[LMT13]', 'LMTbBASEQ[LMT14]', 'LMTbBASEQ[LMT15]',
           'LMTbBASEQ[LMT16]', 'LMTbBASEQ[LMT17]', 'LMTbBASEQ[LMT18]',
           'LMTcBASEQ[LMT19]', 'LMTcBASEQ[LMT20]', 'LMTcBASEQ[LMT21]',
           'LMTcBASEQ[LMT22]', 'LMTcBASEQ[LMT23]']
        
    if out_dir:
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] 
        df[cols_export].to_csv('%s/quest_NYC-Q_23_posttasks.csv' % out_dir, index=False)          
        
        
        
##############################################################################
##################### short NYC-Q post emotional task switching ##############
##############################################################################                
        
def run_NYCQ_postemoswitch(df, out_dir=None):
    
    cols = ['1,00', '2,00', '3,00', '4,00','5,00', '6,00', 
            '7,00', '8,00', '9,00', '10,00', '11,00', '12,00']
            
    drops = df[(df['1'] == '99')
             & (df['2'] == '99')
             & (df['3'] == '99')
             & (df['4'] == '99')
             & (df['5'] == '99')
             & (df['6'] == '99')
             & (df['7'] == '99')
             & (df['8'] == '99')].index

    df.drop(df.index[drops], inplace=True)
    df.reset_index(inplace=True, drop=True)
    
    for col in cols:
        df[col].replace('651,32', '', inplace=True)
    
    if out_dir:
        df['ids'] = df['DB-ID'].map(lambda x: str(x)[0:5])
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] 
        df[cols_export].to_csv('%s/quest_Short-NYC-Q_12_postETS.csv' % out_dir, index=False)

        

##############################################################################
############################## Facebook Intensity#############################
##############################################################################

def run_FIS(df, out_dir=None):
    
    cols = ["FACE0BASEQ","FACE1aBASEQ","FACE1bBASEQ","FACE2aBASEQ",
            "FACE2bBASEQ","FACE3BASEQ","FACE4BASEQ[FACE4]","FACE4BASEQ[FACE5]",
            "FACE4BASEQ[FACE6]","FACE4BASEQ[FACE7]","FACE4BASEQ[FACE8]",
            "FACE4BASEQ[FACE9]"]
        
    if out_dir:
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] 
        df[cols_export].to_csv('%s/quest_FBI_12.csv' % out_dir, index=False)  



##############################################################################
############################ mobile phone usage ###############################
##############################################################################

def run_mobile(df, out_dir=None):
    
    cols = ['HND1', 'HND2', 'HND3', 'HND4', 'HND5', 'HND6', 'HND7', 'HND8', 
            'HND9', 'HND10', 'HND11', 'HND12', 'HND13', 'HND14', 'HND15', 
            'HND16', 'HND17', 'HND18', 'HND19']
        
    if out_dir:
        df['ids'] = df['ID'].map(lambda x: str(x)[0:5])        
        df.rename(columns=dict(zip(cols, [x+1 for x in range(len(cols))])), inplace=True)
        cols_export = ['ids'] + [x+1 for x in range(len(cols))] 
        df[cols_export].to_csv('%s/quest_MPU_19.csv' % out_dir, index=False)  