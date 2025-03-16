<h2 align="center"> Тестовый проект API автотестов на сайт samokat.ru</h2>  


### Используемый стек
<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" height=50 weight=50 />  
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" height=50 weight=50 />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height=50 weight=50 />
  <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/selenoid.svg" height=50 weight=50 />
  <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" height=50 weight=50 />
  <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/Telegram.svg" height=50 weight=50 />
</p>        

### Автоматизированные кейсы
1. Регистрация нового пользователя
2. Регистрация пользователя без данных (негативный)
3. Получение данных пользователя
4. Создание пользователя
5. Обновление данных пользователя
6. Удаление пользователя
7. Получение данных по несуществующему пользователю (негативный)

<details>
<summary><h3> Запуск тестов с помощью Jenkins </h3><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height=30 weight=30 /></summary> 

  > **Перейти в [сборку](https://jenkins.autotests.cloud/job/C17_dmitry_asl_hw14_Samokat/)**  
  > **Перейти на вкладку "Build with Parameters"** 
  <p>
  <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/jenkins.jpg" />
  </p>  
  
  > **Выбрать параметры из выпадающих список и нажать "Build"**
  <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/build_jenkins.jpg" />
  
  > Результаты запуска находятся в левом углу, последний запуск
  <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/check_build.jpg" />
</details>
<details>
<summary><h3> Запуск тестов локально </h3></summary>  
  В терминале в папке проекта выполнить команды
  
  ```
  poetry shell
  pytest tests
  ```
**Если локально установлен Allure можно посмотреть отчет, для этого выполняем**
  ```
  allure.bat serve allure-results
  ```

</details>

### Отчет о результатах в Allure <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" height=30 weight=30 />
> В качестве системы отчетности выбран **Allure Report**  
> Для перехода в отчет, в Jenkins в левом углу нажать на иконку на Вашем запуске  
  <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/check_build.jpg" />
  
> В открывшемся окне представлена общая информация по тестам  
>> Для подробной информации переходим на вкладку **Suits** и раскрываем все тесты для наглядности  
>>> При нажатии на конкретный тест справа отображается подробная информация по нему  
 <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/allure_result_green.jpg" />

### Отправка оповещения прохождения тестов в Telegram <img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/Telegram.svg" height=30 weight=30 />

> Автоматически настроена отправка оповещения о результатах прохождения тестов в чат **Telegram** с тегом ответственных людей.  
> В оповещении присутствует общая информация о запуске и ссылка на отчет в **Allure**.  
>> Для наглядности был выбран запуск тестов с ошибкой (упавший тест - плавающий баг на сайте)
<img src="https://github.com/DmitryAsl/qa_guru_hw_14_Samokat/blob/main/data/icons/telegram_notific.jpg" />

#### Для вопросов и предложений можно связаться в [telegram](https://t.me/Dmitry_Asl) 
