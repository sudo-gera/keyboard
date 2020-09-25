from os import listdir
for w in listdir('.'):
 try:
  q=open(w).read()
  q=q.replace('<Row android:keyHeight="66%p">\n  </Row>\n </Keyboard>','<Row android:keyHeight="0%p">\n  </Row>\n </Keyboard>')
  open(w,'w').write(q)
 except:
  pass
