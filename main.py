import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import seaborn as sns
import spacy
from itertools import combinations
from collections import Counter
import math
import networkx as nx
import ipywidgets as widgets
from ipywidgets import interact
from wordcloud import WordCloud
from PIL import Image
import requests
import warnings
from sklearn.manifold import TSNE
import plotly.express as px
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

warnings.filterwarnings("ignore")
nlp = spacy.load("en_core_web_sm")

# Importing all functions
from Modules.Utils.get_df import get_df
from Modules.Utils.get_corpus import get_corpus
from Modules.Utils.get_tokens import get_tokens
from Modules.Utils.get_bow import get_bow
from Modules.Utils.get_bow_df import get_bow_df
from Modules.Utils.get_dict import get_dict
from Modules.Utils.get_topN_word_bow_df import get_topN_word_bow_df
from Modules.Utils.get_word_frq import get_word_frq
from Modules.Utils.get_combinations import get_combinations
from Modules.Chart.draw_Network import draw_Network
from Modules.Chart.draw_word_cloud import draw_word_cloud
from Modules.Chart.radar_chart import radar_chart
from Modules.Chart.compare_radar import compare_radar
from Modules.Utils.get_wide_df import get_wide_df
from Modules.Utils.get_long_df import get_long_df
from Modules.Chart.Bubble_chart import Bubble_chart
from Modules.Utils.WS import WS
from Modules.Chart.update_bubble_chart import update_bubble_chart
from Modules.Chart.scatterplot3D import scatterplot3D

# Your original workflow continues here
