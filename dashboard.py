import streamlit as st
import pandas as pd

st.title("📊 계약 현황 대시보드")

uploaded_file = "데이터 분석 학습용.xlsx"

@st.cache_data
def load_data():
    return pd.read_excel(uploaded_file)

df = load_data()

# 계약 개요
st.subheader("1️⃣ 계약 개요")
st.metric("총 계약 수", len(df))
cancel_rate = df['계약 상태'].value_counts(normalize=True).get("해지완료", 0) * 100
st.metric("해지율", f"{cancel_rate:.1f}%")
avg_monthly = df['월금액'].mean()
st.metric("평균 월금액", f"₩{avg_monthly:,.0f}")

# 보험 연령 분포
st.subheader("2️⃣ 보험 연령 분포")
age
