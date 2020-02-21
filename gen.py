def create(b,e):
 ext=open('hide_'+str(b)+'_'+str(e)+'.xml','w')
 ext.write('<?xml version="1.0" encoding="utf-8"?>\n<Keyboard\nxmlns:android="http://schemas.android.com/apk/res/android"\nandroid:keyWidth="'+('6.25' if (b-e)<=256 else '12.5')+'%p">\n'
 if e-b<=256:
  for q in range(b,e,16):
   ext.write('<Row android:keyHeight="62.5%p">\n')
   for w in range(q,q+16):
    ext.write('<Key\n')
    try:
     ext.write(' android:keyLabel="'+chr(w)+'"\n')
    except:
     ext.write(' android:keyLabel="'+str(w)+'"\n')
    ext.write(' android:smallLabel="true"\n')
    ext.write(' android:codes="'+str(w)+'"\n')
    ext.write(' android:longCode="-'+str(w)+'"\n')
    ext.write('/>\n')
   ext.write('</Row><!--000000000000000000000000000000000000--/>')
 else:
  for q in range(b,e,(e-b)//8):
   ext.write('<Row android:keyHeight="125%p">\n')
   for w in range(w,w+(e-b)//8,(e-b)//64):
    ext.write('<Key\n')
    ext.write(' android:keyLabel="'+str(w)+'\n'+str(w+(e-b)//64)+'"\n')
    ext.write(' android:smallLabel="true"\n')
    ext.write(' android:keyboard="hide_'+str(w)+'_'+str(w+(e-b)//64)+'.xml"\n')
    ext.write('/>\n')
    create(w,w+(e-b)//64)
   ext.write('</Row><!--000000000000000000000000000000000000--/>')
 ext.write('</Keyboard>')
 ext.close()
create(0,2**26)
