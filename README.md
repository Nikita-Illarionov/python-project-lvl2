<a href="https://codeclimate.com/github/Nikita-Illarionov/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/2ecf27e347ddcab399bd/maintainability" /></a>

<a href="https://codeclimate.com/github/Nikita-Illarionov/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/2ecf27e347ddcab399bd/test_coverage" /></a>

<a href="https://github.com/Nikita-Illarionov/python-project-lvl2/actions"><img src="https://github.com/Nikita-Illarionov/python-project-lvl2/workflows/Travis_CI/badge.svg" /></a>

Вычислитель отличий – программа определяющая разницу между между двумя структурами данных. Это популярная задача, для решения которой существует множество онлайн сервисов http://www.jsondiff.com/. Подобный механизм, например, используется при выводе тестов или при автоматическом отслеживании изменении в конфигурационных файлах.

Возможности утилиты:
- Поддержка разных форматов входных данных: json, yaml
- Генерация отчета в виде plain text, stylish и json

Пример использования:
~~~
$ gendiff --format plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed 
~~~

Инструкция по установке и использованию (видеоинструкцию можно посмотреть ниже):
- создать виртуальное окружение: python -m venv test_env
- обновить pip (рекомендуется): test_env/bin/pip install --upgrade pip
- скачать утилиту: test_env/bin/pip install -i https://test.pypi.org/simple/ nikita-illarionov-gendiff
- запустить утилиту (команда gendiff): gendiff file_path1 file_path2

Видео-инструкции по установке и использованию:
<a href="https://asciinema.org/a/AsTwN0oXV1AFxKqZg6g5po4tC" target="_blank"><img src="https://asciinema.org/a/AsTwN0oXV1AFxKqZg6g5po4tC.svg" /></a>

<a href="https://asciinema.org/a/SXoiVCS1qg4KQYN00MQAzX5b8" target="_blank"><img src="https://asciinema.org/a/SXoiVCS1qg4KQYN00MQAzX5b8.svg" /></a>

<a href="https://asciinema.org/a/jRvjuWBENeJc0NmhF25cj7SD0" target="_blank"><img src="https://asciinema.org/a/jRvjuWBENeJc0NmhF25cj7SD0.svg" /></a>

<a href="https://asciinema.org/a/sHHMz7DIudzaNfwHLic2XMvHU" target="_blank"><img src="https://asciinema.org/a/sHHMz7DIudzaNfwHLic2XMvHU.svg" /></a>
