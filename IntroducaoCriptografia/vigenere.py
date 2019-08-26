import sys

alf = "abcdefghijklmnopqrstuvwxyz"


def vigenere(txt, key, out):
    result = ""
    for i in range(len(txt)):
        if txt[i] not in alf:
            result += txt[i]
            continue
        c_index = alf.find(txt[i])
        key_index = alf.find(key[i%len(key)])
        result += alf[(c_index - key_index)%len(alf)]
    out.write(result)
    return result

def main():
    txt = open(sys.argv[1]).read()
    key = open(sys.argv[2]).read()
    out = open(sys.argv[3], 'w')
    print(vigenere(txt, key, out))


if __name__ == '__main__':
    main()
