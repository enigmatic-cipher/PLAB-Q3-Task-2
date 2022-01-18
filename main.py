"""
Given a string as input. Change every 1 to "ab" and 9 to "c" in given string.
Input-> "2119"
Output-> 2ababc
"""

st = "2119"
ln = len(str(st))
st1 = ""
for i in range(0,ln):
  ch = st[i]
  if (ch=="1"):
    st1 = st1 + "ab"
  elif (ch=="9"):
    st1 = st1 + "c"
  else:
    st1 = st1 + ch
print(st)

