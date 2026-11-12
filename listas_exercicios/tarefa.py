produtos = [ 
    (1,"suco", 7.00),
    (2,"salgadinho", 8.00),
    (3,"chocolate", 6.00),
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

   produtos.append 
