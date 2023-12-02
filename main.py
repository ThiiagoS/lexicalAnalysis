import re
from specs import spec


class Analysis:

    def __init__(self):
        self.tok = '|'.join('(?P<%s>%s)' % pair for pair in spec)
        self.getToken = re.compile(self.tok).match
        
        while(True):
            userInput = input("\nDigite a entrada para o analisador lexico: ")
            
            print("\nResultado:")
            for token in self.lexico(userInput):
                print(token)

            
           

    def lexico(self,codigo):
        #  aplica o <match> do <getToken> para procurar um padrão
        #  na string <codigo> a partir da posição 0;
        val=self.getToken(codigo,0)
        
        while val is not None:
          token = val.lastgroup # token = último grupo encontrado no <match>
          lexema = val.group()  # lexema = grupo da correspondência
          if token != 'SKIP':   # Evita os símbolods indesejáveis
            yield('TOKEN: %s\t VAL: %s' %(token, lexema)) # retorna a estrutura
          pos = val.end()       # Reposiciona o próximo símbolo a ser testado
          val=self.getToken(codigo,pos) # Aplica o <match> para a sequencia
        return token, lexema


if __name__ == '__main__':
    analysis = Analysis()
    