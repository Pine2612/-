import streamlit as st
import pandas as pd
import datetime

st.title("大模型学习需求调查问卷")

st.markdown("请认真填写以下问题，帮助我们更好了解学习需求。")

q1_city = st.text_input("Q1: 您现在在哪个城市，是否在职，所从事的工作是什么？")
q2_knowledge = st.text_area("Q2: 对大模型有多少认知，了解多少原理与技术点？")
q3_need = st.text_area("Q3: 学习大模型的最核心需求是什么？")
q4_code = st.selectbox(
    "Q4: 是否有 Python 编程基础或其他编程经验？",
    ["没有编程经验", "略有了解", "有一定基础，写过一些代码", "熟练掌握"]
)
q5_time = st.text_input("Q5: 每天能花多少时间用于学习，大致空闲时间点处于什么时段？")
q6_other = st.text_area("Q6: 除以上五点外是否还有其他问题想要补充？")

submitted = st.button("生成报告")

if submitted:
    data = {
        "城市与职业": [q1_city],
        "大模型认知": [q2_knowledge],
        "核心学习需求": [q3_need],
        "编程基础": [q4_code],
        "学习时间与时段": [q5_time],
        "其他补充": [q6_other],
        "提交时间": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    }

    df = pd.DataFrame(data)
    csv = df.to_csv(index=False).encode("utf-8-sig")

    st.success("问卷已生成！请点击下方按钮下载问卷数据：")
    st.download_button(
        label="📥 下载 CSV 报告",
        data=csv,
        file_name="大模型学习需求调查问卷.csv",
        mime="text/csv"
    )
