import base64

print("---------------------------------------------------------------------\nIdle Breakout Save Code Generator Upgraded\nEdited by ToasterPanic, original by SCS Psyco29\n---------------------------------------------------------------------\n") 

# added more stuff
# this is my first time doing anything with python so sorry for bad code

print("Level")
level = input()

print("Money")
money = input()

print("Gold")
gold = input()

print("Black Bricks")
bb = input()

print("Skill Points (also sets boss level)")
sp = input()

print("Prestiges")
prs = input()

s = f"{level},{money},{gold},2,{prs},0,0,0,0,0,0,1,1,0,43595.78,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{bb},0,0,0,{int(sp) + 1},{sp},1,0,0,Idle Breakout Save Code Generator Upgraded edited by ToasterPanic and original by SCS Psyco29"
b = s.encode("UTF-8")
e = base64.b64encode(b)
print("Finding Hot Babes in Your Area....")
print("Selecting Server...")
print("Conecting to server....")
print("Generating code...")
print("COMPLETE!")

print(e)

print("\nCopy what's INSIDE the quotes!\n")
print("CTRL+C does not work, use right click and copy.")
print("Once copied, you may exit the console.")

while True:
  input() # i replaced the old loop with one that would work