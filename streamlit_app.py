import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
import numpy as np
st.title("algunas areas y volumenes")
opc = st.selectbox("¿Que figura es?: ",["rectangulo", "triangulo", "circulo", "esfera", "cono", "cilindro","prisma rectangular"])
if opc == "rectangulo":
    ba = float(st.number_input("base: ", min_value=0.0))
    alt = float(st.number_input("altura: ", min_value=0.0))
    st.write("el area es: ", ba*alt)
    fig, ax = plt.subplots()
    draw_rectangle = plt.Polygon([(0, 0), (ba, 0), (ba, alt), (0, alt)], fill=False, color='red')
    ax.add_patch(draw_rectangle)
    plt.axis('equal')  
    plt.title('rectangulo')
    st.pyplot(fig)
elif opc == "triangulo":
    ba = float(st.number_input("base: ", min_value=0.0))
    alt = float(st.number_input("altura: ", min_value=0.0))
    st.write("el area es: ", (ba*alt)/2)
    fig, ax = plt.subplots()
    draw_triangle = plt.Polygon([(0, 0), (ba, 0), (ba/2, alt)], fill=False, color='blue')
    ax.add_patch(draw_triangle)
    plt.axis('equal')  
    plt.title('triangulo')
    st.pyplot(fig)

elif opc == "circulo":
    rad = float(st.number_input("radio: ", min_value=0.0))
    st.write("el area es: ", np.pi*rad**2)
    fig, ax = plt.subplots()
    draw_circle = plt.Circle((0, 0), rad, fill=False)
    ax.add_patch(draw_circle)
    plt.axis('equal')  
    plt.title('Círculo')
    st.pyplot(fig)

elif opc == "esfera":
    rad = float(st.number_input("radio: ", min_value=0.0))
    st.write("el volumen es: ", (4/3)*3.14*rad**3)
    phi, theta = np.mgrid[0.0:2.0*np.pi:100j, 0.0:np.pi:50j]
    x = np.sin(theta) * np.cos(phi)*rad
    y = np.sin(theta) * np.sin(phi)*rad
    z = np.cos(theta)*rad
    color='blue'
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
    fig.update_layout(scene=dict(aspectmode="data"))
    st.title('Visualización de la esfera')
    st.plotly_chart(fig)

elif opc == "cono":
    rad = float(st.number_input("radio: ", min_value=0.0))
    alt = float(st.number_input("altura: ", min_value=0.0))
    st.write("el volumen es: ", (np.pi*rad**2*alt)/3)
    theta = np.linspace(0, 2*np.pi, 100)
    z = np.linspace(0, alt, 100)
    theta, z = np.meshgrid(theta, z)
    x = rad * (1 - z/alt) * np.cos(theta)
    y = rad * (1 - z/alt) * np.sin(theta)
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
    fig.update_layout(scene=dict(aspectmode="data"))
    st.title('Visualización de un cono')
    st.plotly_chart(fig)
elif opc == "cilindro":
    rad = float(st.number_input("radio: ", min_value=0.0))
    alt = float(st.number_input("altura: ", min_value=0.0))
    st.write("el volumen es: ", np.pi*rad**2*alt)
    r = rad
    height = alt
    theta = np.linspace(0, 2*np.pi, 100)
    z = np.linspace(0, height, 100)
    theta, z = np.meshgrid(theta, z)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, alpha=1)
    st.pyplot(fig)
else:
    ba = float(st.number_input("largo: ", min_value=0.0))
    alt = float(st.number_input("altura: ", min_value=0.0))
    anc = float(st.number_input("ancho: ", min_value=0.0))
    st.write("el volumen es: ", ba*alt*anc)
    st.title('Visualización de un Cubo')
    fig = go.Figure(data=[
    go.Mesh3d(
        x=[0,ba, ba, 0, 0, ba, ba, 0],
        y=[0, 0, anc, anc, 0, 0, anc, anc],
        z=[0, 0, 0, 0, alt, alt, alt, alt],
        color='blue',
        opacity=0.9,
        i = [1, 1, 3, 3, 1, 1, 1, 4, 3, 5, 5],
        j = [5, 0, 4, 2, 6, 5, 4, 3, 2, 7, 7],
        k = [6, 2, 0, 1, 2, 4, 0, 7, 0, 4, 6])
        ])

    st.plotly_chart(fig)
    
