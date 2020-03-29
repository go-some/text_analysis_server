# 텍스트 분석 서버
NER, 문서 요약 모듈 및 서버를 포함합니다.


## 제약 사항
- 일반적인 컴퓨터에서 CPU만으로 적당한 성능을 내는 선에서 구현할 것.


## Requirement
```
pip install flask
pip install -U spacy
python -m spacy download en_core_web_sm
```


## NER
- [company_ner by JM](https://github.com/go-some/company_ner) 참고하여 작성
- 참고자료
    - [spacy based](https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da), [tag list](https://spacy.io/api/annotation#section-named-entities)
    - [spacy 학습법](https://spacy.io/usage/examples#training-ner)
    - [spacy 학습법2](https://www.geeksforgeeks.org/python-named-entity-recognition-ner-using-spacy/)
    - [w2v + LogisticRegression](https://lovit.github.io/nlp/2019/02/16/logistic_w2v_ner/)
    - [CRF based](https://lovit.github.io/nlp/2018/06/22/crf_based_ner/)

## Summarization
- TextRank
- LexRank



