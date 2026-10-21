<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/header-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/header-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Java Full Stack — from browser to backend.">
</picture>

<details name="profile-language">
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="assets/lang-en-dark.svg"><img src="assets/lang-en-light.svg" width="108" height="44" alt="English"></picture></summary>

# Aleksandr Kashevarov

**Java Full Stack Developer** · From the browser interaction to the backend transaction.

I build Java services and React applications, with a particular interest in what happens between them: streaming files, delivering events, and keeping state consistent when connections fail.

My work spans Spring APIs, Kafka pipelines, browser media, and containerized infrastructure. I'm now packaging reusable parts of that experience into open-source libraries.

**[Explore the libraries ↓](#building-in-the-open)**

<details open>
<summary><b>The stack in motion</b> · click to show or hide</summary>
<br>
<a href="#what-i-work-with" title="Explore the technologies">
<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/tech-strip-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/tech-strip-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/tech-strip-dark.svg">
  <img src="assets/tech-strip-light.svg" width="100%" alt="Java, Spring, TypeScript, React, Kafka, PostgreSQL, Redis, Docker and Kubernetes. Select to explore the stack.">
</picture>
</a>
</details>

### What I work with

**Backend**<br>
[Java 21](https://dev.java/) · [Spring Boot](https://spring.io/projects/spring-boot) · [WebFlux](https://docs.spring.io/spring-framework/reference/web/webflux.html) · [Kafka](https://kafka.apache.org/) · [PostgreSQL](https://www.postgresql.org/) · [Redis](https://redis.io/)

**Frontend**<br>
[TypeScript](https://www.typescriptlang.org/) · [React](https://react.dev/) · [Vite](https://vite.dev/) · Browser Streams · Server-Sent Events · WebRTC

**Infrastructure**<br>
[Docker](https://www.docker.com/) · [Kubernetes](https://kubernetes.io/) · S3-compatible storage · OAuth2 / Keycloak · Observability

### Building in the open

Three libraries, each focused on a problem I've worked with in application code. **Early development:** the repositories currently contain implementation plans and release criteria.

#### [browser-media-cache](https://github.com/59Alex/browser-media-cache)

**TypeScript · Browser infrastructure**<br>
One media resource, several UI components. Planned shared loading and explicit blob URL ownership keep cleanup predictable as components mount and disappear.

#### [s3-file-streams](https://github.com/59Alex/s3-file-streams)

**Java + TypeScript · Streaming**<br>
One continuous stream from the browser through Java to S3, and back. Designed around bounded buffering, backpressure, cancellation, and the difference between bytes sent and an object committed.

#### [browser-sse-relay](https://github.com/59Alex/browser-sse-relay)

**TypeScript · Real-time delivery**<br>
A reconnect is only the first step. Planned cursor replay and a resync contract address events missed while the client was offline.

---

**How I approach engineering**<br>
I care about where guarantees start, where they stop, and how to demonstrate both with a reproducible test.

Have a use case for one of these libraries? Open an issue in its repository — concrete scenarios help shape the API.

</details>

<details name="profile-language" open>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="assets/lang-ru-dark.svg"><img src="assets/lang-ru-light.svg" width="108" height="44" alt="Русский"></picture></summary>

# Александр Кашеваров

**Java Full Stack разработчик** · От действия пользователя в браузере до транзакции на сервере.

Разрабатываю сервисы на Java и приложения на React. Особенно интересны задачи на их стыке: потоковая передача файлов, доставка событий и согласованность состояния при обрывах соединения.

Работаю со Spring API, потоками событий Kafka, медиа в браузере и контейнерной инфраструктурой. Сейчас выделяю переиспользуемые решения из своего опыта в открытые библиотеки.

**[Посмотреть библиотеки ↓](#открытые-библиотеки)**

<details open>
<summary><b>Технологии в движении</b> · нажми, чтобы скрыть или показать</summary>
<br>
<a href="#с-чем-работаю" title="Перейти к технологиям">
<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/tech-strip-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/tech-strip-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/tech-strip-dark.svg">
  <img src="assets/tech-strip-light.svg" width="100%" alt="Java, Spring, TypeScript, React, Kafka, PostgreSQL, Redis, Docker и Kubernetes. Нажми, чтобы перейти к стеку.">
</picture>
</a>
</details>

### С чем работаю

**Серверная часть**<br>
[Java 21](https://dev.java/) · [Spring Boot](https://spring.io/projects/spring-boot) · [WebFlux](https://docs.spring.io/spring-framework/reference/web/webflux.html) · [Kafka](https://kafka.apache.org/) · [PostgreSQL](https://www.postgresql.org/) · [Redis](https://redis.io/)

**Клиентская часть**<br>
[TypeScript](https://www.typescriptlang.org/) · [React](https://react.dev/) · [Vite](https://vite.dev/) · Browser Streams · Server-Sent Events · WebRTC

**Инфраструктура**<br>
[Docker](https://www.docker.com/) · [Kubernetes](https://kubernetes.io/) · S3-совместимые хранилища · OAuth2 / Keycloak · Наблюдаемость

### Открытые библиотеки

Три библиотеки для задач, с которыми я работал в прикладном коде. **Ранняя стадия разработки:** сейчас в репозиториях находятся планы реализации и критерии готовности релизов.

#### [browser-media-cache](https://github.com/59Alex/browser-media-cache)

**TypeScript · Инфраструктура браузера**<br>
Один медиаресурс — несколько компонентов интерфейса. Планирую общую загрузку и явное управление временем жизни blob URL, чтобы появление и удаление компонентов не приводили к утечкам или преждевременной очистке ресурса.

#### [s3-file-streams](https://github.com/59Alex/s3-file-streams)

**Java + TypeScript · Потоковая передача**<br>
Единый непрерывный поток из браузера через Java в S3 и обратно. В основе проекта — ограниченное потребление памяти, backpressure, отмена операции и чёткое различие между отправленными байтами и сохранённым объектом.

#### [browser-sse-relay](https://github.com/59Alex/browser-sse-relay)

**TypeScript · Доставка событий в реальном времени**<br>
Переподключение — только первый шаг. Планирую повторную доставку по курсору и протокол повторной синхронизации для событий, пропущенных клиентом за время отсутствия связи.

---

**Мой подход к разработке**<br>
Мне важно понимать, при каких условиях система даёт гарантии, где они заканчиваются и как проверить это воспроизводимым тестом.

Есть задача для одной из библиотек? Создай issue в её репозитории — конкретные сценарии помогают спроектировать полезный API.

</details>
