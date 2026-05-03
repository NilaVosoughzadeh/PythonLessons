class AverageClass :
    number1Unit = 2
    number2Unit = 2
    number3Unit = 3

    def AverageMath(self, number1, number2, number3):
        sum = (number1 * self.number1Unit) + (number2 * self.number2Unit) + (number3 * self.number3Unit)
        avg = sum / (self.number1Unit + self.number2Unit + self.number3Unit)
        return(avg)