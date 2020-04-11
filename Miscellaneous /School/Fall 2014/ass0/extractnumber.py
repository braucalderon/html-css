text = 'X-DASPAM-Confidence: 0.8475'
tin = text.find(':')
num = float(text[tin+1:])
print num 