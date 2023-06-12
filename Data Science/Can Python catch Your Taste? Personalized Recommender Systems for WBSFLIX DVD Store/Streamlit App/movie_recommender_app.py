import streamlit as st
import pickle
from my_functions import movie_image, movie_title, movie_url, redirect_button, fun_popularity, special_for_you_general, favourite_movies, item_based_collaborative_filtering
import pandas as pd


#st.set_page_config(layout='wide')
st.title('WBSflix')

#import the data
movies = pd.read_csv('/Users/G/Desktop/Documents/Formazione in Data Science/WBS/WBS Bootcamp/8. Recommender Systems/Data/movies.csv')
links = pd.read_csv('/Users/G/Desktop/Documents/Formazione in Data Science/WBS/WBS Bootcamp/8. Recommender Systems/Data/links.csv')
ratings = pd.read_csv('/Users/G/Desktop/Documents/Formazione in Data Science/WBS/WBS Bootcamp/8. Recommender Systems/Data/ratings.csv')


tab0, tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "👤 Top Picks for You","🔝 Trending now", "🔎 Search", "🤖 ChatBot"])






############################################################################################################

with tab0:
    col1, col2 = st.columns([10, 2])  # Imposta le dimensioni delle colonne come 1, 2 e 1

   
    with col1:
        st.header("Welcome to WBSFLIX!")
        st.markdown("🎬 Discover a world of cinematic wonders at WBSFLIX, your ultimate destination for DVD enthusiasts. Experience the best of both worlds: the cozy charm of a local store combined with the convenience of online shopping. 🍿")
    
        st.subheader("🔥 Our Passion for Movies, Your Perfect Picks 🔥")
        st.markdown("At WBSFLIX, we're all about movies and personal recommendations. We understand that finding the perfect movie is a delightful journey, and we're here to make it even more enjoyable for you. With our handpicked collection of DVDs, we cater to your unique tastes and preferences.")

        st.subheader("🎁 Elevate Your Movie-Watching Experience 🌟")
        st.markdown("Get ready for an enhanced movie-watching experience with our state-of-the-art recommendation systems. Discover personalized picks tailored just for you or explore popular choices loved by our vibrant community. Our rows of movie recommendations will inspire your next cinematic adventure.")

        st.subheader("👩‍💼 Ursula's Expertise, Exceptional Service 👨‍💼")
        st.markdown("Ursula's expertise and commitment to customer service shine brightly in our online store. While we've expanded, our dedication to providing you with exceptional service and expert advice remains unwavering. We're here to be your trusted companion in your cinematic journey.")

        st.subheader("🎉 Join the Magic, Uncover Hidden Gems 🎉")
        st.markdown("Celebrate the magic of movies and the joy of discovering hidden gems with us. Start your exploration of WBSFLIX today and let us guide you through an unforgettable cinematic experience.")

        st.markdown("🍿Happy Movie Watching from the WBSFLIX Team! 🎉")
        

    with col2:
        st.subheader("")


############################################################################################################
with tab1:
    st.header(f"Top Picks for You")
    user_id = st.number_input("Tell me your user ID", help="User ID must be [1-610]", min_value=0, max_value=610)

    if user_id != 0:
        foryou = special_for_you_general(user_id, 6, ratings, movies).iloc[:, 1].tolist()
        c1, c2, c3 = st.columns(3)
        with st.container():
            with c1:
                st.pyplot(movie_image(foryou[0], links))
                redirect_button(movie_url(foryou[0], links), movie_title(foryou[0], movies))
            with c2:
                st.pyplot(movie_image(foryou[1], links))
                redirect_button(movie_url(foryou[1], links), movie_title(foryou[1], movies))
            with c3:
                st.pyplot(movie_image(foryou[2], links))
                redirect_button(movie_url(foryou[2], links), movie_title(foryou[2], movies))
        st.title("")
        c4, c5, c6 = st.columns(3)
        with st.container():
            with c4:
                st.pyplot(movie_image(foryou[3], links))
                redirect_button(movie_url(foryou[3], links), movie_title(foryou[3], movies))
            with c5:
                st.pyplot(movie_image(foryou[4], links))
                redirect_button(movie_url(foryou[4], links), movie_title(foryou[4], movies))
            with c6:
                st.pyplot(movie_image(foryou[5], links))
                redirect_button(movie_url(foryou[4], links), movie_title(foryou[5], movies))
    else:
        st.info("Please enter a valid User ID.")

        

############################################################################################################
with tab2:
    st.header("Trending now")
    popular_movies =  fun_popularity(6, ratings, 0.7).index.tolist()
    c1, c2, c3 = st.columns(3)
    with st.container():
        with c1:
            st.pyplot(movie_image(popular_movies[0],links))
            redirect_button(movie_url(popular_movies[0],links),movie_title(popular_movies[0],movies))
        with c2:
            st.pyplot(movie_image(popular_movies[1],links))
            redirect_button(movie_url(popular_movies[1],links),movie_title(popular_movies[1],movies))
        with c3:
            st.pyplot(movie_image(popular_movies[2],links))
            redirect_button(movie_url(popular_movies[2],links),movie_title(popular_movies[2],movies))
    st.title("")
    c4, c5, c6 = st.columns(3)
    with st.container():
        with c4:
            st.pyplot(movie_image(popular_movies[3],links))
            redirect_button(movie_url(popular_movies[3],links),movie_title(popular_movies[3],movies))
        with c5:
            st.pyplot(movie_image(popular_movies[4],links))
            redirect_button(movie_url(popular_movies[4],links),movie_title(popular_movies[4],movies))
        with c6:
            st.pyplot(movie_image(popular_movies[5],links))
            redirect_button(movie_url(popular_movies[5],links),movie_title(popular_movies[5],movies))



with tab3:
    selected_option = False
    option = st.selectbox('List of your top rated movies', [''] + favourite_movies(user_id, 20, ratings, movies))

    if option != '':
        selected_option = True
        movie_name = option
        similarto_movie_name = item_based_collaborative_filtering(movie_name, 6, movies, ratings).index.to_list()

        c1, c2, c3 = st.columns(3)
        with st.container():
            with c1:
                st.pyplot(movie_image(similarto_movie_name[0], links))
                redirect_button(movie_url(similarto_movie_name[0], links), movie_title(similarto_movie_name[0], movies))
            with c2:
                st.pyplot(movie_image(similarto_movie_name[1], links))
                redirect_button(movie_url(similarto_movie_name[1], links), movie_title(similarto_movie_name[1], movies))
            with c3:
                st.pyplot(movie_image(similarto_movie_name[2], links))
                redirect_button(movie_url(similarto_movie_name[2], links), movie_title(similarto_movie_name[2], movies))

        st.title("")
        c4, c5, c6 = st.columns(3)
        with st.container():
            with c4:
                st.pyplot(movie_image(similarto_movie_name[3], links))
                redirect_button(movie_url(similarto_movie_name[3], links), movie_title(similarto_movie_name[3], movies))
            with c5:
                st.pyplot(movie_image(similarto_movie_name[4], links))
                redirect_button(movie_url(similarto_movie_name[4], links), movie_title(similarto_movie_name[4], movies))
            with c6:
                st.pyplot(movie_image(similarto_movie_name[5], links))
                redirect_button(movie_url(similarto_movie_name[5], links), movie_title(similarto_movie_name[5], movies))

            
with tab4:
    st.header("WORK IN PROGRESS 🚧")
    
    
    