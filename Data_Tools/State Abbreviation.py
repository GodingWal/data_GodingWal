import pandas as pd


def add_state_names_column(my_df):
    """

    :param my_df:
    :return:
    """
    names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}

    breakpoint()
    # new_df

    return my_df


if __name__ == "__main__":
    df = pd.DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    add_state_names_column(df)
    print(df.head())
