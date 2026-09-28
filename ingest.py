import pandas as pd

#check if any columns have null values

def check_unique(df, column_name):
    return df[column_name].is_unique

def check_dtypes(df):
    return df.dtypes
def convert_to_datetime(df, column_name):
    df[column_name] = pd.to_datetime(df[column_name])
    return df

def standardize_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

# def check for duplicates in a column
def check_duplicates(df, column_name):
    return df[column_name].duplicated().any()   

# fill in price per unit null values by dividing total spent by quanittyt
def fill_price_per_unit(df):
    df["price_per_unit"] = df["price_per_unit"].fillna(df["total_spent"] / df["quantity"])
    df["quantity"] = df["quantity"].fillna(df["total_spent"] / df["price_per_unit"])
    df["total_spent"] = df["total_spent"].fillna(df["price_per_unit"] * df["quantity"])
    return df



def main():
    df = pd.read_csv("retail_store_sales.csv")
    print(df)

    print(df.columns)
    df = standardize_column_names(df)
    df = fill_price_per_unit(df)
    # check that price per unit is total spend divided by quantity
    print(df.loc[df["price_per_unit"] != df["total_spent"] / df["quantity"], ["transaction_id","customer_id", "total_spent", "quantity", "price_per_unit"]])
    # check if the above condition is ture for any rows with no null values in them
    # print(df.loc[(df["price_per_unit"] != df["total_spent"] / df["quantity"]) & df["price_per_unit"].notnull() & df["total_spent"].notnull() & df["quantity"].notnull(), ["transaction_id","customer_id", "total_spent", "quantity", "price_per_unit"]])
    df = convert_to_datetime(df, "transaction_date")  # replace "date_column_name" with the actual column name containing dates
    # print(df)
    # print(check_dtypes(df))
    # print(df.isnull().sum())
    # investigate only the columns with null values
    # print(df[df.columns[df.isnull().any()]])
    # for column in df.columns:
    #     print(f"Column '{column}' is unique: {check_unique(df, column)}")

    # check the all the unique values for each column
    # for column in df.columns:
    #     print(f"Unique values for column '{column}': {df[column].unique()}")
    # check rows that have null values
    # print(df[df.isnull().any(axis=1)])
    # print(df.info())
    # check for duplicates in each column
    # check the total spend and quanitty null rows and only print those rows and price epr unit 
    # print(df.loc[df["total_spent"].isnull() | df["quantity"].isnull(), ["transaction_id","customer_id", "total_spent", "quantity", "price_per_unit"]])


main()