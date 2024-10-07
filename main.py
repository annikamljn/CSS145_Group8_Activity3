import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
import networkx as nx
import plotly.graph_objects as go
from io import StringIO

st.title("Group #8, Section BM3: Activity 3")
st.markdown("""
    - **BUNAG, Annika** - `2023102813` - `@annikamljn`
    - **CHUA, Denrick Ronn** -
    - **MALLILLIN, Loragene** - `2023108040` - `@ldmallillin`
    - **SIBAYAN, Gian Eugene** -
    - **UMALI, Ralph Dwayne** -
"""
)

st.markdown("Click [here](https://github.com/annikamljn/CSS145_Group8_Activity3) to be redirected to our project's GitHub repository, and [here](https://colab.research.google.com/drive/1TbRuhYoAk_43i9g--eJ2GA_3-DnHkrWA?usp=sharing) for our Google Colab notebook.")

#import dataset
df = pd.read_csv("laptop_price - dataset.csv")

############ DESCRIBING THE DATASET #############
st.header("Describing the dataset")

#df
st.markdown("`df`")
df

#df.describe
st.markdown("`df.describe()`")
df_desc = df.describe(include='all').fillna("").astype("str") 
st.write(df_desc)

#df.info
st.markdown("`df.info()`")
buffer = StringIO()
df.info(buf=buffer)
df_info = buffer.getvalue()
st.code(df_info)

#df.isna().sum()
st.markdown("`df.isna().sum()`")
st.code(df.isna().sum())

############ Average Price by Laptop Type (Bar Chart) #############
st.header("1. Average Price by Laptop Type (Bar Chart)")

price_type = df.groupby('TypeName')['Price (Euro)'].mean()

plt.figure(figsize=(10, 6))
price_type.plot(kind='bar')

plt.title('Average Price by Laptop Type')
plt.xlabel('Laptop Type')
plt.ylabel('Average Price (Euro)')
plt.xticks(rotation=45)
st.pyplot(plt)
plt.clf()

st.markdown("The bar graph compares laptop prices by type, showing **Workstations** (around €2,000) and **Gaming laptops** (around €1,800) as the most expensive due to their high performance. **Netbooks** are the cheapest at about €500, while **Ultrabooks** and **Notebooks** sit in the middle at around €1,000. The chart makes it easy to see the price differences across categories.")


############ Average Price by Company (Bar Chart) #############
st.header("2. Average Price by Company (Bar Chart)")
price_type = df.groupby('Company')['Price (Euro)'].mean()

plt.figure(figsize=(10, 6))
price_type.plot(kind='bar')

plt.title('Average Price by Company')
plt.xlabel('Company')
plt.ylabel('Average Price (Euro)')
plt.xticks(rotation=45)
st.pyplot(plt)
plt.clf()

st.markdown("The graph shows that **Razer** laptops are the **priciest**, averaging **over €3,000**, with LG and Microsoft also on the high end. Apple and Huawei follow closely. Meanwhile, **Chuwi, Mediacom, and Vero** have the **cheapest** options, all under €500.")

############ Distribution of Laptops by CPU Company (Pie Chart) #############
st.header("3. Distribution of Laptops by CPU Company (Pie Chart)")

cpu_company_count = df['CPU_Company'].value_counts()
st.write("`df['CPU_Company'].value_counts()`")
st.write(cpu_company_count)

percentages = (cpu_company_count / cpu_company_count.sum()) * 100

legend_labels = [f'{company} - {percent:.1f}%' for company, percent in zip(cpu_company_count.index, percentages)]

plt.figure(figsize=(10, 6))
cpu_company_count.plot(kind='pie', startangle=90, labels=['']*len(cpu_company_count))

plt.title('Distribution of Laptops by CPU Company')

plt.legend(labels=legend_labels, loc='center left', bbox_to_anchor=(1.0, 0.5))

plt.ylabel('')  
st.pyplot(plt)
plt.clf()

st.markdown("The pie chart shows that **Intel** dominates the laptop market, powering 95.2% of laptops, while **AMD** comes in second with 4.7%. **Samsung** barely makes a mark, with only 0.1%. It's clear that Intel's processors are the go-to choice for most laptops.")

############ Distribution of Laptop Prices (Histogram) #############
st.header("4. Distribution of Laptop Prices (Histogram)")

