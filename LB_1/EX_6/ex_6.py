inf = ['Protocol:','Prefix:','AD/Metric:','Next-Hop:','Last update:','Last update:','Outbound Interface:']
ospf_route = 'OSPF 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route_list = ospf_route.replace(',','').split()
ospf_route_list[2] = ospf_route_list[2].strip('[]')

print('\n'.join([''.join([f'{x:24}' for x in r]) for r in list(zip(inf,ospf_route_list))]))
