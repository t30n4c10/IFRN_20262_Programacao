# Peça um IP de origem e sua máscara, e um IP de destino e sua máscara;
# E mostre o caminho da origem ao destino, passando pelo roteador da rede (que liga as duas redes).
#
# Variáveis iniciais:
# - IP de origem, máscara de origem -> Solicitados ao usuário (na teoria, deve ser da mesma rede de uma das portas do roteador)
# - IP de destino, máscara de destino -> Solicitados ao usuário
# - Lista contendo 2 ip's de gateway das portas do roteador -> Definido no código
# - Dicionário {IP:mascara}, com a lista de ip's de destino e suas mascaras (uma mesma rede para todos e, na teoria,
# deve ser a rede de uma das portas do roteador) -> Definido no código
#
# Regras:
# - O roteador tem duas portas, uma delas está na rede do IP de origem e a outra na rede dos IP's do dicionário;
# - Caso o IP/máscara de origem (informado pelo usuário) seja de uma rede diferente da rede da porta do roteador
# (que não é a do dicionário), mostre um erro na tela;
# - Caso o IP de destino/máscara esteja em uma rede que não seja a do dicionário, retorne "DESTINATION IP UNKNOWN";
# - Caso o IP de destino esteja em uma rede que o roteador conhece, mostre o caminho até o destino (não mostre a volta).