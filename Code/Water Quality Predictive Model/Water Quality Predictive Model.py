import tkinter as tk
from tkinter import Entry, Button, Label, Frame

import pickle
import pandas as pd
import numpy as np
import joblib

scaler = joblib.load("final_scaler.save")
model = pickle.load(open('final_model.pkl', 'rb'))

# Function to make a prediction
def predict():
    input_features = [float(entry.get()) for entry in entry_widgets]
    features_value = [np.array(input_features)]
    feature_names = ["ph", "Hardness", "Solids", "Chloramines", "Sulfate", "Conductivity", "Organic_carbon",
                     "Trihalomethanes", "Turbidity"]
    df = pd.DataFrame(features_value, columns=feature_names)
    df = scaler.transform(df)
    output = model.predict(df)
    if output[0] == 1:
        prediction = "safe"
        result_label.config(text="Water is Safe for Human Consumption", fg="green")
    else:
        prediction = "not safe"
        result_label.config(text="Water is Not Safe for Human Consumption", fg="red")

# Create a Tkinter application window
app = tk.Tk()
app.title("Water Quality Prediction")

# Set the window geometry and background color
app.geometry("470x480")
app.configure(bg='#ABFFF1')

# Create a frame for the input fields and labels
input_frame = Frame(app, bg='#ABFFF1')
input_frame.pack(pady=10)

# Create input entry fields with labels
entry_labels = ["pH:", "Hardness:", "Solids:", "Chloramines:", "Sulfate:",
                "Conductivity:", "Organic Carbon:", "Trihalomethanes:", "Turbidity"]
entry_widgets = []

for label_text in entry_labels:
    label = Label(input_frame, text=label_text, bg='#ABFFF1', font=("copperplate gothic bold", 14,"bold"), fg='black')
    label.grid(row=entry_labels.index(label_text), column=0, sticky='w', padx=10, pady=5)
    entry = Entry(input_frame, font=("Arial", 12))
    entry.grid(row=entry_labels.index(label_text), column=1, padx=10, pady=5)
    entry_widgets.append(entry)

# Create a prediction button with custom style
predict_button = Button(app, text="Predict", command=predict, font=("copperplate gothic bold", 16,"bold"), bg='#63F07B', fg='black',
                         width = 12)
predict_button.pack(pady=10)

# Create a label to display the prediction with increased font size and custom style
result_label = Label(app, text="", font=("copperplate gothic bold", 14), bg="#ABFFF1")
result_label.pack()

# Start the Tkinter main loop
app.mainloop()
