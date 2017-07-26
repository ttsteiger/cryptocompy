# helper_functions.py
def build_url(func, **kwargs):

	if func == 'coinlist':
		url = "https://www.cryptocompare.com/api/data/coinlist/"
	else:
		url = "https://min-api.cryptocompare.com/data/{}?".format(func)
	
	for key, value in kwargs.items():
		if key == 'fsym':
			fsym_url = "fsym={}".format(value)
			url = "{}&{}".format(url, fsym_url)
		elif key == 'fsyms':
			fsyms_url = "fsyms={}".format(",".join(value))
			url = "{}&{}".format(url, fsyms_url)
		elif key == 'tsym':
			tsym_url = "tsym={}".format(value)
			url = "{}&{}".format(url, tsym_url)
		elif key == 'tsyms':
			tsyms_url = "tsyms={}".format(",".join(value))
			url = "{}&{}".format(url, tsyms_url)
		elif key == 'e' and value != 'all':
			e_url = "e={}".format(value)
			url = "{}&{}".format(url, e_url)
		elif key == 'markets':
			markets_url = "markets={}".format(",".join(value))
			url = "{}&{}".format(url, markets_url)
		elif key == 'avgType' and value != 'HourVWAP':
			at_url = "avgType={}".format(value)
			url = "{}&{}".format(url, at_url)
		elif key == 'UTCHourDiff' and value != 0:
			uhd_url = "UTCHourDiff={}".format(value)
			url = "{}&{}".format(url, uhd_url)
		elif key == 'ts':
			ts_url = "ts={}".format(value)
			url = "{}&{}".format(url, ts_url)
		elif key == 'aggregate' and value != 1:
			agg_url = "aggregate={}".format(value)
			url = "{}&{}".format(url, agg_url)
		elif key == 'limit' and value != 1440:
			lim_url = "limit={}".format(value)
			url = "{}&{}".format(url, lim_url)

	return url