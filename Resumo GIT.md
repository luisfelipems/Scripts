git config --global user.email "you@example.com"
Configura o endereço de e-mail associado ao autor dos commits. Esse e-mail será exibido no histórico de commits e deve corresponder ao cadastrado no repositório remoto (ex.: GitHub).
Observação: Use --global para aplicar a configuração a todos os repositórios do sistema. Para configurar um repositório específico, remova o --global.


git config --global user.name "Your Name"
Descrição: Configura o nome do autor dos commits, que será exibido no histórico. Funciona de forma similar ao comando para configurar o e-mail.


git add .
Descrição: Adiciona todos os arquivos modificados e novos arquivos no diretório atual ao staging (área de preparação), deixando-os prontos para o próximo commit.
Usar com cuidado para evitar arquivos desnecessários.


git add teste.py
Adiciona o arquivo específico teste.py ao staging, preparando-o para o próximo commit.


git commit -m "Mensagem"
Cria um commit para salvar as alterações no histórico do repositório. A mensagem entre aspas descreve as mudanças realizadas (ex.: "Corrige bug na função X").


git push origin main
Envia os commits do branch local (neste caso, main) para o repositório remoto.
origin é o nome padrão para o repositório remoto. Se o branch principal tiver outro nome, substitua main pelo nome correto.


git pull
Baixa as alterações do branch remoto para o branch local e tenta mesclá-las automaticamente.
Boa prática: Sempre sincronize com git pull antes de fazer alterações locais para evitar conflitos.


git status
Exibe o estado atual do repositório, informando: arquivos modificados, arquivos que precisam ser adicionados ao staging, alterações já preparadas para commit.


git log
Mostra o histórico detalhado dos commits no branch atual, incluindo:
Hash do commit, Autor, Data, Mensagem do commit.
git log --oneline para visualizar uma versão resumida.


git reset
Desfaz alterações nos commits, na área de staging e/ou no diretório de trabalho. Pode:
reverter commits recentes, remover arquivos do staging, descartar alterações locais.
Opções comuns:
--soft: Mantém mudanças no staging.
--mixed (padrão): Remove mudanças do staging, mas mantém no diretório de trabalho.
--hard: Desfaz completamente as alterações e apaga as mudanças do diretório de trabalho.
O uso de --hard é irreversível.


git restore
Restaura arquivos ou descarta mudanças no diretório de trabalho ou no staging. Não afeta o histórico de commits.
Cenários comuns:
Descartar mudanças locais em um arquivo:
git restore arquivo.txt
git restore --staged arquivo.txt
Diferença em relação ao git reset: O restore é focado em alterações de arquivos individuais, enquanto o reset pode alterar o histórico de commits.

git init
É usado para inicializar um repositório Git em um diretório. Ele configura o diretório atual para que o Git comece a rastrear alterações nos arquivos, criando uma subpasta chamada .git que contém todos os metadados necessários para o controle de versão.

