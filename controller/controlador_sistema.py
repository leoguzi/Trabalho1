import sys
sys.path.append(".")
from controller.controlador_enfermeiros import ControladorEnfermeiros
from controller.controlador_pacientes import ControladorPacientes
from view.tela_sistema import TelaSistema
from view.tela_enfermeiro import TelaEnfermeiros
from view.tela_paciente import TelaPaciente


class ControladorSistema:
    def __init__(self, tela_sistema: TelaSistema):
        self.__tela_sistema = tela_sistema
        self.__controlador_pacientes = ControladorPacientes(self, TelaPaciente())
        self.__controlador_enfermeiros = ControladorEnfermeiros(self, TelaEnfermeiros())

    def encerra_sistema(self):
        exit(0)

    def abre_menu_principal(self):
        lista_opcoes = {1: self.__controlador_enfermeiros.abre_tela_enfermeiros, 2: self.__controlador_pacientes.abre_tela_pacientes, 0: self.encerra_sistema} #adicionar as outras opções quando prontas
        while True:
            try:
                valor_lido = self.__tela_sistema.mostra_menu_principal()
                if valor_lido >=0 and valor_lido<=5:
                    lista_opcoes[valor_lido]()
                else:
                    raise ValueError
            except ValueError:
                print("\nOpção Invalida! Digite um numero inteiro entre 0 e 5!\n")

