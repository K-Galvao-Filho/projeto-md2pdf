## 3.1 Definição de REST e os 6 Princípios de Roy Fielding

### O que é REST?
Representational State Transfer (REST) é um estilo arquitetural para sistemas distribuídos, introduzido por Roy Fielding em sua dissertação de doutorado em 2000 na Universidade da Califórnia, Irvine. REST não é um protocolo ou padrão rígido, mas um conjunto de diretrizes que aproveitam os recursos do protocolo HTTP para criar APIs escaláveis, interoperáveis e fáceis de manter. Ele é amplamente utilizado em aplicações web modernas devido à sua simplicidade e alinhamento com os padrões da web.

REST foca na manipulação de **recursos**, que são entidades identificáveis (como usuários, produtos ou tarefas) acessadas por meio de **URIs** (Uniform Resource Identifiers). As interações ocorrem através de **métodos HTTP** padrão (GET, POST, PUT, DELETE, etc.), e os dados são geralmente representados em formatos como JSON ou XML. A essência do REST está em sua capacidade de criar interfaces previsíveis e consistentes, permitindo que clientes (como navegadores, aplicativos móveis ou outros servidores) se comuniquem com servidores de forma eficiente.

#### Contexto Histórico
REST surgiu em um momento em que a web estava evoluindo de páginas estáticas para sistemas dinâmicos e distribuídos. Antes do REST, tecnologias como SOAP (Simple Object Access Protocol) dominavam, mas eram complexas devido à sua dependência de XML e envelopes de mensagens pesados. Fielding propôs REST como uma alternativa mais leve, aproveitando a infraestrutura existente do HTTP, como métodos, cabeçalhos e códigos de status, para simplificar o desenvolvimento de APIs.

#### Por que REST é Relevante?
- **Escalabilidade**: Permite que sistemas cresçam sem comprometer a performance, graças à separação entre cliente e servidor.
- **Interoperabilidade**: Funciona com qualquer linguagem ou plataforma que suporte HTTP.
- **Facilidade de Integração**: APIs RESTful são amplamente compatíveis com frameworks modernos, como React, Angular ou aplicativos móveis.
- **Manutenção**: A interface uniforme reduz a complexidade do código.

### Os 6 Princípios de Roy Fielding
Roy Fielding definiu seis restrições arquiteturais que caracterizam um sistema REST. APIs que aderem a essas restrições são chamadas de **RESTful**. Vamos explorar cada princípio com detalhes e exemplos práticos.

#### 1. Cliente-Servidor
O princípio cliente-servidor estabelece uma separação clara entre o cliente, que faz requisições (ex.: um navegador ou aplicativo), e o servidor, que armazena dados e processa essas requisições. Essa separação melhora a portabilidade do cliente (pode ser implementado em qualquer plataforma) e a escalabilidade do servidor (pode ser otimizado independentemente).

- **Exemplo Prático**: Um aplicativo de e-commerce (cliente) solicita a lista de produtos de um servidor via `GET /produtos`. O servidor retorna os dados, sem precisar saber como o cliente os exibirá (em um app móvel, navegador ou desktop).
- **Benefício**: O cliente pode ser atualizado sem impactar o servidor, e vice-versa. Por exemplo, uma empresa pode mudar seu banco de dados (ex.: de MySQL para PostgreSQL) sem alterar o frontend.
- **Implementação**: Em uma API REST, o cliente envia requisições HTTP, e o servidor responde com dados em JSON, sem armazenar informações sobre a interface do cliente.

#### 2. Sem Estado (Stateless)
Cada requisição do cliente ao servidor deve conter todas as informações necessárias para ser processada. O servidor não mantém o estado do cliente entre requisições, ou seja, não armazena informações como "o usuário está na página 2" ou "o usuário está logado". Isso simplifica o servidor e melhora a escalabilidade, pois ele não precisa gerenciar sessões.

- **Exemplo Prático**: Para autenticar um usuário, cada requisição inclui um token JWT (JSON Web Token) no cabeçalho `Authorization`. O servidor valida o token em cada chamada, sem depender de sessões anteriores.
  ```http
  GET /tarefas HTTP/1.1
  Host: api.exemplo.com
  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
  ```
