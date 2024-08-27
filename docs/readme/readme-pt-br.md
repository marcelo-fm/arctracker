[![Readme EN](/assets/readme-en.svg)](/README.md)
# arctracker

![GitHub go.mod Go version](https://img.shields.io/github/go-mod/go-version/marcelo-fm/arctracker?style=for-the-badge) ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/marcelo-fm/arctracker/.github%2Fworkflows%2Fgo.yml?style=for-the-badge) ![GitHub Release](https://img.shields.io/github/v/release/marcelo-fm/arctracker?style=for-the-badge) ![GitHub Tag](https://img.shields.io/github/v/tag/marcelo-fm/arctracker?style=for-the-badge)

ArcGIS Licensing Tracker

ArcTracker fornece uma maneira fácil e interativa de acompanhar as licenças no seu código Python arcpy.

## Descrição

ArcTracker é uma aplicação CLI que busca na documentação do ArcGIS por licenças de ferramentas. Pode ser usada passando o caminho de um repositório como argumento, e ela irá buscar as licenças para cada ferramenta usada nos scripts Python. Também pode ser usada dentro de um pipeline, lendo o comando de uma ferramenta passada no pipeline, quando executada sem argumentos.

## Requisitos

A aplicação requer [ripgrep](https://github.com/BurntSushi/ripgrep) para a busca recursiva no diretório e no Stdin, e [jq](https://github.com/jqlang/jq) para o formatação do resultado do ripgrep.

Abaixo estão os passos de instalação para cada ferramenta:
- [ripgrep](https://github.com/BurntSushi/ripgrep?tab=readme-ov-file#installation)
- [jq](https://github.com/jqlang/jq?tab=readme-ov-file#installation)

## Instalação

Para instalar o programa, basta baixar o binário na página de [release](https://github.com/marcelo-fm/arctracker/releases) mais recente, ou você pode instalá-lo com go executando:

```go
go install github.com/marcelo-fm/arctracker@latest
```

Estou trabalhando na criação de pacotes para a maioria das distribuições Linux e gerenciadores de pacotes do Windows.

## Uso

ArcTracker tem duas formas de uso. A primeira é buscando recursivamente por ferramentas arcpy usadas em um projeto. Para isso, basta passar o caminho do diretório para visualizar uma tabela interativa das ferramentas usadas no projeto e o nível de licenças necessárias para executá-las.

![ArcTracker Usage](/assets/arctracker.gif)

Você também pode passar a flag `--json` para retornar a saída como JSON, ou a flag `--csv` para retornar a saída como CSV.

A flag `--output` é usada para escrever a saída JSON ou CSV em um arquivo.
