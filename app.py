import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv('Data/avocado.csv')
data = data.query("type == 'conventional' and region == 'Albany' ")
data['Data'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            children='Avocado Analysis Dashboard',
            style={"color": 'red', "textAlign": 'center'}
        ),

        html.P(
            children="Analyze the behavior of avocado prices"
                     " and the number of avocados sold in the US"
                     " between 2015 and 2018",
            className="header-description",


        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': data['Date'],
                        'y': data['AveragePrice'],
                        'type': 'lines',
                    },
                ],
                "layout": {
                    "title": "Average Price of Avocado",
                }
            }
        ),
        dcc.Graph(
            figure={
                'data': [
                    {
                        'x': data['Date'],
                        'y': data['Total Volume'],
                        'type': 'lines',
                    },
                ],
                "layout": {"title": "Avocado Sold"}
            }
        )

    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
