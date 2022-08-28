import pickle
import streamlit as st
import pandas as pd
import numpy as np

def recommend(book_name):
    index = np.where(books.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:6]

    recommended_books=[]
    for i in similar_items:
        recommended_books.append(books.index[i[0]])
    return recommended_books

similarity=pickle.load(open('similarity_scores.pkl','rb'))

st.title("Book Recommendations")
st.markdown('Created by Deepak Rawat')




# load books list to let user choose one
books_dict=pickle.load(open('final.pkl','rb'))
books=pd.DataFrame(books_dict)

# create selectbox to select the books for which you want recommendations
selected_books=st.selectbox('Select the Book for which you want to know similar books',
                     books.index.values)

# select button to display
if st.button('Recommend'):
    recommendations=recommend(selected_books)
    for i in recommendations:
        st.write(i)