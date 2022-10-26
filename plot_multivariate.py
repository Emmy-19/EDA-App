import streamlit as st
import numpy as np


def plot_multivariate(obj_plot, radio_plot):

    if radio_plot == ('Boxplot'):
        st.subheader('Boxplot')
        col_y  = st.sidebar.selectbox("Choose main variable (numerical)",obj_plot.num_vars, key ='boxplot')
        col_x  = st.sidebar.selectbox("Choose x variable (categorical) optional", obj_plot.columns.insert(0,None), key ='boxplot')
        hue_opt = st.sidebar.selectbox("Hue (categorical) optional", obj_plot.columns.insert(0,None), key ='boxplot')
        if st.sidebar.button('Plot boxplot chart'):
            st.plotly_chart(obj_plot.box_plot(col_y,col_x, hue_opt))
    
    if radio_plot == ('Violin'):
        st.subheader('Violin')
        col_y  = st.sidebar.selectbox("Choose main variable (numerical)",obj_plot.num_vars, key='violin')
        col_x  = st.sidebar.selectbox("Choose x variable (categorical) optional", obj_plot.columns.insert(0,None),key='violin')
        hue_opt = st.sidebar.selectbox("Hue (categorical) optional", obj_plot.columns.insert(0,None),key='violin')
        split = st.sidebar.checkbox("Split",key='violin')
        if st.sidebar.button('Plot violin chart'):
            fig = obj_plot.violin(col_y,col_x, hue_opt, split)
            st.pyplot()
    
    if radio_plot == ('Swarmplot'):
        st.subheader('Swarmplot')
        col_y = st.sidebar.selectbox("Choose main variable (numerical)",obj_plot.num_vars, key='swarmplot')
        col_x = st.sidebar.selectbox("Choose x variable (categorical) optional", obj_plot.columns.insert(0,None),key='swarmplot')
        hue_opt = st.sidebar.selectbox("Hue (categorical) optional", obj_plot.columns.insert(0,None),key='swarmplot')
        split = st.sidebar.checkbox("Split", key ='swarmplot')
        if st.sidebar.button('Plot swarmplot chart'):
            fig = obj_plot.swarmplot(col_y,col_x, hue_opt, split)
            st.pyplot()

    def pretty(method):
        return method.capitalize()

    if radio_plot == ('Correlation'):
        st.subheader('Heatmap Correlation Plot')
        correlation = st.sidebar.selectbox("Choose the correlation method", ('pearson', 'kendall','spearman'), format_func=pretty)
        cols_list = st.sidebar.multiselect("Select columns",obj_plot.columns)
        st.sidebar.markdown("If None selected, it will plot the correlation of all numeric variables.")
        if st.sidebar.button('Plot heatmap chart'):
            fig = obj_plot.Corr(cols_list, correlation)
            st.pyplot()

    def map_func(function):
        dic = {np.mean:'Mean', np.sum:'Sum', np.median:'Median'}
        return dic[function]
    
    if radio_plot == ('Heatmap'):
        st.subheader('Heatmap between vars')
        st.markdown(" In order to plot this chart remember that the order of the selection matters, \
            chooose in order the variables that will build the pivot table: row, column and value.")
        cols_list = st.sidebar.multiselect("Select 3 variables (2 categorical and 1 numeric)",obj_plot.columns, key= 'heatmapvars')
        agg_func = st.sidebar.selectbox("Choose one function to aggregate the data", (np.mean, np.sum, np.median), format_func=map_func)
        if st.sidebar.button('Plot heatmap between vars'):
            fig = obj_plot.heatmap_vars(cols_list, agg_func)
            st.pyplot()
    
    if radio_plot == ('Histogram'):
        st.subheader('Histogram')
        col_hist = st.sidebar.selectbox("Choose main variable", obj_plot.num_vars, key = 'hist')
        hue_opt = st.sidebar.selectbox("Hue (categorical) optional",obj_plot.columns.insert(0,None), key = 'hist')
        bins_, range_ = None, None
        bins_ = st.sidebar.slider('Number of bins optional', value = 30)
        range_ = st.sidebar.slider('Choose range optional', int(obj_plot.df[col_hist].min()), int(obj_plot.df[col_hist].max()),\
                (int(obj_plot.df[col_hist].min()),int(obj_plot.df[col_hist].max())))    
        if st.sidebar.button('Plot histogram chart'):
                st.plotly_chart(obj_plot.histogram_num(col_hist, hue_opt, bins_, range_))

    if radio_plot == ('Scatterplot'): 
        st.subheader('Scatter plot')
        col_x = st.sidebar.selectbox("Choose x variable (numerical)", obj_plot.num_vars, key = 'scatter')
        col_y = st.sidebar.selectbox("Choose y variable (numerical)", obj_plot.num_vars, key = 'scatter')
        hue_opt = st.sidebar.selectbox("Hue (categorical) optional", obj_plot.columns.insert(0,None), key = 'scatter')
        size_opt = st.sidebar.selectbox("Size (numerical) optional",obj_plot.columns.insert(0,None), key = 'scatter')
        if st.sidebar.button('Plot scatter chart'):
            st.plotly_chart(obj_plot.scatter_plot(col_x,col_y, hue_opt, size_opt))

    if radio_plot == ('Countplot'):
        st.subheader('Count Plot')
        col_count_plot = st.sidebar.selectbox("Choose main variable",obj_plot.columns, key = 'countplot')
        hue_opt = st.sidebar.selectbox("Hue (categorical) optional",obj_plot.columns.insert(0,None), key = 'countplot')
        if st.sidebar.button('Plot Countplot'):
            fig = obj_plot.CountPlot(col_count_plot, hue_opt)
            st.pyplot()
    
    if radio_plot == ('Barplot'):
        st.subheader('Barplot') 
        col_y = st.sidebar.selectbox("Choose main variable (numerical)",obj_plot.num_vars, key='barplot')
        col_x = st.sidebar.selectbox("Choose x variable (categorical)", obj_plot.columns,key='barplot')
        hue_opt = st.sidebar.selectbox("Hue (categorical/numerical) optional", obj_plot.columns.insert(0,None),key='barplot')
        if st.sidebar.button('Plot barplot chart'):
            st.plotly_chart(obj_plot.bar_plot(col_y,col_x, hue_opt))

    if radio_plot == ('Lineplot'):
        st.subheader('Lineplot') 
        col_y = st.sidebar.selectbox("Choose main variable (numerical)",obj_plot.num_vars, key='lineplot')
        col_x = st.sidebar.selectbox("Choose x variable (categorical)", obj_plot.columns,key='lineplot')
        hue_opt = st.sidebar.selectbox("Hue (categorical) optional", obj_plot.columns.insert(0,None),key='lineplot')
        group = st.sidebar.selectbox("Group color (categorical) optional", obj_plot.columns.insert(0,None),key='lineplot')
        if st.sidebar.button('Plot lineplot chart'):
            st.plotly_chart(obj_plot.line_plot(col_y,col_x, hue_opt, group))
