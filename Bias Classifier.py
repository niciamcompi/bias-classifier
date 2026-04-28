import tkinter as tk
from tkinter import Text, ttk
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Dbias.text_debiasing import classifier as debias_classifier
from Dbias.bias_recognition import recognizer
from Dbias.bias_masking import masking

class BiasClassifierApp:
    def __init__(self, master):
        self.master = master
        master.title("Bias Classifier App")

        # Set window size and background color
        master.geometry("800x600")
        master.configure(bg="white")

        self.input_label = tk.Label(master, text="Enter Text:", font=("Helvetica", 14), bg="white")
        self.input_label.pack(pady=10)

        # Enlarge the text field for copy-pasting
        self.text_entry = Text(master, height=10, width=80, font=("Helvetica", 12))
        self.text_entry.pack(pady=10)

        # Set a light blue background for the "Classify" button
        style = ttk.Style()
        style.configure("TButton", background="lightblue")

        self.classify_button = ttk.Button(master, text="Analyze", command=self.classify_text, style="TButton",
                                          cursor="hand2")
        self.classify_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12), bg="white", justify="left", wraplength=700)
        self.result_label.pack(pady=10)

        # Create a Plotly figure for the gauge chart
        self.plotly_canvas = go.Figure()
        self.plotly_canvas.update_layout(title_text="Bias Score")

        # Create a Matplotlib figure for the pie chart
        self.matplotlib_canvas = plt.Figure(figsize=(5, 4), dpi=100)
        self.matplotlib_pie = self.matplotlib_canvas.add_subplot(111)
        self.matplotlib_canvas_widget = FigureCanvasTkAgg(self.matplotlib_canvas, master=self.master)
        self.matplotlib_canvas_widget.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def classify_text(self):
        text_to_classify = self.text_entry.get("1.0", "end-1c")  # Get the text from the text field

        # Apply the provided classifier
        result = debias_classifier(text_to_classify)

        # Format the result label
        formatted_result = (
            f"Classifier Result: {result[0]['label']}\n"
            f"Score: {result[0]['score']}\n"
        )

        # Display the result in the GUI
        self.result_label.config(text=formatted_result)

        # Update the Plotly gauge chart with the score
        self.update_gauge_chart(result[0]['score'])

        # Update the Matplotlib pie chart
        self.update_pie_chart(result[0]['score'])

    def update_gauge_chart(self, score):
        # Clear previous value
        self.plotly_canvas.data = []

        # Create a gauge chart for the score
        gauge_chart = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Bias Score"}
        ))

        self.plotly_canvas.add_trace(gauge_chart.data[0])

        # Update the layout
        self.plotly_canvas.update_layout(title_text="Bias Score")

    def update_pie_chart(self, score):
        # Clear previous value
        self.matplotlib_pie.clear()

        # Create a pie chart for the biased and non-biased categories
        labels = ['Biased', 'Non-biased']
        colors = ['red' if score > 0.5 else 'green', 'green' if score > 0.5 else 'red']
        sizes = [score, 1 - score]

        self.matplotlib_pie.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

        # Equal aspect ratio ensures that the pie is drawn as a circle
        self.matplotlib_pie.axis('equal')

        # Update the layout
        self.matplotlib_canvas_widget.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = BiasClassifierApp(root)
    root.mainloop()
