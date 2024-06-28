import pandas as pd
import streamlit as st

# Load the Excel file
file_path = '/Users/connorhuang/Desktop/2024仓库领用总表.xlsx'
df = pd.read_excel(file_path)

st.title("2024仓库领用数据计算器")

model = st.text_input("型号")
color = st.text_input("颜色")
quantity = st.number_input("产品数量", min_value=1)

if st.button("Calculate"):
    filtered_df = df[(df['型号'] == model) & (df['颜色'] == color)]
    
    if filtered_df.empty:
        st.error("No data found for the given 型号 and 颜色.")
    else:
        materials = []
        for index, row in filtered_df.iterrows():
            material_name = row['材料名称']
            single_use = row['单个用量']
            total_use = single_use * quantity
            materials.append((material_name, total_use, single_use))
        
        st.write(f"Results for 产品数量: {quantity}")
        for material in materials:
            st.write(f"材料名称: {material[0]}, 材料总量: {material[1]}, 单个用量: {material[2]}")
