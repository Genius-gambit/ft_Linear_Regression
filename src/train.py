from utils import *

def	gradientDescent(mileages: list, prices: list,
		learningRate: float, iterations: int) -> tuple:
    lossHistory = []
    t0History = [0.0]
    t1History = [0.0]
    t0 = 0.0
    t1 = 0.0
    message = "max epoch reached"
    
    for iter in range(iterations):
        dt0 = 0
        dt1 = 0
        for mileage, price in zip(mileages, prices):
            dt0 += (t1 * mileage + t0) - price
            dt1 += ((t1 * mileage + t0) - price) * mileage
        
        t0 -= dt0 / len(mileages) * learningRate
        t1 -= dt1 / len(prices) * learningRate
        loss = lossFunction(t0, t1, mileages, prices)
        if iter % 10 == 0:
            print("epoch {} - loss: {:.8}".format(iter, loss))
        t0, t1, learningRate = boldDriver(loss,
								lossHistory, t0, t1, dt0, dt1, learningRate, len(mileages))
        lossHistory.append(loss)
        t0History.append(t0)
        t1History.append(t1)
        if earlyStopping(lossHistory):
            message = "early stopped"
            break
    print("\nend: {}".format(message))
    print("epoch {} - loss: {:.8}".format(iter, loss))
    return (t0, t1, lossHistory, t0History, t1History)
        

def	main():
	learningRate = 0.5
	iterations = 500
	mileages, prices = getData(getPath('data.csv'))
	x = normalizeData(mileages)
	y = normalizeData(prices)
	t0, t1, lossHistory, t0History, t1History = gradientDescent(x, y,
											learningRate, iterations)
	storeData(t0, t1, 'thetas.csv')
	plotting(t0, t1, mileages, prices, lossHistory, t0History, t1History)

if __name__ == '__main__':
	main()