- **Benefício**: Servidores podem ser reiniciados ou escalados horizontalmente (adicionando mais máquinas) sem perder contexto.
- **Desafio**: O cliente precisa enviar mais dados em cada requisição (ex.: tokens ou parâmetros), mas isso é compensado pela simplicidade do servidor.

#### 3. Cache
As respostas do servidor podem ser marcadas como "cacheáveis", permitindo que o cliente armazene os dados localmente para evitar requisições repetidas. Isso melhora a performance e reduz a carga no servidor. O protocolo HTTP fornece cabeçalhos como `Cache-Control`, `ETag` e `Last-Modified` para gerenciar o cache.

- **Exemplo Prático**: Uma requisição `GET /categorias` retorna uma lista de categorias de produtos com o cabeçalho:
  ```http
  Cache-Control: max-age=3600
  ```
  O cliente armazena a resposta por 1 hora (3600 segundos), evitando novas requisições durante esse período.
- **Benefício**: Reduz a latência e o uso de banda, especialmente para dados que mudam raramente (ex.: lista de estados ou países).
- **Implementação**: Frameworks como Express (Node.js) permitem configurar cabeçalhos de cache. Exemplo:
  ```javascript
  res.set('Cache-Control', 'public, max-age=3600');
  ```

#### 4. Interface Uniforme
A interface uniforme é o coração do REST, garantindo que a API seja consistente e previsível. Ela inclui quatro subprincípios:
- **Identificação de Recursos**: Cada recurso (ex.: uma tarefa) é identificado por uma URI única (ex.: `/tarefas/123`).
- **Manipulação por Representações**: O cliente manipula representações do recurso (ex.: JSON) em vez do recurso diretamente. Por exemplo, um cliente envia um JSON para criar uma tarefa e recebe um JSON como resposta.
- **Mensagens Autoexplicativas**: Requisições e respostas usam métodos HTTP padrão e cabeçalhos claros. Por exemplo, `Content-Type: application/json` indica o formato dos dados.
- **HATEOAS (Hypermedia as the Engine of Application State)**: A resposta pode incluir links para ações relacionadas, permitindo que o cliente "navegue" pela API.
  - **Exemplo de HATEOAS**:
    ```json
    {
      "id": 123,
      "titulo": "Estudar REST",
      "_links": {
        "self": "/tarefas/123",
        "delete": "/tarefas/123",
        "update": "/tarefas/123",
        "all": "/tarefas"
      }
    }
    ```

- **Exemplo Prático**: Uma API de tarefas permite listar todas as tarefas (`GET /tarefas`), obter uma tarefa específica (`GET /tarefas/123`), criar uma tarefa (`POST /tarefas`) e excluir uma tarefa (`DELETE /tarefas/123`). Todas as URIs seguem a mesma estrutura, e as respostas são consistentes em formato (JSON).
- **Benefício**: Desenvolvedores podem prever como interagir com a API, mesmo sem documentação detalhada, devido à consistência.

#### 5. Sistema em Camadas (Layered System)
A arquitetura REST pode ser dividida em camadas (ex.: cliente, servidor web, banco de dados, cache), onde cada camada não precisa saber como as outras funcionam. Isso permite escalabilidade e segurança, pois camadas intermediárias (como proxies ou balanceadores de carga) podem ser adicionadas sem afetar o cliente.

- **Exemplo Prático**: Um cliente faz uma requisição a `api.exemplo.com/tarefas`. Um balanceador de carga redireciona a requisição para um dos vários servidores backend, que consulta um banco de dados. O cliente não sabe (nem precisa saber) sobre essas camadas.
- **Benefício**: Permite adicionar camadas de segurança (ex.: firewalls), cache (ex.: Redis) ou monitoramento sem alterar o cliente ou o servidor principal.
- **Implementação**: Em um ambiente de produção, ferramentas como NGINX (open-source) podem atuar como camada de proxy reverso.

