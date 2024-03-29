Создать функцию, которая генерирует конфигурацию для access-портов.

Параметр access ожидает, как аргумент, словарь access-портов, вида:

    {'FastEthernet0/12':10,
    'FastEthernet0/14':11,
    'FastEthernet0/16':17,
    'FastEthernet0/17':150}
    
Функция должна возвращать список всех портов в режиме access с конфигурацией наоснове шаблона access_template.

В конце строк в списке не должно быть символа перевода строки.

Пример итогового списка:

    [
    'interface FastEthernet0/12',
    'switchport mode access',
    'switchport access vlan 10',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable',
    'interface FastEthernet0/17',
    'switchport mode access',
    'switchport access vlan 150',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable',
    ...]
  
Проверить работу функции на примере словаря access_dict.

    def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
    
    { 'FastEthernet0/12':10,
      'FastEthernet0/14':11,
      'FastEthernet0/16':17}
    
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    
    access_dict = { 'FastEthernet0/12':10,
                    'FastEthernet0/14':11,
                    'FastEthernet0/16':17,
                    'FastEthernet0/17':150 }
    
Сделать копию скрипта задания ex_1.

Дополнить скрипт:

  ввести дополнительный параметр, который контролирует будет ли настроен port-security;
  имя параметра 'psecurity';
  по умолчанию значение False.
  
Проверить работу функции на примере словаря access_dict, с генерациейконфигурации port-security и без.

    def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
    
    { 'FastEthernet0/12':10,
      'FastEthernet0/14':11,
      'FastEthernet0/16':17 }
    
    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение F
    alse
    - если значение True, то настройка выполняется с добавлением шаблона port_secu
    rity
    - если значение False, то настройка не выполняется
    
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
                     
    access_dict = { 'FastEthernet0/12':10,
                    'FastEthernet0/14':11,
                    'FastEthernet0/16':17,
                    'FastEthernet0/17':150 }
   
Сделать копию скрипта задания ex_1a.

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:

  ключи: имена интерфейсов, вида 'FastEthernet0/12'
  значения: список команд, который надо выполнить на этом интерфейсе:

    ['switchport mode access',
    'switchport access vlan 10',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable']
    
Проверить работу функции на примере словаря access_dict, с генерацией конфигурации port-security и без.

    def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
    
    { 'FastEthernet0/12':10,
    'FastEthernet0/14':11,
    'FastEthernet0/16':17 }
    
    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение F
    alse
    - если значение True, то настройка выполняется с добавлением шаблона port_secu
    rity
    - если значение False, то настройка не выполняется
    
    Функция возвращает словарь:
    
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
                       
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
                     
    access_dict = { 'FastEthernet0/12':10,
                    'FastEthernet0/14':11,
                    'FastEthernet0/16':17,
                    'FastEthernet0/17':150 }
