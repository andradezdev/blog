# Guia de Instalação e Configuração — Blog

Este documento contém o guia prático de comandos de terminal para instalação, parametrização, atualização e manutenção do aplicativo **Blog** no ecossistema **ERPZ**.

> ⚠️ **Importante**: Substitua `[sitename]` pelo nome do site onde deseja operar (ex: `dev.erpz.io`).

---

## 1. Instalação no Bench

Acesse a pasta do seu bench:

```bash
cd ~/bench
```

Baixe o aplicativo a partir do repositório:

```bash
bench get-app https://github.com/andradezdev/blog.git
```

Instale o aplicativo no site de destino:

```bash
bench --site [sitename] install-app blog
```

Execute a sincronização de tabelas e esquemas de dados:

```bash
bench --site [sitename] migrate
```

Compile os arquivos estáticos de interface:

```bash
bench build --app blog
```

Limpe o cache do site para carregar as novas rotas e permissões:

```bash
bench --site [sitename] clear-cache
```

---

## 2. Configurações e Parametrizações Recomendadas

Após a instalação, configure as opções do seu blog:

1. **Configurações Globais do Blog (`Blog Settings`):**
   - Acesse via barra de busca rápida no Desk ou pelo atalho do Workspace.
   - Defina o **Título do Blog** e a **Introdução do Blog** que aparecerão no cabeçalho público.
   - Configure a seção **Chamada para Ação (CTA)** caso queira exibir um botão de conversão ao final de cada post (Título, Subtítulo, Rótulo e URL de destino).
   - Ajuste as opções de **Moderação de Comentários** e limite de requisições por IP (*Rate Limits*).

2. **Cadastro de Autores (`Blogger`):**
   - Cadastre os membros da equipe que produzirão conteúdo em **Autor / Blogger**.
   - Vincule o registro ao **Usuário** correspondente e adicione uma biografia curta e avatar.

3. **Categorias de Publicação (`Blog Category`):**
   - Crie as categorias editoriais (ex: *Notícias*, *Tecnologia*, *Negócios*) para organizar a navegação dos leitores.

4. **Publicação do Primeiro Artigo (`Blog Post`):**
   - Crie o artigo, selecione o autor e categoria.
   - Escreva o conteúdo em Rich Text, Markdown ou HTML.
   - Configure a imagem de destaque (*Cover Image*) e as tags de SEO.
   - Marque a caixa **Publicado** (`Published`) e defina a data de veiculação.

---

## 3. Atualização do Aplicativo

Para sincronizar o aplicativo com as últimas melhorias do repositório oficial:

```bash
cd ~/bench/apps/blog
git pull origin develop
cd ~/bench
bench build --app blog
bench --site [sitename] migrate
bench --site [sitename] clear-cache
```

Se necessário, reinicie os processos de execução:

```bash
sudo supervisorctl restart all
```

---

## 4. Desinstalação

Para desinstalar o aplicativo de um site específico:

```bash
cd ~/bench
bench --site [sitename] uninstall-app blog
```

Para remover o aplicativo completamente do bench:

```bash
bench remove-app blog
```
