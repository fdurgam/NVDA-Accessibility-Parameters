
if __name__ == '__main__':
    #Crea el loggeer
   
    import datetime
    import loggers
    import time
    logger=loggers.logger()
    server="192.168.1.110"
    puerto="80"
    token="201857ef-f75f-0d00-afc2-4aa0069817e9"
    api="/api/post2.php"
    #logger.setListOflink("lista")
    logger.reconfigure(server,puerto,api,token)
    #Configura los finders
    fecha=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    	
    logger.event(str(fecha),True,"h","xpath","www.google.comm.ar",'next',0)
    print(logger)
    print("lista FlasScrollingWithNVDAadd-on= "+str(len(logger.eventos)))
    print("lista ListLinckforNVDAadd-on= "+str(len(logger.eventosLista)))
    time.sleep(2)
    logger.event(str(fecha),True,"l","xpath","www.google.comm.ar",'next',9)
    print("lista FlasScrollingWithNVDAadd-on= "+str(len(logger.eventos)))
    print("lista ListLinckforNVDAadd-on= "+str(len(logger.eventosLista)))
    logger.push()
    print("lista FlasScrollingWithNVDAadd-on= "+str(len(logger.eventos)))
    print("lista ListLinckforNVDAadd-on= "+str(len(logger.eventosLista)))
    
