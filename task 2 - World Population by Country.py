"""
About Dataset
CONTENT

The US Census Bureau's world population clock estimated that the global population as of September 2022 was 7,922,

312,800 people and was expected to reach 8 billion by mid-November of 2022. This total far exceeds the 2015 world 
population of 7.2 billion. The world's population continues to increase by roughly 140 people per minute, with births 
outweighing deaths in most countries.

Overall, however, the rate of population growth has been slowing for several decades. This slowdown is expected to
continue until the rate of population growth reaches zero (an equal number of births and deaths) around 2080-2100,
at a population of approximately 10.4 billion people. After this time, the population growth rate is expected to turn
negative, resulting in global population decline.

Countries with more than 1 billion people China is currently the most populous country in the world, 
with a population estimated at more than 1.42 billion as of September 2022. Only one other country in the world 
boasts a population of more than 1 billion people: India, whose population is estimated to be 1.41 billion people—and 
rising."""

# World Population Dataset EDA & MAP VISULZATION

# Импорт всех необходимых библиотек

import numpy as np
import pandas as pd
import seaborn as sns
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import plotly.express as px
import missingno as msno
import plotly.offline as py
py.init_notebook_mode(connected=True)
