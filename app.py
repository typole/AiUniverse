import streamlit as st
import hydralit_components as hc
import datetime

# 配置网站基础信息
st.set_page_config(layout='wide', initial_sidebar_state='collapsed', )


def load_css(file_path):
    with open(file_path, "r") as f:
        css = f.read()
    return f"<style>{css}</style>"


def custom_card(link, name, logo_path, description, tags):
    card_html = f"""
    <div class="cardContainer-CcyBWq">
        <a href="{link}" target="_blank" style="text-decoration: none; color: inherit;">
            <div class="card-fxOSSf">
                <div class="cardTop-NT1ftm">
                    <img src="{logo_path}">
                    <div class="text-kMyXvU">
                        <div class="name-JtJcxk">{name}</div>
                        <div class="belong-Rc_0pL">devv.ai</div>
                    </div>
                </div>
                <div class="description-VP9XRQ">{description}</div>
                <div class="tagsContainer-rw2ccN">
                    {''.join(f'<div class="tag-TczjiE">{tag}</div>' for tag in tags)}
                </div>
            </div>
        </a>
    </div>
    """
    return card_html


def custom_nav():
    nav_html = """
    <div class="jj-community-header-container">
        <div class="jj-community-header-left">
            <div class="jj-community-header-logo-container">
                <img class="jj-community-header-logo" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d54f1d72a4d434ea66b4ebac48629e8~tplv-k3u1fbpfcp-jj:0:0:0:0:q75.image#?w=215&amp;h=44&amp;s=2810&amp;e=png&amp;a=1&amp;b=ffffff" alt="logo">
                <div class="jj-community-header-dot"></div>
                <img class="jj-community-header-logo jj-community-header-sub-logo" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7861901cbc92403b9f4b52c86f36417f~tplv-k3u1fbpfcp-jj:0:0:0:0:q75.image#?w=177&amp;h=34&amp;s=2902&amp;e=png&amp;a=1&amp;b=ffffff" alt="logo">
            </div>
            <div class="jj-community-header-tabs">
                <a class="jj-community-header-tab-item jj-community-header-tab-item-active ">行业全景</a>
                <a class="jj-community-header-tab-item  ">最新动态</a>
            </div>
        </div>
        <div class="jj-community-header-right">
            <button type="button" class="jj-community-header-publish-btn">
                <img class="jj-community-header-publish-icon" src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQuODk2NTUgOC41Njg5N0wyIDYuNzc1ODZMMTQgMi41TDEyLjIwNjkgMTIuNzA2OUw5LjE3MjQxIDEwLjkxMzgiIHN0cm9rZT0iIzI1MjkzMyIgc3Ryb2tlLXdpZHRoPSIxLjMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPgo8cGF0aCBkPSJNNi45NjUzMyAxMy42NzIyVjkuODEwMTFMMTMuODYxOSAyLjYzNzciIHN0cm9rZT0iIzI1MjkzMyIgc3Ryb2tlLXdpZHRoPSIxLjMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPgo8L3N2Zz4K" alt="">
                <span class="jj-community-header-publish-text">发布</span>
            </button>
            <div class="jj-community-header-user">
                <div class="jj-community-header-actions">
                    <a class="jj-community-header-action jj-community-headeraction-login" type="button">登录</a>
                    <div class="jj-community-header-divider"></div>
                    <a class="jj-community-header-action jj-community-header-action-register" type="button">注册</a>
                </div>
            </div>
        </div>
    </div>
    """
    return nav_html


# 数据示例
card_data = [
    {
        "link": "https://www.baidu.com/",
        "name": "devv.ai",
        "logo_path": "assets/images/devv_ai.png",
        "description": "面向开发者的下一代AI搜索引擎。",
        "tags": ["效率工具", "不开源", "不可免费商用"]
    },
    {
        "link": "https://www.baidu.com/",
        "name": "devv.ai",
        "logo_path": "assets/images/devv_ai.png",
        "description": "面向开发者的下一代AI搜索引擎。",
        "tags": ["效率工具", "不开源", "不可免费商用"]
    },
    {
        "link": "https://www.baidu.com/",
        "name": "devv.ai",
        "logo_path": "assets/images/devv_ai.png",
        "description": "面向开发者的下一代AI搜索引擎。",
        "tags": ["效率工具", "不开源", "不可免费商用"]
    },
    {
        "link": "https://www.baidu.com/",
        "name": "devv.ai",
        "logo_path": "assets/images/devv_ai.png",
        "description": "面向开发者的下一代AI搜索引擎。",
        "tags": ["效率工具", "不开源", "不可免费商用"]
    },
    {
        "link": "https://www.baidu.com/",
        "name": "devv.ai",
        "logo_path": "assets/images/devv_ai.png",
        "description": "面向开发者的下一代AI搜索引擎。",
        "tags": ["效率工具", "不开源", "不可免费商用"]
    },
    {
        "link": "https://www.baidu.com/",
        "name": "devv.ai",
        "logo_path": "assets/images/devv_ai.png",
        "description": "面向开发者的下一代AI搜索引擎。",
        "tags": ["效率工具", "不开源", "不可免费商用"]
    },
]

# 加载外部CSS文件
css_code = load_css("assets/css/styles.css")

# 在HTML标签中嵌入JavaScript代码，启用JavaScript
javascript_code = """
<script>
document.body.onload = function(){
  // Streamlit加载完成后执行的JavaScript代码
  console.log("JavaScript enabled!");
};
</script>
"""

# 呈现自定义卡片和JavaScript代码
st.markdown(css_code, unsafe_allow_html=True)
st.markdown(javascript_code, unsafe_allow_html=True)
st.markdown(custom_nav(), unsafe_allow_html=True)
for data in card_data:
    st.markdown(custom_card(data["link"], data["name"], data["logo_path"], data["description"], data["tags"]),
                unsafe_allow_html=True)
