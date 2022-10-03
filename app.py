
import streamlit as st

st.write("test")

applist = ["バイトの扶養考慮", "k-median問題", ""]
add_selectbox = st.sidebar.selectbox(
    "アプリリスト",
    applist
)

###########################################
########### バイトの扶養考慮 ###############    (今後)バイトの種類数を選択できるようにしたい
###########################################
if add_selectbox == applist[0]:
    st.title(applist[0])

    import datetime
    maximumsupport = 1030000

    # 時給と1回当たりのシフト時間から平均どれぐらいシフトを入れるべきかを算出
    wage = st.number_input("時給を入力", 800, 5000, 1000)
    meanhour = st.number_input("1回のシフト時間", 0.5, 13., 4., 0.5, )
    oncewage = wage * meanhour
    times_year = maximumsupport // oncewage
    times_month = times_year // 12
    times_week = times_year // 52
    # st.write(times_year, times_month, times_week)
    col1, col2 = st.columns(2)
    col1.metric(label="月間平均", value=times_month)
    col2.metric(label="週間平均", value=times_week)



    # 現在から扶養内で最大限働く場合
    nowwage = st.number_input("現在までの収入を入力", 0, maximumsupport)
    remaining = maximumsupport - nowwage

    # 今年が残り何が月か
    today = datetime.date.today()
    nowmonth = today.month


    # nowmonth = 12
    # 残りの月数で最大限もらうための必須シフト日数(12月以外)
    if nowmonth == 12:
        maximaize_month = remaining // oncewage
        maximaize_week = maximaize_month // 5
        col1, col2 = st.columns(2)
        col1.metric(label="月間平均", value=maximaize_month)
        col2.metric(label="週間平均", value=maximaize_week)

    else:
        if st.checkbox(f"{nowmonth}月をカウントする場合"):
            nowmonth -= 1
        reminemonth = 12 - nowmonth
            # st.write(reminemonth)
        maximaize_inyear = remaining // reminemonth
        maximaize_month = maximaize_inyear // oncewage
        maximaize_week4 = maximaize_month // 4
        maximaize_week5 = maximaize_month // 5

        col1, col2 = st.columns(2)
        col1.metric(label="月間平均", value=maximaize_month)
        if maximaize_week4 == maximaize_week5:
            col2.metric(label="週間平均", value=maximaize_week4)
        else:
            col2.metric(label="週間平均", value=f"{maximaize_week5}~{maximaize_week4}")





elif add_selectbox == applist[1]:
    st.title(applist[1])
    