import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.grouping_and_sorting import *
print("Setup complete.")

# Your code here
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
print(reviews_written)
# Check your answer
q1.check()

taster_twitter_handle
@AnneInVino          3685
@JoeCz               5147
@bkfiona               27
@gordone_cellars     4177
@kerinokeefe        10776
@laurbuzz            1835
@mattkettmann        6332
@paulgwine           9532
@suskostrzewa        1085
@vboone              9537
@vossroger          25514
@wawinereport        4966
@wineschach         15134
@winewchristina         6
@worldwineguys       1005
Name: taster_twitter_handle, dtype: int64

best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
print(best_rating_per_price)
# Check your answer
q2.check()

price
4.0       86
5.0       87
6.0       88
7.0       91
8.0       91
          ..
1900.0    98
2000.0    97
2013.0    91
2500.0    96
3300.0    88
Name: points, Length: 390, dtype: int64

price_extremes = reviews.groupby('variety').price.agg(["min", "max"])
#declaring as string cause the warning by pandas update
print(price_extremes)

# Check your answer
q3.check()

   min    max
variety                 
Abouriou     15.0   75.0
Agiorgitiko  10.0   66.0
Aglianico     6.0  180.0
Aidani       27.0   27.0
Airen         8.0   10.0
...           ...    ...
Zinfandel     5.0  100.0
Zlahtina     13.0   16.0
Zweigelt      9.0   70.0
Çalkarası    19.0   19.0
Žilavka      15.0   15.0

[707 rows x 2 columns]

sorted_varieties = price_extremes.sort_values(by=["min", "max"], ascending=False)
print(sorted_varieties)
# Check your answer
q4.check()

                       min    max
variety                                     
Ramisco                         495.0  495.0
Terrantez                       236.0  236.0
Francisa                        160.0  160.0
Rosenmuskateller                150.0  150.0
Tinta Negra Mole                112.0  112.0
...                               ...    ...
Roscetto                          NaN    NaN
Sauvignon Blanc-Sauvignon Gris    NaN    NaN
Tempranillo-Malbec                NaN    NaN
Vital                             NaN    NaN
Zelen                             NaN    NaN

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# Check your answer
q5.check()

reviewer_mean_ratings.describe()

count    19.000000
mean     88.233026
std       1.243610
min      85.855422
25%      87.323501
50%      88.536235
75%      88.975256
max      90.562551
Name: points, dtype: float64

country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
print(country_variety_counts)
# Check your answer
q6.check()

country  variety                 
US       Pinot Noir                  9885
         Cabernet Sauvignon          7315
         Chardonnay                  6801
France   Bordeaux-style Red Blend    4725
Italy    Red Blend                   3624
                                     ... 
Mexico   Cinsault                       1
         Grenache                       1
         Merlot                         1
         Rosado                         1
Uruguay  White Blend                    1
Length: 1612, dtype: int64
