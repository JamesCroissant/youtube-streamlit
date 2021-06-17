class UppercaseError(Exception):
    pass

def check():
    words=['APPLE','orange','banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except ValueError as ex:
    print('this is my fault,Go next')
