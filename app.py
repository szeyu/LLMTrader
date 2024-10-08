import gradio as gr


def predict_trend(model, df): 
    # initialize Chronos Engine
    if "chronos" in model:
        pass
        

def get_df_for_symbol(symbol_folder, symbol):
    if symbol_folder == "crypto":
        pass
    elif symbol_folder == "forex":
        pass
    elif symbol_folder == "malaysia_stocks":
        pass
    elif symbol_folder == "us_stocks":
        pass
        

# Function to get available models
def get_models():
    return ["chronos-tiny", "chronos-small"]

# Function to get symbol folders
def get_symbol_folders():
    return ["crypto", "forex", "malaysia_stocks", "us_stocks"]

# Function to get symbols from a specific folder
def get_symbols(folder):
    if folder == "crypto":
        return ["BTC", "ETH", "ADA"]
    elif folder == "forex":
        return ["EURUSD", "GBPUSD", "USDJPY"]
    elif folder == "malaysia_stocks":
        return ["MYEG", "TOPGLOV", "HARTA"]
    elif folder == "us_stocks":
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
    output = gr.Textbox(label="Prediction Result")
    
    df = get_df_for_symbol(folder_dropdown, symbol_dropdown)

    # Perform prediction when button is clicked
    predict_button.click(fn=predict_trend, 
                         inputs=[model_dropdown, df], 
                         outputs=output)

demo.launch(share=True)