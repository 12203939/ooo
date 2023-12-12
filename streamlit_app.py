import streamlit as st
from scipy import stats

# アプリケーションのタイトルを設定
st.title('正規分布の確率計算アプリ')

# ユーザーからの入力を受け取る
mean = st.number_input('平均', value=0.0)
std = st.number_input('標準偏差', value=1.0)
x = st.number_input('確率変数の値', value=0.0)

# 正規分布の確率を計算
probability = stats.norm.cdf(x, loc=mean, scale=std)

# 結果を表示
st.write('平均が {} で標準偏差が {} の正規分布において、確率変数が {} 以下である確率は {:.4f} です。'.format(mean, std, x, probability))