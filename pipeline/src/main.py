from typing import Any
import dataFrameDownloader
from strategies import lr_modeling_close
from strategies import smooth_modeling_close
from strategies import forest_modeling_close
from strategies import boost_modeling_close
from strategies import lr_modeling_ind
from strategies import forest_modeling_ind
from strategies import boost_modeling_ind
import trading_simulator
from logger_setup import get_logger

logger = get_logger(__name__)

def main(inputMessage: dict[str, Any]) -> None:

	dataFrame: pd.DataFrame = dataFrameDownloader.main(
		nameExchange=inputMessage['nameExchange'],
		symbol=inputMessage['symbol'],
		type=inputMessage['type'],
		timeFrame=inputMessage['timeFrame']
	)

	if inputMessage["strategy"] == "lr_modeling_close":
		dataFrame = lr_modeling_close.main(inputMessage, dataFrame)
	elif inputMessage["strategy"] == "smooth_modeling_close":
		dataFrame = smooth_modeling_close.main(inputMessage, dataFrame)
	elif inputMessage["strategy"] == "forest_modeling_close":
		dataFrame = forest_modeling_close.main(inputMessage, dataFrame)
	elif inputMessage["strategy"] == "boost_modeling_close":
		dataFrame = boost_modeling_close.main(inputMessage, dataFrame)
	elif inputMessage["strategy"] == "lr_modeling_ind":
		dataFrame = lr_modeling_ind.main(inputMessage, dataFrame)
	elif inputMessage["strategy"] == "forest_modeling_ind":
		dataFrame = forest_modeling_ind.main(inputMessage, dataFrame)
	elif inputMessage["strategy"] == "boost_modeling_ind":
		dataFrame = boost_modeling_ind.main(inputMessage, dataFrame)

	trading_simulator.main(inputMessage, dataFrame)

if __name__ == "__main__":

	listMSGs = [
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '1min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '2min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '4min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '8min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '15min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '30min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '2h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '4h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '6h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '8h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '12h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '1d', 'strategy': 'boost_modeling_ind'},

		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '1min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '2min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '4min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '8min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '15min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '30min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '2h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '4h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '6h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '8h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '12h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '1d', 'strategy': 'boost_modeling_ind'},

		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '1min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '2min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '4min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '8min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '15min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '30min', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '2h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '4h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '6h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '8h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '12h', 'strategy': 'boost_modeling_ind'},
		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '1d', 'strategy': 'boost_modeling_ind'},


#		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'master'},
#		{'nameExchange': 'binance', 'symbol': 'BTC', 'type': 'futures', 'timeFrame': '1h', 'strategy': 'master'},
#
#		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'master'},
#		{'nameExchange': 'binance', 'symbol': 'ETH', 'type': 'futures', 'timeFrame': '1h', 'strategy': 'master'},
#
#		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'master'},
#		{'nameExchange': 'binance', 'symbol': 'BNB', 'type': 'futures', 'timeFrame': '1h', 'strategy': 'master'},
#
#
#
#		{'nameExchange': 'bybit', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'master'},
#		{'nameExchange': 'bybit', 'symbol': 'BTC', 'type': 'futures', 'timeFrame': '1h', 'strategy': 'master'},
#
#		{'nameExchange': 'bybit', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'master'},
#		{'nameExchange': 'bybit', 'symbol': 'ETH', 'type': 'futures', 'timeFrame': '1h', 'strategy': 'master'},
#
#		{'nameExchange': 'bybit', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'master'},
#		{'nameExchange': 'bybit', 'symbol': 'BNB', 'type': 'futures', 'timeFrame': '1h', 'strategy': 'master'},
#
#
#
#		{'nameExchange': 'kucoin', 'symbol': 'BTC', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'master'},
#		{'nameExchange': 'kucoin', 'symbol': 'BTC', 'type': 'futures', 'timeFrame': '1h', 'strategy': 'master'},
#
#		{'nameExchange': 'kucoin', 'symbol': 'ETH', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'master'},
#		{'nameExchange': 'kucoin', 'symbol': 'ETH', 'type': 'futures', 'timeFrame': '1h', 'strategy': 'master'},
#
#		{'nameExchange': 'kucoin', 'symbol': 'BNB', 'type': 'spot', 'timeFrame': '1h', 'strategy': 'master'},
#		{'nameExchange': 'kucoin', 'symbol': 'BNB', 'type': 'futures', 'timeFrame': '1h', 'strategy': 'master'},
	]

	for msg in listMSGs:
		main(msg)