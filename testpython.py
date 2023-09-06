import json

import matplotlib.pyplot as plt
import pandas as pd
import requests


class ClassForDrawingPlots():
    def draw_plots(data):
        url = 'https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json'
        data = json.loads(requests.get(url).text)
        df = pd.DataFrame(data)
        df.plot(x='name', y=["gt_corners", "rb_corners", "floor_mean", "ceiling_mean"], kind="bar", figsize=(100, 100))
        plt.title("Plot For Comparing Different Columns")
        plt.savefig("plots/plot.png")
        plt.ion()
        plt.draw()
        plt.pause(0.1)
        plt.ioff()
        plt.show()
        fig = plt.gcf()
        return fig






