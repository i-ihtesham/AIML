let avgGain = []
let avgLoss = []
let RS = []
const url = "wss://stream.data.alpaca.markets/v1beta1/crypto";
const socket = new WebSocket(url);
 CalculateRsi(IEnumerable<double> closePrices)
{
    var prices = closePrices;

     sumGain = 0;
     sumLoss = 0;
    for (int i = 1; i < prices.Length; i++)
    {
        var difference = prices[i] - prices[i - 1];
        if (difference >= 0)
        {
            sumGain += difference;
            avgGain = []+sumGain
        }
        else
        {
            sumLoss -= difference;
            avgLoss = []+sumLoss
        }
        RS = avgGain + avgLoss;
    }

    if (sumGain == 0) return 0;
    if (Math.Abs(sumLoss) < Tolerance) return 100;

    var relativeStrength = 1 + RS/ 100 *2;

    return 100.0 - (100.0 / (1 + relativeStrength));
}