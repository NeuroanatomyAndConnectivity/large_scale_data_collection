# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:18:21 2015

@author: jgolchert
"""

 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

            
##############################################################################            
################################# TMT ########################################
##############################################################################

def run_TMT(df):
     
     #TMT A numbers: seconds
     print 'TMT_A: numbers: seconds'
     
     TMT_A_numb_sec = df['TMT_A_numbers_seconds'][:200]
     TMT_A_numb_sec = TMT_A_numb_sec.astype(float64)
     print TMT_A_numb_sec.describe()
     
     TMT_A_numb_sec = list(TMT_A_numb_sec.dropna())
     sns.distplot(TMT_A_numb_sec, kde = True, label = 'TMT_A')
     plt.xlabel('TMT_A_sec', fontsize = 14)

     
     #TMT A numbers: errors   
     print '\n' 'TMT_A: numbers: errors'
     
     TMT_A_numb_err = df['TMT_A_numbers_errors'][:200]
     
     print TMT_A_numb_err.describe()
     
     TMT_A_numb_err = list(TMT_A_numb_err.dropna())
     count = 0
     for err in TMT_A_numb_err:
         if err > 0:
             count = count + 1
     print 'at least one error: N = %s' %count    
     
     
     
     #TMT_B_numbers_letters:seconds
     print '\n', 'TMT_B: Numbers-Letters: seconds'   
     
     TMT_B_sec = df['TMT_B_numbersletters_seconds'][:200]
     TMT_B_sec = TMT_B_sec.astype(float64)
     print TMT_B_sec.describe()
     
     TMT_B_sec = list(TMT_B_sec.dropna())
     sns.distplot(TMT_B_sec, kde = True, label = 'TMT_B')
     plt.xlabel('sec', fontsize = 14)
     
    #TMT B: errors 
     print '\n' 'TMT_B: Numbers-Letters: errors'
     
     TMT_B_err = df['TMT_B_numbersletters_errors'][:200]
     
     print TMT_B_err.describe()
     
     TMT_B_err = list(TMT_B_err.dropna())
     count = 0
     for err in TMT_B_err:
         if err > 0:
             count = count + 1
     print 'at least one error: N = %s' %count       
     
     

##############################################################################      
########################## Wortschatztest ####################################
############################################################################## 

def run_WST(df):
    
    print 'Measure of verbal intelligence: Task: find real words; Max = 42'
    print '\n', 'WST raw scores'
    
    WST_RW = df['WST_RW'][:200] 
    print WST_RW.describe()
    
    WST_RW = list(WST_RW.dropna())
    sns.distplot(WST_RW, kde = True)
    
    

##############################################################################     
##################### Leistungsprüfsystem Subtest 3 ########################## 
############################################################################## 
    
def run_LPS(df):
    
    print 'Measure of reasoning: Task: find correct symbol; Max = 40'
    print '\n', 'LPS raw scores'
    
    LPS_RW = df['LPS_RW'][:200] 
    print LPS_RW.describe()
    
    LPS_RW = list(LPS_RW.dropna())
    sns.distplot(LPS_RW, kde = True)
    


##############################################################################     
################ Regensburger Wortflüssigkeitstest ########################### 
############################################################################## 

def run_RWT(df):
    
    print "measures verbal fluency: Task: find as many words as you can from a category or with a certain letter"
    
    ####s words    
    print '\n', "S-words: Raw scores: sum across 2 minutes"
    
    RWT_words_sum = df['Wörter_Summe_min'][:200]

    print RWT_words_sum.describe()
    
    RWT_words_sum = list(RWT_words_sum.dropna())
    sns.distplot(RWT_words_sum, kde = True) 
    
    #Repetitions s-words  
    print '\n' 'Repetitions S-words across 2 minutes'
     
    RWT_words_rep = df['Wörter_Summe_R'][:200]
     
    print RWT_words_rep.describe()
     
    RWT_words_rep = list(RWT_words_rep.dropna())
    count = 0
    for rep in RWT_words_rep:
        if rep > 0:
            count = count + 1
    print 'at least one rep: N(subjects) = %s' %count 
    
    
    #rule books
    print '\n' 'rule books s-words'
    
    RWT_words_rules = df['Wörter_Summe_RB'][:200]
     
    print RWT_words_rules.describe()
     
    RWT_words_rules = list(RWT_words_rules.dropna())
    count = 0
    for rules in RWT_words_rules:
        if rules > 0:
            count = count + 1
    print 'at least one rule book: N(subjects) = %s' %count 
 
    
    ###animals### 
    print '\n', "ANIMALS: Raw scores: sum across 2 minutes"
    
    RWT_animals_sum = df['Tiere_Summe_min'][:200]

    print RWT_animals_sum.describe()
    
    RWT_animals_sum = list(RWT_animals_sum.dropna())
    sns.distplot(RWT_animals_sum, kde = True) 
    plt.xlabel('number of words', fontsize = 14)
    
    #Repetitions animal-words  
    print '\n' 'Repetitions animal-words across 2 minutes'
     
    RWT_animals_rep = df['Tiere_Summe_R'][:200]
     
    print RWT_animals_rep.describe()
     
    RWT_animals_rep = list(RWT_animals_rep.dropna())
    count = 0
    for rep in RWT_animals_rep:
        if rep > 0:
            count = count + 1
    print 'at least one rep: N(subjects) = %s' %count 
    
    
    #rule books animals
    print '\n' 'rule books animals-words'
    
    RWT_animals_rules = df['Tiere_Summe_RB'][:200]
     
    print RWT_animals_rules.describe()
     
    RWT_animals_rules = list(RWT_animals_rules.dropna())
    count = 0
    for rules in RWT_animals_rules:
        if rules > 0:
            count = count + 1
    print 'at least one rule book: N(subjects) = %s' %count 
    
 

##############################################################################    
############################# TAP Alertness ##################################
############################################################################## 
    
#Tap Alertness

def run_TAP_alertness(df):
    
    print '\n' 'Task: press button when target stim appears on screen; two conditions: with and without prime (tone)'
    print 'two runs for each condition'
    
    print '\n\n' 'ALERT: condition without signal - mean RTs'

    Alert_no_sig_Mean = df['Alert_no_sig_Mean'][:200]
    print Alert_no_sig_Mean.describe()
    
    Alert_no_sig_Mean = list(Alert_no_sig_Mean.dropna())
    sns.distplot(Alert_no_sig_Mean, kde = True)    
    
    
    ### condition with signal
    print '\n' 'ALERT: condition with signal - mean RTs'
    
    Alert_sig_Mean = df['Alert_sig_Mean'][:200]
    print Alert_sig_Mean.describe()
    
    Alert_sig_Mean = list(Alert_sig_Mean.dropna())
    sns.distplot(Alert_sig_Mean, kde = True) 
    plt.xlabel('Mean_RTs', fontsize = 14)
    


############################################################################## 
########################## TAP incompat ######################################
############################################################################## 
    
def run_TAP_incompat(df):
    
    print '\n' 'Task: button press left/right depending on which side an arrow points (ignore on which side target appears)'
    print 'two runs for each condition - congruent/incongruent'    
    
    #congruent cond
    print '\n\n' 'INCOMPAT: congruent - mean RTs' 
    
    compat_Mean = df['compat_Mean'][:200]
    print compat_Mean.describe()
    
    compat_Mean = list(compat_Mean.dropna())
    sns.distplot(compat_Mean, kde = True) 
    
    
    # incongruent cond
    print '\n\n' 'INCOMPAT: incongruent - mean RTs'
    
    incompat_Mean = df['Incompat_Mean'][:200]
    print incompat_Mean.describe()    
    
    incompat_Mean = list(incompat_Mean.dropna())
    sns.distplot(incompat_Mean, kde = True)     
    plt.xlabel('Mean_RTs', fontsize = 14)
    

############################################################################## 
########################## TAP WM ############################################
############################################################################## 
    
def run_TAP_WM(df):
    
    print '\n' 'Task: button press if a number is equal to the second last number (numbers 1-9)'
    
    print '\n\n' 'Mean RTs'
    WM_means_ms = df['WM_Mean_ms'][:200]
    print WM_means_ms.describe()
    
    WM_means_ms = list(WM_means_ms.dropna())
    sns.distplot(WM_means_ms, kde = True)     
    plt.xlabel('Mean_RTs', fontsize = 14)



