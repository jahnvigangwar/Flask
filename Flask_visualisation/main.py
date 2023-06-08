from flask import Flask, render_template, send_file
import io 
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt 
import seaborn as sns 

fig, ax = plt.subplots(figsize=(6,6))
ax = sns.set_style(style="darkgrid")

x= [i for i in range(100)]
y= [i for i in range(100)]

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('view.html')

@app.route('/visualize')
def visualize():
    sns.lineplot(x)
    canvas=FigureCanvas(fig)
    img= io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='img/png')

if __name__ == "__main__":
    app.run()