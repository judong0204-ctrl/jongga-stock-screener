import streamlit as st

st.set_page_config(page_title="종가 주식 스크리너", layout="wide")

st.title("📈 종가 주식 스크리너")
st.write("국내주식 종가매매 후보 분석기")

st.subheader("기본 검색 조건")
st.write("- 시가총액: 2,000억 원 이상")
st.write("- 주가: 1,000원 이상")
st.write("- 20일 평균 거래대금: 30억 원 이상")
st.write("- 관리종목 및 거래정지 제외")
st.write("- 5·10·20·60·120일 이동평균선 분석")

st.info("프로그램 기본 화면입니다. 다음 단계에서 실제 주식 데이터를 연결합니다.")
