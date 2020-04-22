import httplib,urllib
import json
import os
from datetime import datetime
import datetime
from __builtin__ import True


class config(object):
    
    def __init__(self, file):
        directorio=os.path.dirname(os.path.abspath(__file__))
        file=directorio+"/conf.ini"
        file=open(file)
        lines=file.readlines()
        for line in lines:
            valor=line.split()
            if valor[0]=="server":
                self.server=valor[2]
            if valor[0]=="port":
                self.port=valor[2]
            if valor[0]=="api":
                self.api=valor[2]
        
    def getserver():
        return self.server

    def getport():
        return self.port

    def getapi():
        return self.api




class logger(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        conf=config('')
        self.server=conf.server
        self.port=conf.port
        self.api=conf.api
        self.eventos=[]
        self.eventosLista=[]
        self.url=[]
        self.token=""

    def reconfigure(self,server,port,api,token):
        try:
            self.server=server
            self.port=port
            self.api=api
            self.token=token
            return True
        except: 
            return None
        
    def logEven(self, name, params):
        try:
            payload = params
            hdr={"content-type":"application/x-www-form-urlencoded"}
            conn = httplib.HTTPConnection(self.server,self.port)
            mydata=urllib.urlencode(params)
            conn.request('POST',self.api,mydata,hdr)
            response = conn.getresponse()
            data = response.read()
            return data
    
          
        except:
            error="error logEven"  
   
    def newEvent(self,event,type,url):
        try:
           
            if not self.url==url:
                self.push()
                
            self.url=url
            if type=='FlasScrollingWithNVDAadd-on':
              if not self.eventosLista==[]: 
                  self.pushLista()             
            if type=='ListLinckforNVDAadd-on':    
                self.eventosLista.append(json.dumps(event)) 
            self.eventos.append(json.dumps(event))
        except: 
            return None
        
    def event(self,time,shift,gesture,xpath,url,direccion,children):
        try:
            if gesture=="l":
                type='ListLinckforNVDAadd-on'
                data = {"fechaHora":time,"parameterName":type,"Shift":shift,"tecla":gesture,"xpath":xpath,"url":url,"children":children}
                self.newEvent(data, type, url)
            else:    
                gestos=['h','1','2','3','i','t','k','f','u','v','e','b','x','c','r','q','s','m','g','d','o']
               
                if gesture in gestos:
                  
                    type="FlasScrollingWithNVDAadd-on"
                    data = {"fechaHora":time,"parameterName": type,"Shift":shift,"tecla":gesture,"xpath":xpath,"url":url}
                    self.newEvent(data, type, url)
            return data
        except:
            return None
            #ui.message("error")
    def push(self):
        try:
            if not self.eventos==[]:  
                eventos_interaccion=json.dumps(self.eventos)
                step=len(self.eventos)
                horaEvento=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                firstEvent= self.eventos[0]
                data=[('fechaHora',horaEvento),('parameterName','FlasScrollingWithNVDAadd-on'),('first_event',firstEvent),('step',step),("Interaction_Event",eventos_interaccion),("url",self.url),("token",self.token)]
                response=self.logEven("",data)
                self.pushLista()
                self.eventos=[]
                return response
            else:
                return None  
        except:
            return None
            
    def pushLista(self):
        try:
            if not self.eventosLista==[]:
                eventos_interaccion=json.dumps(self.eventosLista)
                step=len(self.eventosLista)
                horaEvento=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                firstEvent= self.eventosLista[0]
                data=[('fechaHora',horaEvento),('parameterName','ListLinckforNVDAadd-on'),('first_event',firstEvent),('step',step),("Interaction_Event",eventos_interaccion),("url",self.url),("token",self.token)]
                response=self.logEven("", data)
                self.eventosLista=[]
                return response
            else:
                return None
        except:
            return None
    
    def enviarpush(self,event):
        self.logEven("name", event)
        
   

if __name__ == '__main__':
   
    log=logger()
    log.reconfigure("oran.unsa.edu.ar","8083","/api/post2.php","d204dbe03bae6f041124bdf0f8881fda")
   
    evento=log.event('01-01-01 20:10:10', True, 'l', 'id=31', 'www.google.com.ar', 'next',3)
    evento=log.event('01-01-01 20:10:11', True, 'l', 'id=33', 'www.google.com.ar', 'next',2)
    reponse=log.pushLista()
    if(reponse):
        print ("Enviado evento de listas")
        print(reponse)
   