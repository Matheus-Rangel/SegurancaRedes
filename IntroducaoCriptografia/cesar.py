import sys
import os

alf = [c for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,"]


def cesar_bruteforce(txt, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for i in range(len(alf)):
        txt_out = ""
        for c in txt:
            if c not in alf:
                txt_out += c
                continue
            new_index = (alf.index(c) - i) % len(alf)
            txt_out += alf[new_index]
        file = open(os.path.join(output_folder, (str(i) + ".txt")), 'w')
        file.write(txt_out)


if __name__ == '__main__':
    """
    args:
        argv 1: caminho do arquivo txt criptografado
        argv 2: caminho da pasta onde os resultados seram gravados
    """
    file_path = sys.argv[1]
    output_folder = sys.argv[2]
    txt = open(file_path).read()
    cesar_bruteforce(txt, output_folder)
