# 🔐 Security Scanner

Scanner de segurança em linha de comando que varre arquivos de código em
busca de credenciais expostas (senhas, chaves de API, tokens) deixadas por
engano no código-fonte — o mesmo tipo de problema que ferramentas como
Gitleaks resolvem em pipelines de CI/CD.

Este projeto nasceu do interesse em DevSecOps: a proposta foi entender, na
prática, como esse tipo de ferramenta de segurança funciona por dentro —
desde a leitura de arquivos até o uso de expressões regulares (regex) para
detectar padrões com precisão, evitando falsos positivos.

## Funcionalidades

- **Varredura de pasta completa**: percorre recursivamente todos os
  arquivos `.py` de um diretório e suas subpastas.
- **Detecção por padrão (regex)**: identifica linhas onde uma palavra
  suspeita (`password`, `token`, `key`, `secret`, `adm`) aparece como nome
  de variável atribuída a um valor entre aspas — não apenas em qualquer
  lugar do texto, o que evita alarmes falsos.
- **Tratamento de erros**: avisa de forma amigável se um arquivo ou pasta
  não for encontrado, em vez de quebrar o programa.

## Tecnologias

- **Python 3** (sem dependências externas)
- **re** (expressões regulares, biblioteca padrão)
- **os** (navegação de diretórios, biblioteca padrão)

## Estrutura do projeto

security-scanner/
├── scanner.py # Lógica de varredura: scan_file e scan_folder
├── main.py # Interface de linha de comando
├── teste_inseguro.py # Arquivo de exemplo com credenciais fictícias para teste
└── README.md

## Como funciona a detecção (resumo)

O padrão de busca usado é:

```python
r"(password|token|key|secret|adm)\s*=\s*[\"'].*[\"']"
```

Isso identifica linhas no formato `palavra_suspeita = "valor"`, ignorando
menções à palavra em outros contextos (como listas ou comentários), o que
reduz bastante os falsos positivos comparado a uma busca de texto simples.

## Como rodar

Não precisa instalar nenhuma dependência — só Python 3.

```bash
git clone https://github.com/FabianoSeara/security-scanner.git
cd security-scanner
python main.py
```

O programa vai pedir o caminho da pasta a ser escaneada (use `.` para a
pasta atual).

## Exemplo de saída

Digite o caminho da pasta: .

Iniciando a varredura: .
[ALERT] Suspicious line: api_key = "sk_live_abc123xyz789"
[ALERT] Suspicious line: SECRET_TOKEN = "ghp_1234567890abcdef"

Varredura concluída.

## Próximos passos

- [ ] Suportar outras extensões de arquivo (`.js`, `.env`, `.json`)
- [ ] Contabilizar estatísticas da varredura (arquivos escaneados, total de alertas)
- [ ] Permitir ignorar pastas específicas (como `__pycache__`, `.git`)

---

Projeto desenvolvido por [Fabiano Seára](https://github.com/FabianoSeara) como
parte do meu portfólio de transição de carreira para a área de tecnologia,
com apoio de IA (Claude) no processo de aprendizado.
