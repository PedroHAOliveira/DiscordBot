# 🤖 NOME_DO_BOT - Seu Assistente Inteligente no Discord

Um bot Discord versátil que combina interações simples com o poder da API do Gemini para respostas inteligentes.

## ✨ Funcionalidades Principais

- **Respostas Inteligentes**: Integração com a API do Gemini para respostas contextualizadas
- **Saudações Personalizadas**: Reconhece usuários específicos com mensagens únicas
- **Moderação Básica**: Limpeza automática em canais dedicados
- **Notificações de Inicialização**: Avisa quando o bot está online
- **Comandos Simples**: Interações básicas como `!ping` para testar o bot

## 🛠️ Configuração

1. Clone este repositório
2. Instale as dependências:
   ```bash
   pip install discord.py requests python-dotenv
   ```
3. Crie um arquivo `.env` com suas chaves:
   ```
   DISCORD_TOKEN=seu_token_do_discord
   GEMINI_API_KEY=sua_chave_gemini
   ```
4. Configure os IDs dos canais e usuários no código
5. Execute o bot:
   ```bash
   python nome_do_arquivo.py
   ```

## 🎯 Como Usar

- **Chamar o Gemini**: Digite `!+NOMEDOBOT [sua pergunta]`
- **Testar o bot**: Envie `!ping` para receber `Pong!`
- **Canal de imagens**: Mensagens de texto são automaticamente removidas no canal especificado

## ⚙️ Personalização

Edite o código para:
- Adicionar mais comandos personalizados
- Modificar a lista de usuários com respostas especiais
- Ajustar os canais de notificação
- Mudar o comportamento do bot

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

*"Desenvolvido por Pedro Oliveira [Kynoa]"* ✨
