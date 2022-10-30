#!/usr/bin/python3
from recommend_class import Recommender

import sys


def main():
    paper_index = int(sys.argv[1])
    rec = Recommender(paper_index=paper_index)
    papers = rec.recommend()
    print('Recommended papers:')
    for paper in papers[0]:
        print(paper[1])
    print('------------------------')
    print('What you might also like:')
    for paper in papers[1]:
        print(paper[1])

if __name__ == '__main__':
    main()