#### 6. Código Sob Demanda (Code on Demand) (Opcional)
O servidor pode enviar código executável (ex.: JavaScript) ao cliente para estender suas funcionalidades. Esse princípio é opcional e raramente usado em APIs REST modernas, que priorizam dados em vez de lógica.

- **Exemplo Prático**: Um servidor envia um script JavaScript para renderizar um formulário dinâmico no cliente. Por exemplo:
  ```json
  {
    "form": {
      "script": "function validateForm() { ... }"
    }
  }
  ```
- **Benefício**: Reduz a complexidade do cliente, mas pode introduzir riscos de segurança.
- **Uso Moderno**: Raro em APIs REST, mas comum em aplicações web que combinam REST com renderização no cliente.

#### Por que Seguir Esses Princípios?
Aderir aos princípios REST garante que a API seja:
- **Escalável**: Pode lidar com grandes volumes de requisições.
- **Manutenível**: Fácil de atualizar e estender.
- **Interoperável**: Funciona com diferentes clientes e plataformas.
- **Previsível**: Desenvolvedores podem entender a API rapidamente.

---

## 3.2 Diferença entre REST e RESTful

Os termos **REST** e **RESTful** são frequentemente confundidos, mas têm significados distintos:

- **REST**: É o estilo arquitetural definido por Roy Fielding, composto pelos seis princípios descritos acima. Ele estabelece as diretrizes para projetar sistemas distribuídos que aproveitam o HTTP.
- **RESTful**: Refere-se a uma implementação que segue rigorosamente os princípios REST. Uma API é considerada RESTful apenas se aderir às restrições, como interface uniforme, ausência de estado e suporte a cache.

### Exemplos Práticos
- **API RESTful**:
  - Usa URIs claras (ex.: `/usuarios/123`).
  - Emprega métodos HTTP padrão (ex.: `GET` para leitura, `POST` para criação).
  - Retorna respostas consistentes em JSON, com links HATEOAS.
  - Exemplo: A PokéAPI (`https://pokeapi.co`) segue os princípios REST, com URIs como `/pokemon/pikachu` e respostas que incluem links para recursos relacionados.
- **API Não-RESTful**:
  - Usa URIs baseadas em ações (ex.: `/executarAcao?tipo=criarUsuario`).
  - Mantém estado no servidor (ex.: sessões armazenadas entre requisições).
  - Não segue convenções de métodos HTTP (ex.: usar POST para tudo).
  - Exemplo: Uma API que usa uma única rota `/api` com parâmetros para todas as ações, como `/api?acao=listar`.

### Por que a Distinção Importa?
- **Interoperabilidade**: APIs RESTful são mais fáceis de integrar, pois seguem padrões amplamente aceitos.
- **Manutenção**: APIs não-RESTful podem ser mais difíceis de entender e manter, especialmente em equipes grandes.
- **Escalabilidade**: APIs RESTful são projetadas para suportar grandes volumes de requisições devido à ausência de estado e suporte a cache.

### Como Identificar uma API RESTful?
- Verifique se as URIs representam recursos, não ações.
- Confirme que os métodos HTTP são usados corretamente (ex.: GET para leitura, POST para criação).
- Observe se as respostas incluem metadados úteis, como links HATEOAS ou cabeçalhos de cache.

---

## 3.3 Estrutura de uma API REST

Uma API REST é organizada em torno de **recursos**, **métodos HTTP** e **endpoints**, com respostas que seguem padrões claros. Vamos detalhar cada componente.

### Recursos
Um recurso é qualquer entidade que a API gerencia, como um usuário, uma tarefa ou um produto. Ele é identificado por uma URI única e representado em um formato como JSON.

- **Exemplo de Recurso**:
  ```json
  {
    "id": 1,
    "titulo": "Estudar REST APIs",
    "concluida": false,
    "prioridade": "alta"
  }
  ```
- **URI**: `/tarefas/1` (identifica a tarefa com ID 1).
- **Representação**: O cliente recebe ou envia uma representação do recurso (ex.: JSON acima), não o recurso diretamente armazenado no banco de dados.

