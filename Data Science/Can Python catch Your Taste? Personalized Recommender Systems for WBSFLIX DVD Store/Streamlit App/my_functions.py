import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

api_key = 'c6fd04fa1072286bca9b40146fe5409d'
image_size = (1500, 1000)  # Dimensione desiderata per l'immagine

def movie_image(movie_id,links):
    try:
        # Make the request to the API
        endpoint = f'https://api.themoviedb.org/3/movie/{int(links.loc[links["movieId"] == movie_id].iloc[0, 2])}/images?api_key={api_key}'
        response = requests.get(endpoint)
        data = response.json()

        # Get the first image URL from the response
        image_url = data['backdrops'][0]['file_path']

        # Build the full image URL
        image_base_url = 'https://image.tmdb.org/t/p/original'
        full_image_url = f'{image_base_url}{image_url}'

        # Download the image
        response = requests.get(full_image_url)
        image = Image.open(BytesIO(response.content))

        # Resize the image to the desired size
        image = image.resize(image_size)

        # Create a figure and display the image
        fig, ax = plt.subplots()
        ax.imshow(image)
        ax.axis('off')

        # Return the figure
        return fig

    except:
        # If there is an error, display a placeholder image
        placeholder_url = f'https://via.placeholder.com/{image_size[0]}x{image_size[1]}?text=Image+Not+Found'
        response = requests.get(placeholder_url)
        image = Image.open(BytesIO(response.content))

        # Resize the placeholder image to the desired size
        image = image.resize(image_size)

        # Create a figure and display the placeholder image
        fig, ax = plt.subplots()
        ax.imshow(image)
        ax.axis('off')

        # Return the figure
        return fig
    
    
    
    
def movie_title(movie_id,df):
    return df.loc[df["movieId"]==movie_id,"title"].values[0]


def movie_url(movie_id, df):
    return f'https://www.themoviedb.org/movie/{str(int(df.loc[df["movieId"] == movie_id].iloc[0, 2]))}/'


def redirect_button(url: str, text: str = None):
    st.markdown(
        f"""
        <a href="{url}" target="_self">
            <div style="
                display: inline-flex;
                align-items: center;
                padding: 0.5em 1em;
                color: #321E37;
                background-color: #FFC197;
                border-radius: 20px;
                text-decoration: none;
                height: 20px;
                font-size: 16px;
                font-weight: bold;">
                {text}
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )



def linear_hybrid(n, df, weight_counts):
    #This function linearly combines ratings and counts with appropriate weights
    
    #Error message
    if weight_counts < 0 or weight_counts > 1:
        print("Weight must be in [0, 1]")
    
    #Scaling of the data
    my_scaler = MinMaxScaler().set_output(transform="pandas")
    my_scaler.fit(df)
    df1 = my_scaler.transform(df)
    
    
    col_name = f"lin. {weight_counts*100}%"
    df1[col_name] = weight_counts * df1['rating_count'] + (1 - weight_counts) * df1['avg_rating']
    
    return df1.sort_values(by=col_name, ascending=False).head(n)




def fun_popularity(n, df, weight_counts):
    #This function computes the most popular movies based on linear combination method
    #This function is an upgrade of linear_hybrid() as it also manipulates the original dataframe
    
    #introduce the average rating and the rating count
    popularity = df[['movieId','rating']].groupby(by='movieId').agg(avg_rating=("rating","mean"))
    popularity['rating_count'] = df[['movieId','rating']].groupby(by='movieId').agg(rating_count=("rating","count"))['rating_count']
    
    
    #Scaling of the data
    my_scaler = MinMaxScaler().set_output(transform="pandas")
    my_scaler.fit(popularity)
    df1 = my_scaler.transform(popularity)
    
    
    col_name = f"lin. {weight_counts*100}%"
    df1[col_name] = weight_counts * df1['rating_count'] + (1 - weight_counts) * df1['avg_rating']
    return df1.sort_values(by=col_name, ascending=False).head(n)



def special_for_you_general(uID,n,ratings,movies):

    #create a users-items table
    user_item = pd.pivot_table(data=ratings, values='rating', index='userId', columns='movieId')

    #replace NaNs with zeros
    user_item.fillna(0,inplace=True)

    #cosine similarities
    cos_sim = pd.DataFrame(data=cosine_similarity(user_item), index=user_item.index, columns=user_item.index)
    
    #find the unrated movies and the ratings of the other users
    unseen_rating_uID = user_item.loc[user_item.index!=uID,user_item.loc[uID,:]==0]
    
    #calculate weights
    weights_uID = cos_sim.query('userId!=@uID')[uID]/sum(cos_sim.query('userId!=@uID')[uID])
    
    #construct the predicted_rating by means of the dot product
    predicted_uID = pd.DataFrame(unseen_rating_uID.T.dot(weights_uID), columns = ["predicted_rate"]).sort_values(by="predicted_rate",ascending=False)
    
    #to find the top 5 UNRATED movies we have to merge our findings with the original table
    recommendations = predicted_uID.merge(movies, left_index=True, right_on="movieId")
    
    return recommendations.sort_values("predicted_rate", ascending=False).head(n)





def favourite_movies(user_id,n,ratings,movies):
    best_movieId = ratings.loc[(ratings['userId'] == user_id) & (ratings['userId'] >0)].sort_values(by="rating", ascending=False).head(n)['movieId'].tolist()

    best_movies = []
    for movieId in best_movieId:
        best_movies.append(movies.loc[movies['movieId'] == movieId, 'title'].iloc[0])
    return best_movies



def item_based_collaborative_filtering(movie_name,n,movies,ratings):
    
    #map the movie_name into movieId
    movieID = movies.loc[movies['title'] == movie_name,'movieId'].values[0]

    #pivot table
    ratings_pivot = pd.pivot_table(data = ratings, values='rating', index='userId', columns='movieId')
    
    #create a pandas df with the correlations of the other movies
    similar_to_movieID = ratings_pivot.corrwith(ratings_pivot[movieID])
    corr_movieID = pd.DataFrame(similar_to_movieID, columns = ['Pearson'])
    corr_movieID.dropna(inplace = True) #drop the NaNs
    
    popularity = ratings[['movieId','rating']].groupby(by='movieId').agg(avg_rating=("rating","mean"))
    popularity['rating_count'] = ratings[['movieId','rating']].groupby(by='movieId').agg(rating_count=("rating","count"))['rating_count']
    
    #Construct a df of (movies) VS (Pearson, popularity_metric)
    mixed_movieID = linear_hybrid(len(popularity),popularity, 0.5)[['lin. 50.0%']].join(corr_movieID['Pearson'], how='left')
    #Drop movieID
    mixed_movieID.drop(movieID, inplace=True)
    #We also drop NaNs
    mixed_movieID.dropna(inplace = True) #drop the NaNs
    #Filter out all rows below a threshold 0.7 and then keep only the first n movies in terms of similatities to movieID
    return mixed_movieID.loc[mixed_movieID['lin. 50.0%'] > 0.5].sort_values(by='Pearson',ascending=False).head(n)
