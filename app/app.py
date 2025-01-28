import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pickle
import numpy as np

filename = 'C:/ML/Python-for-Machine-Learning/00_CaseStudy/Car_Data/car2.model'
model = pickle.load(open(filename, 'rb'))
# Load trained model

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Car Price Prediction"),
    html.P("Enter the car features to get a price prediction."),
    
    html.Label("Max Power (bhp):"),
    dcc.Input(id="power", type="number", value=82.4),
    
    html.Label("Mileage (kmpl):"),
    dcc.Input(id="mileage", type="number", value=19.392),
    
    html.Label("Year:"),
    dcc.Input(id="year", type="number", value=2010),

    html.Label("Engine:"),
    dcc.Input(id="engine", type="number", value=1250),

    html.Label("Seats:"),
    dcc.Input(id="seats", type="number", value=1 , step=0.1),
    
    html.Button("Predict", id="predict-btn", n_clicks=0),
    html.H2(id="output-price", children="Predicted price will be shown here")
])

# Define prediction logic
@app.callback(
    Output("output-price", "children"),
    Input("predict-btn", "n_clicks"),
    [Input("power", "value"), Input("mileage", "value"), Input("year", "value") , Input("engine", "value"), Input("seats", "value")]
)
def predict(n_clicks, power, mileage, year , engine ,seats):
    if n_clicks > 0:
        input_data = np.array([[ year ,power, mileage,engine ,seats]])
        price = model.predict(input_data)[0]
        real_price = np.exp(price)
        return f"The predicted car price is: ฿{real_price:,.2f}"
    return "Enter values and press predict."

if __name__ == "__main__":
    app.run_server(debug=True)
