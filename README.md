Projektbeschreibung


Dieses Projekt ist eine Webanwendung, die es Benutzern ermöglicht, Immobilienbuchungen zu verwalten. Mit Hilfe einer RESTful API können Benutzer Immobilien suchen, buchen und verwalten. Die Anwendung umfasst auch eine Verwaltungsschnittstelle, über die Administratoren Immobilienanzeigen und Buchungsprozesse verwalten können.

Funktionen
Suche und Filterung von Immobilien nach Preis, Standort, Anzahl der Zimmer und Typ.

Möglichkeit zur Erstellung, Stornierung und Verwaltung von Buchungen.

Sicherer Zugang mit Benutzer-Authentifizierung.

Benutzerfreundliche Verwaltungsoberfläche zur Verwaltung von Immobilien und Buchungen.


Installation


Um das Projekt auf Ihrem Computer zu installieren, führen Sie die folgenden Schritte aus:

    Repository klonen

    Virtuelle Umgebung erstellen

    Abhängigkeiten installieren und Migrationen durchführen

    Superuser für das Admin-Panel erstellen

    Server starten
    

Verwendung


Immobilien suchen: Gehen Sie zu URL /search/, um eine Liste von Immobilienanzeigen anzuzeigen. Sie können Filter verwenden, um zu suchen.

Buchung erstellen: Verwenden Sie die API, um eine Buchung über den entsprechenden Endpunkt (z.B. /bookings/) zu erstellen.

Verwaltungs-Panel: Gehen Sie zu http://127.0.0.1:8000/admin/, um auf das Admin-Panel zuzugreifen und verwenden Sie die Superuser-Zugangsdaten, die Sie zuvor erstellt haben.


Technologien im Projekt: Django, Django REST Framework, MySQL Workbench.


Lizenz
Diese Anwendung hat keine Lizenz und ist für alle offen.


==================================================================================================================


Описание проекта

Этот проект представляет собой веб-приложение, позволяющее пользователям управлять бронированием недвижимости.
С помощью RESTful API пользователи могут искать, бронировать и управлять объектами недвижимости. 
Приложение включает в себя администрирование, где администраторы могут управлять объявлениями о недвижимости и процессами бронирования.

Функции

- Поиск и фильтрация объектов недвижимости по цене, местоположению, количеству комнат и типу.
- Возможность создания, отмены и управления бронированиями.
- Безопасный доступ с использованием аутентификации пользователей.
- Удобный административный интерфейс для управления объектами и бронированиями.

Установка

Чтобы установить проект на своем компьютере, выполните следующие шаги:

1. Клонируйте репозиторий
2. Создайте виртуальное окружение
3. Установите зависимости, выполните миграции
4. Создайте суперпользователя для админки
5. Запустите сервер

Использование

- Поиск объявлений: Перейдите по URL `/search/`, чтобы увидеть список объявлений. Вы можете использовать фильтры для поиска.
- Создать бронирование: Используйте API для создания бронирования, используя соответствующую конечную точку (например, `/bookings/`).
- Административная панель: Перейдите по адресу `http://127.0.0.1:8000/admin/` для доступа к админской панели и используйте учетные данные суперпользователя, которые вы создали ранее.

Технологии

технологии в проекте: Django, Django REST Framework, MySQL Worckbench.

Лицензия

данное приложение не имеет лицензии и открыто для всех.

