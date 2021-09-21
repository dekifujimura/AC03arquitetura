import abc
from unittest import TestCase, main

class Calculadora(object):
    
    def calculate(self, valor01, valor02, operador):
        operationFabrica = OperationFabrica()
        operation = operationFabrica.criar(operador)
        if (operation == None):
            return 0
        else:
            result = operation.executar(valor01, valor02)
            return result


class OperationFabrica(object):

    def cria(self, operador):
        if (operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()
        elif (operador == 'multiplicacao'):
            return Multiplicacao()
        else: 
            return None

class Operacao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executa(self, valor01, valor02):
        pass
    
class Soma(Operacao):
    def executa(self, valor01, valor02):
        resul = valor01 + valor02
        return result
    
class Subtracao(Operacao):
    def executa(self, valor01, valor02):
        result = valor01 - valor02
        return result

class Multiplicacao(Operacao):
    def executa(self, valor01, valor02):
        result = valor01 * valor02
        return result

class Divisao(Operacao):
    def executa(self, valor01, valor02):
        if valor02 == 0:
            return 'impossivel dividir por 0'
        result = valor01 / valor02
        return result

class Testes(TestCase):

    def test_soma(self):
        calculador = Calculadora()
        result = calculador.calcula(2,3,'soma')
        self.assertEqual(result, 5)
    
    def test_subtracao(self):
        calculador = Calculadora()
        result = calculador.calcula(2,4,'subtracao')
        self.assertEqual(result, -2)
    
    def test_multiplicacao(self):
        calculador = Calculadora()
        result = calculador.calcula(2,5,'multiplicacao')
        self.assertEqual(result, 10)

    def test_divisao(self):
        calculador = Calculadora()
        result = calculador.calcula(4,2,'divisao')
        self.assertEqual(result, 2)

    def test_operacao(self):
        calculador = Calculadora()
        result = calculador.calcula(4,2, 'subtrair')
        self.assertEqual(result, 0)

    def test_divisao_por_zero(self):
        calculador = Calculadora()
        result = calculador.calcula(5,0, 'divisao')
        self.assertEqual(result, 'impossivel dividir por 0')


    
calculador = Calculadora()
calcula = calculador.calcula(5,5, 'soma')
print("RESULTADO:", calcula)


if _name_ == '_main_':
    main()
