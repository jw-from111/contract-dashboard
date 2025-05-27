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
age_counts = df['보험연령'].value_counts()
st.bar_chart(age_counts)

# 기종별 계약 수
st.subheader("3️⃣ 기종별 계약 현황")
model_counts = df['기종'].value_counts()
st.bar_chart(model_counts)

# 지사별 월금액 합계
st.subheader("4️⃣ 지사별 실적")
branch_stats = df.groupby('지사명')['월금액'].sum().sort_values(ascending=False)
st.dataframe(branch_stats)
