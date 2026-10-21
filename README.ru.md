<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/header-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/header-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Aleksandr Kashevarov - Java Full Stack Engineer. Надёжные распределённые высоконагруженные системы.">
</picture>

<a href="#user-content-portfolio-ru" title="RU"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/lang-ru-dark.svg"><img src="assets/lang-ru-light.svg" width="42" height="26" alt="RU"></picture></a><a href="#user-content-portfolio-en" title="EN"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/lang-en-dark.svg"><img src="assets/lang-en-light.svg" width="42" height="26" alt="EN"></picture></a>

<details name="profile-language" open>
<summary>О себе и проектах</summary>
<a id="portfolio-ru"></a>

Разрабатываю **cnnect**: Java-сервисы и React-интерфейс для общения, медиа и событий в реальном времени. Работаю с API, обработкой событий, хранением данных и доставкой изменений в браузер.

- **Backend:** Java, Spring Boot / WebFlux, Kafka, PostgreSQL, Redis. Транзакции, повторная доставка событий, восстановление соединений.
- **Frontend:** TypeScript, React, Vite, WebRTC. Предзагрузка контента, общий медиакэш и управление временем жизни ресурсов.
- **Инфраструктура:** Docker, Kubernetes, S3-совместимые хранилища, Keycloak и наблюдаемость. Node.js использую в инструментах разработки и тестах.

### Библиотеки

Выделяю повторяющиеся задачи из cnnect в самостоятельные проекты. Сейчас в этих репозиториях — описание контрактов и планы реализации; опубликованных пакетов ещё нет.

**[browser-media-cache](https://github.com/59Alex/browser-media-cache)** · TypeScript<br>
Один медиаресурс часто нужен нескольким компонентам. Библиотека для общей загрузки и владения Blob URL: закрытие одной карточки не должно ломать изображение в другой, а неиспользуемые ресурсы должны освобождаться.

**[s3-file-streams](https://github.com/59Alex/s3-file-streams)** · Java / TypeScript<br>
Передача файлов единым потоком между браузером, Java и S3. Цель — обойтись без накопления целого файла в памяти, учитывать скорость получателя и корректно отменять незавершённую передачу.

**[browser-sse-relay](https://github.com/59Alex/browser-sse-relay)** · TypeScript<br>
Восстановление событий после потери связи: продолжить чтение с последнего обработанного курсора, затем перейти к live-потоку. Если история уже недоступна — явно запросить синхронизацию состояния.

</details>

<details name="profile-language">
<summary>About & projects</summary>
<a id="portfolio-en"></a>

I develop **cnnect**, a set of Java services and a React interface for communication, media and real-time events. My work covers APIs, event processing, data storage and delivering updates to the browser.

- **Backend:** Java, Spring Boot / WebFlux, Kafka, PostgreSQL and Redis. Transactions, event redelivery and connection recovery.
- **Frontend:** TypeScript, React, Vite and WebRTC. Content prefetching, shared media caching and resource lifecycles.
- **Infrastructure:** Docker, Kubernetes, S3-compatible storage, Keycloak and observability. I use Node.js for development tooling and tests.

### Libraries

I am extracting recurring problems from cnnect into independent projects. These repositories currently contain contracts and implementation plans; packages have not been released yet.

**[browser-media-cache](https://github.com/59Alex/browser-media-cache)** · TypeScript<br>
Several components often need the same media resource. Shared loading and Blob URL ownership should let one card disappear without breaking another, and release resources when they are no longer needed.

**[s3-file-streams](https://github.com/59Alex/s3-file-streams)** · Java / TypeScript<br>
Continuous file transfer between the browser, Java and S3. The goal is to avoid collecting an entire file in memory, respect the receiver's speed and cancel unfinished transfers correctly.

**[browser-sse-relay](https://github.com/59Alex/browser-sse-relay)** · TypeScript<br>
Recover events after a disconnect: resume from the last processed cursor, then switch to the live stream. If retained history is no longer available, explicitly request a state resync.

</details>
