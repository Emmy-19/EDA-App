import streamlit as st
import pandas as pd
import numpy as np
import base64

# Pandas Utilitys

@st.cache     
def pd_of_stats(df,col):
    #Descriptive Statistics
    stats = dict()
    stats['Mean']  = df[col].mean()
    stats['Std']   = df[col].std()
    stats['Var'] = df[col].var()
    stats['Kurtosis'] = df[col].kurtosis()
    stats['Skewness'] = df[col].skew()
    stats['Coefficient Variance'] = stats['Std'] / stats['Mean']
    return pd.DataFrame(stats, index = col).T.round(2)

@st.cache   
def pd_of_info(df,col):
    info = dict()
    info['Type'] =  df[col].dtypes
    info['Unique'] = df[col].nunique()
    info['n_zeros'] = (len(df) - np.count_nonzero(df[col]))
    info['p_zeros'] = round(info['n_zeros'] * 100 / len(df),2)
    info['nan'] = df[col].isna().sum()
    info['p_nan'] =  (df[col].isna().sum() / df.shape[0]) * 100
    return pd.DataFrame(info, index = col).T.round(2)

@st.cache     
def pd_of_stats_quantile(df,col):
    df_no_na = df[col].dropna()
    stats_q = dict()

    stats_q['Min'] = df[col].min()
    label = {0.25:"Q1", 0.5:'Median', 0.75:"Q3"}
    for percentile in np.array([0.25, 0.5, 0.75]):
        stats_q[label[percentile]] = df_no_na.quantile(percentile)
    stats_q['Max'] = df[col].max()
    stats_q['Range'] = stats_q['Max']-stats_q['Min']
    stats_q['IQR'] = stats_q['Q3']-stats_q['Q1']
    return pd.DataFrame(stats_q, index = col).T.round(2)    

@st.cache
def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href


@st.cache     
def pd_of_stats(df,col):
    #Descriptive Statistics
    stats = dict()
    stats['Mean']  = df[col].mean()
    stats['Std']   = df[col].std()
    stats['Var'] = df[col].var()
    stats['Kurtosis'] = df[col].kurtosis()
    stats['Skewness'] = df[col].skew()
    stats['Coefficient Variance'] = stats['Std'] / stats['Mean']
    return pd.DataFrame(stats, index = col).T.round(2)

@st.cache   
def pf_of_info(df,col):
    info = dict()
    info['Type'] =  df[col].dtypes
    info['Unique'] = df[col].nunique()
    info['n_zeros'] = (len(df) - np.count_nonzero(df[col]))
    info['p_zeros'] = round(info['n_zeros'] * 100 / len(df),2)
    info['nan'] = df[col].isna().sum()
    info['p_nan'] =  (df[col].isna().sum() / df.shape[0]) * 100
    return pd.DataFrame(info, index = col).T.round(2)

@st.cache     
def pd_of_stats_quantile(df,col):
    df_no_na = df[col].dropna()
    stats_q = dict()

    stats_q['Min'] = df[col].min()
    label = {0.25:"Q1", 0.5:'Median', 0.75:"Q3"}
    for percentile in np.array([0.25, 0.5, 0.75]):
        stats_q[label[percentile]] = df_no_na.quantile(percentile)
    stats_q['Max'] = df[col].max()
    stats_q['Range'] = stats_q['Max']-stats_q['Min']
    stats_q['IQR'] = stats_q['Q3']-stats_q['Q1']
    return pd.DataFrame(stats_q, index = col).T.round(2)    

@st.cache
def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href