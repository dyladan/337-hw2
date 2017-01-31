def main():
    Nintey_Nine_Bottles_of_Beer()

def Nintey_Nine_Bottles_of_Beer():
    for i in reversed(range(99)):
        print line1(i)
        print line2(i)

def line1(n):
    if n == 0:
        return '{} bottle of beer on the wall, {} bottle of beer'.format(n+1, n+1)
    return '{} bottles of beer on the wall, {} bottles of beer'.format(n+1, n+1)

def line2(n):
    if n == 1:
        return 'take one down, pass it around, {} bottle of beer on the wall.'.format(n)
    if n != 0:
        return 'take one down, pass it around, {} bottles of beer on the wall.'.format(n)

    return 'take one down, pass it around, no more bottles of beer on the wall.'

main()
