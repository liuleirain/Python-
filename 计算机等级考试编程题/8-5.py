# 词云是设计和统计的结合，也是艺术与计算机科学的碰撞。wordcloud是一款基于python的词云
# 第三方库，支持对词语数量、背景蒙版、字体颜色等各种细节的设置，试结合上一题构建《Hamlet》
# 的词云效果。
from wordcloud import WordCloud


f = open('hamlet.txt', 'r')
txt = f.read()

wordcloud = WordCloud(background_color='white',
                     width=800,
                     height=600,
                     max_words=200,
                     max_font_size=80,
                     ).generate(txt)

wordcloud.to_file('hamlet词云图片.png')