def dist_prices():
    plt.figure(figsize=(10, 6))  # Adjust the figure size for better readability
    plt.hist(df['Price (Euro)'], bins=30, color='gray', edgecolor='black')
    plt.xticks(range(0, 6001, 500), rotation=45)
    plt.xlabel('Price (Euro)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Laptop Prices')
    st.pyplot(plt)
    plt.clf()  # Clear the plot to avoid overlapping with subsequent plots

    # Display a brief explanation after the chart
    st.markdown("""
        The histogram shows the distribution of laptop prices across the dataset. **Most laptops are priced between €500 and €1000**, 
        followed by laptops priced between €1000 and €1500, with fewer laptops available for under €500.
    """)

dist_prices()

############ Laptop Price vs. CPU Frequency (Box Plot) #############
st.header("5. Laptop Price vs. CPU Frequency (Box Plot)")

def price_vs_cpu():
    bins = [0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    bin_labels = ['<1.5 GHz', '1.5-2.0 GHz', '2.0-2.5 GHz', '2.5-3.0 GHz', '3.0-3.5 GHz', '3.5-4.0 GHz']
    df['CPU_Frequency_binned'] = pd.cut(df['CPU_Frequency (GHz)'], bins=bins, labels=bin_labels)

    plt.figure(figsize=(10, 6))  # Adjust the figure size
    sns.boxplot(data=df, x="CPU_Frequency_binned", y="Price (Euro)", hue="CPU_Frequency_binned", palette="Set3", dodge=False)
    plt.xlabel("CPU Frequency (GHz)")
    plt.ylabel("Price (Euro)")
    plt.title("Laptop Price vs. CPU Frequency (GHz)")
    plt.xticks(rotation=45)
    plt.yticks(range(0, 6001, 500))
    plt.grid(axis='y')
    st.pyplot(plt)
    plt.clf()  # Clear the plot

    # Display a brief explanation after the chart
    st.markdown("""
        The box plot shows that **laptops with higher CPU frequencies (3.0-3.5 GHz) tend to be the most expensive**, often ranging 
        between €1500 and €2500 or more. Laptops with lower CPU frequencies have a wider price range, especially those with 2.5-3.0 GHz 
        CPUs, which vary from under €500 to over €3000.
    """)

price_vs_cpu()

# Streamlit app title
st.title("Laptop Price Analysis")




############ Conclusions #############
st.header("Conclusions")
st.markdown("**1. Laptop Price Distribution:**")
st.markdown(
"""
    - Most of the laptops in the dataset are priced between €500 and €1000.
    - The next most common price range is between €1000 and €1500, while fewer laptops cost less than €500.
""")
st.markdown("**2. Distribution by CPU Company:**")
st.markdown("""
    - Intel is the leading CPU brand, powering 95.2% of all laptops.
    - AMD follows with 4.7%, while Samsung processors make up only 0.1%.
    - This shows that Intel is the preferred choice for the vast majority of laptops.
""")
st.markdown("**3. Weight vs. Laptop Type:**")
st.markdown("""
    - Gaming laptops are generally the heaviest, while Ultrabooks are the lightest. Notebooks fall in between, offering a good balance between portability and performance.
    - The weight differences suggest that different types of laptops are designed with different priorities in mind.
""")
st.markdown("**4. OS Distribution:**")
st.markdown("""
    - Windows 10 is the most common operating system, found on 82.2% of laptops.
    - Other operating systems like Linux (4.5%), no OS (5.2%), and others like Chrome OS and macOS have much smaller shares, each under 5%.
""")
st.markdown("**Variation in Laptop Prices:**")
st.markdown("""
    - Workstation and gaming laptops are sold at a higher price, generally costing more than €1500. Netbooks are the cheapest type, averaging around €500.
    - Laptops sold by Razer tend to be the most expensive in the market, averaging over €3000, followed by LG. The companies with the least expensive laptops are Chuwi, Mediacom, and Vero. Prices can also depend on the laptop's offered CPU frequency, with 3.0-3.5 GHz CPUs being the most expensive on average. On the other hand, laptops with 2.5-3.0 GHz CPUs offer the widest price range.
    - Laptops that feature 3840x2160 and 2880x1800 screens tend to be priced higher. As 1920x1080 resolutions are the most common in the market, they are offered at the widest price range. Laptops with the lowest resolution, 1366x768, are priced the lowest.
    - Laptops with GPUS by Intel and Nvidia typically sell at higher price rates compared to AMD and ARM-operated units. Nvidia also has a notably wider price range than the other manufacturers. ARM laptops are usually sold within a lower price range.
    - RAM capacities that range from 16 GB or more tend to have significantly higher prices. Laptops that offer 16 GB RAM have the widest price range.
    - Generally, there is a positive correlation between the weight of laptops and their price, wherein heavier laptops tend to be priced higher.
""")