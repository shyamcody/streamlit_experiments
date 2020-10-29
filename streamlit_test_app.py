#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:22:15 2020

@author: shyambhu.mukherjee
"""

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

#add a title
st.title("The first basic testing app")
"""
 streamlit.write(*args, **kwargs)

    Write arguments to the app.

    This is the Swiss Army knife of Streamlit commands: 
    it does different things depending on what you throw at it. 
    Unlike other Streamlit commands, write() has some unique properties:

        You can pass in multiple arguments, all of which will be written.

        Its behavior depends on the input types as follows.

        It returns None, so it’s “slot” in the App cannot be reused.
"""
st.write("\frac{1}{2} does it support lateX?")
st.write("looks like it doesn't")
st.write("a normal string")
st.write("<b>food</b> is great here; checking if simple html works",
         unsafe_allow_html = True)
st.write("thanks, its a *good* day", unsafe_allow_html = True)
st.write("displaying that numbers can be represented")
st.write(1234)
st.write("showing that dataframes can be printed")
st.write(pd.DataFrame({"first_column":[10,20,30,40],
                      "second_column":[105,405,905,1605]}))

st.write("we can show headers also")
st.header("it shows chart too")

df = pd.DataFrame(np.random.randn(200, 3),
                  columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(x='a', y='b', 
                                       size='c', color='c', 
                                       tooltip=['a', 'b', 'c'])
st.write(c)

st.subheader("showing a codeblock using st.code")
code = """
       for i in range(20):
           print("this is a count of" + str(i))
       """
st.code(code,language = "python")

df = pd.DataFrame(np.random.randn(20,8),
                  columns = ["columns_"+str(i) for i in range(1,9)])
st.subheader("showing dataframe as table")
st.table(df)