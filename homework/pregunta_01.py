"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import os
import matplotlib.pyplot as plt
import pandas as pd


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    df = pd.read_csv("files/input/news.csv", index_col=0)
    plot_properties = {
        "Television": {"color": "dimgray", "zorder": 1, "linewidth": 2},
        "Newspaper": {"color": "grey", "zorder": 1, "linewidth": 2},
        "Internet": {"color": "tab:blue", "zorder": 2, "linewidth": 3},
        "Radio": {"color": "lightgrey", "zorder": 1, "linewidth": 2},
    }

    plt.figure(figsize=(10, 6))
    first_year = df.index[0]
    last_year = df.index[-1]

    for col in df.columns:
        props = plot_properties.get(col, {})
        color = props.get("color", "black") 
        zorder = props.get("zorder", 1)   
        linewidth = props.get("linewidth", 2) 

        plt.plot(
            df[col],
            color=color,
            label=col,
            zorder=zorder,
            linewidth=linewidth,
        )
        plt.scatter(
            x=first_year,
            y=df[col].loc[first_year],
            color=color,
            zorder=zorder,
        )
        plt.text(
            first_year - 0.2,
            df[col].loc[first_year],
            f"{col} {df[col].loc[first_year]}%",
            ha="right",
            va="center",
            color=color,
        )
        plt.scatter(
            x=last_year,
            y=df[col].loc[last_year],
            color=color,
            zorder=zorder,
        )
        plt.text(
            last_year + 0.2,
            df[col].loc[last_year],
            f"{df[col].loc[last_year]}%",
            ha="left",
            va="center",
            color=color,
        )

    plt.title("How people get their news", fontsize=16)
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.tight_layout()
    os.makedirs("files/plots", exist_ok=True)
    plt.savefig("files/plots/news.png")
    plt.show()

pregunta_01()