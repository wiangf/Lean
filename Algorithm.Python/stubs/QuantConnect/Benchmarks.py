# encoding: utf-8
# module QuantConnect.Benchmarks calls itself Benchmarks
# from QuantConnect.Common, Version=2.4.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc

# imports
import datetime
import QuantConnect.Securities
import System
import typing

# no functions
# classes

class FuncBenchmark(System.object, QuantConnect.Benchmarks.IBenchmark):
    """
    Creates a benchmark defined by a function
    
    FuncBenchmark(benchmark: Func[DateTime, Decimal])
    """
    def Evaluate(self, time: datetime.datetime) -> float:
        pass

    @staticmethod # known case of __new__
    def __new__(self, benchmark: typing.Callable[[datetime.datetime], float]) -> None:
        pass


class IBenchmark:
    """ Specifies how to compute a benchmark for an algorithm """
    def Evaluate(self, time: datetime.datetime) -> float:
        pass


class SecurityBenchmark(System.object, QuantConnect.Benchmarks.IBenchmark):
    """
    Creates a benchmark defined by the closing price of a QuantConnect.Benchmarks.SecurityBenchmark.Security instance
    
    SecurityBenchmark(security: Security)
    """
    def Evaluate(self, time: datetime.datetime) -> float:
        pass

    @staticmethod # known case of __new__
    def __new__(self, security: QuantConnect.Securities.Security) -> None:
        pass

    Security: QuantConnect.Securities.Security



