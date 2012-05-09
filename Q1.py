translate_to_english = {" ":" ","a":"y","b":"h","c":"e","d":"s","e":"o","f":"c","g":"v","h":"x","i":"d","j":"u","k":"i","l":"g","m":"l","n":"b","o":"k","p":"r","q":"z","r":"t","s":"n","t":"w","u":"j","v":"p","w":"f","x":"m","y":"a","z":"q"}

for tc in xrange(1, int(raw_input()) + 1):
  english = ''.join(
      [translate_to_english[ch] for ch in raw_input()])
  print 'Case #%d: %s' % (tc, english)