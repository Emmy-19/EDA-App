import streamlit as st
import pandas as pd
import numpy as np

from pd_utils import *

# Utility Functions

# passing file into  
def get_data(file):   
    read_cache_csv = st.cache(pd.read_csv, allow_output_mutation = True)
    df = read_cache_csv(file)
    return df

@st.cache
def get_stats(df):
    stats_num = df.describe()
    if df.select_dtypes(np.object).empty :
        return stats_num.transpose(), None
    if df.select_dtypes(np.number).empty :
        return None, df.describe(include=np.object).transpose()
    else:
        return stats_num.transpose(), df.describe(include=np.object).transpose()

@st.cache
def get_info(df):
    return pd.DataFrame({'types': df.dtypes, 'nan': df.isna().sum(), 'nan%': round((df.isna().sum()/len(df))*100,2), 'unique':df.nunique()})

@st.cache
def get_na_info(df_preproc, df, col):
    raw_info = pd_of_stats(df, col)
    prep_info = pd_of_stats(df_preproc,col)
    return raw_info.join(prep_info, lsuffix= '_raw', rsuffix='_prep').T