#### Tipos de Recursos
- **Recurso Individual**: Representa uma única entidade (ex.: `/tarefas/1`).
- **Coleção de Recursos**: Representa um grupo de entidades (ex.: `/tarefas`).
- **Recursos Aninhados**: Representam relações (ex.: `/usuarios/123/tarefas` para tarefas de um usuário específico).

### Métodos HTTP
Os métodos HTTP definem as ações que podem ser executadas em um recurso:
- **GET**: Recupera dados de um recurso ou coleção.
  - Exemplo: `GET /tarefas` retorna a lista de tarefas.
- **POST**: Cria um novo recurso.
  - Exemplo: `POST /tarefas` com corpo JSON cria uma nova tarefa.
- **PUT**: Atualiza um recurso existente, substituindo-o completamente.
  - Exemplo: `PUT /tarefas/1` atualiza todos os campos da tarefa com ID 1.
- **PATCH**: Atualiza parcialmente um recurso.
  - Exemplo: `PATCH /tarefas/1` altera apenas o campo `concluida`.
- **DELETE**: Remove um recurso.
  - Exemplo: `DELETE /tarefas/1` exclui a tarefa com ID 1.
- **Outros Métodos**:
  - **HEAD**: Similar ao GET, mas retorna apenas cabeçalhos, útil para verificar a existência de um recurso.
  - **OPTIONS**: Retorna os métodos HTTP permitidos para um recurso.

### Endpoints
Endpoints são URIs que identificam recursos ou coleções. Eles devem seguir convenções RESTful:
- **Nomenclatura**:
  - Use substantivos (ex.: `/tarefas`) em vez de verbos (ex.: `/listarTarefas`).
  - Evite extensões de arquivo (ex.: `/tarefas.json`); o formato é indicado pelo cabeçalho `Content-Type`.
- **Hierarquia**:
  - Reflita relações entre recursos (ex.: `/usuarios/123/tarefas` para tarefas de um usuário).
- **Plural vs. Singular**:
  - Use plural para coleções (ex.: `/tarefas`).
  - Use singular para recursos específicos (ex.: `/tarefas/1`).
- **Parâmetros**:
  - **Query Parameters**: Para filtros ou paginação (ex.: `/tarefas?concluida=true&limit=10`).
  - **Path Parameters**: Para identificar recursos específicos (ex.: `/tarefas/1`).

Exemplo de endpoints para uma API de tarefas:
- `GET /tarefas`: Lista todas as tarefas.
- `GET /tarefas/1`: Obtém a tarefa com ID 1.
- `POST /tarefas`: Cria uma nova tarefa.
- `PUT /tarefas/1`: Atualiza a tarefa com ID 1.
- `DELETE /tarefas/1`: Exclui a tarefa com ID 1.

### Respostas HTTP
As respostas de uma API REST incluem:
- **Código de Status**:
  - `200 OK`: Requisição bem-sucedida (GET, PUT).
  - `201 Created`: Recurso criado (POST).
  - `204 No Content`: Sucesso sem corpo (DELETE).
  - `400 Bad Request`: Erro na requisição (ex.: dados inválidos).
  - `404 Not Found`: Recurso não encontrado.
  - `500 Internal Server Error`: Erro no servidor.
- **Cabeçalhos**:
  - `Content-Type`: Formato da resposta (ex.: `application/json`).
  - `Location`: URL do recurso criado (ex.: `/tarefas/123` após POST).
  - `Cache-Control`: Define regras de cache.
- **Corpo**: Contém os dados (JSON ou XML) ou mensagens de erro.
  - Exemplo de resposta para `GET /tarefas/1`:
    ```json
    {
      "id": 1,
      "titulo": "Estudar REST APIs",
      "concluida": false,
      "_links": {
        "self": "/tarefas/1",
        "all": "/tarefas"
      }
    }
    ```

#### Exemplo Completo
- **Requisição**:
  ```http
  GET /tarefas/1 HTTP/1.1
  Host: api.exemplo.com
  Accept: application/json
  ```
- **Resposta**:
  ```http
  HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: max-age=3600

  {
    "id": 1,
    "titulo": "Estudar REST APIs",
    "concluida": false,
    "_links": {
      "self": "/tarefas/1",
      "all": "/tarefas"
    }
  }
  ```

