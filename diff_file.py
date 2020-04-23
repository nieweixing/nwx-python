import difflib
import sys


try:
  textfile1 = sys.argv[1]
  textfile2 = sys.argv[2]
except Exception as e:
  print("Error:"+str(e))
  print("Usage: diff_file.py filename1 filename2")
  sys.exit()

def readfile(filename):
  try:
    fileHand = open(filename, 'rb')
    text = fileHand.read().splitlines()
    fileHand.close()
    return text
  except IOError as error:
    print('Read file Error:' + str(error))
    sys.exit()

if textfile1 == "" or textfile2 == "":
  print("Usage: diff_file.py filename1 filename2") 
  sys.exit()

tex1_lines = readfile(textfile1)
tex2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print(d.make_file(tex1_lines, tex2_lines))