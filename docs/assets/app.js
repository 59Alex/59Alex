(() => {
  'use strict';
  const libraries = window.LIBRARY_GUIDES;
  const $ = (selector) => document.querySelector(selector);
  const strings = {
    subtitle: { en: 'Open source · Practical guides', ru: 'Open source · Руководства' },
    search: { en: 'Find a topic', ru: 'Найти тему' },
    placeholder: { en: 'Retry, schema, context…', ru: 'Повторы, схемы, контекст…' },
    libraries: { en: 'Libraries', ru: 'Библиотеки' },
    footer: { en: 'Java 17 / 21 / 25 / 27\nMIT licensed', ru: 'Java 17 / 21 / 25 / 27\nЛицензия MIT' },
    guide: { en: 'Practical guide', ru: 'Практическое руководство' },
    chapter: { en: 'In this guide', ru: 'В этом руководстве' },
    repository: { en: 'Repository ↗', ru: 'Репозиторий ↗' },
    copy: { en: 'Copy', ru: 'Копировать' },
    copied: { en: 'Code copied', ru: 'Код скопирован' },
    copyFailed: { en: 'Select the code to copy it manually.', ru: 'Выделите код и скопируйте его вручную.' },
    previous: { en: 'Previous topic', ru: 'Предыдущая тема' },
    next: { en: 'Next topic', ru: 'Следующая тема' },
    examples: { en: 'Example files', ru: 'Файлы примера' },
    noResults: { en: 'No topics found. Try another word.', ru: 'Темы не найдены. Попробуйте другое слово.' },
  };
  let language = 'en';
  try { language = localStorage.getItem('library-guides-language') === 'ru' ? 'ru' : 'en'; } catch (_) {}
  let currentLibrary;
  let currentSection;
  const main = $('#reading');
  const navigation = $('#navigation');
  const search = $('#guide-search');
  const results = $('#search-results');

  function node(tag, className, text) {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (text !== undefined) element.textContent = text;
    return element;
  }
  function translated(value, tag = 'span', className = '') {
    const container = node(tag, `i18n ${className}`.trim());
    for (const lang of ['en', 'ru']) {
      const text = node('span', '', value[lang]);
      text.lang = lang;
      text.setAttribute('aria-hidden', String(lang !== language));
      text.inert = lang !== language;
      container.append(text);
    }
    return container;
  }
  function link(library, section, className) {
    const a = node('a', className);
    a.href = `#${library.id}/${section.id}`;
    return a;
  }
  function applyLanguage(nextLanguage, persist = true) {
    if (!['en', 'ru'].includes(nextLanguage)) return;
    // Both translations share a grid cell. Reserving their maximum height
    // keeps the reading position and surrounding controls stable on switching.
    const readingTop = main.scrollTop;
    const navTop = $('#sidebar').scrollTop;
    language = nextLanguage;
    document.documentElement.lang = language;
    document.documentElement.dataset.language = language;
    document.querySelectorAll('.i18n > [lang]').forEach((element) => {
      const inactive = element.lang !== language;
      element.setAttribute('aria-hidden', String(inactive));
      element.inert = inactive;
    });
    document.querySelectorAll('[data-language-button]').forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.languageButton === language));
    });
    search.placeholder = strings.placeholder[language];
    $('#menu-button').setAttribute('aria-label', language === 'ru' ? 'Меню руководств' : 'Guide menu');
    main.setAttribute('aria-label', language === 'ru' ? 'Содержание руководства' : 'Guide content');
    $('#sidebar').setAttribute('aria-label', language === 'ru' ? 'Навигация по руководствам' : 'Guide navigation');
    document.title = currentLibrary ? `${currentSection.title[language]} · ${currentLibrary.name}` : 'Library guides';
    main.scrollTop = readingTop;
    $('#sidebar').scrollTop = navTop;
    if (persist) {
      try { localStorage.setItem('library-guides-language', language); } catch (_) {}
    }
  }
  function renderNavigation() {
    navigation.replaceChildren();
    libraries.forEach((library, index) => {
      const item = link(library, library.sections[0], `library-link${library === currentLibrary ? ' active' : ''}`);
      item.append(node('span', 'library-number', String(index + 1).padStart(2, '0')), node('span', '', library.name));
      if (library === currentLibrary) item.setAttribute('aria-current', 'true');
      navigation.append(item);
      if (library === currentLibrary) {
        const sections = node('div', 'section-nav');
        for (const section of library.sections) {
          const a = link(library, section, 'section-link');
          if (section === currentSection) a.setAttribute('aria-current', 'page');
          a.append(translated(section.title));
          sections.append(a);
        }
        navigation.append(sections);
      }
    });
  }
  async function copyCode(code, button) {
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(code);
      } else {
        const area = node('textarea', 'sr-only');
        area.value = code;
        document.body.append(area);
        area.focus({ preventScroll: true });
        area.select();
        const copied = document.execCommand('copy');
        area.remove();
        button.focus({ preventScroll: true });
        if (!copied) throw new Error('Clipboard unavailable');
      }
      button.replaceChildren(translated(strings.copied));
      $('#announcement').textContent = strings.copied[language];
      setTimeout(() => { if (button.isConnected) button.replaceChildren(translated(strings.copy)); }, 1800);
    } catch (_) {
      $('#announcement').textContent = strings.copyFailed[language];
      button.replaceChildren(translated(strings.copyFailed));
    }
  }
  function renderBlock(block) {
    if (block.type === 'text') return translated(block.text, 'p', 'text-block');
    if (block.type === 'list') {
      const list = node('ul', 'point-list');
      block.items.forEach((item) => { const li = node('li'); li.append(translated(item)); list.append(li); });
      return list;
    }
    if (block.type === 'note') {
      const note = node('aside', 'note');
      note.append(translated(block.title, 'h3'), translated(block.text, 'p'));
      return note;
    }
    if (block.type === 'code') {
      const figure = node('figure', 'code-block');
      const bar = node('div', 'code-toolbar');
      const button = node('button', 'copy-button');
      button.type = 'button';
      button.append(translated(strings.copy));
      button.addEventListener('click', () => copyCode(block.code, button));
      bar.append(node('span', '', block.language), button);
      const pre = node('pre');
      pre.tabIndex = 0;
      pre.setAttribute('aria-label', `${block.language} code`);
      pre.append(node('code', '', block.code));
      figure.append(bar, pre);
      if (block.caption) figure.append(translated(block.caption, 'figcaption', 'code-caption'));
      return figure;
    }
    throw new Error(`Unsupported guide block: ${block.type}`);
  }
  function renderGuide() {
    const guide = $('#guide');
    guide.replaceChildren();
    const intro = node('header', 'library-intro');
    intro.append(translated(strings.guide, 'div', 'eyebrow'), node('h1', 'library-heading', currentLibrary.name), translated(currentLibrary.summary, 'p', 'library-summary'));
    const meta = node('div', 'meta-row');
    meta.append(node('span', 'meta-tag', currentLibrary.runtime), node('span', 'meta-tag', `v${currentLibrary.version}`), node('span', 'meta-tag', 'MIT'));
    const repository = node('a', 'repo-link');
    repository.href = currentLibrary.repo;
    repository.target = '_blank'; repository.rel = 'noopener noreferrer';
    repository.append(translated(strings.repository)); meta.append(repository); intro.append(meta);
    guide.append(intro);
    const article = node('article', 'chapter');
    article.setAttribute('aria-labelledby', 'chapter-title');
    const index = currentLibrary.sections.indexOf(currentSection);
    const topline = node('div', 'chapter-topline');
    topline.append(node('span', 'chapter-counter', `${String(index + 1).padStart(2, '0')} / ${String(currentLibrary.sections.length).padStart(2, '0')}`), translated(strings.chapter));
    const heading = translated(currentSection.title, 'h2'); heading.id = 'chapter-title';
    article.append(topline, heading, translated(currentSection.lead, 'p', 'lead'));
    currentSection.blocks.forEach((block) => article.append(renderBlock(block)));
    const chapterNavigation = node('nav', 'chapter-navigation');
    chapterNavigation.setAttribute('aria-label', 'Previous / Next · Назад / Далее');
    if (index > 0) {
      const previous = currentLibrary.sections[index - 1];
      const a = link(currentLibrary, previous);
      a.append(translated(strings.previous, 'small'), translated(previous.title)); chapterNavigation.append(a);
    }
    if (index < currentLibrary.sections.length - 1) {
      const next = currentLibrary.sections[index + 1];
      const a = link(currentLibrary, next);
      a.append(translated(strings.next, 'small'), translated(next.title)); chapterNavigation.append(a);
    }
    article.append(chapterNavigation);
    const downloads = node('footer', 'downloads');
    downloads.append(translated(strings.examples));
    for (const file of currentLibrary.downloads || []) {
      const a = node('a', '', file.name); a.href = file.path; a.download = file.name; downloads.append(a);
    }
    article.append(downloads); guide.append(article);
  }
  function closeMenu() {
    $('#sidebar').classList.remove('is-open');
    $('#menu-button').setAttribute('aria-expanded', 'false');
    $('#menu-backdrop').hidden = true;
    main.inert = false;
  }
  function route() {
    const [libraryId, sectionId] = location.hash.slice(1).split('/');
    currentLibrary = libraries.find((library) => library.id === libraryId) || libraries[0];
    currentSection = currentLibrary.sections.find((section) => section.id === sectionId) || currentLibrary.sections[0];
    renderNavigation(); renderGuide(); applyLanguage(language, false);
    main.scrollTop = 0;
    closeMenu();
  }
  function renderSearch() {
    const query = search.value.trim().toLocaleLowerCase();
    results.replaceChildren(); results.hidden = !query;
    navigation.hidden = Boolean(query); $('#navigation-label').hidden = Boolean(query);
    if (!query) return;
    let count = 0;
    for (const library of libraries) for (const section of library.sections) {
      if (!JSON.stringify({ name: library.name, section }).toLocaleLowerCase().includes(query)) continue;
      const a = link(library, section);
      a.append(translated(section.title), node('small', '', library.name));
      a.addEventListener('click', () => { search.value = ''; renderSearch(); });
      results.append(a); count++;
    }
    if (!count) results.append(translated(strings.noResults, 'p', 'empty-search'));
  }
  if (!Array.isArray(libraries) || libraries.length === 0) {
    $('#guide').textContent = 'Guides unavailable. Run: python3 scripts/build.py / Выполните: python3 scripts/build.py';
    return;
  }
  $('#brand-subtitle').append(translated(strings.subtitle));
  $('#search-label').append(translated(strings.search));
  $('#navigation-label').append(translated(strings.libraries));
  $('#sidebar-footer').append(translated(strings.footer));
  $('.skip-link').replaceChildren(translated({ en: 'Skip to guide', ru: 'К руководству' }));
  $('.skip-link').addEventListener('click', (event) => {
    event.preventDefault();
    main.focus({ preventScroll: true });
  });
  document.querySelectorAll('[data-language-button]').forEach((button) => {
    button.addEventListener('click', () => applyLanguage(button.dataset.languageButton));
  });
  $('#menu-button').addEventListener('click', () => {
    const isOpen = $('#sidebar').classList.toggle('is-open');
    $('#menu-button').setAttribute('aria-expanded', String(isOpen));
    $('#menu-backdrop').hidden = !isOpen;
    main.inert = isOpen;
    if (isOpen) search.focus({ preventScroll: true });
  });
  $('#menu-backdrop').addEventListener('click', closeMenu);
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      const wasOpen = $('#sidebar').classList.contains('is-open');
      closeMenu(); search.value = ''; renderSearch();
      if (wasOpen) $('#menu-button').focus({ preventScroll: true });
    }
  });
  search.addEventListener('input', renderSearch);
  search.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') { const first = results.querySelector('a'); if (first) first.click(); }
  });
  window.addEventListener('hashchange', route);
  window.matchMedia('(max-width: 760px)').addEventListener('change', closeMenu);
  route();
})();
