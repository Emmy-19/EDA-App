import streamlit as st
import numpy as np

from utils import *
from eda_main import EDA
from plot_multivariate import *
from plot_univariate import *

def main():

    st.title('Perform Your Data Analysis :mag:')
    st.header('Analyze the descriptive statistics and the distribution of your data. Preview and save your graphics.')
    
    file  = st.file_uploader('Upload your file (.csv)', type = 'csv')
 
    if file is not None:
        
        df = get_data(file)

        numeric_features = df.select_dtypes(include=[np.number]).columns
        categorical_features = df.select_dtypes(include=[np.object]).columns

        def basic_info(df):
            st.header("Data")
            st.write('Number of observations', df.shape[0]) 
            st.write('Number of variables', df.shape[1])
            st.write('Number of missing (%)',((df.isna().sum().sum()/df.size)*100).round(2))

        #Visualize data
        basic_info(df)
        
        #Sidebar Menu
        options = ["View statistics", "Statistic univariate", "Statistic multivariate"]
        menu = st.sidebar.selectbox("Menu options", options)
        
        

        #Data statistics
        df_info = get_info(df)   
        if (menu == "View statistics"):
            df_stat_num, df_stat_obj = get_stats(df)
            st.markdown('**Numerical summary**')
            st.table(df_stat_num)
            st.markdown('**Categorical summary**')
            st.table(df_stat_obj)
            st.markdown('**Missing Values**')
            st.table(df_info)

        eda_plot = EDA(df) 

        # Visualize data

        if (menu =="Statistic univariate" ):
            st.header("Statistic univariate")
            st.markdown("Provides summary statistics of only one variable in the raw dataset.")
            main_var = st.selectbox("Choose one variable to analyze:", df.columns.insert(0,None))

            if main_var in numeric_features:
                if main_var != None:
                    st.subheader("Variable info")
                    st.table(pf_of_info(df, [main_var]).T)
                    st.subheader("Descriptive Statistics")
                    st.table((pd_of_stats(df, [main_var])).T)
                    st.subheader("Quantile Statistics") 
                    st.table((pd_of_stats_quantile(df, [main_var])).T) 
                    
                    chart_univariate = st.sidebar.radio('Chart', ('None','Histogram', 'BoxPlot', 'Distribution Plot'))
                    
                    plot_univariate(eda_plot, main_var, chart_univariate)

            if main_var in categorical_features:
                st.table(df[main_var].describe(include = np.object))
                st.bar_chart(df[main_var].value_counts().to_frame())

            st.sidebar.subheader("Explore other categorical variables!")
            var = st.sidebar.selectbox("Check its unique values and its frequency:", df.columns.insert(0,None))
            if var !=None:
                aux_chart = df[var].value_counts(dropna=False).to_frame()
                data = st.sidebar.table(aux_chart.style.bar(color='#3d66af'))

        if (menu =="Statistic multivariate" ):
            st.header("Statistic multivariate")

            st.markdown('Here you can visualize your data by choosing one of the chart options available on the sidebar!')
               
            st.sidebar.subheader('Data visualization options')
            radio_plot = st.sidebar.radio('Choose plot style', ('Correlation', 'Boxplot', 'Violin', 'Swarmplot', 'Heatmap', 'Histogram', \
                'Scatterplot', 'Countplot', 'Barplot', 'Lineplot'))

            plot_multivariate(eda_plot, radio_plot)


if __name__ == '__main__':
    main()