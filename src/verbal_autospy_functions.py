##load the necessary python modules
#--------------------
import pandas as pd
df=pd.read_csv('/Users/Yanfen/Documents/verbal_autopsy_analysis/data/IHME_PHMRC_VA_DATA_ADULT_Y2013M09D11_0.csv',low_memory=False)

def count_per_word(df,word):
    piv = pd.pivot_table(df, values=word,index=['site'], columns=['gs_text34'],aggfunc=sum)
    return piv

