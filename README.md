**ML Project-RECOMMENDER SYSTEM- COLLABORATIVE FILTERING*

**Web app**: https://bookrecommend-vagadro.herokuapp.com/


**Overview:** Recommender systems are one of the most widely used machine learning based systems designed to recommend items to users on the basis of some similarilies. It is being used in almost every consumer facing industry like OTT platforms, ecommerce websites, food delivery apps, seach engines etc and has a huge potential in directing products KPI's in the right track. 
Recommender systems are generally build in product to drive DAU, MAU, YAU and target advertisements as per users past attributes and likeliness. 

Recommender systems generally works on two principles:
1) Content Based Recommendations: Product likeliness for user on the basis of content of the product/commodity
2) Collaborative Filtering based Recommendations: PRoduct likeliness for user on the basis of likeliness of the same product by "similar" other users 

In this project, I have tried to create a recommender system which recommends "similar" books to user as per the selected book on the basis of retings given by different users to a similar book. 

Since we are building Collaborative Filtering recommender system, we will create a item-user similarity matrix rather than a item-item similarity matrix(as in the case of Content based recommender system)

**Constraints:**
While performing EDA we analysed the data available for Users and Books and found out that there are very few users who have rated books all together and there are very few books where were being rated by avid readers. 
This creates two possible problems:
1) Any user who have rated very few times may be a very novice reader and just started reading. This ratings would may not give a clear indication on the rating of the book
2) Any book which have been rated quite less could mean that this is probably a new book and again may result in wrong recommendations

To solve this, we saw that we only chose users who rate > 200 times and books which had >50 ratings for this recommender system. 
In real based scenario this assumptions needs to be validated with some more data or with industry expertise.

**Dataset used:** https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
For building the model, we have used a dataset available in Kaggle. The entire dataset is divided into three dataframes "books","users" and "ratings" having information like ISBN, title, author, location, id, puplisher etc.

**Approach:** 
- Data Loading: load all the files
- EDA: merge the datasets as necessary, idetify total ratings by a user and total ratings on a book to solve constraint mentioned above
- Data Cleaning and preprocessing: Create final pivot dataset having books as index and users on the column and the value as the ratings given by each user on books.
- Model Building: Create the item-user similarity matrix using Cosine Similarity between books and users and store in a pickle file. 
- Deployment: Model deployed using Streamlit framewok using heroku server

In case you want to check out the same visit:  https://bookrecommend-vagadro.herokuapp.com/



Deepak Rawat

Linkedin: linkedin.com/in/deepak-rawat-183316b5

----------------------------------------------------------------------------------------------------------------------------------------------------------------


