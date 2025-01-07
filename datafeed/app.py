import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Welcome to Quantium's Interactive Visualization!"),
    html.P("This is a simple Dash application."),
])

if __name__ == '__main__':
    app.run_server(debug=True)
