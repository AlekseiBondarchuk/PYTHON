Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает два объекта:

  словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
    
    {'FastEthernet0/12':10,
     'FastEthernet0/14':11,
     'FastEthernet0/16':17}
    
  словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:

    {'FastEthernet0/1':[10,20],
     'FastEthernet0/2':[11,30],
     'FastEthernet0/4':[17]}
     
Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Сделать копию скрипта задания ex_3.

Дополнить скрипт:

добавить поддержку конфигурации, когда настройка access-порта выглядит так:

     interface FastEthernet0/20
     switchport mode access
     duplex auto
  
  То есть, порт находится в VLAN 1
  
В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1

Пример словаря:

    {'FastEthernet0/12':10,
     'FastEthernet0/14':11,
     'FastEthernet0/20':1 }
     
Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt
