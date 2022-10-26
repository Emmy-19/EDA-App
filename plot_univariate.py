import streamlit as st

def plot_univariate(obj_plot, main_var, radio_plot_uni):
    
    if radio_plot_uni == 'Histogram' :
        st.subheader('Histogram')
        bins, range_ = None, None
        hue_opt = st.sidebar.selectbox("Hue (categorical) optional",obj_plot.columns.insert(0,None))
        bins_ = st.sidebar.slider('Number of bins optional', value = 50)
        range_ = st.sidebar.slider('Choose range optional', float(obj_plot.df[main_var].min()), \
            float(obj_plot.df[main_var].max()),(float(obj_plot.df[main_var].min()),float(obj_plot.df[main_var].max())))    
        if st.sidebar.button('Plot histogram chart'):
            st.plotly_chart(obj_plot.histogram_num(main_var, hue_opt, bins_, range_))
    
    if radio_plot_uni ==('Distribution Plot'):
        st.subheader('Distribution Plot')
        if st.sidebar.button('Plot distribution'):
            fig = obj_plot.DistPlot(main_var)
            st.pyplot()  

    if radio_plot_uni == 'BoxPlot' :
        st.subheader('Boxplot')
        # col_x, hue_opt = None, None
        col_x  = st.sidebar.selectbox("Choose x variable (categorical) optional", obj_plot.columns.insert(0,None), key ='boxplot')
        hue_opt = st.sidebar.selectbox("Hue (categorical) optional", obj_plot.columns.insert(0,None), key ='boxplot')
        if st.sidebar.button('Plot boxplot chart'):
            st.plotly_chart(obj_plot.box_plot(main_var,col_x, hue_opt))
    