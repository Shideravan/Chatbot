# Chat Bot com Integração ao ChatGPT

## Descrição do Projeto
Este projeto é um chat bot que integra o modelo de linguagem GPT, como o ChatGPT da OpenAI. O chat bot é capaz de receber mensagens dos usuários, processá-las usando o modelo ChatGPT e fornecer respostas inteligentes e contextuais.
A versão atual deste projeto utiliza o modelo GPT 3.5 Turbo. 

![image](https://github.com/Shideravan/Chatbot/assets/12163923/30f3fff2-c493-4975-b076-db693a684d82)


## Requisitos

### Python 3.12.0+
https://www.python.org/downloads/

### Biblioteca requests (https://pypi.org/project/requests/)
`pip install requests`

### OpenAI API Key
1. Crie uma conta junto à plataforma da OpenAI
2. Visite o link: `https://platform.openai.com/api-keys`
3. Associe um número de celular e clique em `Create new secret key`
4. Copie o código gerado e coloque dentro de `dados.py`
5. Adicione sua chave da API do OpenAI ao arquivo `api-key.py`.

### Informações em dados.py
Nesta versão da aplicação, de forma a simular o recebimento de informações em uma base de dados, o arquivo dados.py pode ser preenchido com informações simulando dados no perfil pessoal do cliente.

## Utilização
Execute o arquivo `main.py` dentro da pasta `src` para iniciar o chat bot. Você pode fazer isso com o comando: `python main.py`.
Você poderá conversar com o chatbot a normalmente.

- Se desejar acessar dados sobre encomendas em curso, digite `encomendas`.
- Se desejar acessar dados sobre boletos em aberto, digite `boletos`.
- Se desejar acessar dados sobre promoções disponíveis ao seu usuário, digite `promocoes`.

Você pode sair a qualquer momento com o comando `sair`.

## Estrutura
A arquitetura do chat bot é composta por vários componentes que trabalham juntos para fornecer uma experiência de conversação interativa.

1. **ChatBot Class**: Esta é a classe principal que coordena todas as funcionalidades do chat bot. Ela mantém o estado da conversa, processa a entrada do usuário e gera respostas.

2. **Métodos de ChatBot**:
    - `__init__`: Este método inicializa a instância do chat bot, configurando os cabeçalhos para a API do ChatGPT, o link da API, o modelo a ser usado e inicializando a conversa e o menu.
    - `exibir_menu`: Este método exibe o menu de opções para o usuário.
    - `receber_input_usuario`: Este método recebe a entrada do usuário através da linha de comando.
    - `gerar_resposta`: Este método gera uma resposta para a entrada do usuário. Ele verifica se a entrada do usuário corresponde a uma opção de menu ou contém a palavra "IA". Se sim, ele retorna a resposta correspondente. Caso contrário, ele envia a entrada do usuário para o modelo ChatGPT e retorna a resposta do modelo.
    - `chat`: Este método inicia o chat bot, exibindo o menu e entrando em um loop onde recebe a entrada do usuário, gera uma resposta e exibe a resposta.

3. **Integração com a API do ChatGPT**: O chat bot usa a API da no modelo GPT 3.5 Turbo para gerar respostas contextuais para a entrada do usuário. Ele envia a entrada do usuário e o histórico da conversa para o modelo ChatGPT e recebe uma resposta do modelo.

4. **Dados**: O chat bot usa dados pré-definidos (como `encomendas`, `boletos` e `promocoes`) para fornecer respostas para certas opções de menu.

5. **Utilização de palavras chave**: A solução trabalhar também processando palavras chave. Se em seu texto houver a palavra "IA" como na frase `Você é uma IA?` ele irá trazer a mensagem predefinida:
`Sim, eu sou uma IA e é um prazer ajudar você. Gostaria de falar com um atendente humano? Siga esse link: www.atendentehumano.com` apresentando um link fictício para atendimento com um humano. 
Percaba que a solução pode ser facilmente configurada para atender outros tipos de palavras chave.

6. **Interação**: A interação é feita toda via linha de comando, conforme especificado nos requisitos do projeto.

## Decisões de projeto
  - **Modularização da api key:** Foi uma decisão importante modularizar estas informações, de modo que seja importante modularizar a implementação da API_KEY para facilitar a substituição de chave do modelo, sem que seja necessário editar diretamente o código da aplicação.

  - **Interface de linha de comando:** Os requisitos do projeto especificavam a utilização de linha de comando. Por este motivo, as interações são realizadas através de comandos na plataforma.

  - **Escolha do modelo de linguagem e plataforma:** Atualmente, o modelo disponível em contas gratuitas que traz melhor interação na plataforma da OpenAI para chat bots é a GPT 3.5 Turbo que dadas as restrições na conta utilizada para testes foi a melhor opção disponível. Numa conta premium, existem opções mais robustas como o GPT 4 32k que consegue manter o contexto com até 32 mil tokens. A OpenAI disponibiliza uma plataforma bastante robusta atualmente, que recebe melhorias constantes mesmo nos modelos mais básicos o que tornou uma escolha natural para este projeto.

  - **Respostas automáticas:** Conforme solicitado nos requisitos, o sistema é capaz de gerar interações automáticas segundo determinadas entradas. Como exemplo, foi implementado o recurso que toda a vez que a palavra "IA" fosse citada na entrada do usuário, o sistema geraria uma resposta padrão personalizada. Note que utilizando a mesma lógica é fácil de implementar um número enorme de diferentes interações personalizadas.

  - **Capacidade de trabalhar com comandos pré-determinados:** O sistema trabalha com alguns comandos, como `sair` que automaticamente encerra a seção, `encomendas`, `boletos` e `promocoes` que apresentam dados de seção. Note que utilizando esta estrutura, podem-se incluir outros tipos de comandos conforme venham sendo necessárias.

 - **Menu com instruções sobre os comandos:** Ao iniciar a plataforma ele mostra um rápido menu com opções de comandos que podem ser realizados durante a operação do chat bot. Isso visa apresentar uma interface personalizada que instrua o usuário quais comandos ele poderá realizar.
   
 - **Capacidade de lidar com diferentes dados no perfil de usuário:** De forma a simular a interação com diferentes dados de usuário e seção, alguns dados são fornecidos através do arquivo dados.py. Note que essas informações podem ser facilmente editadas de forma a simular outros dados na seção, incluindo o número de protocolo gerado pelo sistema. Isso facilita que o projeto seja editado para trabalhar com requisições internas e dados de seção.



# Licença
Este projeto está licenciado sob a licença GPLv3. Veja o arquivo `LICENSE` para mais detalhes.
