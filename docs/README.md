# Library guides / Руководства библиотек

A standalone, bilingual documentation browser for model-change-set, relational-paths, pg-task-lease and reactive-pipeline-kit 0.3.0. Each guide explains capabilities through code, expected behavior and boundaries. This directory is a local preview; no site deployment is configured.

Самостоятельный двуязычный обозреватель документации четырёх библиотек версии 0.3.0. Возможности разобраны на примерах с ожидаемым результатом и ограничениями. Сейчас это локальная версия; публикация сайта не настроена.

## Open / Открыть

From this directory / Из этого каталога:

```sh
python3 -m http.server 4179 --bind 127.0.0.1
```

Open / Откройте: http://127.0.0.1:4179/

You can also open `index.html` directly. No third-party scripts, fonts, analytics or network requests are needed to read the guides. Clipboard access depends on browser permissions; the page offers a fallback for file URLs.

Можно открыть `index.html` напрямую. Для чтения не нужны сторонние скрипты, шрифты, аналитика или сетевые запросы. Доступ к буферу обмена зависит от разрешений браузера; предусмотрен резервный способ копирования для file URL.

## Language and navigation / Язык и навигация

- EN/RU changes text in place and remembers the selection in localStorage. If storage is unavailable, switching still works in the current tab.
- The active button has an inset shadow. Both language layouts reserve the same space, keeping the current reading position stable.
- Library/section links can be bookmarked. Browser Back/Forward works between topics; changing language does not add history entries.
- Search matches both languages and code. Inactive translations are visually hidden and excluded from assistive navigation.
- Dark mode follows the system. Keyboard focus and reduced-motion preferences are supported.

- EN/RU меняет текст на месте и сохраняет выбор в localStorage. Если хранилище недоступно, переключение работает в текущей вкладке.
- Активная кнопка выглядит вдавленной. Для обоих переводов резервируется одинаковое место, чтобы позиция чтения не менялась.
- Ссылку на библиотеку и раздел можно сохранить. Назад/вперёд работает между темами; переключение языка не добавляет записи в историю.
- Поиск учитывает оба языка и код. Неактивный перевод скрыт визуально и от вспомогательной навигации.
- Тёмная тема следует системной. Поддержаны клавиатура и предпочтение уменьшенной анимации.

## Update / Обновление

Edit `content/*.json`, then rebuild the offline bundle:

Измените `content/*.json` и пересоберите автономный пакет данных:

```sh
python3 scripts/build.py
```

The builder checks the section IDs, translations, block types and downloadable example files. UI code lives in `assets/app.js` and `assets/style.css`. Do not edit generated `assets/content.js` directly.

Сборщик проверяет идентификаторы разделов, переводы, типы блоков и файлы примеров. Интерфейс находится в `assets/app.js` и `assets/style.css`. Не редактируйте сгенерированный `assets/content.js` вручную.

Examples are in `examples/<library>/`. Follow the guide's build/classpath instructions and the example's prerequisites. The Java snippets use real library APIs; API names stay the same in both languages. Installation is currently through Maven Local, not a claim of Maven Central availability.

Примеры находятся в `examples/<library>/`. Следуйте инструкциям руководства по сборке/classpath и требованиям примера. Java-фрагменты используют реальный API; имена API одинаковы в обоих языках. Установка пока через Maven Local, без заявления о доступности в Maven Central.

## GitHub README

GitHub sanitizes script tags and custom styles in README rendering. This browser is a separate HTML page; it does not imply that JavaScript can execute inside a repository or profile README. See https://github.com/github/markup.

GitHub удаляет скрипты и пользовательские стили из README. Обозреватель — отдельная HTML-страница; он не добавляет исполнение JavaScript в README репозитория или профиля.
