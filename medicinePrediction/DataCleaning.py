import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.plotting import plot_decision_regions

plt.style.use('ggplot')
#%config InlineBackend.figure_format = 'svg'
#%matplotlib inline
np.set_printoptions(suppress=True)
"""
df_train = pd.read_csv('Drugs_Dataset_train.csv',sep=None)
#df_train.info()
#print(df_train.head())


#del df_train['Unnamed: 0']
del df_train['date']

#print("number of drugs:", len(df_train['drugName'].unique()))
#print("number of conditions:", len(df_train['condition'].unique()))

#replace wrong name in condition column with NaN
df_train.loc[df_train['condition'].str.contains('</span>',case=False, na=False), 'condition'] = 'NAN'
df_train['condition'].replace('NAN', np.NaN, inplace=True)
df_train['condition'].replace('Not Listed / Othe', np.NaN, inplace=True)

dictionary=df_train.set_index('drugName')['condition'].to_dict()
#print(len(dictionary))

#fill NaN value with correct condition names using created dictionary
df_train.condition.fillna(df_train.drugName.map(dictionary), inplace=True)
#print(df_train.info())


#drop rows with still missing values in condition (100 rows = 0.0006% of total data)
df_train.dropna(inplace=True)


drug_per_condition = df_train.groupby(['condition'])['drugName'].nunique().sort_values(ascending=False)
#print(drug_per_condition)
#print(drug_per_condition[:30])


drug_per_condition[:10].plot(kind="bar", figsize = (14,6), fontsize = 10, color="#B2B2D8")
plt.xlabel("", fontsize = 20)
plt.ylabel("", fontsize = 20)
plt.title("Top 10 Number of Drugs / Condition", fontsize = 20)
plt.savefig('top10_condition.jpg')

condition_1=drug_per_condition[drug_per_condition<=10].keys()
#print(condition_1)

df_train1=df_train[~df_train['condition'].isin(condition_1)]
#print(df_train1.info())
"""
import re # Regular expression library
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')


stop = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()
import spacy
nlp = spacy.load("en_core_web_sm")


#remove words needs for sentiment analysis from stopwords
n = ["aren't","couldn't","didn't","doesn't","don't","hadn't","hasn't","haven't","isn't","mightn't","mustn't","needn't","no","nor","not","shan't","shouldn't","wasn't","weren't","wouldn't"]
for i in n:
    stop.remove(i)


#add more words to stopwords
a = ['mg', 'week', 'month', 'day', 'january', 'february', 'march', 'april', 'may', 'june', 'july',
     'august', 'september','october','november','december', 'iv','oral','pound', 'lb', 'month', 'day','night']
for j in a:
    stop.add(j)
""""
# Text preprocessing steps - remove numbers, captial letters and punctuation
alphanumeric=lambda x: re.sub('[^a-zA-Z]', ' ', x)
punc_lower=lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x.lower())
split=lambda x: x.split()

df_train1['review'] = df_train1.review.map(alphanumeric).map(punc_lower).map(split)
#print(df_train1)

#remove stopwords
df_train1['review_clean']=df_train1['review'].apply(lambda x: [item for item in x if item not in stop])

#lemmatizing
df_train1['review_lemm']=df_train1['review_clean'].apply(lambda x: [lemmatizer.lemmatize(y) for y in x])

del df_train1['review']
del df_train1['review_clean']

df_train1['review']=df_train1['review_lemm'].apply(lambda x:' '.join(x))

del df_train1['review_lemm']
#print(df_train1)
#export_csv = df_train1.to_csv(r'df_train.csv', index = None, header=True)
"""
#follow the same cleaning steps for test data
df_test = pd.read_csv('Drugs_Dataset_test.csv',sep=None)
#print(df_test.info())

#del df_test['Unnamed: 0']
del df_test['date']

#print("number of drugs:", len(df_test['drugName'].unique()))
#print("number of conditions:", len(df_test['condition'].unique()))

#delete condition with less than 11 drugs
drug_per_condition = df_test.groupby(['condition'])['drugName'].nunique().sort_values(ascending=False)
condition_1=drug_per_condition[drug_per_condition<=10].keys()
df_test1=df_test[~df_test['condition'].isin(condition_1)]
#print(df_test1.info())

df_test1.dropna(inplace=True)
alphanumeric=lambda x: re.sub('[^a-zA-Z]', ' ', x)
punc_lower=lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x.lower())
split=lambda x: x.split()

df_test1['review'] = df_test1.review.map(alphanumeric).map(punc_lower).map(split)
#remove stopwords
df_test1['review_clean']=df_test1['review'].apply(lambda x: [item for item in x if item not in stop])
#lemmatizing
df_test1['review_lemm']=df_test1['review_clean'].apply(lambda x: [lemmatizer.lemmatize(y) for y in x])

del df_test1['review']
del df_test1['review_clean']
df_test1['review']=df_test1['review_lemm'].apply(lambda x:' '.join(x))
del df_test1['review_lemm']
print(df_test1)
#save cleaned test data to csv file for later use
export_csv = df_test1.to_csv(r'df_test.csv', index = None, header=True)