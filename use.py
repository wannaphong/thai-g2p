from g2p import g2p
from pythainlp.tokenize import word_tokenize
text = "คนเล่นเกมที่กรุงเทพ"
print([g2p(i) for i in word_tokenize(text)])