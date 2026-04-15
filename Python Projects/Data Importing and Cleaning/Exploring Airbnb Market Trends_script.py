import pandas as pd

# Load and explore all files
price_df = pd.read_csv("Python Projects/data/airbnb_price.csv")
print(price_df.head(), "\nColumns:Rows", price_df.shape)

room_df= pd.read_excel("Python Projects/data/airbnb_room_type.xlsx")
print(room_df.head(), "\nColumns:Rows", room_df.shape)

review_df = pd.read_csv("Python Projects/data/airbnb_last_review.tsv", sep="\t")
print(review_df.head(), "\nColumns:Row", review_df.shape)

print()