import streamlit as st
import joblib
import pandas as pd

# 1. Tải mô hình từ file .pkl cùng thư mục
model = joblib.load('mo_hinh_gia_nha_boston (1).pkl')

# 2. Thiết kế giao diện Web
st.title("Ứng dụng Dự báo Giá nhà Boston 🏠")
st.write("Nhập thông số căn nhà bên dưới để dự báo giá tự động:")

col1, col2 = st.columns(2)

with col1:
    lot_area = st.number_input("Diện tích khu đất (LotArea):", value=8450)
    year_built = st.number_input("Năm xây dựng (YearBuilt):", value=2003, step=1)
    flr_1st = st.number_input("Diện tích tầng 1 (1stFlrSF):", value=856)
    flr_2nd = st.number_input("Diện tích tầng 2 (2ndFlrSF):", value=854)

with col2:
    full_bath = st.number_input("Số phòng tắm đầy đủ (FullBath):", value=2, step=1)
    bedroom = st.number_input("Số phòng ngủ trên tầng (BedroomAbvGr):", value=3, step=1)
    tot_rooms = st.number_input("Tổng số phòng (TotRmsAbvGrd):", value=8, step=1)

# 3. Xử lý logic dự đoán khi bấm nút
if st.button("Dự báo giá nhà 🚀"):
    data_input = {
        'LotArea': [lot_area], 'YearBuilt': [year_built], '1stFlrSF': [flr_1st],
        '2ndFlrSF': [flr_2nd], 'FullBath': [full_bath], 'BedroomAbvGr': [bedroom],
        'TotRmsAbvGrd': [tot_rooms]
    }
    df_new = pd.DataFrame(data_input)
    prediction = model.predict(df_new)
    st.success(f"💰 Giá nhà dự đoán là: {prediction[0]:,.2f} USD")
