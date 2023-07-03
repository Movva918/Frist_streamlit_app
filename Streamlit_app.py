import streamlit
import pandas




streamlit.title('My parents New healty Meal Plan')

streamlit.header('BreakFast Favourites')
streamlit.text('🥣 Omega3 & Bluberry oatMeal')
streamlit.text('🥗 Kale, Spinach & Roceket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
# New Section to display Fruityice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# change jason version to normalized form
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# shows the data in table form
streamlit.dataframe(fruityvice_normalized)




