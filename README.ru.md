[English](https://github.com/59Alex) · **Русский**

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/header-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/header-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Java Full Stack — от браузера до серверной части.">
</picture>

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

**Серверная часть**  
[Java 21](https://dev.java/) · [Spring Boot](https://spring.io/projects/spring-boot) · [WebFlux](https://docs.spring.io/spring-framework/reference/web/webflux.html) · [Kafka](https://kafka.apache.org/) · [PostgreSQL](https://www.postgresql.org/) · [Redis](https://redis.io/)

**Клиентская часть**  
[TypeScript](https://www.typescriptlang.org/) · [React](https://react.dev/) · [Vite](https://vite.dev/) · Browser Streams · Server-Sent Events · WebRTC

**Инфраструктура**  
[Docker](https://www.docker.com/) · [Kubernetes](https://kubernetes.io/) · S3-совместимые хранилища · OAuth2 / Keycloak · Наблюдаемость

### Открытые библиотеки

Три библиотеки для задач, с которыми я работал в прикладном коде. **Ранняя стадия разработки:** сейчас в репозиториях находятся планы реализации и критерии готовности релизов.

#### [browser-media-cache](https://github.com/59Alex/browser-media-cache)

**TypeScript · Инфраструктура браузера**  
Один медиаресурс — несколько компонентов интерфейса. Планирую общую загрузку и явное управление временем жизни blob URL, чтобы появление и удаление компонентов не приводили к утечкам или преждевременной очистке ресурса.

#### [s3-file-streams](https://github.com/59Alex/s3-file-streams)

**Java + TypeScript · Потоковая передача**  
Единый непрерывный поток из браузера через Java в S3 и обратно. В основе проекта — ограниченное потребление памяти, backpressure, отмена операции и чёткое различие между отправленными байтами и сохранённым объектом.

#### [browser-sse-relay](https://github.com/59Alex/browser-sse-relay)

**TypeScript · Доставка событий в реальном времени**  
Переподключение — только первый шаг. Планирую повторную доставку по курсору и протокол повторной синхронизации для событий, пропущенных клиентом за время отсутствия связи.

---

**Мой подход к разработке**  
Мне важно понимать, при каких условиях система даёт гарантии, где они заканчиваются и как проверить это воспроизводимым тестом.

Есть задача для одной из библиотек? Создай issue в её репозитории — конкретные сценарии помогают спроектировать полезный API.
