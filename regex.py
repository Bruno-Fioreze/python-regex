import re

#findall, search, sub
# compile


string = "string de teste regex teste"
"""regex = r"teste"
print(re.search(regex, string))
print(re.findall(regex, string))
print(re.sub(regex, string ,"teste2"))"""

"""regex = re.compile(r'teste')
print(regex.search(string))
print(regex.findall(string))
print(regex.sub(string ,"teste2"))"""

""" META CARACTERES """

". ^ * + ? { } [ ] \ | ( ) "
". = qualquer caractere"
"[] conjunto de caracteres"

" metacaracter para quantidade de repetições"
"""
* 0 ou n
+ 1 ou n
? 0 ou 1 
{} defini inicio e fim
.* qualquer coisa
"""
from pprint import pprint
texto = "O texto dissertativo-argumentativo é um gênero discursivo muito comum em provas de vestibular,  como a Fuvest, e no Enem. Em resumo, trata-se de uma produção em que um autor defende seu ponto de vista por meio de argumentos. No caso específico do Exame Nacional do Ensino Médio, exige-se, também, que se apresentem propostas de solução para os problemas levantados na argumentação.Leia também: Como fazer uma Redaação nota 1000?O texto dissertativo-argumentativo - ou apenas dissertação - é um tipo de texto que discute assuntos socialmente relevantes. No caso específico do Enem, questões que envolvem o Brasil e seus principais problemas costumam aparecer como tema da redação."

#regex = re.compile(r"[a-zA-Z0-9]edação")
#regex = re.compile(r"reda{1,2}ção", flags=re.I)
#regex = re.compile(r"ama[a-zA-Z]*")
#texto2 = "joao ama ser amado"
#print(regex.findall(texto2))


"flags"
# texto = "O texto dissertativo-argumentativo é um gênero discursivo muito comum em provas de vestibular,  como a Fuvest, e no Enem. Em resumo, trata-se de uma produção em que um autor defende seu ponto de vista por meio de argumentos. No caso específico do Exame Nacional do Ensino Médio, exige-se, também, que se apresentem propostas de solução para os problemas levantados na argumentação.Leia também: Como fazer uma Redaação nota 1000?O texto dissertativo-argumentativo - ou apenas dissertação - é um tipo de texto que discute assuntos socialmente relevantes. No caso específico do Enem, questões que envolvem o Brasil e seus principais problemas costumam aparecer como tema da redação."

# regex = re.compile(r"\w+")

# print(regex.findall(texto))
# print(regex.findall(texto))

texto4 = "007.986.740-59  407.984.744-49 037.936.730-39 027.926.720-59" 
#regex = re.compile(r"<[pdiv]{1,3}>.*<\/[pdiv]{0,3}>")
#regex = re.compile(r"<[pdiv]{0,3}>.*?<\/[pdiv]{0,3}>")

"""() conjuntos """
"""
regra = r"(<([pdiv]{0,3})>(.*?)<\/\2>)"
regex = re.compile(regra)
resultados = regex.findall(texto4)
for resultado in resultados:
    completo, parcial, texto = resultado
    print(texto)
?: não salva em memória"""

"""regex = re.compile(r"((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})")
print(regex.findall(texto4))"""

"^ começa com"
"$ termina com"
# regex = re.compile(r"^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$")
# print(regex.findall(texto4))

"\d todos os números"
"\D nega os números"
"\s todos os espaços"
"\S nega os espaços"

#regex = re.compile(r"\be\w+")
# regex = re.compile(r"\w+e\b")
# print(regex.findall(texto))

texto_8 = "oborno teste enquanto teste3 la tem os" 
regex = re.compile(r"^o.*o$")
print(regex.findall(texto_8))