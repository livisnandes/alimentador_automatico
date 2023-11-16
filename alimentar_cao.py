import time

def alimentar_cao(hora, quantidade):
    # Verificar se é hora de alimentar o cão
    while True:
        agora = time.localtime()
        hora_atual = agora.tm_hour

        if hora_atual == hora:
            # Simular a dispensação de comida (substitua por sua lógica real)
            dispensar_comida(quantidade)
            break
        else:
            # Aguardar 1 minuto antes de verificar novamente
            time.sleep(60)

def dispensar_comida(quantidade):
    # Lógica para dispensar a quantidade específica de comida (substitua por sua lógica real)
    print(f"Dispensando {quantidade} gramas de comida para o cão.")

# Exemplo de uso
hora_alimentacao = 8  # Substitua pelo horário desejado (24 horas)
quantidade_alimentacao = 200  # Substitua pela quantidade desejada em gramas

alimentar_cao(hora_alimentacao, quantidade_alimentacao)
