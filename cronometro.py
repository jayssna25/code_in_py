import time
import os

class Cronometro:
    def __init__(self, segundos=0, minutos=0, horas=0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas
        self._running = False

    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self):
        self._running = True
        try:
            while self._running:
                self.limpar_tela()
                print(self)
                self.incremento()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nCronômetro interrompido.")

    def stop(self):
        self._running = False


cronometro1 = Cronometro()
print("Iniciando o cronômetro. Pressione Ctrl+C para parar.")
cronometro1.start()

cronometro2 = Cronometro(minutos=5, segundos=30)
print("\nIniciando outro cronômetro a partir de 05:30.")
