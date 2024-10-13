import gradio as gr
import plotly.express as px

def start_model_engine(model):
    pass

def predict_trend(model, symbol_folder, symbol):
    # Initialise model engine
    engine = start_model_engine(model)

    df = get_df_for_symbol(symbol_folder, symbol)
    if df.empty:
        return "Error fetching data. Please try again."
    
    # engine prediction
    #######################
    # will be implemented #
    #######################

    # Create a Plotly figure
    fig = px.line(df, x='date', y='price', title=f'{symbol} Price Trend')
    fig.update_layout(xaxis_title='Date', yaxis_title='Price (USD)')

    return fig

        

def get_df_for_symbol(symbol_folder, symbol):
    if symbol_folder == "crypto":
        if symbol == "BTC":
            from symbols.crypto.btc import btc
            return btc()            
        else:
            raise ValueError(f"Crypto symbol '{symbol}' not yet supported")
        
    elif symbol_folder == "forex":
        if symbol == "USDMYR":
            from symbols.forex.USDMYR import usd_myr
            return usd_myr()            
        else:
            raise ValueError(f"Forex symbol '{symbol}' not yet supported")
            
    elif symbol_folder == "stocks":
        if symbol == "AAPL":
            from symbols.stocks.APPL import appl
            return appl()
        else:
            raise ValueError(f"Stock symbol '{symbol}' not yet supported")
    
    else:
        raise ValueError(f"Symbol folder '{symbol_folder}' not yet supported")

        

# Function to get available models
def get_models():
    return ["amazon/chronos-t5-tiny"]

# Function to get symbol folders
def get_symbol_folders():
    return ["crypto", "forex", "stocks"]

# Function to get symbols from a specific folder
def get_symbols(folder):
    if folder == "crypto":
        return ["BTC", "ETH", "ADA"]
    elif folder == "forex":
        return ["EURUSD", "USDMYR", "USDJPY"]
    elif folder == "stocks":
        return ["AAPL", "TSLA", "MSFT"]
    else:
        return []

# Main Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Financial Trend Prediction")

    with gr.Row():
        model_dropdown = gr.Dropdown(choices=get_models(), label="Select Model")
        folder_dropdown = gr.Dropdown(choices=get_symbol_folders(), label="Select Symbol Folder")
        symbol_dropdown = gr.Dropdown(label="Select Symbol")

    # Update symbol dropdown based on folder selection
    def update_symbols(folder):
        symbols = get_symbols(folder)
        return gr.Dropdown(choices=symbols, value=symbols[0] if symbols else None)

    folder_dropdown.change(fn=update_symbols, inputs=folder_dropdown, outputs=symbol_dropdown)

    predict_button = gr.Button("Predict Trend")
    output = gr.Plot(label="Price Trend")

    # Perform prediction when button is clicked
    predict_button.click(fn=predict_trend, 
                         inputs=[model_dropdown, folder_dropdown, symbol_dropdown], 
                         outputs=output)

demo.launch()