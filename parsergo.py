# pip install dkpro-cassis
from cassis import *

with open('data/TypeSystem.xml', 'rb') as f:
    typesystem = load_typesystem(f)

with open('data/2017_2.xmi', 'rb') as f:
   cas = load_cas_from_xmi(f, typesystem=typesystem)

text = cas.sofa_string

with open('data/plain_full.txt', 'w', encoding= 'utf-8') as f:
        f.write(text) # сохрянем очищенный файл