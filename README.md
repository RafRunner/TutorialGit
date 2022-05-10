# Tutorial de git/GitHub

Olá! Nesse repositório temos como objetivo fornecer um projeto extremamente simples (apenas dois arquivos) em python usando conceitos muito simples da linguagem para ter o maior nível de acessibilidade possível.

Com esse projeto podemos demonstrar as funcionalidades mais básicas do git: clone, branch, add, commit, push, pull, merge etc incentivando os participantes a clonarem o projeto, fazerem modificações em suas próprias branches/repositórios e depois commitar e pushar para um repositório git remoto (no caso, no github). Utilizaremos também a funcionalidade de fork e merge requests para dar uma ideia de como é o processo para contribuir em projetos open source (código aberto).

## O que é o git? Pra que ele serve? É a mesma coisa de GitHub?

Git é um software para controle de versionamento distribuído. O que isso significa? Significa que você, juntamente com outros contribuidores, pode manter controle de um repositório (projeto) tendo acesso a cada versão incremental do programa. Cada mudança incremental do programa é chamada de "commit" e todos podem ter acesso a cada commit juntamente com quem o fez, quando foi feito, uma mensagem explicativa entre outras informações. Como cada commit é incremental, podemos "voltar no tempo" no projeto, vendo ele em cada um se seus estágios e cada mudança, como se tivéssemos acesso a todas as versões já salvas de cada arquivo. Isso é um software de controle de versionamento.

Agora, o que significa ele ser distribuído? Um dos principais (se não o principal) objetivo do git é facilitar que diversas pessoas trabalhem simultaneamente em um mesmo projeto (muitas vezes no mesmo arquivo) porém não em tempo real, como no Google Docs. Dessa forma, para evitar os chamados conflitos, cada desenvolvedor cria uma "cópia" do projeto própria para desenvolver uma nova funcionalidade ou corrigir um bug. Ele faz modificações (commits) nessa ramificação (chamada branch) para que seu trabalho não interfira com o código principal até que fique 100% pronto. Assim que o objetivo da ramificação for cumprido, o desenvolvedor propõe que sua branch seja mesclada (chamado merge) na ramificação principal (geralmente chamada de main ou master). Outros contribuidores analisam se as mudanças são desejadas e corretas e então podem fazer o merge, levando todos os commits (logo, as modificações) para a ramificação principal. Note que merges não precisam ser feitos somente para a branch principal. Qualquer branch pode ser mesclada em qualquer outra.

Porém, vamos supor que enquanto o desenvolvedor A trabalhava em um arquivo, um outro desenvolvedor B modificou o mesmo arquivo, ambos modificaram a mesma linha e as mudanças do desenvolvedor B já estão na branch principal. Nessa caso o git não consegue saber qual a versão correta da linha, e portanto o conflito deve ser resolvido manualmente. Isso é feito fazendo o merge na direção contrária (da branch principal para a branch do desenvolvedor A) e então decidindo qual das duas versões da linha é a correta ou a reescrevendo de forma que funcione com ambas as modificações antes do merge ser feito. Após essas correções é feito um commit e o merge pode seguir normalmente.

Além disso, como o git não é um software que funciona em tempo real, quando você "clona" um repositório (baixa um projeto) você terá uma cópia local de todas as informações do repositório remoto. Quando você criar um branch para trabalhar, ela inicialmente será apenas local, assim como qualquer commit que você fizer. Para que suas modificações sejam levadas até o repositório remoto (onde outras pessoas poderão ver, analisar e usar o seu código modificado) é necessário fazer o chamado "push". Da mesma forma, é necessário atualizar sua versão local do repositório remoto. Isso é feito fazendo um "fetch" (atualizando as informações sobre o repositório remoto) e um pull (atualiza a sua branch atual com todos os novos commits).

E agora você me pergunta: então o que é o GitHub? Simples, é necessário um servidor para hospedar o repositório remoto do git para que todos os desenvolvedores tenham acesso a ele. O GitHub é um dos serviços que proveem isso e outras funcionalidades bônus como: revisão (e até edição) de código, resolução de conflitos, criação de projetos, criação de ramificações, solicitações de merge, navegação pelo código e muitas outras no próprio site, sem a necessidade de clonar o projeto localmente. Ou seja, o GitHub é nada mais nada menos que um servidor onde são hospedados diversos projetos versionados pelo git com outras funcionalidades para facilitar a vida dos desenvolvedores. Eles não são a mesma coisa, são complementares. Existem outros sites de hospedagem de projetos git que de certa forma competem com o GitHub, como o GitLab, Assembla, Bitbucket e outros.

## Como usar o git

A melhor forma de aprender a usar o git, é usando a linha de comando. Dessa forma, independentemente do editor de texto, sistema operacional ou até mesmo se você tem ou não acesso a uma interface gráfica (como em um servidor) você não estará totalmente perdido e conseguirá fazer o que quer. Esse guia foi feito em um sistema Linux, porém os processos podem ser replicados no Windows e MacOS sem problemas.

Lembre-se que você sempre pode pesquisar na internet como fazer certas coisas, a sintaxe pode ser um pouco complicada, mas para isso é bom entender os conceitos do git para saber o que pesquisar. O git também tem uma documentação própria muito boa. Para utiliza-la basta adicionar a opção `--help` no fim de algum comando. Por exemplo:

    git --help

