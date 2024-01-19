class ConvertidorTemperaturas:

    MAX_CELCIUS = 100
    MAX_FARENHEINT = 213

    @classmethod
    def c_f(cls, celcius):
        if celcius > cls.MAX_CELCIUS:
            raise ValueError(f'Temperatura C demaciada alta: {celcius}')
        return celcius * 9/5 + 32

    @classmethod
    def f_c(cls, farenheint):
        if farenheint > cls.MAX_FARENHEINT:
            raise  ValueError(f'Temperatura F demaciada alta: {farenheint}')
        return (farenheint-32) *5/9

if __name__ == '__main__':
    resultado = ConvertidorTemperaturas.c_f(112)
    print(f'El cambio de F a C es: {resultado:.2f}')