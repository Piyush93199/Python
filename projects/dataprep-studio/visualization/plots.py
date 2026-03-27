import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(
    df,
    column,
):

    fig = plt.figure()

    plt.hist(
        df[column].dropna(),
        bins=20,
    )

    plt.title(
        f"Histogram — {column}"
    )

    plt.xlabel(column)

    plt.ylabel("Frequency")



    return fig

def plot_boxplot(
    df,
    column,
):

    fig = plt.figure()

    sns.boxplot(
        y=df[column],
    )

    plt.title(
        f"Boxplot — {column}"
    )



    return fig

def plot_correlation_heatmap(
    df,
):

    fig = plt.figure()

    numeric_df = df.select_dtypes(
        include="number"
    )

    corr = numeric_df.corr()

    sns.heatmap(
        corr,
        annot=True,
    )

    plt.title(
        "Correlation Heatmap"
    )



    return fig