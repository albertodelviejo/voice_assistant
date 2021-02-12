class command:
    
    def __init__(self,message):
        
        self.message = message
        
    def check(self):
        
        low_message = self.message.lower()
        if 'enviar' in low_message:
            if 'david' in low_message:
                self.execute('david')
            elif 'alberto' in low_message:
                self.execute('alberto')
            else:
                print('No he podido reconocer el destinatario')
                
    def execute(self, person):
        
        print(self.message)
        #TODO
        
prueba = command('Enviar a Alberto')
prueba.check()