2022-11-10 19:24:37,726 (__init__.py:964 MainThread) ERROR - TeleBot: "Infinity polling exception: cannot access local variable 'k1' where it is not associated with a value"
2022-11-10 19:24:37,729 (__init__.py:966 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 959, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 1047, in polling
    self.__threaded_polling(non_stop=non_stop, interval=interval, timeout=timeout, long_polling_timeout=long_polling_timeout,
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 1122, in __threaded_polling
    raise e
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 1078, in __threaded_polling
    self.worker_pool.raise_exceptions()
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\util.py", line 154, in raise_exceptions
    raise self.exception_info
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\util.py", line 98, in run
    task(*args, **kwargs)
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 6086, in _run_middlewares_and_handler
    result = handler['function'](message)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\p\main.py", line 58, in message_reply
    if message.text == k1:
                       ^^
UnboundLocalError: cannot access local variable 'k1' where it is not associated with a value
"
2022-11-10 19:24:48,152 (__init__.py:964 MainThread) ERROR - TeleBot: "Infinity polling exception: cannot access local variable 'k1' where it is not associated with a value"
2022-11-10 19:24:48,154 (__init__.py:966 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 959, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 1047, in polling
    self.__threaded_polling(non_stop=non_stop, interval=interval, timeout=timeout, long_polling_timeout=long_polling_timeout,
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 1122, in __threaded_polling
    raise e
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 1078, in __threaded_polling
    self.worker_pool.raise_exceptions()
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\util.py", line 154, in raise_exceptions
    raise self.exception_info
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\util.py", line 98, in run
    task(*args, **kwargs)
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 6086, in _run_middlewares_and_handler
    result = handler['function'](message)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\p\main.py", line 58, in message_reply
    if message.text == k1:
                       ^^
UnboundLocalError: cannot access local variable 'k1' where it is not associated with a value
"
2022-11-10 19:25:00,346 (__init__.py:964 MainThread) ERROR - TeleBot: "Infinity polling exception: cannot access local variable 'k1' where it is not associated with a value"
2022-11-10 19:25:00,348 (__init__.py:966 MainThread) ERROR - TeleBot: "Exception traceback:
Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 959, in infinity_polling
    self.polling(non_stop=True, timeout=timeout, long_polling_timeout=long_polling_timeout,
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 1047, in polling
    self.__threaded_polling(non_stop=non_stop, interval=interval, timeout=timeout, long_polling_timeout=long_polling_timeout,
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 1122, in __threaded_polling
    raise e
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 1078, in __threaded_polling
    self.worker_pool.raise_exceptions()
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\util.py", line 154, in raise_exceptions
    raise self.exception_info
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\util.py", line 98, in run
    task(*args, **kwargs)
  File "C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\site-packages\telebot\__init__.py", line 6086, in _run_middlewares_and_handler
    result = handler['function'](message)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\p\main.py", line 58, in message_reply
    if message.text == k1:
                       ^^
UnboundLocalError: cannot access local variable 'k1' where it is not associated with a value
"
