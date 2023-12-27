import streamlit as st

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
      color: #fff;
    }

    </style>
    """,
    unsafe_allow_html=True
)

#Titulo principal
st.title('Proyecto final Automatización y control')

st.header('Proyecto en construcción...')

#Caja de habilitación de cámara
show_camera = st.checkbox('Mostrar cámara') 

picture = None

if show_camera:
    picture = st.camera_input("Tomar una foto")

if picture:
    st.image(picture);

# URL del video de YouTube
video_url = "https://www.youtube.com/watch?v=n6Qj3PYyjEk&list=RDGMEM29nh-so2GiiVvCzzeO3LJQVMn6Qj3PYyjEk&start_radio=1&ab_channel=Kariganreggaedrummer"

# Mostrar el video en la aplicación Streamlit
st.video(video_url)

#Conexión con una base de datos
conn = st.connection("sql")
df = conn.query("select * from pet_owners")
st.dataframe(df)




