#!/usr/bin/env python
# coding: utf-8

import lxml
import markovify
import sacremoses

class MosesText(markovify.NewlineText):
    mt = sacremoses.MosesTokenizer()
    md = sacremoses.MosesDetokenizer()
    def word_join(self, words):
        return self.md.detokenize(words)
    def word_split(self, text):
        return self.mt.tokenize(text)

# https://www.buzzfeed.com/mrloganrhoades/a-complete-ranking-of-almost-every-single-mitch-hedberg-joke
html = lxml.html.parse("a-complete-ranking-of-almost-every-single-mitch-hedberg-joke.html").getroot()

corpus = ''
for p in html.cssselect("div.subbuzz > p"):
    joke = p.text_content()
    joke = joke.split('.', 1)
    if len(joke) < 2: break
    joke = joke[1].replace('[Listen]','').strip()
    corpus += joke + '\n'

joke_model = MosesText(corpus)
jokes = []
for i in range(275):
    jokes.append(joke_model.make_sentence())

for i, joke in zip(range(275,0,-1), jokes):
    print("{}. {}".format(i, joke))




