<details name="profile-language">
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="assets/lang-en-dark.svg"><img src="assets/lang-en-light.svg" width="42" height="26" alt="EN"></picture></summary>

<picture>
  <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/header-en-static-mobile-dark.svg">
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/header-en-static-mobile-light.svg">
  <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/header-en-static-dark.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/header-en-static-light.svg">
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/header-en-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/header-en-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-en-dark.svg">
  <img src="assets/header-en-light.svg" width="100%" alt="Aleksandr Kashevarov · Java &amp; TS Full Stack Engineer. Reliable Distributed High-load Systems.">
</picture>

### About me

I've been building backend applications and distributed systems since 2019. I worked as a lead developer on banking and enterprise projects. My work covered integrations, data models and the transition to event-driven workflows, with a focus on service performance and resilience.

I'm now building a **mass-market messenger for secure, real-time communication**, from Java services to a TypeScript and React interface. My focus is speed and reliability: prompt message delivery, continuous file streaming and connection recovery that keeps conversations going.

I pay particular attention to **call audio quality**, so people can hear each other comfortably. I'm developing a custom system that combines several neural networks to remove noise and pass microphone audio through only while someone is speaking.

### My Open Source Libraries

I'm developing libraries that make complex systems with continuous data streams easier to build. They cover file transfers, media resources and event recovery in the browser.

<sub>Libraries are licensed under MIT.</sub>

**[browser-media-cache](https://github.com/59Alex/browser-media-cache)** · TypeScript · <sub><a href="https://github.com/59Alex/browser-media-cache/blob/main/LICENSE">MIT</a></sub><br>
Shared media loading and caching across components. Blob URL lifecycle management avoids repeated downloads: a resource stays available while any component needs it, then its memory is released.

**[s3-file-streams](https://github.com/59Alex/s3-file-streams)** · Java / TypeScript · <sub><a href="https://github.com/59Alex/s3-file-streams/blob/main/LICENSE">MIT</a></sub><br>
Continuous file streaming between the browser, Java and S3 without buffering the entire file in memory. Backpressure respects the receiver's capacity, and cancellation releases the resources held by a transfer.

**[browser-sse-relay](https://github.com/59Alex/browser-sse-relay)** · TypeScript · <sub><a href="https://github.com/59Alex/browser-sse-relay/blob/main/LICENSE">MIT</a></sub><br>
SSE reconnection from the last processed event, followed by a transition to the live stream. If the server no longer retains the missed history, the application is signalled to resync its state.</details>

<details name="profile-language" open>
<summary><picture><source media="(prefers-color-scheme: dark)" srcset="assets/lang-ru-dark.svg"><img src="assets/lang-ru-light.svg" width="42" height="26" alt="RU"></picture></summary>

<picture>
  <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/header-static-mobile-dark.svg">
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/header-static-mobile-light.svg">
  <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/header-static-dark.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/header-static-light.svg">
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/header-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/header-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Александр Кашеваров · Java &amp; TS Full Stack Engineer. Надежные Распределенные Высоконагруженные Системы.">
</picture>

### Обо мне

С 2019 года разрабатываю серверные приложения и распределённые системы. Работал ведущим разработчиком в банковских и корпоративных проектах. Проектировал интеграции и модели данных, переводил бизнес-процессы на событийное взаимодействие. Занимался производительностью и устойчивостью сервисов.

Сейчас разрабатываю **массовый мессенджер для безопасного общения в реальном времени** — от Java-сервисов до интерфейса на TypeScript и React. В центре работы — скорость и надёжность: быстрая доставка сообщений, потоковая передача файлов и восстановление связи, чтобы общение оставалось непрерывным.

Особое внимание уделяю **качеству звука в звонках**, чтобы собеседникам было комфортно слышать друг друга. Для этого разрабатываю собственный механизм на базе нескольких нейросетей: они очищают звук от шума и пропускают сигнал микрофона только во время речи.

### Мои Open Source библиотеки

Разрабатываю библиотеки для построения сложных систем с потоковой передачей данных. Они посвящены работе с файлами и медиа, а также восстановлению событий в браузере.

<sub>Библиотеки защищены лицензией MIT.</sub>

**[browser-media-cache](https://github.com/59Alex/browser-media-cache)** · TypeScript · <sub><a href="https://github.com/59Alex/browser-media-cache/blob/main/LICENSE">MIT</a></sub><br>
Общая загрузка и кэширование медиа для нескольких компонентов. Управление временем жизни Blob URL помогает избежать повторных загрузок: изображение остаётся доступным, пока оно нужно хотя бы одному компоненту, а затем память освобождается.

**[s3-file-streams](https://github.com/59Alex/s3-file-streams)** · Java / TypeScript · <sub><a href="https://github.com/59Alex/s3-file-streams/blob/main/LICENSE">MIT</a></sub><br>
Передача файлов сквозным потоком между браузером, Java и S3 без накопления целого файла в памяти. Управление скоростью потока учитывает возможности получателя, а отмена передачи освобождает занятые ресурсы.

**[browser-sse-relay](https://github.com/59Alex/browser-sse-relay)** · TypeScript · <sub><a href="https://github.com/59Alex/browser-sse-relay/blob/main/LICENSE">MIT</a></sub><br>
Восстановление SSE-соединения с последнего обработанного события и переход к текущему потоку. Если сервер уже удалил пропущенную историю, приложение получает сигнал заново синхронизировать состояние.</details>
