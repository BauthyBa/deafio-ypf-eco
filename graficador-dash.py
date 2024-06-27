import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import time

# Conexión a la base de datos MySQL
engine = create_engine('mysql+pymysql://root:Bautista?2006@localhost/ejemplo_db')

# Consulta de datos
def cargar_datos():
    query = "SELECT * FROM ventas"
    df = pd.read_sql(query, engine)
    return df

app = dash.Dash(__name__)

# Definir la plantilla HTML
app.index_string = '''
<!DOCTYPE html>
<html>
<head>
    <title>Mi Aplicación Dash</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Mi Aplicación Dash</a>
    </nav>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                {%app_entry%}
            </div>
        </div>
    </div>
    <footer class="footer">
        <div class="container">
            <p class="text-muted">Pie de página de mi aplicación.</p>
        </div>
    </footer>
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
        interval=60*100,  # en milisegundos, actualiza cada 1 minuto
        n_intervals=0
    )
])

@app.callback(
    Output('grafico-barras', 'figure'),
    Output('grafico-lineas', 'figure'),
    Input('interval-component', 'n_intervals')
)
def actualizar_graficos(n):
    df = cargar_datos()  # Cargar datos actualizados de la base de datos
    fig_barras = px.bar(df, x='producto', y='cantidad', title='Cantidad de Productos Vendidos')
    fig_lineas = px.line(df, x='fecha', y='precio', title='Precio de Ventas por Fecha', markers=True)
    return fig_barras, fig_lineas

if __name__ == '__main__':
    app.run_server(debug=True)
