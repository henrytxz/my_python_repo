import os, re

if __name__ == '__main__':
  os.chdir("C:\Users\henry\Google Drive\LEARN\Spark\slides")
  now_names = os.listdir('.')
  now_names = [name for name in now_names if name.endswith('.pdf')]
  # pat = '^Week(\d)Lec(\d).pdf'
  pat = 'lecture(\d)_(\d).pdf'
  # new_pattern = 'lecture{}_{}.pdf'
  new_pattern = '{0}.pdf'
  for name in now_names:
    match = re.search(pat, name)
    if match:
      # print match.group(2)
      # os.renames(name, new_pattern.format(match.group(1), match.group(2)))
      os.renames(name, new_pattern.format(match.group(2)))