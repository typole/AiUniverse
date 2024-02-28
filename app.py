import streamlit as st

# 数据，这里假设有一个包含多个卡片信息的列表
cards_data = [
    {
        "logo": "https://example.com/logo1.png",
        "name": "Card 1",
        "description": "这是卡片 1 的中文描述。",
        "functionality": "卡片 1 的功能介绍。",
        "tags": ["标签1", "标签2"]
    },
    {
        "logo": "https://example.com/logo2.png",
        "name": "Card 2",
        "description": "这是卡片 2 的中文描述。",
        "functionality": "卡片 2 的功能介绍。",
        "tags": ["标签3", "标签4"]
    },
    # 可以添加更多卡片信息
]

# 设置页面布局，每行显示四个卡片
st.set_page_config(layout="wide")

# 呈现卡片信息
for i in range(0, len(cards_data), 4):
    row_data = cards_data[i:i+4]
    col1, col2, col3, col4 = st.columns(4)
    for j, card in enumerate(row_data):
        with locals()[f"col{j+1}"]:
            st.image(card["logo"], use_column_width=True)
            st.header(card["name"])
            st.write(card["description"])
            st.write(card["functionality"])
            st.write("标签: ", ", ".join(card["tags"]))

