class Interval:
    intervals = {
		 "1m" : "INTERVAL_1_MINUTE",
		 "5m" : "INTERVAL_5_MINUTES",
		 "15m" : "INTERVAL_15_MINUTES",
		 "30m" : "INTERVAL_30_MINUTES",
		 "1h" : "INTERVAL_1_HOUR",
		 "2h" : "INTERVAL_2_HOURS",
		 "4h" : "INTERVAL_4_HOURS",
		 "1d" : "INTERVAL_1_DAY",
		 "1W" : "INTERVAL_1_WEEK",
		 "1M" : "INTERVAL_1_MONTH"
	}

    @classmethod
    def get_interval(cls, key):
     return cls.intervals.get(key, "")