'''
Created on 14 oct. 2019

@author: fernando
'''
import ConfigParser

from ConfigParser import SafeConfigParser
if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read('file.conf')
    server = config.get('configuracion', 'server')
    port = config.get('configuracion', 'port')
    api = config.get('configuracion', 'api')
    #print server
    #print port
    #print api
   
    server = raw_input("Introduce Servidor(actual="+server+"):")
    port = raw_input("Introduce puerto (actual="+port+"): ")
    api = raw_input("Introduce api (actua="+api+"): ")
    #print server
    #print port
    #print api
    cparser = SafeConfigParser()
    cparser.add_section('configuracion')
    cparser.set('configuracion', 'server', server)
    cparser.set('configuracion', 'port', port)
    cparser.set('configuracion', 'api', api)
   
    with open('file.conf', 'wb') as archivo:
        cparser.write(archivo)
    exit
    