from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = open('roadmap_of_data_scientist.txt', 'r').read()
stopwords = set(STOPWORDS)

custom_mask = np.array(Image.open('Sir_Zin.jpg'))
wc = WordCloud(background_color = 'red',
               stopwords = stopwords,
               mask = custom_mask,
               contour_width = 3,
               contour_color = 'black')

# wc = WordCloud(background_color = (255, 242, 0),
#                max_words =30,
#                max_font_size = 100,
#                stopwords = stopwords,
#                mask = custom_mask)

wc.generate(text)
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)

#Plotting
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()


# wc.to_file('result.png')