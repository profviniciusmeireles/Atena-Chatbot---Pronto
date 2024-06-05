Introdução:

Este repositório contém o código para a ATENA CHATBOT que utiliza o LLM Gemini do Google para gerar respostas às consultas dos usuários. O chatbot é implementado usando Streamlit e fornece uma interface amigável para interação com o LLM.

Interface da Aplicação:

![tela](https://github.com/profviniciusmeireles/Gemini-Chat/assets/169489043/e0e61af7-068d-45b4-ac5f-338c2047c9d9)


Funcionalidades:

- Iniciar conversa: Os usuários podem iniciar uma nova conversa digitando uma pergunta ou frase inicial.
- Interação com LLM: O chatbot envia as consultas dos usuários para o LLM Gemini e exibe as respostas geradas.
- Histórico de conversas: O histórico das conversas anteriores é exibido na barra lateral, permitindo que os usuários acompanhem o fluxo da conversa.
- Limpar histórico: Um botão na barra lateral permite que os usuários apaguem todo o histórico de conversas.
- Iniciar nova conversa: Um botão na barra lateral permite que os usuários iniciem uma nova conversa, limpando o histórico anterior.

Requisitos:

Python 3.10
Streamlit
Google Cloud Platform (conta com LLM Gemini habilitado)
Arquivo .env com a chave de API do Google Cloud (GEMINI_API_KEY)

Instalação:

1. Instale as dependências:
pip install -r requirements.txt

2. Configure a chave de API do Google Cloud:

Crie um arquivo .env na raiz do projeto.
Adicione a seguinte linha ao arquivo .env, substituindo SEU_PROJETO_ID pelo ID do seu projeto do Google Cloud:
GEMINI_API_KEY=<SEU_CHAVE_DE_API>

3. Executando o Chatbot

Navegue até a pasta do projeto no seu terminal.
Execute o seguinte comando:
streamlit run app.py

4. O chatbot será aberto em seu navegador.

Uso:

Digite sua pergunta ou frase inicial na caixa de texto e pressione Enter para iniciar a conversa.
O chatbot exibirá a resposta gerada pelo LLM Gemini.
Você pode continuar a conversa digitando novas perguntas ou frases.
Utilize os botões na barra lateral para limpar o histórico de conversas ou iniciar uma nova conversa.
Observações

Este é um projeto de exemplo simples e pode ser adaptado para atender às suas necessidades específicas.
Certifique-se de ter uma conta do Google Cloud Platform e de ter habilitado o LLM Gemini em seu projeto.
A chave de API do Google Cloud deve ser armazenada de forma segura no arquivo .env e não deve ser compartilhada publicamente.

5. Melhorias Futuras

Implementar um sistema de persistência para armazenar o histórico de conversas permanentemente.
Permitir que os usuários personalizem suas preferências de conversa, como idioma ou estilo de comunicação.
Integrar o chatbot com outras ferramentas ou serviços para oferecer uma experiência mais completa.

---------------------------------------------------------------------------------------------------------------------------------------
Contribuição e desenvolvedor:

Vinicius Meireles

Cientista de Dados e Especialista em IA

Professor de Computação

email: prof.viniciusmeireles@gmail.com

![logo](https://github.com/profviniciusmeireles/Gemini-Chat/assets/169489043/857c28b5-dd7b-410d-82aa-1dd628276c6f)

