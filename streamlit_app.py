import streamlit as st

st.title("👋🏻 나의 스트림릿 첫번째 앱 만들기")
st.subheader("마장중학교 고윤희입니다.")
st.info("중3 과학 페이지에 오신것을 환영합니다.")
#교과서 링크
st.link_button("비상교과서", "http://ebook.vivasam.com/v2/textbookviewer/viewer.jsp?contentId=/dvd/2015/20200225/M0SC0103_2018/data/ebook.pdf#")

st.success("초록색 창")
st.error("빨간색 창")
st.info("파란색 창")
st.warning("노란색 창") # ctrl+/ : 주석처리

st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDZ3dXhyNG9mN2g5dXppNHl5bHl0NXVkdzd4c2RrNTk2eGFtN2JlYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/J39gurpvL7SHpnTTJB/giphy.gif")
st.video("https://www.youtube.com/watch?v=ekr2nIex040&ab_channel=ROS%C3%89")
st.video("/workspaces/myfirststreamlit/data/스크린샷 2024-10-22 150411.png")