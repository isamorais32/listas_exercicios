produtos = [ 
     [1,"suco", 7.00],
    [2,"salgadinho", 8.00],
    [3,"chocolate", 6.00],
]
for produto in produtos:
    print (produto)  

id_procurado =1
for indice, produto in enumerate(produtos) :
 if produto[0] == id_procurado:
    removido = produtos.pop (indice)   
    print ("registro removido", removido)
    
for produto in produtos:
   print (produto) 

produtos.append([4,"cereal", 9.00]) 

print (produtos)

alter = int(input("deseja alterar o preço? (1 para sim, 0 para não): "))
if alter == 1:
    id_procurado = int(input("Digite o id do produto que deseja alterar: "))
    for produto in produtos:
        if produto[0] == id_procurado:
            novo_preco = float(input("Digite o novo preço: "))
            produto[2] = novo_preco
            print("Preço alterado com sucesso!")
            break
    else:
        print("Produto não encontrado.")


