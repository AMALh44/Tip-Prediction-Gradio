import pickle
import gradio as gr


def predicted(total_bill, size, time):
    with open('Linear_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    

    time_encoded = 0 if time == "Lunch" else 1
    
 
    input_data = [[total_bill, size, time_encoded]]
    

    prediction = loaded_model.predict(input_data)[0]
    
    return f"Predicted Value: {prediction:.2f}"


iface = gr.Interface(
    fn=predicted,
    inputs=[
        gr.Number(label="Total Bill"),
        gr.Number(label="Size"),
        gr.Radio(label="Time", choices=["Lunch", "Dinner"])
    ],
    outputs="text"
)


iface.launch(share=True)
