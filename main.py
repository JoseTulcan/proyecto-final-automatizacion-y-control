import streamlit as st
import sqlite3 
import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from streamlit_option_menu import option_menu

#Configuración de diseño general de página(Fondo,texto)
st.markdown(
    """
    <style>
    .stApp {
      background-color: #333333; 
    }
    .main h1,
    .main h2,
    .main h3, 
    .main p,
    .main li {
      color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)


#Titulo principal
st.title('Recomendador de peliculas')

st.header('Proyecto en construcción...')


#Menu principal
with st.sidebar:
    selected = option_menu (
        menu_title = "Menu principal", #requerido
        options = ["Home", "Projects", "Contact"], #Requerido
        icons = ["house","book","heart-pulse"],  #Opcional
        
        menu_icon="cast",   #Opcional
        default_index=0,    #Opcional
    
    )

########################## PAGINA 1 ######################################
if selected == "Home":
    st.header(f"Ha seleccionado {selected} ")
    #Caja de habilitación de cámara
    #show_camera = st.checkbox('Mostrar cámara') 

    #picture = None

    #if show_camera:
    #   picture = st.camera_input("Tomar una foto")

    #if picture:
        #st.image(picture);

    # loading the data from the csv file to apandas dataframe
    movies_data = pd.read_csv('movies.csv')

    # selecting the relevant features for recommendation
    selected_features = ['genres','keywords','tagline','cast','director']

    # replacing the null valuess with null string
    for feature in selected_features:
     movies_data[feature] = movies_data[feature].fillna('')

    # combining all the 5 selected features
    combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

    # converting the text data to feature vectors
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)

    # getting the similarity scores using cosine similarity
    similarity = cosine_similarity(feature_vectors)

    # getting the movie name from the user
    #movie_name = input(' Enter your favourite movie name : ')
    movie_name = str(st.text_input('Ingrese el nombre de su pelicula favorita'))

    # creating a list with all the movie names given in the dataset
    list_of_all_titles = movies_data['title'].tolist()
    #print(list_of_all_titles)

    # finding the close match for the movie name given by the user
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    #print(find_close_match)

    #close_match = find_close_match[0]
    if len(find_close_match) == 0:
        #print('No hay ninguna coincidencia cercana con el nombre de tu película.')
        aviso = "No hay ninguna coincidencia cercana con el nombre de tu película."
        st.markdown(f'<p style="color: white;">{aviso}</p>', unsafe_allow_html=True)
    else:
        close_match = find_close_match[0]
    ####################
        
        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

        similarity_score = list(enumerate(similarity[index_of_the_movie]))

        sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
        #print('Movies suggested for you : \n')
        sugerencia = "Peliculas sugeridas para ti"
        st.markdown(f'<p style="color: white;">{sugerencia}</p>', unsafe_allow_html=True)

        i = 1

        for movie in sorted_similar_movies:
            index = movie[0]
            title_from_index = movies_data[movies_data.index==index]['title'].values[0]
            if (i<30):
                #print(i, '.',title_from_index)
                st.markdown(f'<p style="color: white;">{title_from_index}</p>', unsafe_allow_html=True)
                i+=1

############################ PAGINA 2 ##################################
if selected == "Projects":
    st.title (f"Ha seleccionado {selected} ")

    st.header('Este es un video de prueba')
    
    # URL del video de YouTube
    video_url = "https://www.youtube.com/watch?v=n6Qj3PYyjEk&list=RDGMEM29nh-so2GiiVvCzzeO3LJQVMn6Qj3PYyjEk&start_radio=1&ab_channel=Kariganreggaedrummer"

    # Mostrar el video en la aplicación Streamlit
    st.video(video_url)

############################# PAGINA 3 #################################
if selected == "Contact":
    st.title (f"Ha seleccionado {selected} ")
    
    #st.markdown(f'<p style="color: white;">{list_of_all_titles}</p>', unsafe_allow_html=True)

    #Conexión con una base de datos
    #conn = sqlite3.connect('datos_cultivos.db')
    #df = pd.read_sql_query("SELECT * FROM Finca", conn)

    #st.dataframe(df)




