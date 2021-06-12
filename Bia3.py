import os
import time

red  = "\033[1;31m" 

xingamentos = ['puta', 'vaca', 'vagabunda', 'cachorra', 'vadia', 'merda', 'gostosa', 'solteira?', 'pobre', 'preta', 'macaca', 'safada', 'feia', 'sequelada', 'chupa cu', 'arrombada', 'idiota', 'putinha', 'escrava', 'santander']

rico = {'oi': 'bia: pobre', 'preciso de ajuda': 'bia: sérgio', 'iae': 'bia: pobre imundo', 'pobre': 'bia: sua família seu otário se mata', 'jesus' : 'bia: hail satan', 'negro': 'bia: sem rascismo aqui', 'eae' : 'bia: eae o karalho seu pobre', }

os.system('clear')

print('bia do bradesco')
print()
time.sleep(2)
for riqueza, xingamentos in rico.items():
  
  inicio = input('diga algo: ')
  
  print(rico.get(inicio) if rico.get(inicio) else "Essas palavras são ofensivas e se distanciam da relação de respeito que eu tenho com as pessoas. Recomendo mudar seu jeito de falar e me chamar depois disso.") 