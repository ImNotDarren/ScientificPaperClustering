import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def main():
    df = pd.read_csv('../dataset/arxiv-metadata-oai.csv', low_memory=False)
    df = df.fillna('None')
    # get rid of journal_ref column
    df = df.drop(columns=['journal_ref', 'doi'])
    # drop duplicated abstracts
    df.drop_duplicates(['abstract'], inplace=True)
    # extract all abstracts and replace \n token with a space
    corpus = []
    for index, row in df.iterrows():
        text = row.abstract
        text = text.replace('\n', ' ')
        corpus.append(text)

    cv = TfidfVectorizer(stop_words='english')
    X = cv.fit_transform(corpus)
    vec = pd.DataFrame(X.toarray(), columns=cv.get_feature_names())
    vec.to_csv('../dataset/tfidf.csv')

if __name__ == '__main__':
    main()