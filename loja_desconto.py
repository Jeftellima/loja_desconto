print('Bem Vindo a Loja do Jefte Lima- Mini Sistema | Loja que dá descontos')
valorProduto = float(input('Digite o valor do produto: ')) # entrada de dados, ponto  flutuante
quantidadeProduto = int(input('Digite a quantidade do produto ?'))
valorTotalProduto = valorProduto * quantidadeProduto

if (quantidadeProduto <= 4): #executando-o apenas se ela for verdadeira
  print('O valor total da sua compra é R${} e pela quantidade o desconto é de 0% ' .format(valorTotalProduto))
elif (quantidadeProduto >= 5 and quantidadeProduto <= 19): # verificação de outra expressão caso a primeira validação seja falsa.
  valorDesconto = valorTotalProduto * 0.03
  valorDescontoProduto = valorTotalProduto - valorDesconto
  print('O valor sem desconto foi: R${:.2f}' .format(valorTotalProduto))   
  print('O valor com desconto foi: R${:.2f} (desconto 3%)' .format(valorDescontoProduto))
elif (quantidadeProduto >= 20 and quantidadeProduto <= 90): # verificação de outra expressão caso a primeira validação seja falsa.
  valorDesconto = valorTotalProduto * 0.0610
  valorDescontoProduto = valorTotalProduto - valorDesconto
  print('O valor sem desconto foi: R${:.2f}' .format(valorTotalProduto))
  print('O valor com desconto foi: R${:.2f} (desconto 6%)' .format(valorDescontoProduto))
else :  # executado um bloco de código, caso o resultado da expressão informada na instrução if seja falso
  valorDesconto = valorTotalProduto * 0.10
  valorDescontoProduto = valorTotalProduto - valorDesconto
  print('O valor sem desconto foi: R${:.2f}' .format(valorTotalProduto))  #jogado na tela o valor sem o desconto
  print('O valor com desconto foi: R${:.2f} (desconto 10%)' .format(valorDescontoProduto))  #jogado na tela o valor com o desconto
  print("Obrigado pela preferência - Volte sempre!!!") # mensagem de finalização