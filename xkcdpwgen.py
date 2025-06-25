import random
import sys

listNums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
listSymb = ["~","!","@","#","$","%","^","&","*",".",":",";"]
argArray = sys.argv
argStr = str(sys.argv)


def PasswordGenerator():
  randPassword = []

  if len(argArray) == 1:
    randPassword = (default(4))

  elif "-h" in argArray or "--help" in argArray:
    return help()

  if "-w" in argArray or "--words" in argArray:
    randPassword = word()
  else:
    randPassword = (default(4))

  if "-c" in argArray or "--caps" in argArray:
    if "-c" in argArray:
      cPos = argArray.index("-c")
      newCount = int("".join(argArray[cPos + 1:cPos + 2]))
      if newCount > len(randPassword):
        raise Exception('There has been an error in the system')
      else:
        randPassword = cap("-c", randPassword)
    else:
      cPos = argArray.index("--caps")
      newCount = int("".join(argArray[cPos + 1:cPos + 2]))
      if newCount > len(randPassword):
        raise Exception('There has been an error in the system')
      else:
        randPassword = cap("--caps", randPassword)

  if "-n" in argArray or "--numbers" in argArray:
    randPassword = AInsert(randPassword, "-n", "--numbers", listNums)
  if "-s" in argArray or "--symbols" in argArray:
    randPassword = AInsert(randPassword, "-s", "--symbols", listSymb)

  print("".join(randPassword))


#########################################


#default
def default(num):
  password = []
  for i in range(num):
    x = random.choice(list(open('words.txt')))
    password.append(x.strip('\n'))
  return password


#word count
def word():
  if "-w" in argArray:
    wPos = argArray.index("-w")
  else:
    wPos = argArray.index("--words")
  newCount = int("".join(argArray[wPos + 1:wPos + 2]))
  return default(newCount)


#capatalization
def cap(str, rp):
  cPos = argArray.index(str)
  newCount = int("".join(argArray[cPos + 1:cPos + 2]))
  toBeCap = (random.sample(rp, newCount))
  for i in range(newCount):
    if toBeCap[i] in rp:
      ind = rp.index(toBeCap[i])
      rp[ind] = toBeCap[i].title()
  return rp

#add symbols to password
def AInsert(rp, arg1, arg2, list):
  if arg1 in argArray:
    Pos = argArray.index(arg1)
  else:
    Pos = argArray.index(arg2)
  newNum = int("".join(argArray[Pos + 1:Pos + 2]))
  for i in range(newNum):
    rp.insert(random.randint(0,len(rp)), random.choice(list))
  return rp
  
#add symbols to password
def Symb(rp):
  if "-s" in argArray:
    sPos = argArray.index("-s")
  else:
    sPos = argArray.index("--symbols")
  newNum = int("".join(argArray[sPos + 1:sPos + 2]))
  for i in range(newNum):
    rp.insert(random.randint(0,len(rp)), random.choice(listSymb))
  return rp
  
#add numbers to pass
def Num(rp):
  if "-n" in argArray:
    nPos = argArray.index("-n")
  else: 
    nPos = argArray.index("--numbers")
  newNum = int("".join(argArray[nPos + 1:nPos + 2]))
  for i in range(newNum):
    rp.insert(random.randint(0, len(rp)), random.choice(listNums))
  return rp


#ignores all other tags, prints help menu
def help():
  print(
    "usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n\nGenerate a secure, memorable password using the XKCD method\n\noptional arguments:\n    -h, --help            show this help message and exit\n    -w WORDS, --words WORDS\n                          include WORDS words in the password (default=4)\n    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words\n                          (default=0)\n    -n NUMBERS, --numbers NUMBERS\n                          insert NUMBERS random numbers in the password\n                          (default=0)\n    -s SYMBOLS, --symbols SYMBOLS\n                          insert SYMBOLS random symbols in the password\n                          (default=0)\")"
  )


PasswordGenerator()
