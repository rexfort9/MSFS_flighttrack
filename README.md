MSFS 2020 Virtual flightlog
====
Этот код использует библиотеки [Python-SimConnect](https://pypi.org/project/SimConnect/) для отслеживания положения самолета в MSFS2020 и визуализации пройденного пути на веб-странице с помощью Flask и JavaScript.
----
Предполагается, что уже установлены библиотеки Flask и python-SimConnect, а также что есть файл шаблона HTML с именем ["index.html"](https://github.com/rexfort9/MSFS_flighttrack/blob/main/index.html) для отображения веб-страницы. <br>

В файле "index.html" можно использовать JavaScript и библиотеки, такие как Leaflet.js, для создания интерактивной веб-карты и отображения пройденного пути. В JavaScript можно подписаться на событие  "'position_update'", чтобы обновлять карту в реальном времени с новыми данными о положении самолета. <br>
