1. **На чому ґрунтується криптостійкість генератора BBS?**
   Генератор BBS (Blum Blum Shub) ґрунтується на складності факторизації великих чисел. Базова ідея алгоритму полягає в використанні добутку двох великих простих чисел та генерації бітів на основі операцій з числом за модулем цього добутку. Генератор є криптостійким, оскільки обчислення кореня за модулем великого числа (яке є частиною операцій у генераторі) є важким завданням, що базується на проблемі факторизації.

2. **Які переваги і недоліки потокових шифрів?**
   - **Переваги:**
     - **Швидкість:** Потокові шифри зазвичай швидші за блочні шифри, оскільки працюють з бітами або байтами даних по черзі.
     - **Менші вимоги до пам'яті:** Потокові шифри зазвичай не потребують великої пам'яті для зберігання блоків даних, що робить їх зручними для роботи з великими обсягами даних.
     - **Гнучкість:** Потокові шифри добре підходять для шифрування даних, що передаються в реальному часі (наприклад, потокові аудіо та відео).
   - **Недоліки:**
     - **Проблеми з синхронізацією:** Якщо в процесі передачі даних виникає помилка або втрата синхронізації, декодування може стати неможливим.
     - **Вразливість до повторного використання ключа:** Потокові шифри можуть стати вразливими, якщо ключ або початкове значення (IV) використовуються більше одного разу, що дозволяє зловмисникам виконати атаку на основі порівняння повторних потоків.

3. **Які переваги і недоліки шифрів однократного гамування?**
   - **Переваги:**
     - **Безпека:** Якщо ключ гамування використовується тільки один раз і має достатню довжину, шифр однократного гамування забезпечує ідеальну конфіденційність, оскільки неможливо відновити вихідні дані без знання ключа.
     - **Простота:** Алгоритм однократного гамування дуже простий у реалізації та не потребує складних математичних операцій.
   - **Недоліки:**
     - **Проблеми з ключем:** Найбільша проблема полягає в необхідності мати таку ж довжину ключа, як і повідомлення, що робить його важким для практичного застосування.
     - **Неможливість повторного використання ключа:** Якщо ключ буде використаний повторно, безпека системи буде порушена.

4. **Які вимоги ставляться до генераторів випадкових та псевдовипадкових послідовностей?**
   - **Незалежність:** Кожен елемент послідовності має бути незалежним від інших, щоб уникнути передбачуваності.
   - **Рівномірність:** Розподіл значень в послідовності має бути рівномірним, тобто кожен можливий результат повинен з'являтися з однаковою ймовірністю.
   - **Необхідність довгого періоду:** Генератор повинен генерувати послідовності з великим періодом, щоб уникнути повторів значень.
   - **Прогнозованість:** Псевдовипадкові генератори не повинні бути передбачуваними без знання початкових умов або внутрішнього стану генератора.

5. **Запропонуйте кілька реалізацій генераторів випадкових послідовностей за допомогою комп‘ютера.**
   - **Метод лінійного конгруентного генератора (LCG):** Це один з найпростіших методів генерації псевдовипадкових чисел. Генератор визначається через рекурентне співвідношення:
     \[
     X_{n+1} = (aX_n + c) \mod m
     \]
     де \(a\), \(c\), та \(m\) — константи, а \(X_0\) — початкове значення.
   - **Генератор Мерсеннєвих твістів (MT19937):** Це швидкий генератор псевдовипадкових чисел з великим періодом (2^19937−1). Він використовується в багатьох мовах програмування.
   - **Генератор на основі криптографічних хеш-функцій:** Наприклад, можна використовувати хешування SHA-256 для створення випадкових чисел, генеруючи їх із хешів деяких вхідних даних (наприклад, часу або попереднього значення).
   - **Апаратний генератор випадкових чисел:** Використовує фізичні явища (наприклад, шум або рух електронів) для генерації випадкових чисел. Цей метод зазвичай забезпечує найвищу якість випадковості.
