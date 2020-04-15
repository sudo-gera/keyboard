x={'"':'&quot;','&':'&amp;',"'":'&apos;','<':'&lt;','>':'&gt;'}
u='º¹²³⁴⁵⁶⁷⁸⁹'
l='₀₁₂₃₄₅₆₇₈₉'
n='01234567890'
def less(q,a=0):
 q=str(q)
 if a:
  y=u
 else:
  y=l
 return ''.join([y[n.index(w)] for w in q])
def create(b,e):
 if e-b>256:
  print(b,end='\r')
 if b>=2**16*17:
  return 0
 ext=open('hide_auto_'+str(b)+'_'+str(e)+'.xml','w')
 if e-b<=256:
  ext.write('<?xml version="1.0" encoding="utf-8"?>\n<Keyboard\nxmlns:android="http://schemas.android.com/apk/res/android"\nandroid:keyWidth="6.25%p">\n')
  for q in range(b,e,16):
   ext.write('<Row android:keyHeight="62.5%p">\n')
   for w in range(q,q+16):
    ext.write('<Key\n')
    try:
     if b==0 and chr(w) in x:
      ext.write(' android:keyLabel="'+x[chr(w)]+'"\n')
     else:
      ext.write(' android:keyLabel="'+chr(w)+'"\n')
    except:
     ext.write(' android:keyLabel="'+str(w)+'"\n')
#    ext.write(' android:smallLabel="true"\n')
#    ext.write(' android:codes="'+str(w)+'"\n')
#    ext.write(' android:longCode="-'+str(w)+'"\n')
    ext.write('/>\n')
   ext.write('</Row><!--000000000000000000000000000000000000-->')
 else:
  ext.write('<?xml version="1.0" encoding="utf-8"?>\n<Keyboard\nxmlns:android="http://schemas.android.com/apk/res/android"\nandroid:keyWidth="12.5%p">\n')
  for q in range(b,e,(e-b)//8):
   ext.write('<Row android:keyHeight="125%p">\n')
   for w in range(q,q+(e-b)//8,(e-b)//64):
    if create(w,w+(e-b)//64):
     ext.write('<Key\n')
     ext.write(' android:keyLabel="'+less(w,1)+less(w+(e-b)//64)+'"\n')
     ext.write(' android:smallLabel="true"\n')
     ext.write(' android:keyboard="auto/hide_auto_'+str(w)+'_'+str(w+(e-b)//64)+'.xml"\n')
     ext.write('/>\n')
   ext.write('</Row><!--000000000000000000000000000000000000-->')
 ext.write(''' <Row>
  <Key
   android:keyLabel="⟪⟪⟪⟪"
   android:keyboard="auto/hide_auto_'''+str(b+b-e)+'_'+str(b)+'''.xml"
   android:longCode="0"
   android:isRepeatable="true"
   android:keyWidth="10.0%p"
                                                  />
  <Key
   android:keyLabel="⇦"
   android:codes="21"
   android:isRepeatable="true"
   android:keyWidth="10.0%p"
                                                  />
  <Key
   android:keyLabel="⇨"
   android:codes="22"
   android:isRepeatable="true"
   android:keyWidth="10.0%p"
                                                  />
  <Key
   android:keyLabel="cop"
   android:codes="-320"
   android:isRepeatable="true"
   android:keyWidth="10.0%p"
                                                  />
  <Key
   android:keyLabel="pas"
   android:codes="-504"
   android:isRepeatable="true"
   android:keyWidth="10.0%p"
                                                  />
  <Key
   android:keyLabel="⌫"
   android:codes="-5"
   android:isRepeatable="true"
   android:keyWidth="10.0%p"
                                                  />
  <Key
   android:keyLabel="sel"
   android:codes="-310"
   android:isRepeatable="true"
   android:isSticky="true"
   android:keyWidth="10.0%p"
                                                  />
  <Key
   android:keyLabel="'''+str(b)+' '+str(e)+'''"
   android:isRepeatable="true"
   android:goQwerty="true"
   android:codes="-2"
   android:longCode="0"
   android:keyWidth="20.0%p"
                                                  />
  <Key
   android:keyLabel="⟫⟫⟫⟫"
   android:isRepeatable="true"
   android:keyboard="auto/hide_auto_'''+str(e)+'_'+str(e+e-b)+'''.xml"
   android:longCode="0"
   android:keyWidth="10.0%p"
                                                  />
  </Row>''')
 ext.write('</Keyboard>')
 ext.close()
 return 1
create(0,2**26)
