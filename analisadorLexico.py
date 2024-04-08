import re
#teste
# Definindo as expressões regulares para os tokens
token_patterns = [
    (r'\bfor\b', 'LOOP FOR'),         # Loop FOR
    (r'\bwhile\b', 'LOOP WHILE'),     # Loop WHILE
    (r'\band\b', 'PORTA LÓGICA AND'),  # IF
    (r'\bor\b', 'PORTA LÓGICA OR'),    # Else
    (r'\bin\b', 'OPERADOR ESTÁ CONTIDO'), # in 'ESTÁ CONTIDO'
    (r'\blist\b', 'LISTA'),
    (r'\bint\b', 'Tipo de dado INTEIRO'),
    (r'\bstring\b', 'Tipo de dado STRING'),
    (r'\bfloat\b', 'Tipo de dado FLOAT'),
    (r'\bbreak\b', 'BREAK POINT'),
    (r'\bif\b', 'SE'),
    (r'\belse\b', 'SE NÃO'),
    (r'\{', 'Chave esquerdo'),
    (r'\}', 'Chave direito'),
    (r'\[', 'Colchete esquerdo'),
    (r'\]', 'Colchete direito'),
    (r'\bnot\b', 'Condicional de NEGAÇÃO'),
    (r'\btrue\b', 'Tipo de dado VERDADE'),
    (r'\bfalse\b', 'Tipo de dado FALSO'),
    (r'\bas\b', 'Atribuição de VALOR'),
    (r'\bdef\b', 'Atribuição de FUNÇÃO'),
    (r'\breturn\b', 'RETORNO DE VALOR'),
    (r'\bNone\b', 'Tipo de dado NONE'),
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),  # Identificador de variável
    (r'\d+', 'NUMBER'),                # Número
    (r'\+', 'PLUS'),                   # Operador de adição
    (r'-', 'MINUS'),                   # Operador de subtração
    (r'\*', 'MULTIPLY'),               # Operador de multiplicação
    (r'/', 'DIVIDE'),                  # Operador de divisão
    (r'=', 'ASSIGN'),                  # Operador de atribuição
    (r'\(', 'LPAREN'),                 # Parêntese esquerdo
    (r'\)', 'RPAREN'),                 # Parêntese direito
]

# Função para analisar o código fonte e gerar tokens
def tokenize(code):
    tokens = []
    code = code.strip()
    while code:
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                tokens.append((value, token_type))
                code = code[match.end():].strip()
                break
        if not match:
            return f"Não foi possível reconhecer o token: {code}"
    return tokens

# Exemplo de uso
code = "for while 001 return true None if else not in list () {} []"
tokens = tokenize(code)
print(tokens)
