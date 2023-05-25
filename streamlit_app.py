import streamlit

streamlit.title('My Parent\'s New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

### My own idea, may need to remove if it causes problems for snowflake

# Add a row to the bottom of the table that sums every column except "fruit" and any column# that starts with "serving"
cols_to_sum = [col for col in fruits_to_show.columns if col != 'Fruit' and not col.startswith('Serving')]
sum_row = pd.DataFrame(fruits_to_show[cols_to_sum].sum()).T
sum_row.index = ['Total']
fruits_to_show = pd.concat([fruits_to_show, sum_row])

### end my section


# Display the table on the page.
streamlit.dataframe(fruits_to_show)
