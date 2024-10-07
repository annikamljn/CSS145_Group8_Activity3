import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
import networkx as nx
import plotly.graph_objects as go
from io import StringIO
import re

st.title("Group #8, Section BM3: Activity 3")
st.markdown("""
    - **BUNAG, Annika** - `2023102813` - `@annikamljn`
    - **CHUA, Denrick Ronn** - `2023108259` - `@chuadenrick`
    - **MALLILLIN, Loragene** - `2023108040` - `@ldmallillin`
    - **SIBAYAN, Gian Eugene** - `2023108887` - `@GianSibayan`
    - **UMALI, Ralph Dwayne** - `2021135163` - `@UmaliDwayneRalph`
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

############ Laptop Price vs. Screen Resolution (Box Plot) #############
st.header("6. Laptop Price vs. Screen Resolution (Box Plot)")

def price_vs_resolution():
    # Extract the numerical part of the screen resolution
    def extract_resolution(resolution):
        match = re.search(r'\d+x\d+', resolution)  # Extract resolution like '1920x1080'
        if match:
            return match.group(0)
        return resolution  # Return the original if no match found

    # Apply the function to the 'ScreenResolution' column to clean the data
    df['CleanResolution'] = df['ScreenResolution'].apply(extract_resolution)

    # Sorting the resolutions for better display
    sorted_resolutions = df['CleanResolution'].value_counts().index.tolist()

    # Create a boxplot grouped by the cleaned numerical screen resolution
    plt.figure(figsize=(10, 6))  # Adjust the figure size
    sns.boxplot(data=df, x='CleanResolution', y='Price (Euro)', hue='CleanResolution', palette='Set3', order=sorted_resolutions)

    # Add labels, title, and formatting
    plt.xlabel('Screen Resolution')
    plt.ylabel('Price (Euro)')
    plt.title('Laptop Price vs. Screen Resolution')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.yticks(range(0, 6001, 500))  # Customize y-axis tick intervals
    plt.grid(axis='y')  # Add grid lines for better readability

    # Display the plot in Streamlit
    st.pyplot(plt)
    plt.clf()  # Clear the plot

# Call the function
price_vs_resolution()

# Display explanation after the chart
st.markdown("""
    Laptops with higher screen resolutions (e.g., 3840x2160 and 2880x1800) tend to be more expensive. Common resolutions like 1920x1080
    are more affordable, while lower resolutions such as 1366x768 are generally cheaper.
""")

############ Laptop Price vs. GPU Company (Box Plot) #############
st.header("7. Laptop Price vs. GPU Company (Box Plot)")

def price_vs_gpu():
    # Bin the GPU Company column
    df['GPU_Company_binned'] = df['GPU_Company']

    # Create a boxplot for GPU Company vs. Price
    plt.figure(figsize=(8, 6))  # Adjust the figure size
    sns.boxplot(data=df, x="GPU_Company_binned", y="Price (Euro)", palette="Set3", hue="GPU_Company_binned", dodge=False)

    # Add labels, title, and formatting
    plt.xlabel("GPU Company")
    plt.ylabel("Price (Euro)")
    plt.title("Laptop Price vs. GPU Company")
    plt.xticks(rotation=45)
    plt.yticks(range(0, 6001, 500))
    plt.grid(axis='y')  # Add grid lines for better readability

    # Display the plot in Streamlit
    st.pyplot(plt)
    plt.clf()  # Clear the plot

# Call the function
price_vs_gpu()

# Display explanation after the chart
st.markdown("""
    Laptops with Intel and Nvidia GPUs generally have higher prices. Nvidia, in particular, shows the widest price range,
    indicating a lineup from mid-range to very high-end models. Meanwhile, AMD laptops are typically more affordable. 
    There is insufficient data on ARM-based laptops to form conclusions.
""")

############ Laptop Price vs. RAM (Box Plot) #############
st.header("8. Laptop Price vs. RAM (Box Plot)")

def price_vs_ram():
    df['RAM_binned'] = df['RAM (GB)']

    plt.figure(figsize=(10, 6))  # Adjust the figure size
    sns.boxplot(data=df, x="RAM_binned", y="Price (Euro)", hue="RAM_binned", palette="Set2", dodge=False)
    plt.xlabel("RAM (GB)")
    plt.ylabel("Price (Euro)")
    plt.title("Laptop Price vs. RAM (GB)")
    plt.yticks(range(0, 6001, 500))
    plt.grid(axis='y')
    st.pyplot(plt)
    plt.clf()  # Clear the plot

    # Display a brief explanation after the chart
    st.markdown("""
        Laptops with more RAM tend to cost more, with noticeable price increases for laptops with 16 GB or more RAM. However, even within the same RAM category, prices can vary significantly, as shown by the wide range of some boxes and the presence of outliers.
    """)

price_vs_ram()

############ Laptop Price vs. Weight (Scatter Plot) #############

st.header("9. Laptop Price vs. Weight (Scatter Plot)")

def price_vs_weight():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the scatter plot
    sns.scatterplot(x='Weight (kg)', y='Price (Euro)', data=df, color='slateblue', s=50, alpha=0.6, ax=ax)
    
    # Add a regression line
    sns.regplot(x='Weight (kg)', y='Price (Euro)', data=df, scatter=False, color='darkorange', ci=None, ax=ax)
    
    # Set plot labels and title
    ax.set_xlabel('Weight (kg)')
    ax.set_ylabel('Price (Euro)')
    ax.set_title('Laptop Price vs. Weight (kg)')
    
    # Add a grid
    ax.grid(True)
    
    # Display the plot in Streamlit
    st.pyplot(fig)
    plt.clf()  # Clear the plot

    # Display a brief explanation after the chart
    st.markdown("""
        More often than not, laptops that are heavy receive higher asking prices. This trend suggests a positive correlation, which implies that as weight increases, the price will probably rise too. Still, there exists a major variation, with a few lighter models costing like heavier counterparts.
    """)

price_vs_weight()

############ Weight vs. Laptop Type (Box Plot) #############
st.header("10. Weight vs. Laptop Type (Box Plot)")

def weight_vs_type():
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='TypeName', y='Weight (kg)', data=df, palette='viridis')
    plt.xlabel('Laptop Type')
    plt.ylabel('Weight (kg)')
    plt.title('Weight Distribution on Different Laptop Types')
    plt.xticks(rotation=45)
    plt.grid(True)

    st.pyplot(plt)
    plt.clf()

# Call the function
weight_vs_type()

st.markdown("""
Laptops labeled as Gaming typically carry the most weight, while the lighter Ultrabooks are shown by the box plot. 
The weights represented for each laptop type reveal that Notebooks maintain a moderate balance between portability and performance. 
This visualization indicates different weight disparities among laptop types, suggesting that design aims can vary.
""")

############ Operating System Distribution (Pie Chart) #############
st.header("11. Operating System Distribution (Pie Chart)")

def os_distribution():
    # Grouping by 'OpSys' and counting the occurrences
    os_count = df['OpSys'].value_counts()

    # Calculating percentages
    percentages = (os_count / os_count.sum()) * 100
    legend_labels = [f'{os} - {percent:.1f}%' for os, percent in zip(os_count.index, percentages)]

    # Plotting the distribution of operating systems as a pie chart
    plt.figure(figsize=(10, 6))
    os_count.plot(kind='pie', startangle=90, labels=[''] * len(os_count))  # Empty labels for clean pie chart
    plt.title('Operating System Distribution')

    # Adding a legend with percentages on the side
    plt.legend(labels=legend_labels, loc='center left', bbox_to_anchor=(1.0, 0.5))

    # Hide the y-label
    plt.ylabel('')

    st.pyplot(plt)
    plt.clf()

# Call the function
os_distribution()

st.markdown("""
Windows 10 dominates the laptop market with an 82.2% share. Other operating systems like No OS (5.2%), Linux (4.5%), 
and various Windows versions, Chrome OS, and macOS each have less than 5% market share.
""")

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