---

## 3.4 Atividade Prática: Análise de Exemplos de APIs REST Públicas

Nesta atividade, você explorará APIs REST públicas para aplicar os conceitos teóricos. Usaremos ferramentas gratuitas e open-source, como **cURL** ou a extensão **REST Client** para Visual Studio Code, para fazer requisições e analisar respostas. O objetivo é identificar recursos, métodos HTTP, endpoints e avaliar a conformidade com os princípios REST.

### APIs Sugeridas
1. **JSONPlaceholder** (https://jsonplaceholder.typicode.com):
   - API fictícia para testes, com recursos como usuários, postagens e comentários.
   - Endpoints: `/users`, `/posts`, `/comments`, `/todos`.
2. **PokéAPI** (https://pokeapi.co):
   - API para dados de Pokémon, com recursos como pokémons, tipos, habilidades e evoluções.
   - Endpoints: `/pokemon`, `/type`, `/ability`.
3. **OpenWeatherMap** (https://openweathermap.org/api):
   - API gratuita (com limite) para dados meteorológicos.
   - Endpoint: `/weather` (requer chave de API gratuita).

### Passo a Passo
1. **Ferramentas Necessárias**:
   - **cURL**: Ferramenta de linha de comando para requisições HTTP, incluída em Linux/macOS e disponível para Windows.
   - **REST Client**: Extensão open-source para VS Code que permite testar APIs diretamente no editor.
   - **Postman**: Ferramenta gratuita para testar APIs (use a versão gratuita).
   - Para OpenWeatherMap, crie uma conta em https://openweathermap.org para obter uma chave de API gratuita.

2. **Análise da JSONPlaceholder**:
   - **Endpoint**: `GET /todos`
   - **Requisição**:
     ```bash
     curl https://jsonplaceholder.typicode.com/todos
     ```
   - **Resposta (parcial)**:
     ```json
     [
       {
         "userId": 1,
         "id": 1,
         "title": "delectus aut autem",
         "completed": false
       },
       {
         "userId": 1,
         "id": 2,
         "title": "quis ut nam facilis et officia qui",
         "completed": false
       },
       ...
     ]
     ```
   - **Análise**:
     - **Recurso**: Tarefas (`todos`).
     - **Método HTTP**: GET.
     - **Princípios REST**:
       - Interface uniforme: URI clara (`/todos`), resposta em JSON.
       - Sem estado: Cada requisição é independente.
       - Cache: Verifique cabeçalhos com `curl -v` (ex.: `Cache-Control`).
       - Limitação: Não implementa HATEOAS (falta links para recursos relacionados).

3. **Análise da PokéAPI**:
   - **Endpoint**: `GET /pokemon/charizard`
   - **Requisição**:
     ```bash
     curl https://pokeapi.co/api/v2/pokemon/charizard
     ```
   - **Resposta (parcial)**:
     ```json
     {
       "id": 6,
       "name": "charizard",
       "base_experience": 267,
       "height": 17,
       "abilities": [
         {
           "ability": {
             "name": "blaze",
             "url": "https://pokeapi.co/api/v2/ability/66/"
           }
         }
       ],
       ...
     }
     ```
   - **Análise**:
     - **Recurso**: Pokémon (`charizard`).
     - **Método HTTP**: GET.
     - **Princípios REST**:
       - HATEOAS: Inclui links para recursos relacionados (ex.: `"url": "https://pokeapi.co/api/v2/ability/66/"`).
       - Interface uniforme: URIs consistentes (`/pokemon/{nome}`).
       - Sem estado: Requisições são independentes.
       - Cache: Suporta cache via cabeçalhos (verifique com `curl -v`).

4. **Análise da OpenWeatherMap**:
   - **Endpoint**: `GET /data/2.5/weather?q=Sao%20Paulo,br&appid=SUA_CHAVE_API`
   - **Requisição**:
     ```bash
     curl "https://api.openweathermap.org/data/2.5/weather?q=Sao%20Paulo,br&appid=SUA_CHAVE_API"
     ```
   - **Resposta (parcial)**:
     ```json
     {
       "coord": { "lon": -46.6361, "lat": -23.5475 },
       "weather": [
         {
           "id": 800,
           "main": "Clear",
           "description": "clear sky"
         }
       ],
       "main": {
         "temp": 298.15,
         "feels_like": 298.37,
         ...
       },
       ...
     }
     ```
   - **Análise**:
     - **Recurso**: Clima (`weather`).
     - **Método HTTP**: GET.
     - **Princípios REST**:
       - Interface uniforme: Usa query parameters (`q` para cidade) e retorna JSON.
       - Sem estado: Cada requisição inclui a chave de API.
       - Cache: Suporta cache (verifique cabeçalhos).
       - Limitação: Não usa HATEOAS.

5. **Tarefa Prática**:
   - Escolha duas APIs (ex.: JSONPlaceholder e PokéAPI).
   - Explore pelo menos três endpoints por API (ex.: `/users`, `/posts`, `/todos` no JSONPlaceholder; `/pokemon`, `/type`, `/ability` na PokéAPI).
   - Documente:
     - **Recurso**: Qual entidade é representada (ex.: usuários, tarefas).
     - **Método HTTP**: GET, POST, etc.
     - **Estrutura da URI**: Ex.: `/todos` ou `/pokemon/{nome}`.
     - **Resposta**: Formato (JSON), campos principais e metadados.
     - **Princípios REST**:
       - Interface uniforme (URIs claras, métodos corretos).
       - Sem estado (independência das requisições).
       - Cache (verifique cabeçalhos com `curl -v`).
       - HATEOAS (presença de links).
   - Exemplo de documentação para `/users/1` no JSONPlaceholder:
     ```
     Recurso: Usuário
     Endpoint: GET https://jsonplaceholder.typicode.com/users/1
     Resposta:
     {
       "id": 1,
       "name": "Leanne Graham",
       "username": "Bret",
       "email": "Sincere@april.biz",
       "address": {
         "street": "Kulas Light",
         "city": "Gwenborough"
       }
     }
     Princípios REST:
     - Interface uniforme: URI clara (/users/1), resposta JSON.
     - Sem estado: Requisição independente.
     - Cache: Suporta cache (verifique Cache-Control).
     - Limitação: Não implementa HATEOAS.
     ```
   - Use cURL ou REST Client para testar. Exemplo:
     ```bash
     curl https://jsonplaceholder.typicode.com/users/1
     ```

### Dicas para a Atividade
- Use `curl -v` para inspecionar cabeçalhos HTTP e confirmar suporte a cache ou outros metadados.
- Explore a documentação oficial das APIs (ex.: https://pokeapi.co/docs/v2) para descobrir endpoints adicionais.
- Tente fazer requisições com métodos diferentes (ex.: POST na JSONPlaceholder) para entender respostas e erros.
- Compare as APIs em termos de consistência, clareza e adesão aos princípios REST.

---

## Conclusão

Este capítulo forneceu uma base sólida sobre REST, cobrindo sua definição, os seis princípios de Roy Fielding, a diferença entre REST e RESTful, e a estrutura de uma API REST (recursos, métodos HTTP, endpoints). A atividade prática conectou a teoria à prática, analisando APIs públicas para identificar como os princípios são aplicados. Este conhecimento é a base para os próximos capítulos, onde exploraremos a modelagem de dados (Capítulo 4) e a implementação prática de APIs REST com ferramentas open-source (Capítulos 5 e 6).

### Dicas para Continuar
- Explore outras APIs públicas, como a **GitHub API** (https://api.github.com) ou **SWAPI** (https://swapi.dev).
- Pesquise cabeçalhos HTTP (ex.: `ETag`, `If-Modified-Since`) para entender melhor o cache.
- Experimente criar requisições com diferentes métodos HTTP na JSONPlaceholder para observar respostas e erros.

### Conexão com o Próximo Capítulo
O Capítulo 4 abordará a estrutura de dados em APIs REST, focando em JSON e XML, que são os formatos usados para representar recursos nas requisições e respostas. Compreender os princípios REST deste capítulo será essencial para modelar dados de forma consistente e eficiente.