# Nome: Thiago F. Santos

import re
from specs import spec


class Analysis:

    def __init__(self):
        self.tok = '|'.join('(?P<%s>%s)' % pair for pair in spec)
        self.getToken = re.compile(self.tok).match
        
        while(True):
            userInput = input("Digite a entrada para o analisador lexico: ")
            
            print("\nResultado:")
            for token in self.lexico(userInput):
                print(token)
            
            print("\n")

        
    def lexico(self,codigo):
        #  aplica o <match> do <getToken> para procurar um padrão
        val=self.getToken(codigo,0)
        
        while val is not None:
          token = val.lastgroup # token = último grupo encontrado no <match>
          lexema = val.group()  # lexema = grupo da correspondência
          if token != 'SKIP':   # Evita os símbolods indesejáveis
            yield('TOKEN: %s\t VAL: %s' %(token, lexema)) # retorna a estrutura
          pos = val.end()       # Reposiciona o próximo símbolo a ser testado
          val=self.getToken(codigo,pos) # Aplica o <match> para a sequencia
        
        if "token" in locals() and "lexema" in locals():
          return token, lexema
        else:
          print("\nNão foi encontrado nenhum padrão para essa entrada. Tente novamente.")
          return None


if __name__ == '__main__':
    analysis = Analysis()
    