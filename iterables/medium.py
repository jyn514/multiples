def double_char(str):
  new = []
  for char in str:
     new.append(2*char)
  return "".join(new)
def end_other(a, b):
  a=a.lower()
  b=b.lower()
  return a==b[-len(a):] or b==a[-len(b):]
##but the easy way was b.endswith(a)