irá te mostrar os comandos existentes do git e as possessives opções. Para ver ajuda de um comando específico, coloque o nome do comando antes de help, como:

    git commit --help

Além disso, eu te recomendo criar um arquivo de texto onde você anotará os comandos que considerar mais importantes, juntamente com a explicação de cada um nas suas palavras. Esse arquivo será um recurso muito importante ao londo da sua jornada.

Antes de mais nada, você primeiro deve configurar qual será seu nome e email de forma global (para todos os projetos que você trabalhar no computador atual) no git. Eles serão usado para te identificar entre os commits e contribuidores de um projeto. Caso você já tenha uma conta no GitHub, é bom que você use o mesmo email que sua conta, e de preferência use seu nome completo ou primeiro + último nome como o nome:

    git config --global user.name "Seu nome completo"
    git config --global user.email "Seu email"

Ok, então para começar a usar o git você precisa criar um repositório git ou clonar um já existente. Vamos começar criando um do zero. Navegue até a pasta onde você quer criar o repositório pelo terminal e então execute:

    git init

Isso irá criar uma pasta escondida, a `.git`, onde o git guardará informações relevantes do projeto. Não mexa nessa pasta manualmente!

Agora crie um arquivo qualquer, pode ser um README.md (arquivo no formato markdown presente em quase qualquer projeto que geralmente contêm descrições de como instalar,compilar ou contribuir para o projeto) e insira algumas linhas de texto quaisquer. Note que por padrão, o git não irá "acompanhar" novos arquivos criados no projeto. Execute `git status` e veja que o arquivo aparece abaixo de "Untracked files". Para adicionar o arquivo no projeto, é necessário usar o comando:

    git add README.md

Execute novamente o `git status` e note que o arquivo aparece agora sob "Changes to be committed" com a cor verde. É bom saber que, caso você não queira digitar o nome do arquivo criado ou adicionar múltiplos arquivos ao mesmo tempo você pode executar o comando acima como `git add .` , porém tome cuidado para não adicionar arquivos sem querer.

Outro ponto importante, é que antes de fazer um commit é necessário fazer o "staging" das suas modificações, ou seja, confirmar quais modificações (no caso por arquivo) você quer que sejam commitadas. O git faz isso para que seja possível fazer um commit sem incluir todas as modificações atuais. Isso é feito através do comando `git add` que acabei de apresentar. Ou seja, antes de fazer um commit, você precisar rodar um `git add` citando os arquivos que quer commitar.

Assim que estiver satisfeito com suas modificações, vamos criar um commit. Para isso, usamos o comando:

    git commit -m "Sua mensagem de commit aqui"

Para confirmar que o commit foi feito, é bom executar o comando

    git log

Ele irá te mostrar uma lista com cada commit na branch atual (que, caso você tenha seguido o tutorial até aqui, é a principal e a única que existe) com informações como o hash, nome e email do autor (por isso a importância de configura-los), data e hora do commit e a mensagem de commit. Caso queira ver uma versão resumida do log, use `git log --oneline` onde só será mostrado o hash e a mensagem de cada commit.


Agora, faça algumas modificações no arquivo README: adicione linhas, remova linhas, edite linhas, faça o que desejar. Caso queira você pode também adicionar um novo arquivo qualquer. Após salvar os arquivos, para ver exatamente quais mudanças foram feitas, execute: `git diff`. Você deve ver uma saída como:

![git diff output](./imagens/git%20diff%20output.png)

Note que o `git diff` mostra somente modificações em relação ao commit anterior de arquivos modificados mas que ainda não passaram por staging (ou seja não foram adicionados pelo `git add`). Caso você queira ver modificações que já foram para staging, execute:

    git diff --staged

E caso queira remover um arquivo do staging, execute:

    git reset nome_arquivo

Caso queira desfazer todas as suas modificações e voltar ao mesmo estado commit anterior (mas cuidado, você perderá todo o seu progresso, mesmo que tenha salvado os arquivos!):

    git reset --hard

Outra coisa importante: muitas vezes, temos arquivos dentro do projeto que não queremos incluir no git, por serem dependências muito grandes ou então arquivos de configuração do editor, que variam de desenvolvedor para desenvolvedor. Para evitar que os arquivos sejam adicionados no git deve ser criado o arquivo `.gitignore` . Nesse arquivos temos esse arquivo, ele tem uma linha com `__pycache__/` , o que significa que todas as pastas com esse nome serão ignoradas, já que são apenas caches do python. Leia mais sobre esses arquivos e o que pode ser feito neles no seguinte link (em inglês):

https://gist.github.com/jstnlvns/ebaa046fae16543cc9efc7f24bcd0e31

Agora você já tem o básico para usar o git localmente. Na próxima parte, você vai aprender a usar o GitHub (e qualquer outro servidor de git) e trabalhar com projetos remotos e com outros desenvolvedores.

## Como usar o GitHub (e repositórios remotos do git de forma geral)

## Os principais e mais usados comandos do git

Esse repositório foi inicialmente criado com o propósito de servir como um mini curso/palestra organizado pelo Centro Acadêmico do curso de Engenharia da Computação da Universidade Federal de Goiás, idealizado por Rafael Nunes Santana.