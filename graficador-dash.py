import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import time

engine = create_engine('mysql+pymysql://user:password@localhost/(nombre de la base de datos)') # Esta linea la tienen que completar con sus datos.

def cargar_datos():
    query = "SELECT * FROM (nombre de la base de datos)" #Aca tambien tienen que cambiar el nombre de la base de datos.
    df = pd.read_sql(query, engine)
    return df

app = dash.Dash(__name__)

app.index_string = '''
<!DOCTYPE html>
<html>
<head>
    <title>Aplicacion Dash</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Dash</a>
    </nav>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                {%app_entry%}
            </div>
        </div>
    </div>
    {%config%}
    {%scripts%}
    {%renderer%}
</body>
</html>
'''

app.layout = html.Div([
    html.H1("Visualización de Datos con Dash"),
    dcc.Graph(id='grafico-barras'),
    dcc.Graph(id='grafico-lineas'),
    dcc.Interval(
        id='interval-component',
        interval=60*100,  # Esto es para que la pagina se actualiza cada 10 segundos.
        n_intervals=0
    )
])

@app.callback(
    Output('grafico-barras', 'figure'),
    Output('grafico-lineas', 'figure'),
    Input('interval-component', 'n_intervals')
)
def actualizar_graficos(n):
    df = cargar_datos()  
    fig_barras = px.bar(df, x='voltaje', y='velocidad', title='Ejemplo de Datos en Barra')            # En el caso de que su base de dato tenga nombres diferentes aca tambien tiene que cambier los valores de x e y.
    fig_lineas = px.line(df, x='fecha', y='tiempo', title='Ejemplo de datos en Grafico de Linea', markers=True)
    return fig_barras, fig_lineas

if __name__ == '__main__':
    app.run_server(debug=True)
