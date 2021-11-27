import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

#st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

st.latex(r'''
    a + ar + ar^2 + ar^3 + \cdots + ar^{n-1} =
    \sum_{k=1}^{n} ar^{k-1} =
    a \left(\frac{1-r^n}{1-r}\right)
    ''')

df1 = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)

st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

#新宿付近の緯度経度を100個マッピングする
df2 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

st.map(df2)

st.write('WordCloud')
img = Image.open('wordcloud.png')
st.image(img, caption='Mr.Children', use_column_width=True)

#チェックボックスをつけて画像を表示
st.write('Word Cloud')
if st.checkbox('Show Image'):
    img = Image.open('wordcloud.png')
    st.image(img, caption='Mr.Children', use_column_width=True)

#セレクトボックスの使い方
st.write('Select Box')
option = st. selectbox(
    'あなたが好きな数字を選んでください。',
    list(range(1, 11))
)
'あなたの好きな数字は,', option, 'です。'

#テキストインプットの使い方
# st.write('Text Input')
# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は', text, 'です。'

#スライダー
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition

#サイドバーの使い方
#st.sidebar.write('Interative Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味：', text
# 'コンディション：', condition

#2つのカラムの表示方法
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

#プログレスバーの表示
st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'